# Candidate: German E-Invoice Legacy Bridge

**Preliminary decision:** DEEP VALIDATE
**Preliminary score:** ~80/100

## Wedge
A compatibility layer for German SMEs with custom/legacy billing systems: map existing invoice exports/data into compliant XRechnung/ZUGFeRD, validate against EN 16931/business rules, generate/send/receive E-Rechnungen, and keep formats current without replacing the company's ERP or bespoke software.

## Why this is interesting
A fresh German Reddit discussion (28 Aug 2026) describes firms with custom software facing implementation costs of several thousand euros plus significant internal effort just to become compliant, with frustration around ZUGFeRD implementation quality.

## Regulatory tailwind
Germany introduced mandatory B2B e-invoicing rules from 1 Jan 2025 with transition periods. General issuance remains possible in non-E-invoice form through end-2026; businesses with prior-year turnover up to EUR 800k have an extended transition through end-2027. Receiving capability has already been required since 2025. XRechnung and qualifying ZUGFeRD formats satisfy the structured e-invoice requirements.

## Competition
There are already APIs/services that generate and validate XRechnung/ZUGFeRD, including products explicitly targeting legacy systems. Therefore the opportunity is not another raw XML API. The possible wedge is implementation-as-product: inspect an arbitrary old system, infer/map its invoice fields, validate outputs, and provide a low-touch adapter plus ongoing compliance updates.

## Validation under EUR 500
Interview 15 German SMEs/software houses using bespoke ERP/Access/FileMaker/industry systems. Offer a fixed-price conversion proof: take one current PDF/CSV/export and return a validated XRechnung/ZUGFeRD plus a mapping report. Test willingness to pay EUR 300-1500 for setup plus recurring compliance/transport service.

## Biggest risks
Crowded API market, accounting vendors may solve this natively, legacy systems vary wildly, support burden can turn SaaS into consultancy, and German tax/compliance expectations require high reliability.
