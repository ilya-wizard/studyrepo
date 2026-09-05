# Capturing founder feedback

Use normal conversation. When presenting at most three options, ask which is worth exploring and why. An optional compact prompt: 'Что цепляет: аудитория, проблема или сам продукт? Насколько хочется этим заниматься — 0–10?'

Record actual replies in data/feedback.jsonl with source_ref and date; never fill absent answers. Explicit numeric ratings alone feed founder_pull. Keep attraction, aversion, reaction, daily-work/audience preference and reason category separate. 'Скучно' with no explanation gets reason_category=unspecified; do not invent its cause.

One idea rejection is not a domain ban. Only explicit broad feedback updates profile. Unknown interest remains null and early discovery continues. When the user explicitly selects a test, record that source, set selected_by_user, activate its experiment and update cycle.active_experiment_id atomically; do not activate another until the first is stopped/completed.

This is a public repository: keep only non-sensitive feedback appropriate to business research. Never store identifiable participant records or private communications; use redacted evidence and safe references.
