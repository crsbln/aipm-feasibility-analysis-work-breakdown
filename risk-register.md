# Risk and Control Register (optional extension)

**Reference date:** 2026-11-27 · Likelihood and severity are Claude's judgement ratings (Low / Medium / High),
**not measurements**; the owner should re-rate them. Every response maps to a WBS work package.

| ID | Cause | Event | Impact | Likelihood | Severity | Preventive control | Response if it happens | Owner | Trigger | Residual | WBS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | A single number looks like a verdict | Creators read "below average" as "don't launch", or re-run inputs to push the number up | Creators abandon viable plans or act on model habits (E08) | Medium | High | Bands relative to 36 %; patterns worded as patterns; no what-if; comprehension test | Change the format; drop C if misreading stays above the threshold | AI PM | Misreading above the 1.3.3 threshold | Medium | 1.4.1, 1.5.1, 1.5.2 |
| R02 | Non-commercial, share-alike licence; unread platform terms | Legal reading says a table or a model may not be published | No public output possible on this data | Medium | High | Legal reading before any publishing (G1) | Stop, or look for another data basis (1.2.2) | Legal reviewer / AI PM | 1.2.1 verdict "no" or "unclear" | Low (nothing published early) | 1.2.1, 1.2.3 |
| R03 | Data ends January 2018 | No lawful recent data exists | C can never pass G2 | High | Medium | Source assessment before any build | Keep B as history, or stop | Data scientist role | 1.2.2 finds no usable source | Medium | 1.2.2, 1.3.2 |
| R04 | Small network, no incentives | Too few creators agree to talk | Demand stays unknown | Medium | High | Recruit across several categories; short sessions | Report as "insufficient evidence"; the gate cannot say "publish" | AI PM | Fewer than 5 interviews | Medium | 1.1.1, 1.1.2 |
| R05 | The owner built the model | Analysis leans towards C | A weak case gets built | Medium | Medium | Gates fixed before rating; four arguments; thresholds set before results (1.3.3) | Independent review of the gate memo | AI PM | Thresholds changed after results | Low | 1.3.3, 1.7.2, 1.8.2 |
| R06 | A server call per check | Running cost grows with traffic | Surprise bill | Low | High | Measure cost per visit at 50,000 visitors before going live (G3) | Prefer the static or in-browser design | Data scientist role | Measured cost above the owner's limit | Low | 1.6.1 |
| R07 | Interview notes hold personal data | Notes leak or are kept too long | Privacy breach | Low | High | Consent pack, anonymised notes, deletion date, notes never in the repo or AI tools | Report and delete; inform participants | AI PM | Personal data found in a spot check | Low | 1.1.1, 1.1.2, 1.8.4 |
| R08 | Joint authorship | A teammate objects to reuse | C cannot use the Week 9 model | Low | Medium | Ask before any C mock is shown | Use B only, or retrain separately | AI PM | A "no" in 1.8.1 | Low | 1.8.1 |

Check: every response above maps to at least one work package in `wbs.md`. No new scope was needed.
