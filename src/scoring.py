from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "scoring.json"


def load_config(path: Path = DEFAULT_CONFIG) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def score_candidate(candidate: Dict[str, Any], config: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Return deterministic 0-100 opportunity score plus applied penalties.

    Candidate dimensions are expected on a 0-10 scale. Missing dimensions score 0,
    which intentionally rewards evidence completeness rather than optimistic guessing.
    """
    config = config or load_config()
    weights = config["weights"]
    penalties_cfg = config.get("penalties", {})

    weighted = 0.0
    dimensions: Dict[str, float] = {}
    for key, weight in weights.items():
        value = float(candidate.get(key, 0))
        value = max(0.0, min(10.0, value))
        dimensions[key] = value
        weighted += value * weight

    base_score = weighted * 10.0
    flags = candidate.get("flags", {}) or {}
    applied_penalties: Dict[str, float] = {}
    penalty_total = 0.0

    for flag, penalty in penalties_cfg.items():
        if bool(flags.get(flag, False)):
            applied_penalties[flag] = float(penalty)
            penalty_total += float(penalty)

    final_score = max(0.0, min(100.0, base_score - penalty_total))
    thresholds = config.get("thresholds", {})

    if final_score >= thresholds.get("priority", 86):
        status = "priority"
    elif final_score >= thresholds.get("notify", 78):
        status = "notify"
    elif final_score >= thresholds.get("deep_validate", 68):
        status = "deep_validate"
    else:
        status = "watch_or_reject"

    return {
        "score": round(final_score, 1),
        "base_score": round(base_score, 1),
        "status": status,
        "dimensions": dimensions,
        "penalties": applied_penalties,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Score one Problem Hunter candidate JSON file")
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()

    candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
    print(json.dumps(score_candidate(candidate), indent=2, ensure_ascii=False))
