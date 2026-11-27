# Feasibility Matrix

**Reference date:** 2026-11-27 · Built from `templates/feasibility-matrix.md` · Labels and IDs as in
`assumptions-and-evidence.md`. Ratings were drafted by Claude and **await owner approval** (lesson 05 approval gate).

## Decision Question

> Should we put Launch Check online as a public model-based tool (C), offer the simpler pattern sheet (B), or keep
> things as they are (A), and under which conditions?

Intended outcome: creators decide to launch, change their plan, or wait, with an honest picture of their odds.

## Options

| Option | Description | Why it is credible |
|---|---|---|
| Business as usual (A) | No Launch Check for creators; the Week 9 work stays a course prototype. | Costs nothing; no legal or misreading risk; it is today's situation. |
| Simpler alternative (B) | Static pattern sheet: historical funding rates by category x goal band (120 cells) plus the three patterns, labelled 2009 to 2018. | Measured ROC-AUC 0.681 vs 0.754 for the model (E09); nothing to run, nothing to store. |
| Proposed option (C) | Launch Check Online: public page, creator enters the plan, the Week 9 model returns a calibrated chance and band. | Best measured quality: ROC-AUC 0.754, Brier 0.189, calibrated on average (E05, E06). |

## How to Read the Ratings

**Strong** = evidence supports it · **Adequate** = workable with known limits · **Weak** = a serious problem ·
**Gate open** = a hard gate is not yet passed · **Unknown** = no evidence either way.
Confidence (High / Medium / Low) says how sure we are of the rating itself.
**No total score is calculated.** A sum would let strengths hide a failed gate, which lesson 01 warns against.

## Summary

| Dimension | A. Business as usual | B. Pattern sheet | C. Launch Check Online |
|---|---|---|---|
| Strategic and user value | Weak (Medium) | Unknown (Low) | Unknown (Low) |
| Economic | Strong (High) | Adequate (Low) | Unknown (Low) |
| Technical | Strong (High) | Strong (High) | Adequate (Medium) |
| Data and model | Not applicable | Adequate (High) | Strong for 2009-2018, Gate open for today (High) |
| Operational | Strong (High) | Adequate (Medium) | Weak (Medium) |
| Legal, privacy, and safety | Strong (High) | Gate open (Medium) | Gate open (Medium) |
| Scheduling and resources | Strong (High) | Adequate (Medium) | Weak (Medium) |
| Adoption and sustainability | Weak (Medium) | Unknown (Low) | Unknown (Low) |

Reading across: **A is the safest and does nothing for the outcome; C is the strongest estimate with the most open
gates; B keeps most of the signal with the fewest open gates. Demand is unknown for both B and C.**

## Assessment

