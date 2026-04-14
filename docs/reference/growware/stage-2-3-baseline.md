# Growware Stage 2 And Stage 3 Paper Baseline

[English](stage-2-3-baseline.md) | [中文](stage-2-3-baseline.zh-CN.md)

## Purpose

This document records the maximum truthful Stage 2 and Stage 3 baseline that can be completed inside this repository without pretending that runtime implementation is already live.

It answers one practical question:

`what must already be explicit, reviewable, and machine-compilable before Growware can later claim a real Stage 2 or Stage 3 runtime path?`

## Status

- status: `draft / review required`
- project mode: `discussion and documentation`
- stage scope: `paper baseline only`
- last reviewed: `2026-04-14`

## Why This Exists

The user asked to push the project through Stage 3 in one uninterrupted long task.

Inside this repo, the truthful limit is:

- complete the Stage 2 and Stage 3 delivery contracts on paper
- compile them into a machine-readable layer
- avoid claiming that the runtime loop is already implemented

So this baseline is not a runnable completion claim.

It is the durable source pack that later runtime work should read instead of guessing from chat or from one broad planning memo.

## What This Baseline Covers

- one explicit Stage 2 local-loop delivery baseline for `Project 1`
- one incident lifecycle contract v1
- one verification profile contract v1
- one deployment gate contract v1
- one close-out provenance contract v1
- one judge-promotion contract v1
- one Stage 3 low-risk automation band model
- one regression-asset writeback contract v1

## What This Baseline Does Not Claim

- that `openclaw-task-system/.growware/` already consumes these contracts
- that `feishu6 -> Growware -> Project 1` is already running end to end
- that Stage 2 runtime is complete
- that Stage 3 low-risk automation is enabled
- that production deployment is autonomous

## Stage 2 Paper Outcome

Stage 2 is treated as explicit only when the repo can point to one reviewable pack for:

- incident intake and lifecycle
- verification payloads and result handling
- deployment approval gates and rollback rules
- close-out provenance and daemon-owned vs terminal-takeover marking

## Stage 3 Paper Outcome

Stage 3 is treated as explicit only when the repo can point to one reviewable pack for:

- judge promotion rules
- low-risk automation bands
- regression-asset writeback rules
- escalation and rollback constraints for automated execution

## Ordered Workstreams

### WS1 - Incident Lifecycle

Define how runtime evidence or human feedback becomes one durable incident lifecycle.

### WS2 - Verification And Deploy Gate

Define what must be verified, what approval payload must exist, and how rollback remains gated.

### WS3 - Close-Out Provenance

Define how every close-out preserves execution source, validation refs, and deferred writeback.

### WS4 - Judge Promotion

Define how repeated human judgments later become reusable judge candidates.

### WS5 - Automation Bands

Define what counts as `manual-only`, `approval-gated`, or `low-risk automatic`.

### WS6 - Regression Asset Writeback

Define how fixes later produce tests, replays, fixtures, or explicit deferrals.

### WS7 - Machine Layer

Compile the source docs into one local machine-readable layer that later runtime work can load.

## Current Durable Source Pack

- [stage-2-3-contracts/README.md](stage-2-3-contracts/README.md) is the human-reviewable source pack
- `python3 scripts/growware_stage23_contract_sync.py --write --json` compiles it into `.growware/stage-2-3/`
- `python3 scripts/growware_stage23_contract_sync.py --check --json` validates drift

## Runtime-Only Remaining Work

- teach the target project to consume these contracts from its own project-local control surface
- wire the channel host, project adapter, and executor against the same machine layer
- run one real local observe -> report -> repair -> verify -> deploy path
- accumulate real repeated incidents before enabling any Stage 3 automation band

## Paper Exit Criteria

- `stage-2-3-baseline*` exists and is reviewable
- `stage-2-3-contracts/*` exists as the detailed source pack
- `.growware/stage-2-3/*` compiles and validates against that source pack
- roadmap, development plan, test plan, and `.codex/*` point to the same Stage 2/3 paper-baseline checkpoint
- the repo still does not claim runnable runtime completion by assumption

