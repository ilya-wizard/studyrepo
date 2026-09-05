"""Record an explicit user reaction; never manufacture a rating."""
import argparse
from datetime import datetime, timezone
from .store import DATA, REGISTRY, read_jsonl, write_jsonl

def record(candidate_id, statement, source_ref, reaction, reason='unspecified', rating=None):
    rows=read_jsonl(REGISTRY)
    c=next(r for r in rows if r['candidate_id']==candidate_id)
    if rating is not None and not 0<=rating<=10:raise ValueError('Rating must be 0..10')
    now=datetime.now(timezone.utc).isoformat()
    f=dict(feedback_id='feedback-'+now,candidate_id=candidate_id,recorded_at=now,source_ref=source_ref,user_statement=statement,interest_rating=rating,reaction=reaction,reason_category=reason,attraction=None,aversion=None,wants_to_work_with_users=None,next_action=None)
    feedback=read_jsonl(DATA/'feedback.jsonl');feedback.append(f)
    c['feedback_ids'].append(f['feedback_id'])
    if rating is not None:
        c['assessment']['dimensions']['founder_pull']=rating
        c['assessment']['founder_feedback_id']=f['feedback_id']
        c['validation_gates']['founder_pull']='pass' if rating>=7 else 'unknown'
    c['updated_at']=now[:10]
    write_jsonl(DATA/'feedback.jsonl',feedback);write_jsonl(REGISTRY,rows)
    return f

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',required=True);p.add_argument('--statement',required=True);p.add_argument('--source',required=True)
    p.add_argument('--reaction',required=True,choices=['interested','not_interested','unsure','selected','paused'])
    p.add_argument('--reason',default='unspecified',choices=['audience','problem','daily_work','business_model','distribution','ethics','novelty','other','unspecified'])
    p.add_argument('--rating',type=float)
    a=p.parse_args();print(record(a.candidate,a.statement,a.source,a.reaction,a.reason,a.rating)['feedback_id'])
