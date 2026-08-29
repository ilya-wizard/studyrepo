from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[^a-z0-9а-яёіїєґ\s-]", " ", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def candidate_key(candidate: Dict[str, Any]) -> str:
    canonical = "|".join(
        normalize_text(str(candidate.get(field, "")))
        for field in ("problem", "target_user", "job_to_be_done")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:20]


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    rows: List[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def append_unique(candidate: Dict[str, Any], filename: str = "candidates.jsonl") -> bool:
    """Append candidate if its deterministic key is new. Returns True if written."""
    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / filename
    key = candidate.setdefault("candidate_id", candidate_key(candidate))
    existing = {row.get("candidate_id") for row in read_jsonl(path)}
    if key in existing:
        return False

    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(candidate, ensure_ascii=False, sort_keys=True) + "\n")
    return True


def merge_evidence(candidate_id: str, evidence: Iterable[Dict[str, Any]]) -> Dict[str, Any] | None:
    """Merge new evidence into an existing candidate, deduplicating by URL/source+quote."""
    path = DATA / "candidates.jsonl"
    rows = read_jsonl(path)
    target = next((row for row in rows if row.get("candidate_id") == candidate_id), None)
    if target is None:
        return None

    current = target.setdefault("evidence", [])
    seen = {
        (item.get("url") or "", normalize_text(str(item.get("quote") or item.get("summary") or "")))
        for item in current
    }
    for item in evidence:
        sig = (item.get("url") or "", normalize_text(str(item.get("quote") or item.get("summary") or "")))
        if sig not in seen:
            current.append(item)
            seen.add(sig)

    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows) + "\n",
        encoding="utf-8",
    )
    return target
