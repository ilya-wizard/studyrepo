# Problem Hunter — Current State

Updated: 2026-08-30

## Search profile
- Markets: B2B + B2C
- MVP duration: flexible; idea quality matters more than speed
- Initial validation budget: <= €500
- Domains allowed: broad, including health, dating, enterprise, hardware, marketplaces
- Reject generic AI wrappers, hypothetical-demand ideas, one-off complaints, saturated categories without a wedge, and ideas requiring large paid acquisition before validation.

## Validation pipeline
Signal -> customer-research synthesis -> independent evidence -> buyer/spend -> competition -> switching dynamics -> distribution / first-customer signals -> why now -> test price + <=€500 experiment -> scoring -> promotion gates -> red-team -> promote/watch/reject.

## Marketing validation layer — added 2026-08-30
Selected patterns from `coreyhaines31/marketingskills` are now integrated into the operating protocols:
- customer research: five signal buckets, confidence, recency, bias checks, customer language
- competitor profiling: direct/secondary/manual/do-nothing alternatives, pricing, complaints, product direction
- product marketing: user vs economic buyer, JTBD, switching forces
- pricing: next-best alternative, value metric hypothesis, explicit test price
- prospecting: top 10 evidence-backed first-customer prospects before claiming distribution is strong
- offers/cold email: concrete validation offer + low-friction source-based outreach; never auto-send without explicit authorization
- marketing loops: self-check, state/deduplication, stop conditions, notify only on meaningful change

The deterministic scoring weights remain unchanged. These additions operate as **promotion gates**, not extra score dimensions.

## Promotion gates
A candidate cannot become PRIORITY from score alone. Deep validation must explicitly pass:
1. Research quality
2. Competition gap
3. Monetization / test price
4. Evidence-backed reachability
5. Disconfirmation / red-team quality

A failed gate can keep a candidate in WATCH even when the score is high.

## Fresh scan after marketing-skill integration — 2026-08-30
A broad fresh scan was run using the new gates. **No new theme passed the scan promotion gate**, so no new formal candidate or score was created.

Closest misses:
1. **Multi-marketplace settlement reconciliation** — unusually strong measurable pain at a ~$16m ecommerce brand, but insufficient independent evidence for the exact wedge and custom marketplace reconciliation already exists (including Cointab). Reopen only if 3+ mid-market brands identify the same unsupported marketplace/fee logic and one will pay for a manual pilot.
2. **Cyber Resilience Act incident-reporting workflow** — exceptional timing because 24h/72h reporting obligations begin 11 September 2026, but generic CRA/SBOM/reporting products already exist and no surviving second-order workflow has repeated user evidence yet.
3. **PE/VC portfolio-company reporting normalization** — recurring heterogeneous monthly reporting is real, but Standard Metrics, Rundit and other portfolio-monitoring products directly cover collection/normalization/reporting. Reopen on explicit incumbent rejection + paid managed-service demand.

Other fresh themes rejected before scoring: COI/vendor insurance tracking, accounting/tax client document chasing, CBAM supplier-data collection, EUDR compliance, PPWR packaging compliance, freight invoice audit, nonprofit post-award grant tracking, and customer-specific PPAP/spec documentation.

Full scan: `reports/scan-2026-08-30-marketing-gates.md`.

### Search implication
Future scans should bias toward **second-order failures of products people already pay for**, rather than generic categories created by regulation or obvious manual work. Highest-value evidence now includes:
- paid incumbent + persistent manual exception workflow
- explicit switching because one workflow remains broken
- a recent change that breaks incumbent behavior
- a narrow segment where general-purpose tools are structurally too heavy, expensive or incompatible
- willingness to pay for a manual/concierge fix before software exists

## Current ranking after red-team review
1. **Prior Authorization Evidence-Pack Copilot — 74.8/100 (demoted from 83.1).** Pain and regulatory tailwind remain excellent, but the original wedge is now directly served by Humata Health, EasyPA, Roseate, HiPaaS and Optum/Humata. Do not build generic PA evidence-pack automation. Reopen only around a specialty/payer-specific second-order workflow incumbents demonstrably fail.
2. **Dental Schedule QA Copilot — 74.0/100 (demoted from 78.2).** Pain remains real, but fresh competitor review shows Dentina booking with practice rules/right providers/operatories plus NexV and DSM scheduling optimization. Continue only through real-practice discovery and paid audit evidence.
3. **Construction AI Takeoff — ~72/100.** Watchlist only; crowded category and no sharp wedge.

## No current >=78 candidate
The portfolio currently has no idea strong enough to recommend building. This is intentional: red-team validation should remove attractive-looking ideas when direct competition collapses the wedge.

## Rejected memory
`data/rejected.jsonl` is the authoritative rejection memory. It now includes the 2026-08-30 fresh-scan themes so generic versions are not rediscovered repeatedly.

## Decision thresholds
- <68: watch or reject
- 68–77.9: deep validation / watch
- >=78: strong candidate only if promotion gates pass
- >=86: priority candidate only if promotion gates pass

## Current rule
Do not build from a score alone. Promotion requires evidence that a specific underserved workflow survives direct competitor comparison, a credible first-customer path, and preferably willingness to pay for a concierge/manual pilot before integrations.
