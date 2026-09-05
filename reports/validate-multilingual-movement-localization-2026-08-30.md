> Historical research. Current stages and scores live in `data/opportunities.jsonl` and generated `CURRENT_STATE.md`. Reopen original sources before relying on claims; historic assistant interest ratings are not user feedback.

# Validation — Multilingual movement creator localization studio

Date: 2026-08-30

## Plain-language idea
Take yoga, Pilates, fitness, dance, breathwork or other movement teachers who already have a successful course/library in their native language and turn that existing content into a sellable product for another language market — initially English or another high-demand language.

The service can range from dubbing only to full market expansion: translation, teacher-voice dubbing, movement-specific terminology QA, subtitles, localized landing pages, platform upload, launch assets, and distribution. Commercial model can be project fee, revenue share, or a hybrid.

## Decision
**VALIDATE / WATCH — provisional score 76.2/100.**

This is materially more interesting than generic dubbing because the technology itself is already commoditized. The possible wedge is **international expansion as a managed service for movement creators**, where accurate cueing, brand voice, course packaging and market launch matter.

Do not build software first. Test it as a service.

## Evidence

### 1. Language blocks instructors from international reach
- English Yoga Academy sells an 8-week program specifically because non-native yoga teachers feel held back teaching in English and want international audiences: https://englishyogaacademy.com/teachlikeapro
- Loka Yoga School sells a dedicated English-for-yoga-teachers course and explicitly frames English vocabulary/cueing as necessary to teach internationally and safely: https://lokayogaschool.com/online-english-course-for-yoga-teachers/
- A Korean Pilates instructor sells a 247-page bilingual English cueing guide aimed at instructors who want to teach globally: https://leegster78.gumroad.com/l/llhnbz

These are not direct requests for dubbing, but they are strong willingness-to-pay proxies for the underlying language barrier.

### 2. Multilingual video is already producing measurable creator value
YouTube states that creators who uploaded multi-language audio saw more than 25% of watch time come from non-primary-language views. YouTube now supports automatic dubbing broadly, which validates demand but also makes basic dubbing less defensible: https://support.google.com/youtube/answer/13338784 and https://support.google.com/youtube/answer/15569972

### 3. Exact business model already exists outside the movement niche
Lingrow translates and dubs existing courses, uploads the localized version, and offers revenue-share deals. It claims localized versions can add meaningful incremental revenue and explicitly supports co-instructor revenue share on Udemy: https://lingrow.me/

Udemy formally supports co-instructors and configurable revenue sharing, so the model is operationally feasible on that platform: https://support.udemy.com/hc/en-us/articles/229605728-Co-instructor-relationships-Rules-and-guidelines and https://support.udemy.com/hc/en-us/articles/229605008-Instructor-revenue-share

### 4. Production cost has collapsed
Self-serve AI dubbing is cheap enough that localization can have strong service margins:
- HeyGen Creator: $29/month; video translation capacity is credit-based; audio-only dubbing is now unlimited on paid plans: https://www.heygen.com/pricing
- ElevenLabs automatic dubbing: roughly $2–$3/minute on common paid tiers for current Dubbing v2 pricing: https://elevenlabs.io/dubbing-studio
- Rask starts around $60/month for 25 minutes, with larger annual bundles: https://www.rask.ai/pricing
- CourseLocalize charges customers from $10/min for standard dubbing and $20/min for premium dubbing: https://courselocalize.com/

This means the value is not generating the audio. The value must be QA + packaging + launch + distribution.

### 5. Movement content has a real specialization angle
Movement instruction is unusually language-sensitive because timing and wording affect what the student physically does. Pilates/yoga sources emphasize that short, precise, well-timed cues are central to safe/effective instruction, and terminology differs across lineages and languages:
- https://corevapilates.com/pilates-terminology-glossary/
- https://www.pilatesplans.com/en/blog/pilates-cueing-guide
- https://yogajala.com/yoga-cueing-guide-for-teachers/

