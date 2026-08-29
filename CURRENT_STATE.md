# Problem Hunter — Current State

Updated: 2026-08-29

## Search profile
- Markets: B2B + B2C
- MVP duration: flexible; idea quality matters more than speed
- Initial validation budget: <= €500
- Domains allowed: broad, including health, dating, enterprise, hardware, marketplaces
- Boring ideas are acceptable when the underlying problem/business is compelling
- Reject generic AI wrappers, hypothetical-demand ideas, one-off complaints, saturated categories without a wedge, and ideas that require large paid acquisition before validation

## Research cadence
- Signal scan: 3x/day — approximately 07:00, 13:00, 19:00 Europe/Berlin
- Deep portfolio review: weekly on Sunday around 11:00 Europe/Berlin
- User notification: only when a candidate becomes genuinely strong, meaningful evidence materially changes a candidate, or the ranking changes in a decision-relevant way

## Validation pipeline
1. Find primary pain signals and workarounds
2. Require repeated/independent evidence
3. Identify buyer and existing spend
4. Map current alternatives and competition
5. Check reachability/distribution
6. Check why-now dynamics
7. Define <= €500 validation experiment
8. Score commercial strength + founder interest separately
9. Red-team the idea by actively searching for reasons it fails
10. Promote, watch, or reject; persist the decision to avoid rediscovery

## Current ranking
1. **Prior Authorization Evidence-Pack Copilot — 83.1/100** — strongest current candidate; deep-validate one specialty and test paid concierge evidence packs before integrations.
2. **Dental Schedule QA Copilot — 78.2/100** — real repeated pain and direct product request, but meaningful competition; validate with paid schedule-audit pilots.
3. **Construction AI Takeoff — ~72/100** — watchlist only; pain is real but the category is crowded and the wedge is not yet sharp enough.

## Rejected after validation
- **German E-Invoice Legacy Bridge — rejected 2026-08-29.** Pain is real, but the proposed wedge is already directly served by multiple vendors offering legacy-ERP integration, API conversion, validation, and even AI-assisted mapping/PDF-to-E-invoice conversion. No sufficiently differentiated second-order problem was identified to justify further research.

## Decision thresholds
- <68: watch or reject
- 68–77.9: deep validation / watch
- >=78: strong enough to notify when evidence quality supports it
- >=86: priority candidate

## Source-of-truth files
- `config/profile.json` — search constraints
- `config/scoring.json` — scoring model
- `data/candidates.jsonl` — promoted candidates
- `data/watchlist.jsonl` — weaker candidates worth monitoring
- `data/rejected.jsonl` — rejected ideas and reasons
- `reports/` — human-readable candidate research
- `prompts/scan.md` — recurring scan protocol
- `prompts/validate.md` — deep-validation / red-team protocol

## Current rule
Do not build anything substantial from a score alone. The next meaningful promotion criterion is willingness to engage with real workflow data and, preferably, willingness to pay for a concierge/manual pilot before integration work.
