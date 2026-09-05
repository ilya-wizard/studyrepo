> Historical research. Current stages and scores live in `data/opportunities.jsonl` and generated `CURRENT_STATE.md`. Reopen original sources before relying on claims; historic assistant interest ratings are not user feedback.

# Candidate: Dental Schedule QA Copilot

**Decision:** VALIDATE NOW  
**Score:** 79.8/100  
**Wedge:** internal front-desk schedule guardrails and repair suggestions; not an AI receptionist and not a PMS replacement.

## Problem
Dental scheduling is a constraint problem disguised as a calendar. A booking may look free while still being wrong because two doctors need the same scanner, an assistant is unavailable, a procedure needs a particular chair, appointment duration is unrealistic, or the day becomes economically poor because production-heavy procedures were not balanced correctly.

Practices currently encode these rules in staff knowledge, cheat sheets, color coding, flowcharts, consultants, and repeated training. When the rules are missed, the result is double booking, delays, idle capacity, lost production, staff stress, and sometimes rushed care.

## Strongest evidence
1. **Direct product request — Nov 2025:** a dentist says they do *not* want an AI receptionist. They want an interface that guides staff, detects shared-equipment/procedure conflicts, applies their scheduling logic, and offers three valid alternatives. Other dentists in the thread express interest.  
   https://www.reddit.com/r/Dentistry/comments/1onghkk/ai_scheduler/

2. **Admin chaos — Dec 2025:** a solo dentist says phone + text/WhatsApp scheduling causes missed calls, double bookings and no-shows and asks what software or process is actually worth paying for.  
   https://www.reddit.com/r/Dentistry/comments/1pscb7g/front_desk_scheduling_feels_like_constant_chaos/

3. **Staff consequences — Dec 2025 / Mar 2026:** hygienists describe inconsistent and double-booked schedules causing burnout, physical pain and rushed care.  
   https://www.reddit.com/r/DentalHygiene/comments/1ptak2z/dental_hygienist_2nd_year/  
   https://www.reddit.com/r/DentalHygiene/comments/1rl6olp/double_bookedassisted_hygiene/

4. **Existing products still feel wrong — Jul 2026:** a developer building for a dentist reports that existing scheduling products were hard to use, overbuilt, or priced for much larger organizations.  
   https://www.reddit.com/r/promoteMyApp/comments/1usowud/my_sister_runs_a_dental_practice_and_hated_every/

## Market validation / competition
The market is not empty. Dental Intelligence offers scheduling; Kairos Health AI encodes scheduling rules inside an AI receptionist; NexV markets schedule optimization; SmartChair.AI measures chair utilization; custom firms are building predictive schedulers.

That is both positive and dangerous: money is clearly being spent, but a generic "AI dental scheduler" would be too broad and crowded.

### Defensible first wedge
**Schedule QA layer:** connect to or import the existing PMS schedule and act like a linter for appointments.

For every booking/change:
- detect hard conflicts (doctor, chair, assistant, equipment)
- check practice-specific flow rules
- warn about unrealistic durations/sequencing
- flag production/capacity anomalies
- return 3 compliant alternative slots with reasons

The product initially does not talk to patients, answer phones, replace the PMS, or autonomously make clinical decisions.

## €500 validation experiment
Do not build integrations first.

1. Recruit 15-20 owner-dentists/practice managers through direct outreach and dental communities.
2. Ask them to show the last scheduling mistake that cost time, money, or stress.
3. For 3 practices, manually encode their scheduling rules in a small ruleset.
4. Have them export or anonymize one week of schedule data.
5. Produce a manual "schedule lint" report: conflicts, suspicious bookings, empty high-value capacity, and three suggested repairs.
6. Ask for **€99-€249 for a paid pilot** that checks the next 2-4 weeks.

Success criterion: at least 2 paid pilots or 5/15 practices willing to provide real schedule data and actively request integration.

## Main risks
- PMS APIs/integrations may be the hardest technical bottleneck.
- Incumbents can copy the feature.
- Rules vary substantially by practice.
- Recommendations need clear human approval to avoid clinical/operational liability.
- Front-desk teams may resist software perceived as monitoring them.

## What would kill the idea
Reject if interviews show that scheduling errors are mostly management/staff-performance problems that owners prefer to solve by hiring/training, or if existing PMS products already enforce the needed constraints well enough once configured.

## Next research question
Is the highest-value entry point **real-time booking guardrails**, **overnight schedule QA**, or **production/capacity optimization**? The first interviews should determine this rather than assuming it.
