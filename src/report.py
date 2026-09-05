"""Generate state and compatibility views from canonical data."""
import argparse
import json
from collections import Counter
from pathlib import Path
from .scoring import decision, load_config
from .store import read_jsonl

ROOT=Path(__file__).resolve().parents[1]

def render(root=ROOT):
    rows=read_jsonl(root/'data/opportunities.jsonl')
    cfg=load_config(root/'config/scoring.json')
    cycle=json.loads((root/'config/cycle.json').read_text())
    counts=Counter(r['stage'] for r in rows)
    dates=[cycle['updated_at']]+[r['updated_at'] for r in rows]
    out=['# Opportunity Hunter — Current State','', '> GENERATED: edit canonical data/configs, then run `python -m src.report --write`.','',f"Updated: {max(dates)} · Criteria: {cfg['version']}",'',
         '## Current cycle','',f"{cycle['cycle_id']} · {cycle['start_date']} → {cycle['review_date']}",'']
    out += [f"- {a['segment']}: {a['question']}" for a in cycle['audiences']]
    cadence=cycle['cadence']
    out += ['',f"Focus / adjacent discovery: {cycle['focus_share']:.0%} / {cycle['adjacent_share']:.0%}. Maximum shortlist: {cycle['max_shortlist']}. Maximum active experiments: {cycle['max_active_experiments']}.",
            f"Research: {', '.join(cadence['scan_days'])} {cadence['scan_time']}; review: {cadence['review_day']} {cadence['review_time']} ({cadence['timezone']}).",'',
            f"Active experiment: {cycle['active_experiment_id'] or 'none'}. Prepared option: {cycle['prepared_experiment_id']}. Selection: {cycle['selection_status']}.",'',
            '## Portfolio','',f"Total: {len(rows)}; " + '; '.join(f'{k}: {v}' for k,v in sorted(counts.items()))+'.','',
            '| Opportunity | Stage | Current score | Founder interest | Next action |','|---|---|---|---|---|']
    active=[r for r in rows if r['stage']!='reject']
    for row in sorted(active,key=lambda r:(r['stage']!='explore',r['title'])):
        result=decision(row,cfg)
        score=str(result['score']) if result['score'] is not None else 'unknown; assessment incomplete'
        interest=row['assessment']['dimensions']['founder_pull']
        out.append('| '+' | '.join(str(x).replace('|','/').replace('\n',' ') for x in [row['title'],row['stage'],score,interest if interest is not None else 'awaiting user rating',row['next_step']])+' |')
    out += ['', '## Experiment facts','']
    for path in sorted((root/'data/experiments').glob('*.json')):
        e=json.loads(path.read_text())
        out += [f"- {e['experiment_id']}: **{e['status']}**. Contacts {e['actual_contacts']}; interviews {e['actual_interviews']}; paid pilots {e['actual_paid_pilots']}; spend €{e['spend_eur']}; planned budget €{sum(e['budget_eur'].values())} / cap €{e['budget_cap_eur']}."]
    out += ['', '## Interpretation rules','',
            '- Historical scores are preserved in historical_record/archive; they are not current rankings.',
            '- Unknown dimensions stay null; no total score until all dimensions are supported. Founder interest comes only from explicit user feedback.',
            f"- Complete-assessment score tiers: deep validation {cfg['thresholds']['deep_validate']}, notify {cfg['thresholds']['notify']}, priority {cfg['thresholds']['priority']}. Tiers do not bypass gates or block exploration.",
            '- Explore means a problem is worth learning about; it does not assert commercial validation.',
            '- Historical reports are unverified until original sources are reopened. Vendor offers are not demand or sales evidence.',
            '- Rejected solution scopes and reopening triggers are in the canonical registry. Do not discard a good problem because one solution failed.',
            '- Next useful input: an actual user preference/selection; next field evidence: recent expansion attempts and a paid pilot. Prepared materials are not completed experiments.',
            '- No private participant data or private message contents in this public repository.', '']
    outputs={'CURRENT_STATE.md':'\n'.join(out)}
    groups={'candidates':{'explore','validate','experiment'},'watchlist':{'watch'},'rejected':{'reject'}}
    for name,stages in groups.items():
        outputs[f'data/{name}.jsonl']=''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows if r['stage'] in stages)
    return outputs

def sync(root=ROOT,check=False):
    outputs=render(root)
    stale=[]
    for name,content in outputs.items():
        path=root/name
        if not path.exists() or path.read_text()!=content:stale.append(name)
        if not check:path.write_text(content)
    return stale

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--check',action='store_true');a=p.parse_args()
    from .check import validate
    errors=validate()
    if errors:print('\n'.join(errors));raise SystemExit(1)
    if a.check:
        stale=sync(check=True)
        if stale:print('Stale generated files: '+', '.join(stale));raise SystemExit(1)
        print('Generated state and views: current')
    elif a.write:sync();print('Generated state and views updated')
    else:print(render()['CURRENT_STATE.md'])
