# 2026-04-14 Stage 2 And Stage 3 Paper Baseline

[English](2026-04-14-stage23-paper-baseline.md) | [中文](2026-04-14-stage23-paper-baseline.zh-CN.md)

## Problem

The repo already had the pilot-loop gate, the policy source, and Growware's own daemon-foundation contracts, but Stage 2 and Stage 3 were still spread across roadmap-level prose.

That left three risks:

- the user could ask to "finish Stage 3" and the repo would have no truthful way to close that request inside documentation mode
- later runtime work would be forced to infer incident, verification, deployment, and automation rules from scattered text
- entry docs and `.codex/*` could drift and accidentally imply runtime completion

## Key Thinking

- `AGENTS.md` still keeps the repo in discussion and documentation mode, so "push through Stage 3" could only mean the maximum truthful paper-complete version.
- The right shape was the same one already used for policy source and daemon contracts: editable docs as source, plus a local compiler that produces one machine-readable layer.
- Stage 2 and Stage 3 needed to be split into smaller contracts so review could focus on delivery boundaries instead of one broad milestone label.

## Solution

- Added `docs/reference/growware/stage-2-3-baseline*` as the explicit paper-baseline checkpoint for Stage 2 and Stage 3.
- Added `docs/reference/growware/stage-2-3-contracts/` as the durable source pack for incident lifecycle, verification profile, deployment gate, close-out provenance, judge promotion, automation bands, and regression assets.
- Implemented `scripts/growware_stage23_contract_sync.py` to compile those docs into `.growware/stage-2-3/` and validate drift.
- Aligned README, docs home, roadmap, development plan, test plan, `.codex/*`, and host views so they point to the same paper-baseline checkpoint without claiming runnable runtime.

## Validation

```bash
python3 scripts/growware_stage23_contract_sync.py --write --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
```

## Follow-Up

- Review whether the Stage 2/3 contracts are still too wide or too narrow before runtime integration begins.
- Keep all changes flowing through the doc source and rerun all three sync scripts after every contract edit.
- Do not describe this paper baseline as proof that runtime integration, low-risk automation, or autonomous deployment already exists.
