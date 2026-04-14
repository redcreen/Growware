# Project-Bound Executor Bridge V0

[English](project-bound-executor-bridge-v0.md) | [中文](project-bound-executor-bridge-v0.zh-CN.md)

## Purpose

This document records the first real project-bound executor bridge used by Growware's experimental runtime.

It answers one practical question:

`how does Growware touch the real Project 1 workspace without skipping straight to mutation or deploy?`

## Status

- status: `active experimental bridge`
- last reviewed: `2026-04-14`
- implementation root: `experiments/mock_runtime/runtime.py`

## Allowed Bridge Actions

- resolve the real `openclaw-task-system` project root from the experimental capsule
- run `python3 scripts/runtime/growware_preflight.py --json`
- run `python3 scripts/runtime/growware_openclaw_binding.py --json`
- read a project summary through `scripts/runtime/growware_project.py`
- persist command results as executor snapshots in the experimental workspace

## Out Of Scope

- `--write` or `--restart` binding actions
- local deploy
- rollback
- target-project file mutation
- host restarts

## Verification Rule

The bridge is considered healthy only when all readonly commands exit cleanly and their results are preserved in the experimental runtime state.

If any bridge command fails:

- the incident flow must stop or block
- the runtime must not continue toward deploy-affecting work
- the failure must stay visible in the executor snapshot

## Verification

```bash
python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```
