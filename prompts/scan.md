# Opportunity Hunter Scan Protocol

## Mission
Find product opportunities worth caring about and building, not merely monetizable inefficiencies.

The core intersection is:
1. a meaningful human problem or aspiration,
2. genuine founder pull — intellectually or creatively interesting enough to work on for years,
3. a real new lever from modern AI/agents,
4. credible adoption and monetization.

Primary question:

> What still works surprisingly badly for people despite the arrival of AI, and what can now be done that was impractical 2–3 years ago?

Separate **problem quality** from **solution quality**. A bad first product concept must not cause a strong underlying problem to be rejected.

## Priority domains
Search broadly, with extra attention to:
- loneliness and social connection
- relationships and dating
- learning and personal development
- mental wellbeing and self-regulation
- embodiment, movement and physical development
- creativity
- travel and real-world exploration
- work, meaning and useful productivity
- money and personal autonomy
- life administration and decision-making

Adjacent domains are allowed when the opportunity is unusually strong.

## What counts as a strong signal
Look for repeated evidence that people:
- struggle with an important outcome,
- repeatedly fail with current tools or methods,
- spend money, time, attention or emotional energy trying to solve it,
- build workarounds or combine multiple products,
- abandon existing products because they do not create the desired outcome,
- explicitly ask for something that does not exist,
- exhibit a behavior that a new AI capability could materially improve.

Search Reddit, specialist forums, app reviews, product reviews, research, creator communities, GitHub discussions, public professional discussions, niche communities, and other primary sources.

Do not confuse loud complaints with important problems. Prefer repeated behavior over stated preferences.

## AI-leverage test
For every promoted candidate, answer:
- What specifically became possible or economically viable because of current AI/agents?
- Could this product have been built almost as well in 2022–2023?
- Is AI core to the product behavior, or merely a chat interface / content-generation layer?
- Does memory, personalization, multimodality, agentic action, reasoning, simulation, or cheap generation create a qualitatively different product?

If AI is cosmetic, penalize heavily.

## Human-importance test
Ask:
- Does solving this materially improve someone's capability, relationships, wellbeing, autonomy, creativity, learning, income, or experience of life?
- Is the outcome meaningful enough that users already invest effort in it?
- Is this more than a small convenience or minor time saving?

A narrow problem can still be important. A large market with trivial human value is not automatically attractive.

## Founder-pull test
Ask:
- Is the problem rich enough to keep learning about?
- Is there room for product invention rather than only implementation?
- Would building it create curiosity rather than obligation?
- Does the problem involve human behavior, systems, interaction, or a genuinely new product model?

Founder pull is a first-class criterion, not a tie-breaker.

## Strongly deprioritize
Unless there is an unusually large human or strategic consequence, down-rank:
- generic compliance/regulation tooling
- invoicing/bookkeeping
- CRM and commodity workflow automation
- procurement/document chasing
- back-office efficiency products
- vertical SaaS whose main benefit is administrative convenience
- products whose pitch is mainly “save a few minutes”

Reject generic AI wrappers and cosmetic AI differentiation.

## Evidence capture
For each signal capture:
- date + source URL
- precise user/segment
- observed behavior or complaint
- current workaround / spend / effort
- intensity and recurrence clues
- desired outcome
- why current alternatives fail
- what is observed vs inferred
- confidence

Prefer 3+ independent sources before promotion and 5+ before serious validation where feasible.

## Candidate synthesis
For every candidate explain plainly:
1. Who has the problem?
2. What are they trying to achieve?
3. What happens today instead?
4. Why does this matter in their life?
5. What do they already spend — money, time, attention or emotional effort?
6. Why do existing solutions fail?
7. What new AI lever exists now?
8. What product directions are plausible? Keep multiple directions open when appropriate.
9. What behavior change would the product require?
10. How could the first users be reached?
11. How might it monetize?
12. What would make the opportunity false?

## Promotion gate
Promote only when:
- the underlying problem is meaningful,
- evidence is repeated and segment-specific,
- founder pull is high enough to justify further attention,
- AI provides a real new lever,
- existing alternatives are meaningfully inadequate,
- adoption does not require implausible behavior change,
- there is at least a plausible distribution and monetization path.

Do not promote an idea simply because a buyer exists.

## Scoring
Use `config/scoring.json`.

Always report these three summary scores:
- **Human importance**
- **Founder pull**
- **Business potential**

The numerical score is subordinate to judgment. A commercially strong but uninspiring administrative tool should not become PRIORITY.

## Output
Keep candidate reports concise and concrete:
- problem + target user
- why it matters
- strongest evidence
- current alternatives and failure mode
- why now / AI lever
- possible product direction(s)
- behavior-change burden
- monetization + acquisition
- <= €500 validation test
- strongest argument against
- Human importance / Founder pull / Business potential

If nothing feels genuinely worth building, return no candidate rather than filling the backlog with mediocre ideas.
