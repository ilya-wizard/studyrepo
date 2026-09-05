# Opportunity Hunter

Find business ideas Ilya wants to explore, then test the riskiest assumption with real users within €500.

## Start a session
1. Read `CURRENT_STATE.md` (generated overview).
2. Read `config/profile.json`, `config/cycle.json`, `config/scoring.json` and the relevant protocol in `prompts/`.
3. Read `data/opportunities.jsonl`, `data/feedback.jsonl`, `data/observations.jsonl`, `data/runs.jsonl` and experiment records.
4. Open original sources before treating historical claims as verified. Reports are supporting history, never the live ranking.

## Source of truth
- `data/opportunities.jsonl`: **only editable opportunity registry**, including explore, validate, experiment, watch and reject.
- `data/candidates.jsonl`, `data/watchlist.jsonl`, `data/rejected.jsonl`: generated compatibility views; do not edit.
- `CURRENT_STATE.md`: generated from the registry, cycle and current criteria; do not edit.
- `data/feedback.jsonl`: actual user reactions and ratings. Missing interest is unknown, never an assistant estimate.
- `data/observations.jsonl`: user-supplied observations and field research; distinguish observation from interpretation.
- `data/experiments/*.json`: prepared/active/completed tests, costs and actual results.
- `data/runs.jsonl`: coverage, decisions, changed evidence and stalled-search tracking.
- `archive/2026-09-05/`: original scores and records, preserved before migration.
- `experiments/`: ready-to-use field-test kits.

## Two stages of research
**Explore:** specific people, meaningful situation, initial credible signal, plausible user interest. No requirement for proven monetization or a high total score. Keep multiple solutions open.

**Validate:** test alternatives, actual behavior, acquisition and payment. A competitor's marketing claim is not proof of problem resolution. Select the cheapest test of the largest uncertainty. Unknown adoption or monetization is a reason for an experiment, not an automatic rejection.

The user selects what to test. Prepare proposals autonomously, but do not invent founder ratings, contacts, interviews, payments or results. Sending messages requires explicit authorization. Do not put private participant records, personal contact details or confidential material into this public repository; retain redacted observations and safe references.

## Operating rhythm
Two focused research passes per week and a Sunday review; exact schedules are in `config/automations/`. Work on two audiences per cycle, roughly 80% focused / 20% adjacent discovery, at most three items for user choice and one active experiment. Stop repeating exhausted searches. MVP duration remains flexible; €500 is the validation spending limit, not the product price.

## Commands
```sh
python -m pip install -r requirements.txt
python -m src.check
python -m unittest discover -s tests -v
python -m src.report --write
python -m src.report --check
```

Use `python -m src.feedback --help` to record an explicit user reaction. After every canonical edit, validate, regenerate and commit related files atomically. Read the latest remote head before writing; never force-push over another session.

`MARKETING_SKILLS.md` describes adapted research methods; `prompts/` and versioned configs govern current behavior. Numerical scores support decisions only when complete and sourced. Historical scores are never comparable across criteria versions.
