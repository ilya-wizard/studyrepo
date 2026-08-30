# Problem Hunter

Persistent research system for finding product opportunities backed by real pain signals.

> **For a new chat/session:** read `CURRENT_STATE.md` first, then `config/`, `prompts/`, `MARKETING_SKILLS.md`, `data/`, and the relevant reports. The repository is the long-term source of truth; chat history is not.

## Objective
Find B2B or B2C ideas worth building — not idea-generator output. A strong candidate needs repeated evidence, a clear target user and buyer, a believable path to first paid users, and an experiment that can start with <= €500.

## User constraints
- Markets: B2B and B2C
- MVP duration: flexible; idea quality matters more than speed
- Pre-revenue validation budget: <= €500
- Domains: broad, including health, dating, enterprise, hardware, marketplaces
- Boring is acceptable when the underlying problem/business is genuinely interesting

## Pipeline
`signal -> customer-research synthesis -> normalize -> deduplicate -> cluster -> score -> deep validation -> promotion gates -> opportunity backlog -> paid/manual experiment`

## Core rules
1. Evidence before ideas.
2. Multiple independent signals beat one viral complaint.
3. Existing spend/workarounds are strong evidence of willingness to pay.
4. Search explicit demand, pain, workarounds, switching and timing triggers separately.
5. Separate observed evidence from inference and attach confidence.
6. Penalize generic AI wrappers and saturated categories.
7. Record rejected ideas so they are not rediscovered endlessly.
8. Separate "interesting" from "commercially strong" and score both.
9. Red-team strong candidates before promoting them.
10. A numerical score cannot bypass the validation gates.
11. Prefer evidence-backed first-customer prospects over generic ICP lists.
12. Prefer paid concierge/manual validation before expensive integrations or product build-out.
13. Notify only on strong candidates or meaningful new evidence.

## Marketing validation layer
Problem Hunter selectively adapts patterns from `coreyhaines31/marketingskills` for customer research, competitive intelligence, product positioning, pricing, demand-signal prospecting, validation offers and recurring research loops.

See `MARKETING_SKILLS.md` for the exact mapping and what was intentionally excluded.

### Promotion gates
Deep validation explicitly checks:
- research quality
- competition gap
- monetization / test price
- evidence-backed reachability
- disconfirmation / red-team quality

A failed gate can keep a high-scoring candidate in WATCH.

## Repository
- `CURRENT_STATE.md` — latest ranking, cadence, decisions and operating rules
- `MARKETING_SKILLS.md` — adapted marketing-skill layer and source mapping
- `config/profile.json` — founder/search constraints
- `config/scoring.json` — deterministic scoring model
- `src/scoring.py` — deterministic score calculator
- `src/store.py` — JSONL persistence and deduplication
- `prompts/scan.md` — customer-research + demand-signal hunting protocol
- `prompts/validate.md` — deep validation, competitor profiling, first-customer and red-team protocol
- `schema/candidate.schema.json` — candidate evidence, switching, pricing, prospect and validation-gate structure
- `data/candidates.jsonl` — promoted candidate memory
- `data/watchlist.jsonl` — lower-confidence opportunities worth monitoring
- `data/rejected.jsonl` — rejection memory
- `reports/` — human-readable research reports

The scheduled research loop complements the code: it searches public sources, persists high-quality findings, deduplicates against repository state, and only alerts when something crosses the quality threshold or materially changes.
