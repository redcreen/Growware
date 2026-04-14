# Growware Daemon Contract Pack

[English](README.md) | [中文](README.zh-CN.md)

## Purpose

This directory holds the durable contract pack for Growware's own daemon foundation.

The docs in this directory are the human-reviewable source of truth. The local machine layer is compiled from them into `.growware/daemon-foundation/`.

## Contracts

- [daemon-boundary.md](daemon-boundary.md): what the Growware daemon owns and what it must not own
- [project-capsule.md](project-capsule.md): the minimum contract Growware reads from each attached project
- [channel-command-model.md](channel-command-model.md): the stable channel-side command and event model
- [progress-push.md](progress-push.md): the structured progress, approval, verification, and close-out payload contract
- [policy-loading.md](policy-loading.md): how Growware loads machine-readable project rules before acting
- [execution-handoff.md](execution-handoff.md): when Growware answers from state, delegates, or stops for approval
- [learning-writeback.md](learning-writeback.md): how resolved work is turned into reusable follow-up assets

## Compile And Validate

```bash
python3 scripts/growware_daemon_contract_sync.py --write --json
python3 scripts/growware_daemon_contract_sync.py --check --json
```

## Reading Rule

- read [../daemon-foundation-plan.md](../daemon-foundation-plan.md) first for the planning line
- read this contract pack when implementation needs stable boundaries and interfaces
- treat the generated `.growware/daemon-foundation/` files as machine-readable output, not as the editable source
