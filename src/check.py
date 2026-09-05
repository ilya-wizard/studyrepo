"""Validate schemas, provenance, references and generated state."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from .store import read_jsonl
from .scoring import load_config, score_candidate

ROOT=Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    errors=[]
    def check_schema(row, filename, label):
        schema=json.loads((root/'schema'/filename).read_text())
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(row):
            errors.append(f'{label}: {list(error.path)} {error.message}')
    candidates=read_jsonl(root/'data/opportunities.jsonl')
    feedback=read_jsonl(root/'data/feedback.jsonl')
    for row in feedback:check_schema(row,'feedback.schema.json',row.get('feedback_id'))
    feedback_by_id={r['feedback_id']:r for r in feedback}
    if len(feedback_by_id)!=len(feedback):errors.append('Duplicate feedback ID')
    ids={r['candidate_id'] for r in candidates}
    if len(ids)!=len(candidates):errors.append('Duplicate candidate ID across stages')
    for filename, schema_name, id_key in [('observations.jsonl','observation.schema.json','observation_id'),('runs.jsonl','run.schema.json','run_id')]:
        records=read_jsonl(root/'data'/filename)
        seen=set()
        for record in records:
            check_schema(record,schema_name,record.get(id_key))
            if record[id_key] in seen:errors.append(f'{filename}: duplicate ID')
            seen.add(record[id_key])
            if filename=='observations.jsonl' and record['candidate_id'] is not None and record['candidate_id'] not in ids:
                errors.append('Observation references missing candidate')
            if filename=='runs.jsonl' and not set(record['changed_candidate_ids'])<=ids:
                errors.append('Run references missing candidate')
    experiments={}
    for path in (root/'data/experiments').glob('*.json'):
        e=json.loads(path.read_text());check_schema(e,'experiment.schema.json',path.name)
        if e['experiment_id'] in experiments:errors.append('Duplicate experiment ID')
        experiments[e['experiment_id']]=e
        if e['candidate_id'] not in ids:errors.append(f'{path.name}: missing candidate')
        if sum(e['budget_eur'].values())>e['budget_cap_eur'] or e['spend_eur']>e['budget_cap_eur']:errors.append(f'{path.name}: over budget')
        if e['status']=='active' and not e['selected_by_user']:errors.append(f'{path.name}: active without user selection')
        if e['status']=='completed' and (not e['results'] or not e['completed_at']):errors.append(f'{path.name}: completion without results')
        if any(e[k]>0 for k in ('actual_contacts','actual_interviews','actual_paid_pilots')) and not e['results']:errors.append(f'{path.name}: activity without evidence')
        if not (root/e['kit']).is_file():errors.append(f'{path.name}: missing kit')
    cycle=json.loads((root/'config/cycle.json').read_text())
    active=[e['experiment_id'] for e in experiments.values() if e['status']=='active']
    if len(active)>cycle['max_active_experiments']:errors.append('Too many active experiments')
    if cycle['active_experiment_id'] not in active+[None]:errors.append('Cycle active experiment mismatch')
    if active and cycle['active_experiment_id']!=active[0]:errors.append('Active experiment not tracked in cycle')
    if cycle.get('prepared_experiment_id') not in experiments:errors.append('Prepared experiment missing')
    for f in feedback:
        if f['candidate_id'] is not None and f['candidate_id'] not in ids:errors.append('Feedback references missing candidate')
    for c in candidates:
        cid=c['candidate_id'];check_schema(c,'candidate.schema.json',cid)
        result=score_candidate(c,load_config(root/'config/scoring.json'))
        errors.extend(f'{cid}: {issue}' for issue in result['issues'])
        eid=c['validation_experiment']
        if eid is not None and (eid not in experiments or experiments[eid]['candidate_id']!=cid):errors.append(f'{cid}: invalid experiment reference')
        if c['stage']=='experiment' and (eid not in experiments or experiments[eid]['status']!='active'):errors.append(f'{cid}: experiment stage without active experiment')
        for fid in c['feedback_ids']:
            if fid not in feedback_by_id or feedback_by_id[fid]['candidate_id']!=cid:errors.append(f'{cid}: invalid feedback reference')
        rating=c['assessment']['dimensions']['founder_pull'];fid=c['assessment']['founder_feedback_id']
        if rating is not None:
            f=feedback_by_id.get(fid,{})
            if f.get('candidate_id')!=cid or f.get('interest_rating')!=rating:errors.append(f'{cid}: founder rating differs from user feedback')
        evidence=c['evidence'];eids={e['evidence_id'] for e in evidence}
        if len(eids)!=len(evidence):errors.append(f'{cid}: duplicate evidence ID')
        for e in evidence:
            if not e['source_url'] and not e.get('source_ref'):errors.append(f'{cid}: evidence has no provenance')
            if not set(e['contradicts'])<=eids:errors.append(f'{cid}: unresolved contradiction reference')
        behavioral={e['independence_key'] for e in evidence if e['verification']=='verified' and e['source_kind'] in ('customer_behavior','user_observation') and e['stance']=='supports' and e['independence_key']}
        if c['validation_gates']['evidence']=='pass' and len(behavioral)<3:errors.append(f'{cid}: evidence gate lacks independent behavioral sources')
        if c['validation_gates']['founder_pull']=='pass' and (rating is None or rating<7):errors.append(f'{cid}: founder gate lacks positive user rating')
        for p in c['source_reports']:
            if not (root/p).is_file():errors.append(f'{cid}: missing report {p}')
    return errors

if __name__=='__main__':
    errors=validate()
    if errors:
        print('\n'.join(errors));raise SystemExit(1)
    print('Schemas, provenance, references, budget and lifecycle: OK')
