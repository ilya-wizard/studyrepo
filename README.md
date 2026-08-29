# Problem Hunter

Persistent research system for finding product opportunities backed by real pain signals.

> **For a new chat/session:** read `CURRENT_STATE.md` first, then `config/`, `data/`, and the relevant reports. The repository is the long-term source of truth; chat history is not.

## Objective
Find B2B or B2C ideas worth building — not idea-generator output. A strong candidate needs repeated evidence, a clear target user, a believable path to first paid users, and an experiment that can start with <= €500.

## User constraints
- Markets: B2B and B2C
- MVP duration: flexible; idea quality matters more than speed
- Pre-revenue validation budget: <= €500
- Domains: broad, including health, dating, enterprise, hardware, marketplaces
- Boring is acceptable when the underlying problem/business is genuinely interesting

## Pipeline
`signal -> normalize -> deduplicate -> cluster -> score -> deep validation -> opportunity backlog -> experiment`

## Core rules
1. Evidence before ideas.
2. Multiple independent signals beat one viral complaint.
3. Existing spend/workarounds are strong evidence of willingness to pay.
4. Penalize generic AI wrappers and saturated categories.
5. Record rejected ideas so they are not rediscovered endlessly.
6. Separate "interesting" from "commercially strong" and score both.
7. Red-team strong candidates before promoting them.
8. Notify only on strong candidates or meaningful new evidence.
9. Prefer paid concierge validation before expensive integrations or product build-out.

## Repository
- `CURRENT_STATE.md` — latest ranking, cadence, decisions and operating rules
- `config/profile.json` — founder/search constraints
- `config/scoring.json` — scoring model
- `src/scoring.py` — deterministic score calculator
- `src/store.py` — JSONL persistence and deduplication
- `prompts/scan.md` — signal-hunting protocol
- `prompts/validate.md` — deep-validation / red-team protocol
- `data/candidates.jsonl` — promoted candidate memory
- `data/watchlist.jsonl` — lower-confidence opportunities worth monitoring
- `data/rejected.jsonl` — rejection memory
- `reports/` — human-readable research reports

The scheduled research loop complements the code: it searches public sources, persists high-quality findings, and only alerts when something crosses the quality threshold or materially changes.
