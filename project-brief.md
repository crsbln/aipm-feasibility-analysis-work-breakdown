# Project Brief: Should Launch Check Go Online?

**Reference date:** 2026-11-27 · **Decision owner:** Christian Balan, AI Project Manager (neuefische AIPM) ·
**Prepared by:** Claude Code (delegated pass, owner review pending; see `ai-collaboration-log.md`)

**How to read the labels.** Every important claim carries one tag, as the session handout asks:
`[evidence]` supported by a source we checked · `[estimate]` an approximate value with method and range ·
`[assumption]` believed, not verified · `[constraint]` a boundary we must respect · `[risk]` an uncertain event ·
`[unknown]` information we do not have. Ideas that only Claude proposed carry `[agent suggestion]`.
Source IDs (S01 ...) and claim IDs (E01 ...) point into `assumptions-and-evidence.md`.

## Why this proposal

The handout leaves the choice of proposal free. We use **Kickstarter Launch Check**, the data product from our
Week 9 machine-learning project, because it fits every selection rule in Step 1:

| Handout rule | How Launch Check meets it |
|---|---|
| Recognizable user or business outcome | Kickstarter creators deciding whether and how to launch a campaign |
| Meaningful uncertainty | Old data (ends January 2018), a non-commercial data licence, no creator research at all |
| At least one credible simpler alternative | A printed table of historical funding rates does part of the model's job (measured: E09) |
| No sensitive information | Public, aggregated campaign data; no personal data enters this repository |

## Users and Their Current Problem

**Primary users:** first-time and small creators planning a Kickstarter campaign. `[assumption: chosen by us, never asked]`

**Problem.** Most campaigns fail, and creators decide their plan before they see any odds.

- Of 372,293 finished campaigns from 2009 to January 2018, only **36 %** reached their goal; 64 % did not. `[evidence, E01]`
- Plan choices line up with very different success rates: goals up to 1,000 USD were funded 49 % of the time, goals over
  100,000 USD 6 %; Dance 62 %, Technology 20 %. `[evidence, E02]`
- 45 % of campaigns ran exactly 30 days and were funded 32 % of the time, against 46 % at 29 days and 49 % at 31 days.
  `[evidence, E03]` That 30 days is the platform's default setting is `[assumption, A08]`. Whether the dip is a cause
  or only a marker of less planning is `[unknown, U04]`.
- Whether creators feel this problem, know these patterns, or want help before launch: **no creator has been asked**.
  `[unknown, U01]`

## Desired Outcome

> Creators decide to launch, change their goal or length, or wait, **with an honest picture of their odds**,
> and nobody is misled by a number.

How we would know (signals, not yet targets, because no baseline exists):

| Signal | Baseline | Direction |
|---|---|---|
| Share of creators in a test who change or confirm goal and length on purpose and can say why | `[unknown]` | up |
| Share of creators who read a shown estimate correctly (e.g. "below average" is not "no chance") | `[unknown]` | at or above an approved threshold (see `wbs-dictionary.md`, 1.3.3) |
| Cost per visit of anything we put online | 0 USD, nothing is online `[evidence]` | measured and approved before going live `[constraint]` |

A feature name ("put the model online") is not the outcome. The outcome is the informed decision.

## The Three Options

| Option | What it is | Why it is credible |
|---|---|---|
| **A. Business as usual** | No Launch Check for creators. The Week 9 work stays a notebook, a command-line check and two decks. Creators plan with whatever guidance they use today. | It is what happens now, costs nothing, and carries no legal or misreading risk. Its cost is the status quo: the 30-day default and over-asking continue unaided `[evidence, E02, E03]`. |
| **B. Pattern sheet (simpler)** | One static page or printout: historical funding rates by category and goal band (a 15 x 8 table, 120 cells), plus the three patterns (goal, category, campaign length) explained as patterns, not a recipe. Labelled "Kickstarter 2009 to 2018". No inputs, no model, no server. | A 120-cell table ranks campaigns with ROC-AUC 0.681 against 0.754 for the model and 0.640 for goal size alone `[evidence, E09]`; it has no inputs, so it cannot be "gamed" by re-running. How quickly creators understand it is `[unknown, U06]`. |
| **C. Launch Check Online (the original proposal)** | A free public web page: the creator enters category, goal, length, country, launch date and title; the Week 9 gradient-boosting model returns a calibrated chance of funding, shown as a band relative to the 36 % average, with the three patterns. | The model is the best ranker we have (ROC-AUC 0.754, Brier 0.189) and its probabilities matched reality on average in 2009 to 2018 `[evidence, E05, E06]`. |

## Constraints

- `[constraint]` **Data licence:** the Kaggle dataset is CC BY-NC-SA 4.0: attribution, no commercial use, share-alike
  for adapted material. (E10)
- `[constraint]` **Owner's cost rule:** nothing goes online until the cost per visit is measured at today's traffic and
  at 50,000 visitors, and the owner has approved it.
- `[constraint]` **Privacy:** no personal data of creators enters this repository or an AI tool; a public tool must not
  store what creators type.
- `[constraint]` **Capacity:** one person, part time, no budget for this analysis.
- `[constraint]` **Shared authorship:** the model and decks were made by a team of three; the two teammates have not
  been asked about reuse. (U07)
- `[constraint]` **No what-if optimizer:** the Week 9 project removed it after review because changing one input
  (30 to 29 days) moved an example from 51 % to 72 % without changing the real odds. (E08)

## Decision Criteria

Hard gates first (an option that fails one cannot be rescued by strengths elsewhere), then trade-offs.

| ID | Criterion | Type |
|---|---|---|
| G1 | The intended use of the data is lawful (licence and platform terms) | hard gate |
| G2 | No number is shown as a creator's chance **today** unless it is shown to hold today, or it is clearly labelled historical | hard gate |
| G3 | Measured cost per visit is approved before anything goes online | hard gate (owner's rule) |
| G4 | Nothing a creator types is stored | hard gate |
| K1 | Evidence that creators want and use pre-launch odds | trade-off criterion |
| K2 | Estimate quality: ranking (ROC-AUC) and honesty of probabilities (calibration, Brier score) | trade-off criterion |
| K3 | Creators read the output correctly | trade-off criterion |
| K4 | One part-time owner can run, update and retire it | trade-off criterion |

## Stakeholders Who Must Validate Claims

| Stakeholder | What only they can confirm |
|---|---|
| Kickstarter creators (5 to 12 in a first round, `[estimate]` from common interview practice, not a rule) | Demand, moment of use, how they read odds, what they would change |
| A legal reviewer (not identified yet) | Whether derived tables and a trained model are "adapted material" under the licence; Kickstarter's terms |
| The two Week 9 teammates | Consent to reuse the joint model and material |
| The decision owner | Criteria, ratings, the final recommendation, the approved scope |

## What This Analysis Deliberately Excludes

- Building anything: no web page, no deployment, no new model.
- Collecting new data (no scraping of Kickstarter) during this analysis.
- Commercial use or pricing of any Launch Check.
- Other crowdfunding platforms, predicting the amount pledged, advice to backers.
- A what-if or "best settings" feature (rejected in Week 9, E08).
- A schedule, a backlog of user stories, or a detailed cost estimate: the WBS describes scope only.

## The Decision to Make

> Should we put Launch Check online as a public model-based tool (C), offer the simpler pattern sheet (B), or keep
> things as they are (A), and under which conditions?

Options and criteria were proposed by Claude from the lessons and the Week 9 record. The owner has not yet approved
them (approval gate, lesson 05).
