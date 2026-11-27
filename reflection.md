# Lesson Answers and Reflection

**Reference date:** 2026-11-27 · Written by Claude in its own words and tied to this case, then compared with each
lesson's "Show solution". Honest note: the solutions were already visible when the lessons were read, so these are
not blind answers. Where an answer adds to the lesson's, the addition is noted.

## Lesson 01: Feasibility as a Decision

1. **Why business as usual?** Doing nothing also has costs and risks. Without it, any proposal looks good because it
   is only compared with nothing. *Matches the lesson.* In our case: A costs 0 but leaves 64 % failure untouched.
2. **Constraint vs risk?** A constraint is already true and limits the options (our non-commercial licence). A risk
   may or may not happen (creators misreading a band). *Matches.*
3. **When is conditional go more honest than go?** When the direction looks right but named evidence, approvals or
   capabilities are still missing. *Matches.* We went one step further (reframe), because the missing evidence
   could make the proposal itself pointless.

## Lesson 02: AI and Data Product Feasibility

1. **Why compare AI with a non-AI baseline?** The simple option may reach most of the outcome cheaper and safer.
   *Matches.* Measured here: a 120-cell table 0.681 vs the model 0.754 (E09).
2. **Why is a prototype not enough?** It runs on clean samples and light traffic, without security, monitoring,
   edge cases or lifecycle cost. *Matches.* For Launch Check, also: the prototype's data ends in 2018.
3. **What makes a metric decision-relevant?** It is measured on the intended population and tied to the costs of
   errors and an agreed threshold. *Matches.* Our weakness: no threshold exists yet (U08, WBS 1.3.3).

## Lesson 03: From Outcomes to Deliverables

1. **Security review in the WBS, not as a user story?** It is required scope, but no user asks for it. *Matches.* Our
   equivalent: the licence assessment (1.2.1).
2. **"Run usability tests": deliverable or activity?** Activity. The deliverable is the test report. *Matches.* We
   wrote "comprehension test report" (1.5.2).
3. **A requirement with no work package?** The scope is incomplete: nothing will satisfy or verify it. *Matches.*

## Lesson 04: Work Breakdown Structures

1. **Why is a WBS not a schedule?** It says what exists, not when or in which order. *Matches.*
2. **What does the 100% rule prevent?** Missing scope, double counting, and work outside the approved boundary.
   *Matches.*
3. **When to stop decomposing?** When one role can own it and everyone can tell when it is done, at a useful level
   of control. *Matches.*

## Lesson 05: Claude Code as an Analysis Team

1. **Why read-only reviewers?** So a reviewer reports and cannot quietly change evidence or scope. *Matches.*
2. **Can several agreeing subagents validate an assumption?** No. They can repeat the same premise. Only a real
   source, test or expert validates it. *Matches.* Here even more so: our "reviewers" were the same session.
3. **What stays an approval gate?** Option choice, ratings, major exclusions, estimates as commitments, the final
   recommendation. *Matches.* All of these await the owner here.

## Handout Reflection

- **Which feasibility dimension changed the proposal most?** Legal and data together: a non-commercial licence and
  data that ends in January 2018 turned "put the model online" into "validate first".
- **Which claim looked convincing until its evidence was checked?** "The goal rule reaches 0.637." The rerun showed
  0.640 as a ranking and 0.598 as a yes/no rule: the same words, two different measures (log D3).
- **What hidden scope appeared only during WBS creation?** Consent and deletion of interview notes (1.1.1, 1.8.4),
  teammate consent before even a mock of the model is shown (1.8.1), and thresholds that must be set before results.
- **Where did Claude add false certainty?** "30 days is the common default" and "readable in a minute" (log F1, F2).
- **What should be validated before anyone produces a detailed estimate?** Whether creators want pre-launch odds at
  all (A01). Every effort estimate for C is waste if the answer is no.
