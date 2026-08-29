# Audit — Constraint-aware dental schedule QA

**Decision:** keep, but treat as a validation candidate rather than a proven business.

## What is strongly supported

- A dentist explicitly describes repeated front-desk scheduling failures after seminars, meetings, cheat sheets and a practice consultant. Their examples include one scanner shared by two doctors being booked simultaneously, root canals/equipment conflicts, bad new-patient slot selection, and low-production sequencing. They explicitly ask for an AI interface that guides staff and offers three valid appointment options.
- Another commenter says they would be interested in the same kind of product for front-desk guidance.
- Separate dental-hygiene discussions repeatedly describe double/staggered booking as a source of stress, rushed care and burnout.
- Another dentist asks how to improve variable appointment durations without overwhelming the admin team, showing that rule complexity itself is a scheduling problem.
- Existing dental software spend is meaningful; practices already pay for PMS and front-desk add-ons when they reduce staffing burden.

## Competition check

Competition is stronger than the initial hypothesis implied. Dental Intelligence and many PMS products expose automated scheduling features. Newer products such as NexV and CareFlow explicitly market production-aware optimization, gap filling and AI scheduling.

The remaining wedge must therefore be narrower:

> **Practice-specific scheduling guardrails / QA inside the existing PMS**, focused on validating a booking against equipment, assistant/provider, procedure, duration, sequencing and production constraints before it is accepted — not another patient receptionist, generic calendar, or cancellation filler.

## Updated assessment

- Pain: high
- Frequency: high
- Willingness to pay: high, but not yet proven for this exact wedge
- Evidence quality: high
- Reachability: good
- Competition gap: moderate, not high
- Buildability: moderate due to PMS integrations and healthcare data constraints
- Founder-interest score remains neutral until user feedback

**Updated score: ~78/100.** It stays above the deep-validation threshold, but should not receive more investment until a concierge test produces paid pilots.

## Cheapest decisive test

1. Interview 15–20 owner-dentists / practice managers.
2. Ask for anonymized screenshots or exports of one week of appointments plus their scheduling rules.
3. Manually audit the schedule and return conflicts + better slot options.
4. Ask for €99–€249 to repeat the audit or configure their rules for a pilot.
5. Stop if fewer than ~3 practices show strong pain or nobody will pay before an integration exists.

## Verified public evidence

- https://www.reddit.com/r/Dentistry/comments/1onghkk/ai_scheduler/
- https://www.reddit.com/r/Dentistry/comments/1pscb7g/front_desk_scheduling_feels_like_constant_chaos/
- https://www.reddit.com/r/DentalHygiene/comments/1rl6olp/double_bookedassisted_hygiene/
- https://www.reddit.com/r/DentalHygiene/comments/1sb2ll4/scheduling_for_dental_hygienists/
- https://www.reddit.com/r/DentalHygiene/comments/1p7rdk3/is_doublebooking_just_the_expectation_now_in/

## Competition references

- https://nexv.ai/product/schedule-optimizer
- https://www.careflowdental.com/features/scheduling
- GetApp dental software / automated scheduling category (73 products as of August 2026)
