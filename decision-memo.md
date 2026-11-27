# Feasibility Decision Memo

**Reference date:** 2026-11-27 · Built from `templates/decision-memo.md` · Draft by Claude, **recommendation awaits the
decision owner's approval** (lesson 05: the final recommendation is a human approval gate).

## Decision

**Reframe.** Do not build Launch Check Online (C) now. Run a bounded **Launch Check validation project** that uses
the simpler pattern sheet (B) as its research probe and ends in a gate decision: publish B, proceed to C under
conditions, or stop.

## Outcome and Options Considered

Outcome: creators decide to launch, change their plan, or wait, with an honest picture of their odds.

| Option | One line | Verdict |
|---|---|---|
| A. Business as usual | No Launch Check for creators. | Safe, but does nothing for the 64 % who miss their goal. Kept as the fallback if the gate says stop. |
| B. Pattern sheet | Historical rates by category x goal band, plus three patterns. | Most of the signal, fewest open gates. Chosen as the probe, not yet for release. |
| C. Launch Check Online | Public model-based chance for the creator's own plan. | Best estimate, but two hard gates open (G1 licence, G2 currency) and demand unknown. |

## Four Arguments on the Same Evidence

| Argument | Strongest case | Why it did not win |
|---|---|---|
| **Go (build C)** | The model beats every simpler option (0.754 vs 0.681 for the table, 0.640 for goal size; E05, E09) and is calibrated on average (E06). | It would show a 2018 number as a 2026 chance (G2) on data with a non-commercial, share-alike licence whose reach to a model is unclear (G1), for users nobody has asked (E12). A strong score cannot rescue a failed gate. |
| **Conditional go (build C once conditions hold)** | Name the conditions (licence, recency, comprehension, consent) and build C when they pass. | Every condition is still open, and the first one (demand) could make C pointless. Calling this "go" would invite building before learning. |
| **Reframe (validate with B, decide later)** | Tests the riskiest assumptions (demand, reading, licence) cheaply. B keeps about a third of the model's gain over goal size alone and holds on 2016-2018 data (E09, E11). Nothing goes online. | Slower to a public tool; B is weaker than C (0.681 vs 0.754). |
| **No-go (stop)** | No demand evidence and a non-commercial licence: why spend more? | The problem is real and measured (E01 to E03), the next step is cheap, and stopping teaches nothing. A no-go stays possible at the gate. |

## Strongest Evidence

- 36 % of 372,293 campaigns were funded; plan choices line up with large differences (goal up to 1k: 49 %, over
  100k: 6 %; 30 days: 32 % vs 46 % at 29 days). (E01 to E03)
- Measured on the same test split: model ROC-AUC 0.754, 120-cell table 0.681, goal size 0.640. The model's lead
  holds on 2016-2018 data (0.757 vs 0.671). (E05, E09, E11; our rerun S05)
- In Week 9, a what-if feature moved an example from 51 % to 72 % without changing its real odds and was removed:
  model outputs invite misuse. (E08)
- Zero creators have been asked anything. (E12)

## Critical Assumptions and Unknowns

| ID | What | Validation (WBS) |
|---|---|---|
| A01, A02 | Creators want pre-launch odds and would act on them | Interviews (1.1), test with the sheet (1.5) |
| A04 | A labelled historical table is honest and useful in 2026 | Comprehension test (1.5) |
| U02, U05 | Patterns and levels after 2018; a lawful recent data source | Source assessment (1.2.2), recency check (1.3.2) |
| U03, A06 | Licence reach to tables and models; platform terms; AI Act class | Legal reading (1.2.1) |
| U06 | How often creators misread a band or percentage | Comprehension test (1.5) |
| A07 | Teammates' consent | Consent record (1.8.1) |

## Hard Gates and Conditions

- **G1** lawful use, **G3** cost approved: required before **anything** goes online, including B.
- **G2** currency: B passes only with a clear "2009 to 2018" label that creators understand; C needs lawful recent
  data and a recency check within approved thresholds.
- **G4** nothing typed is stored: B has no input; C must prove it by design.
- Gate decision rules (proposed, owner to approve), applied in WBS 1.7.2:
  - **Stop** if interviews show no wish for pre-launch odds, or G1 fails for every output.
  - **Publish B** if creators want it, read the label correctly, and G1 and G3 pass.
  - **Proceed to C (conditional go)** only if, in addition, G2 can be met with recent data, creators read the C band
    at least as well as the B sheet, and both teammates consent.

## Main Trade-offs

- **Quality vs honesty:** C ranks better (0.754 vs 0.681), but a personal percentage looks current and precise;
  a table reads as history.
- **Speed vs learning:** going straight to C saves weeks if demand exists, and wastes all of them if it does not.
- **Owner preference vs evidence:** C is the owner's own project, which is exactly why the gates were fixed before
  the options were rated (R05).

## Recommended Next Action

Start the validation project with its two cheapest, riskiest pieces at once: a short creator interview plan with a
consent pack (WBS 1.1.1), and a request for a legal reading of the licence question (WBS 1.2.1). Ask both teammates
for consent (WBS 1.8.1). Nothing is published until the gate decision (WBS 1.7.2).

## Confidence and Limits

- **Confidence in the direction (reframe): medium.** It follows from open gates, not from new evidence of demand.
- **Confidence in demand: low.** No creator was asked; this is the biggest limit of the whole analysis.
- All data ends January 2018. The licence reading is ours, not legal advice. Option ratings, criteria and this
  recommendation were drafted by Claude in one pass on 2026-11-27 and still need the owner's review. No group took
  part; the reviewer "perspectives" in `ai-collaboration-log.md` were simulated, not real experts.
