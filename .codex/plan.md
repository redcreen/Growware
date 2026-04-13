# Project Plan

## Current Phase

Stage 1 planned; waiting for a user start command.

## Current Execution Line

- Objective: finish planning the long Stage 1 task for `Project 1`, including OpenClaw binding, daemon boundaries, and the first feedback/incident/judge/verifier/deploy contracts, while keeping execution paused until the user starts it
- Plan Link: stage-1 project-1 pilot foundation
- Runway: one planning-sized checkpoint that ends when the long task is explicit and start-ready
- Progress: 0 / 7 tasks complete
- Stop Conditions:
  - `Project 1` is still ambiguous
  - the Stage 1 deliverables are still incomplete
  - the user has not yet issued a start command
- Validation:
  - `brief.md`, `plan.md`, and `status.md` all point to the same Stage 1 long task
  - roadmap and development-plan describe the same Stage 1 workstreams and exit criteria
  - the repo can pause cleanly without accidentally starting implementation

## Execution Tasks

- [ ] EL-1 lock the recommended `Project 1` target for the Stage 1 plan
- [ ] EL-2 define the OpenClaw static channel and log binding for `Project 1`
- [ ] EL-3 define the `feedback adapter -> project daemon` boundary
- [ ] EL-4 define feedback event and incident record v0
- [ ] EL-5 define judge / verifier / deploy gate v0
- [ ] EL-6 define the daemon interface and Stage 2 start-gate checklist
- [ ] EL-7 keep execution paused until the user explicitly starts Stage 1

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
