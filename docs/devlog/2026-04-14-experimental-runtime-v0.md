# 2026-04-14 Experimental Runtime V0

[English](2026-04-14-experimental-runtime-v0.md) | [中文](2026-04-14-experimental-runtime-v0.zh-CN.md)

## Problem

The repo had enough paper contracts to start runtime work, but it still had no runnable implementation that consumed the compiled machine layers directly.

That left a gap between approved contracts and executable behavior.

## Key Thinking

- The user explicitly approved implementation, so keeping the repo in paper-only mode would no longer be truthful.
- The first runtime step still needed to stay isolated, local, and approval-gated.
- The safest bridge was a no-dependency mock runtime that loads `.policy/`, `.growware/daemon-foundation/`, and `.growware/stage-2-3/` directly.

## Solution

- Switched the repo boundary from paper-only mode to experimental runtime foundation mode.
- Added `docs/reference/growware/experimental-runtime-v0*` to record the approved runtime boundary.
- Implemented `experiments/mock_runtime/` as a local CLI harness and smoke-test target.
- Kept deploy and rollback out of scope while still exercising incident, verification, approval, close-out, and writeback flow.

## Validation

```bash
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## Follow-Up

- Replace the synthetic mock executor path with a real project-bound executor only after the next explicit approval.
- Keep the experimental runtime consuming compiled machine layers rather than drifting back to prose parsing.
- Do not represent this harness as proof that `Project 1` deploy wiring is already live.
