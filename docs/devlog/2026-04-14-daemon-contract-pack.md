# 2026-04-14 Daemon Contract Pack

[English](2026-04-14-daemon-contract-pack.md) | [中文](2026-04-14-daemon-contract-pack.zh-CN.md)

## Problem

Growware's self-improvement line had already been made explicit in planning docs, but it still lacked a machine-readable daemon contract layer of its own.

That gap created two risks:

- the repo could drift back into treating target-project expansion as Growware progress
- future runtime work would be forced to guess daemon boundaries from prose instead of loading a stable contract pack

## Key Thinking

- The repo is still in discussion / documentation mode, so the next long task should not guess runtime shape or scaffold app code.
- The right bridge is the same pattern already used for policy source: docs stay the editable truth, and a local script compiles them into a machine layer.
- The daemon boundary needed to be split into smaller durable contracts so later runtime work can consume them without re-parsing one planning memo.

## Solution

- Added `docs/reference/growware/daemon-contracts/` as the durable source pack for Growware's own daemon contracts.
- Defined seven contract documents covering daemon boundary, project capsule, channel command model, progress push, policy loading, execution handoff, and learning writeback.
- Implemented `scripts/growware_daemon_contract_sync.py` to compile those docs into `.growware/daemon-foundation/` and validate drift.
- Aligned README, docs home, roadmap, development plan, test plan, `.codex/*`, and host views to the new contract-pack checkpoint.

## Validation

```bash
python3 scripts/growware_daemon_contract_sync.py --write --json
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
```

## Follow-Up

- Review whether the contract fields are still too wide or too narrow before runtime integration starts.
- Keep all edits flowing through the doc source and rerun both sync scripts after every contract change.
- Do not treat this contract pack as proof that Growware runtime wiring is already implemented.
