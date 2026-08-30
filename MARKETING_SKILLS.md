# Marketing Skills Integration

This repository selectively adapts research and validation patterns from:

- https://github.com/coreyhaines31/marketingskills

The goal is **not** to turn Problem Hunter into a general marketing agent. Only patterns that improve opportunity discovery, commercial validation, and first-customer evidence are included.

## Skills used

### customer-research
Integrated into `prompts/scan.md` and `prompts/validate.md`:
- digital watering-hole research
- Jobs to Be Done extraction
- trigger events, alternatives and customer language
- frequency + intensity synthesis
- confidence levels
- recency and sample-bias checks
- segment-specific evidence instead of invented personas

### competitor-profiling
Integrated into deep validation:
- facts over opinions
- consistent competitor dimensions
- direct / secondary / indirect alternatives
- pricing, positioning, capabilities, reviews and product-direction signals
- customer complaints as the basis for a wedge

### product-marketing
Adapted for candidate-specific market briefs:
- user vs economic buyer
- JTBD
- pain + cost
- competitor landscape
- differentiation hypothesis
- JTBD switching forces: Push / Pull / Habit / Anxiety

Problem Hunter does **not** create one global product-marketing context because each opportunity is a different potential product.

### pricing
Integrated into validation:
- next-best alternative as a pricing anchor
- value metric hypothesis
- current spend/cost evidence
- an explicit test price chosen to learn from real buyers
- avoid ultra-cheap pricing that creates false validation

### prospecting / demand-signals
Integrated into distribution validation:
- first-customer discovery starts from evidenced pain, not only firmographic fit
- top prospects require a cited public signal
- pain / switching / workaround / timing stages
- prefer ten strong evidence-backed matches over a large generic lead list

### offers + cold-email
Used narrowly for validation experiments:
- define a concrete deliverable and outcome
- reduce time-to-value and customer effort
- honest risk reversal where useful
- one low-friction CTA
- source-based outreach: observation -> problem -> offer -> question
- no automatic sending without explicit authorization

### marketing-loops
Applied to the scheduled research system:
- cadence should match signal speed
- every loop needs a self-check, persistent state/deduplication, stop/bail-out rules and output criteria
- most runs should be allowed to produce "no meaningful change"
- notify only when a candidate crosses a threshold or material evidence changes

## What was intentionally not imported

Most acquisition/content skills are irrelevant before a strong opportunity exists, including SEO, ads, social, CRO, copywriting, referral and lifecycle marketing.

The repository also keeps its existing deterministic scoring model. The marketing layer adds **promotion gates** rather than adding more weighted score dimensions.

## Promotion gates

A candidate cannot become PRIORITY solely because its numerical score is high. Deep validation explicitly checks:

1. **Research quality** — enough independent, segment-specific, sufficiently recent evidence.
2. **Competition gap** — the exact workflow survives comparison with direct and indirect alternatives.
3. **Monetization** — existing spend/value or a credible paid test, with a test price.
4. **Reachability** — evidence-backed first-customer prospects and a realistic contact path.
5. **Disconfirmation** — serious failure cases have been researched and evidence that would reverse the decision is stated.

A failed gate can keep a candidate in WATCH even when its score is high.

## Source and license

The upstream `marketingskills` repository is MIT-licensed. Problem Hunter uses adapted concepts and workflows rather than vendoring the complete skill library.
