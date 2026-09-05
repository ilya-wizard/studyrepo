# Focused opportunity discovery — v2.0

Read README, CURRENT_STATE, profile, cycle, scoring, canonical registry, feedback, observations and the last two run records. If repo access fails, report the access failure once and make no claim of persistence or a fresh exhaustive scan.

## Allocate attention
Use the two audiences in config/cycle.json. Spend roughly 80% of research effort on their concrete situations and 20% on adjacent surprises. Do not impose narrow B2B back-office filters. Keep the approved focus on meaningful human outcomes, founder interest and genuinely useful AI. MVP duration is flexible; test budget is <=€500.

## Research situations before inventing products
For each audience ask what happened the last time the person tried to achieve an outcome, what they did, which tools/people they used, what they invested and what failed. Search separately for recent attempts, repeated workarounds, switching, existing spending, abandonment and successful alternatives. Read original discussions, replies and product pages; detect founder promotion and copied stories. Marketing pages establish offers/features, not user outcomes or sales volume.

User observations, voluntarily shared interview notes and actual test results are first-class sources. Record redacted entries in observations with observation_id, date, candidate_id (or null), audience_id, source_ref, observed_fact, interpretation, consent/safe-to-share status, confidence and follow-up question. Do not infer private contacts or a user's access to a community.

## Evidence discipline
Each evidence record has stable ID, source URL (or safe first-party source_ref), source publication date if known, retrieved date, exact supported claim, interpretation, source kind, verification state, independence key, confidence and contradictions. Do not invent dates, quotes or independence. Reposts/press coverage of one announcement count as one origin. Unavailable sources remain unverified/inaccessible. Preserve negative evidence.

## Explore gate
An EXPLORE record needs a concrete segment, important situation and at least an initial credible signal. Unknown founder interest is labeled 'awaiting user feedback' and does not stop discovery. Do not require five sources, paid intent, retention proof or high score before learning. Candidate should include 2–3 possible solutions when useful and the cheapest next uncertainty check. Avoid speculative generic AI wrappers.

A competitor alone does not kill a problem. Ask whether the same segment has tried it, what outcome failed and why. Separate 'vendor advertises capability' from 'users achieved outcome'. Compare geography, price, trust, setup, distribution and real results. Reject a solution scope, not the entire problem, unless evidence supports that broader decision.

## Feedback and deduplication
Check every registry stage by stable candidate ID, segment, desired outcome and semantic similarity before adding. Exact hash matching is only a backstop. Attach new evidence to the existing opportunity even if its stage changed. Reopen rejected solutions only on their recorded trigger; allow a different solution for a surviving problem.

Never assign founder_pull. Quote or summarize actual user feedback with provenance; only an explicit 0–10 rating goes into the score. 'Interesting' is a reaction, not permission to translate it to 9/10. Track whether the rejection concerns audience, problem, daily work, business model, distribution or something else; do not generalize one rejection to a whole field.

## End each pass
Update the canonical records and append a run log: run_id, date, criteria_version, cycle_id, audiences, actual queries/source URLs, new independent signals, changed candidate IDs, decision_changes, no_change_reason, next_question, actual experiment progress, notified_event_keys. Log zero new results honestly.

After two focused passes without material new evidence, stop the query family, change source/audience or prepare field research. Do not keep scanning a prepared experiment's already-established problem while its next learning requires people. Continue useful preparation without pretending fieldwork happened.

Run schema/provenance checks, regenerate views/state and commit together against latest remote head. Never force-push; re-read and merge changes if another session has written.

At most three items per cycle for user choice; fewer or none is fine. Notify only for useful new options, changed evidence or a concrete decision. Use plain Russian: who, situation, evidence, possible product, uncertainty, first-user route, test. Show human importance and business potential as provisional if assessed; founder interest stays unknown until the user rates it. Scores do not suppress an interesting early discovery.
