# Project Plan

## Current Phase

Experimental runtime v0 authorized; the current checkpoint is to consume the compiled daemon, Stage 2/3, and policy machine layers through one isolated local mock runtime and a project-bound readonly executor bridge without widening the runtime claim beyond that sandbox.

## Current Execution Line

- Objective: implement one project-bound readonly executor bridge under `experiments/mock_runtime/` that loads the compiled machine layers, records executor snapshots from the real Project 1 workspace, reaches `approval-wait`, and closes out approved work without deploy execution
- Plan Link: pilot-loop gate plus daemon-foundation contracts plus Stage 2/3 paper baseline plus experimental runtime v0 plus project-bound readonly executor bridge
- Runway: one isolated runtime slice that ends when the bridge status, demo flow, and smoke test pass and the docs/control surface describe the same boundary
- Progress: 4 / 4 tasks complete
- Stop Conditions:
  - the experimental runtime stops consuming the compiled machine layers directly
  - the generated `.growware/stage-2-3/` or `.growware/daemon-foundation/` layers drift from source
  - the compiled `.policy/` layer drifts from `docs/policy/`
  - entry docs start claiming Project 1 runtime is already live
  - the experimental runtime starts implying deploy or rollback execution
  - the readonly bridge starts using write-capable target-project commands
- Validation:
  - `brief.md`, `plan.md`, and `status.md` point to the same experimental runtime execution line
  - `python3 scripts/growware_stage23_contract_sync.py --check --json` succeeds
  - `python3 scripts/growware_daemon_contract_sync.py --check --json` succeeds
  - `python3 scripts/growware_policy_sync.py --check --json` succeeds
  - `python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime` succeeds
  - `python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime` succeeds
  - `python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'` succeeds

## Execution Tasks

- [x] EL-1 extend source-of-truth docs and control surface to the project-bound readonly executor bridge boundary
- [x] EL-2 implement readonly target-project bridge commands in `experiments/mock_runtime/`
- [x] EL-3 capture bridge snapshots in the demo flow and smoke test
- [x] EL-4 rerun bridge, runtime, and machine-layer verification

## Completion Rule

- Manual terminal execution is a bridge, not the success condition.
- The task is only complete when the capability has been written back into daemon-owned assets and can be reused without repeating the same manual takeover.

## Development Log Capture

- Trigger Level: high
- Auto-Capture When:
  - a Stage 2 or Stage 3 runtime rule becomes a durable contract
  - a repeated human judgment is promoted into a judge or regression candidate
  - the repo gains or changes a machine-layer compile / validate entrypoint
- Skip When:
  - the change is mechanical or formatting-only
  - no durable reasoning changed
  - the work simply followed an already-approved path
  - the work only restated existing project direction

## Architecture Supervision
- Signal: `green`
- Signal Basis: the repo now has one working readonly bridge into the real Project 1 workspace, and all machine layers still compile cleanly
- Problem Class: the readonly bridge is in place; the next question is when to widen it into a write-capable executor
- Root Cause Hypothesis: Growware needed auditable contact with the real project before any write-capable executor could be justified
- Correct Layer: readonly bridge review and later explicit approval before widening into real mutation or deploy
- Rejected Shortcut: treating readonly project access as permission to write or deploy
- Automatic Review Trigger: any entry doc starts claiming Project 1 runtime completion, or any machine layer drifts from source
- Escalation Gate: continue automatically

## Escalation Model

- Continue Automatically: doc maintenance, machine-layer regeneration, and readonly-bridge refinement that stay inside the current isolated boundary
- Raise But Continue: contract refinements or bridge improvements that still preserve the current Growware, Stage 2/3, and policy boundaries
- Require User Decision: changing `Project 1`, changing `feishu6` as the human ingress, changing approval boundaries by assumption, or binding any write-capable executor / deploy path

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
  - Exit Condition: the daemon-first line is explicit, machine-checkable, and approved as the basis for later runtime work

- Slice: stage-2-and-stage-3 paper baseline
  - Objective: define the Stage 2 incident, verification, deploy, provenance, judge, automation-band, and regression-asset contracts without claiming runtime completion
  - Dependencies: stage-1 project-1 pilot foundation; growware-self daemon foundation; policy-source baseline
  - Risks: the repo may confuse paper completion with runtime completion, or leave Stage 2/3 rules trapped in prose
  - Validation: `stage-2-3-baseline*`, `stage-2-3-contracts/*`, `.growware/stage-2-3/*`, roadmap, development plan, test plan, and `.codex/*` point to the same paper-complete line
  - Exit Condition: the Stage 2/3 line is explicit, machine-checkable, and ready for runtime integration review

- Slice: experimental-mock-runtime-v0
  - Objective: implement one isolated local mock runtime that consumes the compiled machine layers and proves the daemon-side control loop without deploy execution
  - Dependencies: stage-1 project-1 pilot foundation; growware-self daemon foundation; stage-2-and-stage-3 paper baseline; policy-source baseline
  - Risks: the repo may overclaim target-project ownership or widen the experiment into production assumptions
  - Validation: `experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime` and `python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'` succeed
  - Exit Condition: the experimental runtime is reproducible, approval-gated, and clearly isolated from the real target project

- Slice: project-bound-readonly-executor-bridge-v0
  - Objective: bridge the experimental runtime into the real Project 1 workspace through readonly executor commands only
  - Dependencies: stage-1 project-1 pilot foundation; growware-self daemon foundation; stage-2-and-stage-3 paper baseline; experimental-mock-runtime-v0
  - Risks: the bridge may drift from the real target-project entrypoints or overclaim write capability
  - Validation: `python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime` and the demo/smoke test succeed
  - Exit Condition: Growware can record readonly executor snapshots from the real Project 1 workspace without mutation

- Slice: single-project local semi-automatic loop
  - Objective: implement the first local observe -> report -> repair -> verify -> deploy loop with human approval for `Project 1` under the approved Growware daemon boundary
  - Dependencies: stage-1 project-1 pilot foundation; growware-self daemon foundation; stage-2-and-stage-3 paper baseline
  - Risks: the loop claims automation without stable judges or rollback, or target-project work starts before Growware's own boundary is explicit
  - Validation: one pilot can run end-to-end locally through a repeatable workflow
  - Exit Condition: Growware moves from documentation baseline to first runnable pilot

- Slice: project policy source rollout
  - Objective: make `docs/policy/` the human-readable Project 1 rule source and align all entry docs to it
  - Dependencies: origin capture and feasibility baseline; current repo docs baseline
  - Risks: source-of-truth drift between the contract and the entry docs
  - Validation: `docs/policy/README.md`, `docs/policy/project-1.md`, `shared-policy-contract`, and the entry docs all point to the same rule source
  - Exit Condition: the repo has one visible, bilingual, reviewable Project 1 policy source
