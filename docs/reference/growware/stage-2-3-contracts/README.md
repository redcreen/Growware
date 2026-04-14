# Growware Stage 2 And Stage 3 Contract Pack

[English](README.md) | [中文](README.zh-CN.md)

## Purpose

This directory holds the detailed source contracts for the Stage 2 and Stage 3 paper baseline.

The docs in this directory are the human-reviewable source of truth. The local machine layer is compiled from them into `.growware/stage-2-3/`.

## Contracts

- [incident-lifecycle.md](incident-lifecycle.md): how incidents are created, promoted, advanced, and closed
- [verification-profile.md](verification-profile.md): what every repair verification record must contain
- [deployment-gate.md](deployment-gate.md): what actions are approval-gated, blocked, or rollback-only
- [close-out-provenance.md](close-out-provenance.md): how close-out preserves provenance and unresolved follow-up
- [judge-promotion.md](judge-promotion.md): how repeated judgments become durable judge candidates
- [automation-bands.md](automation-bands.md): what qualifies for manual-only, approval-gated, or low-risk automatic handling
- [regression-assets.md](regression-assets.md): how regression assets are proposed, accepted, deferred, or missing

## Compile And Validate

```bash
python3 scripts/growware_stage23_contract_sync.py --write --json
python3 scripts/growware_stage23_contract_sync.py --check --json
```

## Reading Rule

- read [../stage-2-3-baseline.md](../stage-2-3-baseline.md) first for the high-level boundary
- read this contract pack when implementation details need stable fields and rules
- treat the generated `.growware/stage-2-3/` files as machine-readable output, not as editable source

