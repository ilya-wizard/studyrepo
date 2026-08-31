# Problem Hunter Scan — 2026-08-31

## Result
No new candidate passed the >=78 promotion threshold.

## Themes checked

### 1. Windows update / BitLocker / Windows Hello recovery readiness
Fresh evidence: a 21 Aug 2026 r/Intune thread reports BitLocker recovery prompts and Windows Hello PIN failures after KB5120994 / KB5123607 in some managed Windows environments, with additional admins reporting similar incidents. Microsoft separately documents BitLocker recovery risk around incompatible PCR7 policy configurations on current Windows updates.

Potential second-order workflow: pre-update fleet readiness / recovery-key verification / TPM-PCR policy audit for MSPs and Intune admins before staged rollout.

Why not promoted:
- the current incident may be transient/vendor-specific rather than a durable market;
- Intune and Microsoft already expose recovery keys, compliance status, rollout rings and BitLocker policy controls;
- no repeated evidence yet that MSPs will pay for a separate preflight layer rather than scripts/RMM/Intune policy;
- product risks collapsing into a feature of existing patch-management/RMM platforms.

Reopen if 3+ MSPs or endpoint teams report repeated failed recovery-key availability / PCR-policy drift across clients and will pay for an automated preflight audit before patch waves.

Sources:
- https://www.reddit.com/r/Intune/comments/1vud43r/bitlocker_whfb_issues_after_august_2026_patch/
- https://support.microsoft.com/en-us/servicing/os/windows-10/2026/08/kb5120249-windows-10-21h2-22h2-security-update

### 2. Dating-app trust / romance-scam verification
Fresh signals remain very strong: users report suspicious paywall behavior, fake/bot profiles, verified profiles used in suspected romance scams, and poor trust in platform verification.

Why not promoted:
- the solution space is already crowded with romance-scam detectors, reverse-image tools, liveness verification and chat analyzers (Love Llama, GotCatfished, SnapTrust, VerifyDating, DateCheck, SocialFinder, etc.);
- distribution is expensive in B2C safety apps;
- willingness to pay for an independent verification layer is unclear and free alternatives are plentiful;
- the strongest pain is partly caused by the dating platforms themselves, making platform-level distribution/integration difficult.

Sources:
- https://www.reddit.com/r/Bumble/comments/1vpzvth/my_subscription_was_going_to_expire_and_boom_i/
- https://www.reddit.com/r/datingoverfifty/comments/1vuzdjf/old_isnt_even_trying_to_come_off_as_credible/
- https://www.reddit.com/r/Scams/comments/1vznxay/eudoes_this_sound_like_the_early_stage_of_a/
- https://lovellama.ai/
- https://gotcatfished.com/
- https://snaptrust.app/use-cases/online-dating

### 3. CRA incident reporting
The forcing event remains unusually strong: reporting duties begin 11 Sep 2026 with 24h/72h deadlines, and current guidance indicates the ENISA SRP initially lacks an API, making the submission workflow manual.

Why not reopened:
- generic CRA reporting is already in rejection memory;
- CRA-specific vendors, consultancies and product-security platforms already target the workflow;
- no fresh primary evidence surfaced a repeated second-order failure in legal-security handoff, evidence ownership, or SRP submission that survives competitor comparison.

Sources:
- https://www.crowell.com/en/insights/client-alerts/eu-cyber-resilience-act-countdown-11-september-2026-incidentvulnerability-reporting-deadline-is-less-than-100-days-away
- https://www.telit.com/blog/cra-vulnerability-reporting-september-2026/

## Decision
No user notification. Continue searching for second-order failures inside workflows where customers already pay for incumbent software but still maintain a costly manual exception process.