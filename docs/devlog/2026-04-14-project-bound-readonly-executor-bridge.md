# 2026-04-14 Project-Bound Readonly Executor Bridge

[English](2026-04-14-project-bound-readonly-executor-bridge.md) | [中文](2026-04-14-project-bound-readonly-executor-bridge.zh-CN.md)

## Problem

The isolated mock runtime could prove the Growware control flow locally, but it still did not touch the real `Project 1` workspace at all.

That left a gap between a fully synthetic demo and a truthful runtime bridge.

## Key Thinking

- The next bridge had to stay readonly.
- The target project already exposed safe preview and preflight entrypoints.
- Growware should call those entrypoints from its own experimental runtime and record the results as executor snapshots.

## Solution

- Added a readonly project-bound bridge to `experiments/mock_runtime/runtime.py`.
- The bridge now calls the real `openclaw-task-system` entrypoints for project summary, preflight, and binding preview.
- The demo and smoke test now verify that Growware can reach the real Project 1 workspace without mutation.

## Validation

```bash
python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## Follow-Up

- Keep the bridge readonly until a later explicit approval allows a write-capable executor.
- Preserve executor snapshots as durable provenance instead of hiding them in terminal output.