This supports a domain-specific glossary / human QA wedge over generic one-click translation.

## Competition

### Direct technology
HeyGen, ElevenLabs, Rask, LipDub, Synthesia, Speechlab and similar tools can already translate/dub content while preserving or cloning the speaker's voice. Therefore **"we dub your videos with AI" is not a business wedge.**

### Direct services
- CourseLocalize AI — course localization at $10–20/minute.
- Lingrow — course localization plus revenue share / launch support.
- Traditional e-learning localization agencies — more expensive but stronger human QA.

### Platform threat
YouTube auto-dubbing is free for eligible content. This destroys much of the value proposition for basic YouTube dubbing, but it can also be used as a free demand test before localizing a paid course.

## Surviving wedge

**International expansion studio for movement creators.**

Instead of selling dubbing, sell an outcome:
> "You already built a successful Polish/Spanish/German/Ukrainian yoga or Pilates library. We launch it in English without you re-recording anything, and we only win when the new market makes money."

Specific specialization:
- teacher's own voice / brand preserved
- movement/anatomy terminology glossary
- human review of safety-critical cues, breathing, left/right, timing and transitions
- localized title, description, thumbnails, sales page and course materials
- choose market based on analytics rather than blindly translating every language
- publish/operate the localized course or channel
- optionally run launch/distribution and share revenue

## ICP
Best first customer:
- established independent yoga/Pilates/fitness teacher or small school
- already has 5–50+ hours of polished recorded content
- already sells membership/course successfully in one non-English language
- audience is large enough to support expansion (ideally meaningful existing digital revenue or 20k+ followers/email audience)
- no mature English-language product
- creator does not want to personally re-record the whole catalog in English

Avoid:
- brand-new teachers with no audience/revenue
- huge global brands that already have localization teams
- free-only creators with no proven monetization
- creators whose content is mostly music / non-verbal workouts where dubbing adds little

## Public potential-customer pool
These are **potential customers based on public signals, not people known to be interested**. Each already has local-language paid or substantial recorded movement content.

1. Yoga con Paty — Spanish paid membership/courses: https://yogaconpaty.com/
2. Yoga con Carolina — Spanish yoga platform with 500+ classes: https://yogaconcarolina.com/plataforma-yoga-online/
3. VidaZenter — Spanish recorded yoga subscription: https://vidazenter.com/yogaonline/
4. AleYoga — Spanish courses sold through Udemy/Thinkific: https://aleyoga.com/cursos.html
5. FisioLeón — Spanish Pilates video courses: https://www.fisioleon.es/pilates-online/
6. Le Yoga d'Hélène — French online yoga subscription/coaching: https://www.leyogadhelene.fr/
7. Home Yoga Paris — French online classes/replays: https://www.homeyogaparis.fr/cours-yoga-paris/cours-de-yoga-en-ligne
8. ProSSto Pilates — Polish platform with 100+ lessons: https://pilates-online.pl/
9. Warsaw Pilates — large Polish Pilates online platform: https://www.warsawpilates.pl/pilatesonline
10. WohnzimmerPilates — German platform with 200+ Pilates/yoga videos: https://www.wohnzimmerpilates.de/member/details
11. Pilatesiarka — Polish paid Pilates programs/subscription: https://www.pilatesiarka.pl/pilates-online
12. Portal Jogi Online — Polish multi-teacher yoga library: https://joga-online.pl/

Reachability gate therefore passes in principle: there are many public businesses with existing catalogues and obvious buyer contacts.

## Pricing / offer hypotheses

### Offer A — paid pilot
"English Expansion Pilot"
- localize 30–60 minutes of the creator's best material
- teacher voice preserved
- English movement terminology QA
- subtitles + final MP4/audio
- localized title/description/landing-page copy
- optional YouTube or course-platform upload

**Test price: €500–€1,000.**
The purpose is not margin optimization; it tests whether a creator pays for expansion rather than saying it sounds interesting.

