# Project Plan

## Current Phase

Stage 1.5 daemon-contract implementation established; Growware's readable daemon contract source now lives in `docs/reference/growware/daemon-contracts/`, and the current checkpoint is to keep that source, the generated `.growware/daemon-foundation/` layer, and the control surface aligned.

## Current Execution Line

- Objective: stand up one visible Growware-self daemon contract pack, compile it into `.growware/daemon-foundation/`, and keep it aligned with the policy source and entry docs
- Plan Link: daemon-foundation planning plus contract-pack implementation
- Runway: the current checkpoint is closed; reopen only when the daemon contract boundary changes or runtime integration is explicitly approved
- Progress: 4 / 4 tasks complete
- Stop Conditions:
  - the daemon contract pack remains hidden or split across docs
  - the generated `.growware/daemon-foundation/` layer drifts from `docs/reference/growware/daemon-contracts/`
  - the compiled `.policy/` layer drifts from `docs/policy/`
  - entry docs treat target-project expansion as the active line before Growware's own boundary is approved
  - the project policy or daemon contract still depends on chat-only agreement
- Validation:
  - `brief.md`, `plan.md`, and `status.md` point to the same Growware-self execution line
  - `daemon-foundation-plan*` and `daemon-contracts/*` exist and are linked from the entry docs
  - `python3 scripts/growware_daemon_contract_sync.py --write --json` and `--check --json` succeed
  - `docs/policy/README.md` and `docs/policy/project-1.md` remain linked from the entry docs
  - `python3 scripts/growware_policy_sync.py --write --json` and `--check --json` succeed

## Execution Tasks

- [x] EL-1 create `daemon-contracts/*` and record the Growware-self daemon contracts as durable docs
- [x] EL-2 implement `scripts/growware_daemon_contract_sync.py` and compile the contract pack into `.growware/daemon-foundation/`
- [x] EL-3 align README, docs home, roadmap, development plan, test plan, and reference docs to the new contract-pack checkpoint
- [x] EL-4 rerun daemon and policy machine-layer validation after the contract-pack pass

## Completion Rule

- Manual terminal execution is a bridge, not the success condition.
- The task is only complete when the capability has been written back into daemon-owned assets and can be reused without repeating the same manual takeover.

## Development Log Capture

- Trigger Level: high
- Auto-Capture When:
  - a natural-language daemon rule becomes a durable contract
  - the shared-contract / entry-doc boundary changes
  - a repeated human correction is promoted into a reusable daemon contract
  - the repo gains or changes a machine-layer compile / validate entrypoint
- Skip When:
  - the change is mechanical or formatting-only
  - no durable reasoning changed
  - the work simply followed an already-approved path
  - the work only restated existing project direction

## Architecture Supervision
- Signal: `green`
- Signal Basis: the daemon-foundation line is now explicit in both human-readable contracts and a generated machine layer, and the policy layer still compiles cleanly
- Problem Class: no active contract gap in the current implementation checkpoint; the next question is when and how runtime integration should start
- Root Cause Hypothesis: Growware previously had planning intent but no machine-readable daemon contract pack of its own
- Correct Layer: README, docs home, reference pack, roadmap, development plan, test plan, daemon-contract pack, and future runtime integration after approval
- Rejected Shortcut: treating chat agreement as a substitute for a durable daemon contract source
- Automatic Review Trigger: any entry doc starts pointing at a different daemon boundary, or the generated `.growware/daemon-foundation/` layer drifts from source
- Escalation Gate: continue automatically

## Escalation Model

- Continue Automatically: doc maintenance and machine-layer regeneration that keep the current contract truthful
- Raise But Continue: contract refinements or runtime-integration design that still preserve the current Growware-self daemon boundary
- Require User Decision: changing `Project 1`, changing `feishu6` as the human ingress, changing the approval boundary by assumption, or starting runtime implementation beyond the current contract pack

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
  - Exit Condition: Stage 1 is complete on paper and used as one pilot validation input rather than the active expansion line

- Slice: growware-self daemon foundation
  - Objective: define Growware's own daemon boundary, project capsule, channel-progress contract, execution handoff, and learning writeback before broader project execution
  - Dependencies: origin capture and feasibility baseline; pilot-loop paper gate; policy-source baseline
  - Risks: Growware keeps borrowing target-project work as false progress, or the daemon boundary stays too vague to implement safely
  - Validation: `daemon-foundation-plan*`, `daemon-contracts/*`, `.growware/daemon-foundation/*`, roadmap, development plan, test plan, and `.codex/*` point to the same self-improvement line
  - Exit Condition: the daemon-first line is explicit, machine-checkable, and approved for runtime integration

- Slice: single-project local semi-automatic loop
  - Objective: implement the first local observe -> report -> repair -> verify -> deploy loop with human approval for `Project 1` under the approved Growware daemon boundary
  - Dependencies: stage-1 project-1 pilot foundation; growware-self daemon foundation
  - Risks: the loop claims automation without stable judges or rollback, or target-project work starts before Growware's own boundary is explicit
  - Validation: one pilot can run end-to-end locally through a repeatable workflow
  - Exit Condition: Growware moves from documentation baseline to first runnable pilot

- Slice: project policy source rollout
  - Objective: make `docs/policy/` the human-readable Project 1 rule source and align all entry docs to it
  - Dependencies: origin capture and feasibility baseline; current repo docs baseline
  - Risks: source-of-truth drift between the contract and the entry docs
  - Validation: `docs/policy/README.md`, `docs/policy/project-1.md`, `shared-policy-contract`, and the entry docs all point to the same rule source
  - Exit Condition: the repo has one visible, bilingual, reviewable Project 1 policy source
