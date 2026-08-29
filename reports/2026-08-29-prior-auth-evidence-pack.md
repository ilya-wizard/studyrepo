# Candidate: Prior Authorization Evidence-Pack Copilot

**Preliminary decision:** DEEP VALIDATE
**Preliminary score:** ~83/100

## Wedge
For small US medical practices, assemble payer-specific prior-authorization evidence packs from the chart: identify whether PA is needed, extract the exact clinical proof each payer wants, map it to the payer's criteria language, track renewals/denials, and prepare appeal packets. Human submits/approves.

## Why this is interesting
Recent clinicians describe prior auth volume overwhelming small practices, payer criteria being hard to find, buggy/sparse pre-filled forms, long backlogs, and denials caused by wording/documentation mismatch. Another PA worker says the information is usually already in the chart; the work is repeatedly finding and restructuring it for each payer.

## Strong public signals
- r/FamilyMedicine, Aug 2026: small practice says PAs are "drowning us"; 1-2 per patient, diverse payer rules, CoverMyMeds is useful but buggy/sparse.
- r/FamilyMedicine, Jun 2026: practices report GLP-1-driven PA volume and backlogs growing from ~1 week to ~6 weeks; denials/appeals are a major time sink.
- r/PriorAuthorization, Jul 2026: practitioner says the answer is usually in the chart but must be reassembled into each payer's exact criteria language.
- r/healthIT, Sep 2025: provider-side user describes confusion over whether PA is needed and which entity handles it (payer, IPA, third party), especially with multiple coverage.

## Why now
CMS operational requirements begin in 2026 and major prior-authorization FHIR API requirements begin in 2027 for impacted payers, making payer rules/status increasingly machine-accessible. This creates a transition window for workflow products on top of existing EHRs rather than full RCM replacements.

## Validation under EUR 500
Recruit 10-15 small specialty practices. Take 20 recent PA cases (de-identified or synthetic for first tests). Manually produce payer-specific checklists/evidence packs and compare time-to-submit, missing documentation, and denial rate. Ask for a paid pilot before integrations.

## Biggest risks
HIPAA/security, EHR access, payer variability, strong incumbents, legal/clinical workflow liability, and the possibility that payer/EHR-native tools absorb the wedge.
