from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable

from scoring import score_candidate

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "candidates.jsonl"


def load_candidates(path: Path = DATA) -> list[Dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def ranked_candidates(rows: Iterable[Dict[str, Any]]) -> list[Dict[str, Any]]:
    enriched = []
    for row in rows:
        result = score_candidate(row)
        copy = dict(row)
        copy["computed_score"] = result["score"]
        copy["computed_status"] = result["status"]
        enriched.append(copy)
    return sorted(enriched, key=lambda item: item["computed_score"], reverse=True)


def markdown(rows: list[Dict[str, Any]]) -> str:
    out = ["# Problem Hunter — Ranked Opportunities", ""]
    if not rows:
        return "\n".join(out + ["No candidates yet.", ""])

    for i, row in enumerate(rows, 1):
        out.extend([
            f"## {i}. {row.get('title', row.get('candidate_id', 'Untitled'))}",
            f"**Score:** {row['computed_score']}/100 · **Status:** {row['computed_status']}",
            "",
            f"**Target:** {row.get('target_user', '—')}",
            "",
            f"**Problem:** {row.get('problem', '—')}",
            "",
            f"**Wedge:** {row.get('solution_wedge', '—')}",
            "",
            f"**Next step:** {row.get('next_step', '—')}",
            "",
        ])
    return "\n".join(out)


if __name__ == "__main__":
    ranked = ranked_candidates(load_candidates())
    print(markdown(ranked))