### Offer B — revenue-share partnership
For proven creators only:
- creator pays little/no upfront
- we fund/perform localization + launch
- take roughly **25–35% of net revenue from the new-language product** for a defined term

A lower share (15–20%) is more appropriate if the creator pays production costs. A higher share is justified only if we also own launch/distribution work and take financial risk.

### Offer C — hybrid
€500–€1,500 setup + 10–20% of incremental new-language revenue.

This may align incentives better than pure project work while avoiding financing large catalogues ourselves.

## Cheapest validation experiment (<= €500)

1. Pick one non-English movement creator with an existing paid library.
2. Take one strong 5–10 minute lesson and create a polished English sample in their own voice.
3. Build a one-page "English expansion forecast": what content to localize first, target market, suggested price/channel.
4. Contact 20 carefully selected creators/schools from the prospect pool. Do not pitch "AI dubbing". Pitch "launch your existing course in English without re-recording".
5. Ask for one of two commitments:
   - €500 paid pilot; or
   - signed revenue-share pilot where they grant rights to localize and sell a defined mini-course.

**Pass condition:** at least 2 serious sales conversations and 1 paid/signed pilot from 20 highly targeted prospects.

**Fail condition:** creators like the sample but refuse both a modest project fee and a revenue-share commitment. That would indicate admiration without commercial demand.

## Smart validation shortcut
Before spending money dubbing an entire course, use YouTube's automatic dubbing / multi-language analytics on a creator's top evergreen videos where possible. If English/Spanish dubbed watch time has no traction, do not localize the paid catalogue into that market.

## Risks / red-team
1. **Basic dubbing is commoditized.** Tools and YouTube keep improving; price will trend toward zero.
2. **Distribution is the actual hard part.** A translated course with no audience may sell nothing.
3. **English is a huge market but extremely competitive.** The best language depends on the creator's niche and existing audience signals.
4. **Translation errors matter more in movement instruction.** Left/right, anatomy, breath and timing require QA.
5. **Revenue share can finance losing projects.** Only use it for creators with proven sales/audience.
6. **Platform dependence.** Udemy/YouTube economics and localization features can change.
7. **Voice/likeness rights.** Written authorization is mandatory. Some platforms require the voice owner to create/verify their own clone and share access. Example: ElevenLabs Professional Voice Clone must be created by the voice owner: https://help.elevenlabs.io/hc/en-us/articles/36842751624209-Can-I-create-a-Professional-Voice-Clone-of-someone-else-s-voice

## Promotion gates
- Research quality: **PARTIAL PASS** — multiple independent signals and strong proxy WTP, but no direct interviews yet.
- Competition gap: **PARTIAL PASS** — generic dubbing fails; movement-specific expansion studio remains plausible but Lingrow is a close horizontal competitor.
- Monetization/test price: **PASS** — clear project and revenue-share structures; comparable services already charge meaningful rates.
- Evidence-backed reachability: **PASS** — 10+ concrete public potential customers identified.
- Disconfirmation/red-team: **PASS** — YouTube free auto-dubbing, cheap tools and direct localization agencies were explicitly considered.

## Score
- pain_intensity: 7.0
- frequency: 6.0
- willingness_to_pay: 8.0
- evidence_quality: 7.5
- reachability: 9.0
- competition_gap: 6.0
- why_now: 9.0
- buildability: 9.0
- founder_interest: 9.0

Deterministic score: **76.2/100**.

## What would move it above 78
- one paid pilot, or a signed revenue-share pilot with a creator who already sells digital content
- 3+ creators independently saying international expansion is wanted but re-recording / localization execution is the blocker
- evidence that movement-specific QA or distribution materially outperforms generic dubbing tools

## Bottom line
Do not build a dubbing product. **Try to become the international expansion partner for a small number of already-successful movement creators.** This is service-first, cheap to test, aligned with current AI economics, and much more defensible than selling minutes of AI voice generation.