> Historical research. Current stages and scores live in `data/opportunities.jsonl` and generated `CURRENT_STATE.md`. Reopen original sources before relying on claims; historic assistant interest ratings are not user feedback.

# Candidate: German E-Invoice Legacy Bridge

**Final decision:** REJECTED — do not pursue further
**Rejected:** 2026-08-29
**Previous preliminary score:** ~80/100

## Wedge originally considered
A compatibility layer for German SMEs with custom/legacy billing systems: map existing invoice exports/data into compliant XRechnung/ZUGFeRD, validate against EN 16931/business rules, generate/send/receive E-Rechnungen, and keep formats current without replacing the company's ERP or bespoke software.

## Why the pain looked promising
A fresh German Reddit discussion (28 Aug 2026) described firms with custom software facing implementation costs of several thousand euros plus significant internal effort just to become compliant, with frustration around ZUGFeRD implementation quality.

## Why this is rejected
The underlying pain is real, but the proposed wedge is already directly served by multiple vendors. Existing products already offer combinations of:
- legacy ERP / bespoke-system integration;
- JSON/data-to-XRechnung/ZUGFeRD conversion;
- EN 16931 validation;
- inbound and outbound E-Rechnung handling;
- ongoing format/compliance updates;
- fixed-price integration for old or custom systems;
- AI-assisted mapping and PDF/DOCX/XLSX-to-E-Rechnung conversion.

The strongest originally proposed differentiation — "implementation-as-product" for arbitrary legacy systems without replacing the ERP — is therefore not sufficiently differentiated. No compelling second-order problem or underserved segment was identified during follow-up research.

## Decision
Stop research and remove from active ranking. Preserve as rejected so the same idea is not rediscovered unless new evidence reveals a materially different wedge.

## Revisit only if
New evidence shows a specific legacy-system segment, workflow, distribution channel, or compliance problem that existing bridge/API vendors consistently fail to serve.
