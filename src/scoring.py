"""Evidence-aware scoring: unknown inputs are never zero."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_config(path=None):
    return json.loads((path or ROOT / 'config/scoring.json').read_text())

def score_candidate(candidate, config=None):
    config = config or load_config()
    assessment = candidate.get('assessment', {})
    dimensions = assessment.get('dimensions', {})
    missing = [k for k in config['weights'] if dimensions.get(k) is None]
    issues = []
    if assessment.get('criteria_version') != config['version']:
        issues.append('criteria_version_mismatch')
    if dimensions.get('founder_pull') is not None and not assessment.get('founder_feedback_id'):
        issues.append('founder_rating_not_user_confirmed')
    for key, value in dimensions.items():
        if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 10):
            raise ValueError(f'Invalid dimension: {key}')
    penalties = {k: v for k, v in config['penalties'].items() if candidate.get('flags', {}).get(k) is True}
    score = None
    if not missing and not issues:
        score = round(max(0, sum(dimensions[k] * w * 10 for k, w in config['weights'].items()) - sum(penalties.values())), 1)
    tier = 'incomplete' if score is None else 'below_threshold'
    if score is not None:
        for name in ('deep_validate', 'notify', 'priority'):
            if score >= config['thresholds'][name]:
                tier = name
    return dict(criteria_version=config['version'], score=score, score_tier=tier,
                missing_dimensions=missing, issues=issues, penalties=penalties)

def decision(candidate, config=None):
    config = config or load_config()
    result = score_candidate(candidate, config)
    gates = candidate.get('validation_gates', {})
    blocked = [g for g in config['commercial_gates'] if gates.get(g) != 'pass']
    result.update(stage=candidate.get('stage', 'explore'), blocked_gates=blocked,
                  priority_eligible=result['score_tier'] == 'priority' and not blocked and candidate.get('stage') != 'reject')
    return result

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('candidate', type=Path)
    args = parser.parse_args()
    print(json.dumps(decision(json.loads(args.candidate.read_text())), ensure_ascii=False, indent=2))
