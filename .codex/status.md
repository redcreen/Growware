# Project Status

## Delivery Tier
- Tier: `medium`
- Why this tier: the repository now has machine-layer contracts plus one isolated experimental runtime path, but it still needs multiple sessions before any real target-project loop is approved
- Last reviewed: 2026-04-14

## Current Phase

Experimental runtime v0 authorized on top of the pilot-loop, policy-source, daemon-foundation, and Stage 2/3 paper baselines; the repo is now moving from an isolated local mock runtime into one project-bound readonly executor bridge under `experiments/mock_runtime/`.

## Active Slice

`project-bound-readonly-executor-bridge-v0`

## Current Execution Line

- Objective: implement one project-bound readonly executor bridge that loads the compiled machine layers, records executor snapshots from the real Project 1 workspace, reaches `approval-wait`, and closes out approved work without deploy execution
- Plan Link: pilot-loop gate plus daemon-foundation contracts plus Stage 2/3 paper baseline plus experimental runtime v0 plus project-bound readonly executor bridge
- Runway: one experimental checkpoint that ends when bridge status, demo, smoke test, and entry docs all agree on the same boundary
- Progress: 4 / 4 tasks complete
- Stop Conditions:
  - the experimental runtime stops consuming the compiled machine layers directly
  - the generated `.growware/stage-2-3/` layer drifts from `docs/reference/growware/stage-2-3-contracts/`
  - the generated `.growware/daemon-foundation/` layer drifts from `docs/reference/growware/daemon-contracts/`
  - the compiled `.policy/` layer drifts from `docs/policy/`
  - entry docs start implying that Project 1 runtime is already live
  - the experimental runtime starts implying deploy or rollback execution
  - the readonly bridge starts using write-capable target-project commands

## Execution Tasks

- [x] EL-1 extend source-of-truth docs and control surface to the project-bound readonly executor bridge boundary
- [x] EL-2 implement readonly target-project bridge commands in `experiments/mock_runtime/`
- [x] EL-3 capture bridge snapshots in the demo flow and smoke test
- [x] EL-4 rerun bridge, runtime, and machine-layer verification

## Execution Standard

- Terminal takeover is allowed only as a temporary bridge.
- A task is not considered complete just because Codex finished it manually in the terminal.
- It counts as complete only after the new capability is written back into daemon-owned assets such as code, runtime rules, `.growware/` contracts, tests, or deployment flow.
- Every close-out must make clear whether the result was `daemon-owned` or `terminal-takeover`.

## Development Log Capture

- Trigger Level: high
- Pending Capture: no
- Last Entry: 2026-04-14 project-bound readonly executor bridge connected the experimental runtime to the real Project 1 workspace without mutation

## Architecture Supervision
- Signal: `green`
- Signal Basis: the pilot gate exists, the machine layers compile, and the current next risk is bridging into the real target project safely
- Root Cause Hypothesis: the isolated runtime harness exists, but it still needs auditable contact with the real Project 1 workspace
- Correct Layer: project-bound readonly bridge plus source-of-truth alignment before target-project execution broadens
- Automatic Review Trigger: any doc starts treating Project 1 runtime as already live, or any machine layer drifts from source
- Escalation Gate: continue automatically

## Current Escalation State
- Current Gate: continue automatically
- Reason: runtime experimentation is now explicitly approved, but it must stay readonly and truthful at the project boundary
- Next Review Trigger: review again when the bridge requests any write-capable executor or deploy capability

## Done

- repository renamed to `growware`
- medium-tier `.codex` control surface created
- origin transcript archived in Markdown
- feasibility, architecture, roadmap, development-plan, and test-plan docs created
- public docs aligned to Growware naming
- `docs/policy/README*` and `docs/policy/project-1*` now define the visible Project 1 policy source
- `pilot-loop-v1*` now records the first pilot target, operator path, real usage path, incident contract, verification contract, and deployment approval boundary
- `daemon-foundation-plan*` and `docs/reference/growware/daemon-contracts/*` now record Growware's own daemon boundary and handoff contracts
- `stage-2-3-baseline*` and `docs/reference/growware/stage-2-3-contracts/*` now record the Stage 2 incident, verification, deploy, provenance, judge, automation-band, and regression contracts
- `scripts/growware_daemon_contract_sync.py` compiles and validates the daemon contract source into `.growware/daemon-foundation/`
- `scripts/growware_stage23_contract_sync.py` compiles and validates the Stage 2/3 contract source into `.growware/stage-2-3/`
- `scripts/growware_policy_sync.py` compiles and validates the Project 1 source into `.policy/`
- `experiments/mock_runtime/runtime.py` now consumes the compiled machine layers and can run a local `status -> incident -> approval-wait -> close-out` demo
- `experiments/mock_runtime/test_runtime.py` now smoke-tests that isolated mock flow
- `experiments/mock_runtime/runtime.py bridge-status` now records readonly executor snapshots from the real `openclaw-task-system` workspace
- `project-bound-executor-bridge-v0*` now records the allowed readonly bridge boundary explicitly

## In Progress

- none; the project-bound readonly executor bridge slice is implemented and verified

## Blockers / Open Decisions

- How far the readonly bridge can go before it must hand off to a write-capable executor remains open.
- Whether Growware's future runtime should materialize as a sidecar, service, or another approved shape remains intentionally undecided.
- Whether the current Stage 2/3 contracts are still too narrow or too broad once exercised by the mock runtime remains open for review.

## Next 3 Actions
1. Review whether the readonly bridge boundary is still too narrow or too wide before binding a write-capable executor.
2. Keep contract edits flowing through the doc source, then rerun all three sync scripts plus bridge/runtime checks.
3. Bind a real write-capable target-project executor only with an explicit follow-up approval.
