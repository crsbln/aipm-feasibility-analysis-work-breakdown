# AI Collaboration Log

**Reference date:** 2026-11-27

## How this was done (read first)

- The handout expects a group that supervises Claude. **There was no group.** The owner delegated the whole
  session to Claude Code, which did one pass on 2026-11-27. **Owner review is pending** for every entry below.
- Three read-only reviewer definitions were written to `.claude/agents/` (feasibility challenger, data and model
  reviewer, WBS auditor). In this run they were **not executed as separate subagents**: the same Claude session
  re-read all files following each reviewer's checklist. That is a self-review, weaker than an independent one.
  Running them for real (`/agents` in Claude Code) is open.
- The reviewers are simulated perspectives, not legal, data or project experts (lesson 05).
- "Response" uses the four choices from handout Step 4: accept, turn into an assumption or open question,
  request stronger evidence, or reject.

## Drafting decisions

| # | Claude contribution | Accepted, corrected, or rejected? | Evidence or reason |
|---|---|---|---|
| D1 | Chose Kickstarter Launch Check as the proposal. | Accepted (by Claude, under the owner's standing instruction for free choices) | Fits all four Step 1 rules (`project-brief.md`). Owner to confirm. |
| D2 | Measured Option B instead of rating it by opinion: wrote `analysis/option_b_lookup_check.py`, which rebuilds the Week 9 split and scores lookup tables against the model. | Accepted | The rerun reproduced the Week 9 model exactly (ROC-AUC 0.754, Brier 0.189), so the comparison is like for like (S05, E09). |
| D3 | The Week 9 deck says the goal rule reaches ROC-AUC 0.637. The rerun gives 0.640 for goal size as a ranking and 0.598 for the yes/no rule. | Corrected | E09 now names both and says which is which, instead of reusing 0.637 as if it were the same measure. |
| D4 | Wanted to cite Kickstarter's rules for "all-or-nothing funding". The page returned HTTP 403. | Turned into an assumption (A03) | A claim we could not read is not evidence. |
| D5 | No total score in the matrix; hard gates checked first, ratings in words with a confidence. | Accepted, owner to approve | Lesson 01: a high average can hide one fatal weakness. |
| D6 | Estimates N01 to N03 kept as wide ranges with a method, not single numbers. | Accepted | Lesson 05 and the handout ground rules: estimates use ranges and are not commitments. |
| D7 | Drafted four arguments (go, conditional go, reframe, no-go) on the same evidence and recommended **reframe**. | **Pending owner decision** | The final recommendation is a human approval gate (lesson 05). |

## Review findings (self-review following the three reviewer files)

| # | Reviewer checklist | Finding | Response | What changed |
|---|---|---|---|---|
| F1 | Feasibility challenger, item 1 | The brief called 30 days "the common default" with no source. | Turned into an assumption | New A08; the brief now tags it `[assumption, A08]`. |
| F2 | Feasibility challenger, item 1 | Option B "can be read in a minute": no evidence. | Rejected the wording | Replaced by "how quickly creators understand it is unknown (U06)". |
| F3 | Feasibility challenger, item 6 | Brier 0.230 for "36 % for everyone" was worked out by hand, not by the script. | Requested stronger evidence | The script now computes it (0.230 random split, 0.228 time split). |
| F4 | Data and model reviewer, item 5 | Lookup smoothing k = 50 was picked, not tuned; it could flatter or hurt B. | Requested stronger evidence | Sensitivity run: k = 0, 10, 50, 200 gives 0.680 to 0.681. Finding closed. |
| F5 | Data and model reviewer, item 5 | The model's settings were tuned in Week 9 on data that includes 2016-2017, so its time-based score may be slightly flattering. | Accepted | Limitation added to E11 and to WBS 1.3.1. The decision does not change: the model leads either way. |
| F6 | Data and model reviewer, item 4 | Checked whether any file shows a 2018 number as a current chance. | No finding | G2 is applied to C; B passes only with its "2009 to 2018" label. |
| F7 | WBS auditor, item 1 | The C mock in the comprehension kit (1.5.1) uses the joint Week 9 model before teammates have agreed. | Accepted | 1.5.1 now depends on 1.8.1 (consent). |
| F8 | WBS auditor, item 5 | Closure (1.8.4) was "done when deletion of personal data is confirmed", which can only happen after the deletion date. | Accepted | "Done when" now: deletion date set, a person named, all other copies already deleted. |
| F9 | WBS auditor, item 5 | `wbs.md` said "23 work packages"; the hierarchy has 21. | Accepted | Corrected to 8 deliverables, 21 work packages. |
| F10 | WBS auditor, item 2 | Checked for scope that serves the rejected direction (building C). | No finding | Building, hosting and a what-if feature are listed as exclusions. |

## What Claude could not do here

- Interview creators, consult a lawyer, or ask the Week 9 teammates: these need real people.
- Run the reviewers as independent subagents (see above).
- Create GitHub issues: by instruction, proposed issues are written to `issue-drafts.md` only.

## Where Claude added false certainty (and where it was caught)

F1 and F2 are the clearest cases: plausible sentences ("the common default", "read in a minute") written as facts.
D3 is a quieter one: a number from our own deck, reused without checking what it measured.

## Independent fact check (2026-11-27, a second Claude session)

After the pass above, a separate Claude session re-read every file against the handout and recomputed the numbers
of E01 to E03, E09 and E11 from the raw CSV with this repository's own script. E04 to E08 were compared with the
Week 9 `results.json` only. This is still an AI review, not the owner's.

| # | Finding | Response | What changed |
|---|---|---|---|
| FC1 | "31 days: 50 %" in the brief and in E03. The exact share is 49.49 % of 13,049 campaigns; the Week 9 file stores 0.495, and rounding that a second time gave 50. | Corrected | Both places now say 49 %. |
| FC2 | The README named five optional extensions and the one left out; the handout lists seven. | Corrected | The README now says that "Design a validation project" is covered by the main direction (`wbs.md`, gate rules in `decision-memo.md`). |

Every other recomputed number matched to the stated precision: rows and funded share, goal bands, categories, the
29, 30 and 60 day rates, yearly rates, and every ROC-AUC and Brier score in `analysis/option_b_lookup_results.json`
(random and time-based split).
