# Experimental Runtime V0

[English](experimental-runtime-v0.md) | [中文](experimental-runtime-v0.zh-CN.md)

## Purpose

This document records the first approved runtime step after the paper baseline.

It answers one practical question:

`what runtime work is now allowed in this repo, and what still remains out of scope?`

## Status

- status: `active experimental slice`
- last reviewed: `2026-04-14`
- implementation root: `experiments/mock_runtime/`

## Allowed Scope

- implement one local-only mock runtime
- load `.policy/`, `.growware/daemon-foundation/`, and `.growware/stage-2-3/` directly
- run one project-bound readonly executor bridge into `openclaw-task-system`
- model the control loop as command intake, project resolution, incident recording, verification, approval wait, approval, and close-out
- keep all state inside an isolated experimental workspace
- prove the control-plane flow before touching a real target-project executor

## Out Of Scope

- direct `feishu6` host binding
- mutation of the real `openclaw-task-system` workspace
- deploy execution
- rollback execution
- production readiness
- autonomous release

## Required Runtime Behaviors

- support `status`, `incident`, `continue`, `approve`, `block`, and `close` command shapes
- validate the experimental capsule against the project-capsule contract
- load the policy machine layer before action evaluation
- stop at approval-gated actions instead of pretending deploy is allowed
- record one executor snapshot from the real Project 1 workspace before approval-wait
- emit structured progress, approval, and close-out payloads
- write close-out provenance and at least one writeback proposal during the demo flow

## Verification

```bash
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## Exit Criteria

- the mock runtime can initialize an isolated workspace
- the demo flow records an incident, reaches `approval-wait`, and produces a close-out after explicit approval
- the demo flow does not execute deploy or rollback
- the source-of-truth docs and `.codex/*` point to the same experimental boundary