| Dimension | Option | Evidence | Assumptions / unknowns | Hard gate? | Confidence | Next validation action |
|---|---|---|---|---|---|---|
| Strategic and user value | A | 64 % of campaigns miss their goal; 45 % keep the 30-day default, funded 32 % (E01, E03). Nothing changes that. | Whether creators already know the patterns (U01). | No | Medium | Ask creators what guidance they use today (WBS 1.1). |
| Strategic and user value | B | Shows the patterns that line up with success (E02, E03). | Demand (A01); whether a table changes decisions (A02). | No | Low | Interviews and a test with the sheet (WBS 1.1, 1.5). |
| Strategic and user value | C | A personal estimate for the creator's own plan; best ranking (E05). | Demand (A01, A02); value over B for a creator is unmeasured. | No | Low | Same interviews; compare B and a C mock in one test (WBS 1.5). |
| Economic | A | No cost. | - | No | High | None. |
| Economic | B | Static page, no server logic (N02). | Hosting cost unmeasured (C02). | G3 applies | Low | Measure cost per visit (WBS 1.6.1). |
| Economic | C | Model inference per check; design open (N03). | Browser vs server design (A05); no revenue possible on this data (C01). | G3 applies | Low | Measure both designs (WBS 1.6.1). |
| Technical | A | Nothing to build. | - | No | High | None. |
| Technical | B | A table and text; the numbers are already computed (E09, S05). | - | No | High | None beyond review (WBS 1.4.2). |
| Technical | C | Model, pipeline and command-line check exist and reproduce (E05). | Running the model in a browser is untested (A05). | No | Medium | Small technical spike, only if the gate decision reaches C. |
| Data and model | A | Not applicable. | - | No | - | - |
| Data and model | B | 120-cell table: ROC-AUC 0.681, Brier 0.209; holds on the 2016-2018 test (0.671) (E09, E11). | Levels after 2018 unknown (U02). Shown as history, so G2 can be met by labelling. | G2 (met by label) | High | Comprehension test of the "historical" label (WBS 1.5). |
| Data and model | C | ROC-AUC 0.754, calibrated on average; time-based 0.757 (E05, E06, E11). Data ends January 2018; yearly levels moved between 28 % and 46 %. | A personal "your chance" implies today; no recent data (U02, U05). | **G2 open** | High | Find lawful recent data and run a recency check, or C cannot pass G2 (WBS 1.2.2, 1.3.2). |
| Operational | A | Nothing to run. | - | No | High | None. |
| Operational | B | Static content; a yearly review at most. | Who owns updates and retirement (WBS 1.6.2). | No | Medium | Name an owner and a retirement date. |
| Operational | C | A live model needs monitoring of drift, cost and errors; owner capacity is one person part time (C04). | Whether monitoring is possible without recent outcomes (U02). | No | Medium | Ownership outline (WBS 1.6.2). |
| Legal, privacy, and safety | A | No processing, no output. | - | No | High | None. |
| Legal, privacy, and safety | B | Publishing derived rates; licence is non-commercial and share-alike (E10). Misreading risk lower: no personal number (E08 does not apply). | Is a rate table "adapted material"? Kickstarter terms (U03). | **G1 open** | Medium | Legal reading (WBS 1.2.1). |
| Legal, privacy, and safety | C | Same licence (E10). Inputs typed by creators must not be stored (C03). Misuse shown in Week 9: re-running inputs to push the number up (E08). | Is a trained model "adapted material"? AI Act class (A06). | **G1 open, G4 by design** | Medium | Legal reading; design review that nothing is stored (WBS 1.2.1). |
| Scheduling and resources | A | None needed. | - | No | High | None. |
| Scheduling and resources | B | Content exists; review and test remain. | Interview time (N01). | No | Medium | Plan interviews in the validation project. |
| Scheduling and resources | C | Needs data basis, recency check, front end, monitoring, legal review, teammate consent (A07). | Too much for one part-time owner before demand is known. | No | Medium | Decide only after the gate (WBS 1.7.2). |
| Adoption and sustainability | A | No adoption needed; creators keep current habits. | - | No | Medium | None. |
| Adoption and sustainability | B | Low energy and compute; a static page. | Whether creators trust a table from 2018 (A04). | No | Low | Comprehension test (WBS 1.5). |
| Adoption and sustainability | C | Model run per check; small compute. Trust depends on reading the band right (R01). | Misreading rate unknown (U06). | No | Low | Comprehension test (WBS 1.5). |

## Hard Gate Check

| Gate | A | B | C |
|---|---|---|---|
| G1 Lawful use of the data | passes (no use) | **open**: legal reading needed | **open**: legal reading needed |
| G2 No historical number shown as today's chance | passes | passes **if** labelled and the label is understood | **open**: needs recent data and a recency check |
| G3 Cost measured and approved | passes (no cost) | open, but likely easy (static) | open; design-dependent |
| G4 Nothing typed is stored | passes | passes (no input) | passes only by design; must be verified |

## Critical Conditions

Before **anything** goes online:

1. G1: a qualified legal reading confirms the intended use (non-commercial, attributed, share-alike) is allowed for
   the chosen output, and Kickstarter's terms do not forbid it.
2. G3: cost per visit is measured at today's traffic and at 50,000 visitors, and the owner approves it.
3. Creator evidence exists (A01, A02): at least one round of interviews shows that creators want pre-launch odds.

Before **C** in particular:

4. G2: lawful recent data and a recency check show the model still ranks and calibrates on current campaigns, within
   thresholds the owner approves (WBS 1.3.3).
5. Comprehension: creators read the band correctly at least as often as they read the B sheet correctly.
6. Teammates consent to reuse of the joint model (A07).
