import copy
import json
import tempfile
import unittest
from pathlib import Path
from src.scoring import load_config,score_candidate,decision
from src.store import upsert,merge_evidence,read_jsonl
from src.check import validate
from src.report import render,sync

ROOT=Path(__file__).resolve().parents[1]

class HunterTests(unittest.TestCase):
    def setUp(self):
        self.cfg=load_config()
        self.row=copy.deepcopy(read_jsonl(ROOT/'data/opportunities.jsonl')[0])
    def complete(self):
        self.row['assessment']['dimensions']={k:10 for k in self.cfg['weights']}
        self.row['assessment']['founder_feedback_id']='explicit-user-rating'
        return self.row
    def test_legacy_fields_do_not_create_fake_low_score(self):
        old={'score':74,'pain_intensity':9,'evidence_quality':9}
        r=score_candidate(old)
        self.assertIsNone(r['score']);self.assertIn('criteria_version_mismatch',r['issues'])
    def test_unknown_is_not_zero(self):
        self.assertIsNone(score_candidate(self.row)['score'])
    def test_zero_is_a_real_complete_rating(self):
        row=self.complete();row['assessment']['dimensions']={k:0 for k in self.cfg['weights']}
        self.assertEqual(score_candidate(row)['score'],0)
    def test_model_cannot_invent_founder_rating(self):
        row=self.complete();row['assessment']['founder_feedback_id']=None
        self.assertIsNone(score_candidate(row)['score'])
    def test_high_score_cannot_bypass_unknown_or_failed_gates(self):
        row=self.complete()
        self.assertEqual(score_candidate(row)['score'],100)
        self.assertFalse(decision(row)['priority_eligible'])
        row['validation_gates']={k:'pass' for k in self.cfg['commercial_gates']}
        row['validation_gates']['evidence']='fail'
        self.assertFalse(decision(row)['priority_eligible'])
    def test_version_mismatch_requires_reassessment(self):
        row=self.complete();row['assessment']['criteria_version']='1.0'
        self.assertIsNone(score_candidate(row)['score'])
    def test_invalid_and_nonfinite_scores_rejected(self):
        for bad in (11,-1,float('nan'),True):
            self.row['assessment']['dimensions']['evidence_quality']=bad
            with self.assertRaises(ValueError):score_candidate(self.row)
    def test_stage_transition_does_not_duplicate_and_watch_evidence_merges(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'registry.jsonl';upsert(self.row,p)
            self.row['stage']='explore';upsert(self.row,p)
            self.assertEqual(len(read_jsonl(p)),1)
            e=dict(self.row['evidence'][0],evidence_id='new')
            merge_evidence(self.row['candidate_id'],[e,e],p)
            self.assertEqual(len(read_jsonl(p)[0]['evidence']),2)
    def test_duplicate_problem_with_different_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'registry.jsonl';upsert(self.row,p)
            self.row['candidate_id']='another'
            with self.assertRaises(ValueError):upsert(self.row,p)
    def test_entire_migrated_registry_is_valid(self):
        self.assertEqual(validate(),[])
        rows=read_jsonl(ROOT/'data/opportunities.jsonl')
        self.assertEqual(len(rows),20)
        self.assertIn('social-connection-continuity',{r['candidate_id'] for r in rows})
    def test_generated_views_partition_registry(self):
        outputs=render();ids=[]
        for n in ('candidates','watchlist','rejected'):
            ids.extend(json.loads(l)['candidate_id'] for l in outputs[f'data/{n}.jsonl'].splitlines())
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids),{r['candidate_id'] for r in read_jsonl(ROOT/'data/opportunities.jsonl')})
    def test_generated_state_reproducible(self):
        self.assertEqual(sync(check=True),[])

if __name__=='__main__':unittest.main()
