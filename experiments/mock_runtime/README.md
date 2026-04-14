# Growware Mock Runtime

This directory contains the first isolated experimental runtime for Growware.

It is intentionally narrow:

- local only
- standard-library only
- no direct `feishu6` binding
- real project-bound readonly executor bridge
- no target-project mutation
- no deploy or rollback execution

## Commands

```bash
python3 experiments/mock_runtime/runtime.py init --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py status --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py incident --workspace /tmp/growware-mock-runtime --summary "Channel reply missing after task completion"
python3 experiments/mock_runtime/runtime.py continue --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py approve --workspace /tmp/growware-mock-runtime --incident-id INC-0001
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## What It Proves

- Growware can load the compiled daemon, Stage 2/3, and policy machine layers directly.
- Growware can call the real `openclaw-task-system` readonly entrypoints before verification and approval.
- Growware can model `status -> incident -> approval-wait -> close-out` in one isolated workspace.
- Approval-gated actions still stop before deploy.

## What It Does Not Prove

- that `Project 1` is wired end to end
- that code changes are executed against the real target project
- that deploy or rollback works
- that production automation is ready
