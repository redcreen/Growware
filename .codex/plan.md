# Project Plan

## Current Phase

Stage 0-3 pilot baseline active; converging terminal takeover work into daemon-owned execution.

## Current Execution Line

- Objective: make the first real `feishu6` feedback path produce durable code changes and then convert that path into daemon-owned behavior
- Plan Link: single-project local semi-automatic loop
- Runway: one execution-sized checkpoint ending when the same class of feedback no longer depends on manual terminal takeover
- Progress: 2 / 5 tasks complete
- Stop Conditions:
  - daemon still cannot own completion notification
  - daemon still cannot distinguish and report `daemon-owned` vs `terminal-takeover`
  - the natural-language feedback path still depends on manual intervention
- Validation:
  - `brief.md`, `plan.md`, and `status.md` point to the same active execution line
  - the first real feedback change is represented in code, tests, and deploy flow
  - daemon close-out behavior is explicit and user-visible

## Execution Tasks

- [x] EL-1 bind `feishu6` to `growware` and verify the route is live
- [x] EL-2 use the first real feedback to drive one code change through test and local deploy
- [ ] EL-3 add completion notification back to `feishu6`
- [ ] EL-4 add execution provenance reporting: `daemon-owned` vs `terminal-takeover`
- [ ] EL-5 convert the current manual execution path into daemon-owned intake and execution rules

## Completion Rule

- Manual terminal execution is a bridge, not the success condition.
- The task is only complete when the capability has been written back into daemon-owned assets and can be reused without repeating the same manual takeover.

## Development Log Capture

- Trigger Level: high
- Auto-Capture When:
  - the first pilot target or boundary is chosen
  - a natural-language preference becomes a durable judge or contract
  - the approval boundary for deployment changes
  - a repeated human correction is promoted into a reusable rule
- Skip When:
  - the change is mechanical or formatting-only
  - no durable reasoning changed
  - the work simply followed an already-approved path
  - the work only restated existing project direction

## Architecture Supervision
- Signal: `yellow`
- Signal Basis: open blockers or architectural risks are still recorded; ownership or boundary drift is visible in the current slice
- Problem Class: premature execution before the planned long task is explicitly started
- Root Cause Hypothesis: planning clarity is now higher than start-control clarity unless the paused state is made explicit
- Correct Layer: roadmap, development plan, and explicit start-gate control
- Rejected Shortcut: treating a planned Stage 1 as if execution had already started
- Automatic Review Trigger: ownership or boundary drift is visible in the current slice
- Escalation Gate: raise but continue

## Escalation Model

- Continue Automatically: control-surface maintenance and doc alignment that keep the Stage 1 long task truthful
- Raise But Continue: planning refinements that still preserve the paused-until-start state
- Require User Decision: opening Stage 1 for execution, changing `Project 1`, or changing approval boundaries by assumption

## Slices
- Slice: bootstrap control surface
  - Objective: establish the minimum medium-tier control surface and entry routing
  - Dependencies: initial repository bootstrap
  - Risks: the project starts moving without a source of truth for scope or next actions
  - Validation: `validate_control_surface.py` returns `ok: True`
  - Exit Condition: the control surface exists and records current unknowns truthfully

- Slice: origin capture and feasibility baseline
  - Objective: preserve the shared conversation, align the project name, and publish truthful baseline docs
  - Dependencies: bootstrap control surface; captured share page
  - Risks: the project loses its starting context or overstates what exists
  - Validation: transcript, feasibility, architecture, roadmap, and test-plan docs exist and align
  - Exit Condition: the repo has a durable documentation baseline under the Growware name

- Slice: stage-1 project-1 pilot foundation
  - Objective: define `Project 1`, its OpenClaw wiring, its daemon boundary, and its core contracts as one long task
  - Dependencies: origin capture and feasibility baseline; architecture discussion
  - Risks: the repo starts building before the long task is complete or before the user starts it
  - Validation: Stage 1 workstreams, deliverables, exit criteria, and start gate are explicit in docs and `.codex/*`
  - Exit Condition: Stage 1 is complete on paper and waiting for a start command

- Slice: single-project local semi-automatic loop
  - Objective: implement the first local observe -> report -> repair -> verify -> deploy loop with human approval for `Project 1`
  - Dependencies: stage-1 project-1 pilot foundation
  - Risks: the loop claims automation without stable judges or rollback
  - Validation: one pilot can run end-to-end locally through a repeatable workflow
  - Exit Condition: Growware moves from documentation baseline to first runnable pilot
