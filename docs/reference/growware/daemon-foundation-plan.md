# Growware Daemon Foundation Plan

[English](daemon-foundation-plan.md) | [中文](daemon-foundation-plan.zh-CN.md)

## Purpose

This document records the planning line for improving Growware itself before broadening target-project execution work.

It answers one practical question:

`what must Growware itself own so users can drive project progress through channel dialogue without turning every target project into the current mainline?`

## Status

- status: `draft / review required`
- project mode: `discussion and documentation`
- current line: `Growware self-improvement before broader project execution`
- last reviewed: `2026-04-14`

## Why This Is The Current Mainline

The current repo already has:

- the origin material
- the pilot-loop paper gate
- the policy-source baseline

What it does not yet have clearly enough is Growware's own daemon-first control contract.

Without that layer, work drifts in the wrong direction:

- target-project feature work starts looking like Growware progress
- channel dialogue still depends on repo-local manual takeover
- project progress is not daemon-owned
- `Project 1` becomes the mainline instead of one validation target

So the next planning line should improve Growware itself, not broaden another project's scope.

## Outcome

Growware should become a daemon-owned project control layer that can:

1. accept channel dialogue as structured project-driving input
2. resolve which project the input belongs to
3. maintain project progress state outside ad hoc chat memory
4. decide whether to steer, report, approve, or delegate execution
5. push progress and close-out back through channels
6. keep the same policy and approval rules across daemon-owned execution and terminal takeover

## What Growware Must Own

### 1. Channel Dialogue Ingress

Growware needs one daemon-owned ingress contract that turns channel dialogue into durable events such as:

- project steering
- progress query
- approval
- incident report
- continue / resume
- close-out acknowledgement

### 2. Project Registry And Binding

Growware needs a project registry that answers:

- which projects are attached
- which channels can steer them
- which approvals are valid
- which project-local control surface belongs to each project
- which validation and deploy entrypoints are allowed

### 3. Project Capsule

Each attached project should appear to Growware as one project capsule, not as arbitrary repo state.

At minimum, a project capsule should expose:

- project identity
- current phase
- current execution line
- current blockers
- approval boundary
- policy source and machine layer entrypoints
- validation entrypoints
- deploy / rollback entrypoints

### 4. Daemon State Machine

Growware needs its own state machine for:

- intake
- triage
- project selection
- planning
- delegation
- verification review
- approval wait
- close-out
- learning writeback

### 5. Progress Push Contract

Growware should be able to push project progress back through channels in a structured way.

That contract should cover:

- current progress snapshot
- next action
- blocker summary
- approval request
- verification result
- close-out provenance

### 6. Execution Handoff Boundary

Growware itself should decide when to:

- answer from daemon-owned project state
- update project progress without code execution
- delegate to a target-project executor
- stop and request approval

This handoff boundary must stay explicit so Growware does not collapse into “just edit Project 1 again”.

### 7. Policy And Rule Consumption

Growware must load active project rules from the machine layer rather than inventing them from chat context.

That includes:

- project policy source location
- compiled machine policy loading
- approval checks
- daemon-owned vs terminal-takeover consistency

### 8. Durable Learning Capture

Growware should preserve the rule that every resolved human-reported problem later becomes a reusable asset.

So the daemon plan must include how close-out writes back:

- rule proposals
- judge proposals
- regression assets
- provenance of execution source

## What Growware Must Not Own

- target-project business logic
- OpenClaw host internals
- arbitrary per-project implementation details
- direct rewriting of another project's roadmap by assumption
- autonomous deployment promises without explicit approval

## Current Planning Workstreams

### WS1 - Daemon Responsibility Boundary

Define what the Growware daemon owns, and what remains in:

- channel host
- target-project adapter
- target-project runtime
- terminal takeover

### WS2 - Channel Command And Event Model

Define the minimal channel-level inputs that Growware can accept durably, such as:

- `status`
- `continue`
- `approve`
- `block`
- `incident`
- `close`

### WS3 - Project Capsule Contract

Define the stable project-facing contract Growware reads for each attached project.

### WS4 - Progress Push And Close-Out Contract

Define how Growware reports:

- current status
- next action
- blockers
- verification result
- approval wait
- final close-out

### WS5 - Policy Loading And Gate Evaluation

Define how Growware reads `.policy/` or the approved compatibility layer before acting.

### WS6 - Executor / Adapter Handoff

Define how Growware delegates work into a target project without turning that target project into the active roadmap by default.

### WS7 - Learning Writeback

Define how resolved work becomes a reusable rule, judge, or regression asset proposal.

## Ordered Planning Backlog

1. Define the daemon boundary and non-goals.
2. Define the project capsule schema and minimum fields.
3. Define the channel command / event model.
4. Define the progress push payload and close-out payload.
5. Define the policy-loading and approval-check path.
6. Define the executor / adapter handoff contract.
7. Define the learning-writeback contract.

## Relationship To `Project 1`

`Project 1` remains a pilot target and validation object.

It is not the current mainline for feature expansion.

The intended order is:

1. make Growware's daemon-owned control contract explicit
2. review and approve that contract
3. only then implement or tighten target-project integration work under that daemon boundary

## Review Gates

Before implementation starts on this line, the repo should explicitly record:

- one approved daemon responsibility boundary
- one approved project capsule contract
- one approved channel command / event model
- one approved progress push contract
- one approved execution handoff rule
- one approved learning-writeback rule

## Current Durable Source Pack

- [daemon-contracts/README.md](daemon-contracts/README.md) is the current reviewable source pack for these contracts
- `python3 scripts/growware_daemon_contract_sync.py --write --json` compiles the reviewed docs into `.growware/daemon-foundation/`
- `python3 scripts/growware_daemon_contract_sync.py --check --json` validates that the machine layer still matches the contract docs

## Exit Criteria

- roadmap, development plan, and `.codex/*` point to the Growware-self daemon foundation line
- the daemon foundation workstreams are explicit
- the daemon contract pack exists as reviewable source and compiles cleanly into `.growware/daemon-foundation/`
- `Project 1` is treated as a validation target, not the active expansion line
- the user has reviewed the planning docs and explicitly approved implementation to start
