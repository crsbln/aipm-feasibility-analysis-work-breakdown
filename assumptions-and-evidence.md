# Assumptions and Evidence

**Reference date:** 2026-11-27 · Labels as defined in `project-brief.md`.
Rule used throughout: nothing moves from one category to another (for example assumption to evidence) without a new
source, and every move is recorded in `ai-collaboration-log.md`.

## Sources

| ID | Source | Type | Date | Limits |
|---|---|---|---|---|
| **S01** | Kaggle dataset "Kickstarter Projects" (kemical), file `ks-projects-201801.csv`, as cleaned in the Week 9 project (`crsbln/ds-ml-project-template`, `reports/results.json`) | Observational platform data, collected by a third party | Campaigns 2009 to January 2018; numbers generated 2026-10-21 | Old; no campaign content (video, rewards, promotion); associations, not causes; canceled campaigns count as not funded |
| **S02** | Week 9 model evaluation in the same `results.json` (held-out test set, calibration, chance bands, time-based test) | Quantitative evaluation | 2026-10-21 | One dataset, one platform; the test set was reused across review rounds (disclosed by the team) |
| **S03** | `crsbln/aipm-roadmapping`, `evidence-map.md` (findings F04, F10, F11, F12), which summarizes the Week 9 reviews and the licence check | Our own earlier analysis | 2026-11-06 | Written by the same owner with Claude; reviews were of method, not of creators |
| **S04** | Kaggle dataset page, read in a browser on 2026-11-06 and recorded as S04 in `aipm-roadmapping`: "License CC BY-NC-SA 4.0", "Updated 9 years ago" ([link](https://www.kaggle.com/datasets/kemical/kickstarter-projects)) | Public web page | 2026-11-06 | Page text only; not legal advice; not re-read in this pass |
| **S05** | **This repository:** `analysis/option_b_lookup_check.py` and `analysis/option_b_lookup_results.json`: Option B lookup tables vs the Week 9 model, same rows and same 80/20 split | Quantitative check run by Claude | 2026-11-27 | Lookup smoothing (k = 50) was chosen, not tuned (a sensitivity check shows it barely matters); data still ends January 2018 |
| **S06** | [Creative Commons: CC BY-NC-SA 4.0 deed](https://creativecommons.org/licenses/by-nc-sa/4.0/) | Licence summary | Not re-read in this pass | The deed is a summary, not the legal code |
| **S07** | [European Commission: AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Official overview | Linked from lesson 02 | An overview; classification of our case needs a legal reading |
| **GAP** | Creator research | - | - | Zero creators interviewed, surveyed or observed |

Tried and failed: the Kickstarter rules page (`kickstarter.com/rules`) returned HTTP 403 to this PC on 2026-11-27, so
platform rules are not used as evidence here (see A03).

## Evidence

| ID | Claim | Source | Confidence | Note |
|---|---|---|---|---|
| E01 | 372,293 finished campaigns; 133,956 (36 %) reached their goal, 238,337 (64 %) did not. | S01 | High | Canceled campaigns count as not funded. |
| E02 | Funding rate falls with the goal: up to 1k USD 49 %, 5k to 10k 35 %, over 100k 6 %. By category: Dance 62 %, Theater 60 %, Technology 20 %. | S01 | High | Association, not cause; goal and category are entangled (Technology median goal 20,000 USD). |
| E03 | 166,483 campaigns (45 %) ran exactly 30 days, funded 32 %; 29 days 46 %, 31 days 49 %. 60 days: 19 %. | S01 | High | Pattern; cause unknown (U04). |
| E04 | Model inputs by importance: category, goal, length far ahead; title words, country, launch weekday and month add little. | S02 | High | Permutation importance on the test set. |
| E05 | Week 9 model on 74,459 unseen campaigns: ROC-AUC 0.754, Brier score 0.189. In cross-validation logistic regression reached 0.728, random forest 0.718. | S02, rerun in S05 | High | Our rerun reproduced 0.754 and 0.189 exactly. |
| E06 | Probabilities are right on average (36 % predicted, 36 % funded). Per launch year the gap reaches about 4 points (2015: 32 % predicted, 28 % funded). | S02 | High for 2009 to 2018 | Says nothing about 2026 (U02). |
| E07 | Chance bands: "below average" (under 25 %) holds 34 % of test campaigns, 14 % of them funded; "about average" 39 %, 37 % funded; "above average" 27 %, 62 % funded. | S02 | High | Even "above average" fails 38 times in 100. |
| E08 | The Week 9 what-if feature was removed: changing 30 to 29 days moved an example (US tabletop game, 10k USD) from 51 % to 72 % without changing its real odds. | S02, S03 | High | Shows how a model output can be misused as a lever. |
| E09 | Option B lookup tables on the same test split: category only 0.623; category x goal band (120 cells) **0.681**, Brier 0.209; plus length (823 cells) 0.703; subcategory x goal band (1,246 cells) 0.715. Goal size alone as a ranking: 0.640 (the Week 9 deck reported 0.637 for the goal rule); the goal rule as a yes/no answer: 0.598. Saying "36 %" to everyone gives Brier 0.230. The untuned smoothing does not matter: k = 0, 10, 50 or 200 gives 0.680 to 0.681. | S05 | High (for 2009 to 2018) | The model stays ahead (0.754); a 120-cell table closes about a third of the gap between goal size and the model. |
| E10 | Dataset licence CC BY-NC-SA 4.0: attribution, non-commercial, share-alike for adapted material. | S04, S06 | Medium | "Adapted material" status of a trained model or a rate table is not settled (U03). |
| E11 | Ranking quality holds on a time-based test (train before 2016, test 2016 to January 2018): model 0.757; 120-cell table 0.671; table with length 0.700. | S02, S05 | High for that window | Funding levels still moved: yearly rates 46 % (2011), 28 % (2015), 37 % (2017). Small flaw: the model's settings were tuned in Week 9 on data that included 2016-2017, so its time-based score may be slightly flattering; the tables have no tuned settings. |
| E12 | No creator has been interviewed, surveyed or observed using any Launch Check output. | GAP, S03 | High | The whole demand side is unknown (U01). |

## Estimates

| ID | Estimate | Method | Range | Confidence |
|---|---|---|---|---|
| N01 | Creators needed for a first round of demand and comprehension interviews | Common qualitative-research practice: patterns usually repeat after a handful of interviews per user type | 5 to 12 creators | Low: a planning guide, not a requirement |
| N02 | Running cost of Option B as a static page at 50,000 visits | Static files need no server logic; many hosts serve static pages on free tiers | 0 to a few USD per month | Low until measured (C02, WBS 1.6.1) |
| N03 | Running cost of Option C at 50,000 visits | Depends on design: model in the browser (static) or a server call per check | 0 USD (browser) to an unmeasured amount (server) | Low until measured |

N02 and N03 are deliberately wide. Lesson 05 warns against precise-looking numbers without a basis.

## Assumptions

| ID | Assumption | Why it matters | Critical? | Smallest validation action |
|---|---|---|---|---|
| A01 | First-time creators want to see their odds **before** launch. | Without demand, B and C both have no value. | Yes | Interview 5 to 12 creators (WBS 1.1). |
| A02 | Creators would change goal or length, or wait, when they see poor odds. | The outcome depends on a decision changing. | Yes | Ask in interviews; observe choices in a test with the B sheet (WBS 1.5). |
| A03 | Kickstarter is all-or-nothing: creators receive nothing if the goal is missed. | Makes the pre-launch decision high-stakes. | No | Re-read Kickstarter's rules page from a network that is not blocked. |
| A04 | A 2009 to 2018 table, clearly labelled historical, is honest enough to help a 2026 creator. | B's main claim. | Yes | Comprehension test (WBS 1.5); recency check if lawful recent data exists (WBS 1.3.2). |
| A05 | Showing the model in the browser would make C cost about as little as B. | C's economic case. | No | Cost measurement (WBS 1.6.1). |
| A06 | Launch Check is not a high-risk system under the AI Act (it does not decide on people's access to credit, jobs or services). | Would add heavy obligations. | Yes | Legal reading of the AI Act categories for this use (WBS 1.2.1). |
| A07 | The two Week 9 teammates would agree to reuse of the joint model. | C depends on the model. | Yes for C | Ask them and record the answer (WBS 1.8.1). |
| A08 | 30 days is Kickstarter's default campaign length, which would explain why 45 % of campaigns use it. | Changes how the 30-day pattern is explained to creators. | No | Check the campaign set-up page on Kickstarter (blocked from this PC on 2026-11-27, see Sources). |

## Constraints

| ID | Constraint | Source |
|---|---|---|
| C01 | No commercial use of the data; share-alike for adapted material; attribution required. | E10 |
| C02 | Owner's cost rule: cost per visit measured at today's traffic and at 50,000 visitors, approved before anything goes online. | Owner's standing rule |
| C03 | No personal data in the repository or in AI tools; a public tool stores no inputs. | Handout ground rules; owner rule |
| C04 | One person, part time, no budget. | Owner |
| C05 | No what-if optimizer. | E08 |
| C06 | Interview notes are personal data: consent, anonymisation and a deletion date are required. | GDPR principle of purpose limitation and storage limitation `[constraint, legal detail to confirm in WBS 1.1.1]` |

## Risks

| ID | Risk | Linked claims | Where it is handled |
|---|---|---|---|
| R01 | Creators read a band or percentage as a verdict ("below average" = "don't bother"). | E07, E08 | `risk-register.md`, WBS 1.5 |
| R02 | The licence or platform terms rule out the intended use. | E10, U03 | WBS 1.2.1 |
| R03 | No lawful source of recent campaign data exists, so G2 can never be met for C. | U02, U05 | WBS 1.2.2, 1.3.2 |
| R04 | Not enough creators agree to an interview. | N01 | WBS 1.1.1 |
| R05 | The owner's preference for C (it is his project) colours the analysis. | - | Hard gates set before scoring; four arguments in `decision-memo.md` |
| R06 | Costs grow after going live (for example a server call per check). | N03, C02 | WBS 1.6.1 |

## Unknowns

| ID | Unknown | Smallest credible validation action | WBS |
|---|---|---|---|
| U01 | Do creators want pre-launch odds, when, and in which form? | Creator interviews | 1.1 |
| U02 | Do the 2009 to 2018 patterns and probability levels hold for campaigns in 2026? | Recency check on a lawful recent sample, or record that none exists | 1.3.2 |
| U03 | Is a trained model, or a table of rates, "adapted material" under CC BY-NC-SA 4.0? What do Kickstarter's terms say about using scraped campaign data? | Legal reading by a qualified reviewer | 1.2.1 |
| U04 | Is the 30-day dip a cause or only a marker of less planning? | Cannot be settled with observational data; state it as a pattern only | 1.4.1 (wording) |
| U05 | Which lawful source of recent campaign data exists, at what cost? | Desk search of sources and their terms | 1.2.2 |
| U06 | What share of creators misreads a band or a percentage? | Comprehension test with B and a C mock | 1.5 |
| U07 | Do the teammates consent to reuse? | Ask and record | 1.8.1 |
| U08 | What does "good enough" quality mean for creators (a minimum acceptable performance)? | Derive from interviews and the comprehension test; owner approves | 1.3.3 |
