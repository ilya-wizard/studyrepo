"""Canonical storage. Preserve candidate identity across lifecycle stages."""
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
REGISTRY = DATA / 'opportunities.jsonl'

def read_jsonl(path):
    path = Path(path)
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []

def write_jsonl(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as handle:
        handle.write(''.join(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n' for row in rows))
        temp = handle.name
    os.replace(temp, path)

def normalize_text(text):
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s-]', ' ', text.lower())).strip()

def candidate_key(candidate):
    canonical = '|'.join(normalize_text(str(candidate.get(k, ''))) for k in ('problem', 'target_user', 'job_to_be_done'))
    return hashlib.sha256(canonical.encode()).hexdigest()[:20]

def upsert(candidate, path=REGISTRY):
    if not candidate.get('candidate_id'):
        raise ValueError('Stable candidate_id required; search registry before creating one')
    rows = read_jsonl(path)
    existing = next((i for i, row in enumerate(rows) if row['candidate_id'] == candidate['candidate_id']), None)
    if any(row['candidate_id'] != candidate['candidate_id'] and candidate_key(row) == candidate_key(candidate) for row in rows):
        raise ValueError('Same problem and segment already exists under another ID')
    if existing is None:
        rows.append(candidate)
    else:
        rows[existing] = candidate
    write_jsonl(path, rows)

def merge_evidence(candidate_id, evidence, path=REGISTRY):
    rows = read_jsonl(path)
    target = next((row for row in rows if row['candidate_id'] == candidate_id), None)
    if target is None:
        return None
    seen = {item['evidence_id'] for item in target['evidence']}
    for item in evidence:
        if item['evidence_id'] not in seen:
            target['evidence'].append(item)
            seen.add(item['evidence_id'])
    write_jsonl(path, rows)
    return target
