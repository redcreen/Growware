# Growware Stage 2 And Stage 3 Paper Baseline

[English](stage-2-3-baseline.md) | [中文](stage-2-3-baseline.zh-CN.md)

## Purpose

这份文档记录的是：在这个仓库里、又不伪造“runtime 已经落地”的前提下，Stage 2 和 Stage 3 最强但仍然真实的基线能做到什么程度。

它回答一个实际问题：

`Growware 以后要真地声称自己进入了 Stage 2 或 Stage 3 运行态，今天至少得先把哪些东西写清楚、可 review、可编译？`

## Status

- status: `draft / review required`
- project mode: `discussion and documentation`
- stage scope: `paper baseline only`
- last reviewed: `2026-04-14`

## Why This Exists

用户要求把项目从当前状态一口气推进到 Stage 3。

但在这个仓库里，真实边界只能是：

- 把 Stage 2 和 Stage 3 的交付合同补齐到纸面完成
- 把这些合同编译成机器可读层
- 不去假装 runtime 闭环已经真实跑起来

所以这份基线不是“可运行完成态”的声明。

它是后续 runtime 工作应该直接读取的 durable source pack，而不是继续从聊天记录或一份大而泛的规划 memo 里靠猜。

## What This Baseline Covers

- 一份面向 `Project 1` 的 Stage 2 本地闭环交付基线
- 一份 incident lifecycle contract v1
- 一份 verification profile contract v1
- 一份 deployment gate contract v1
- 一份 close-out provenance contract v1
- 一份 judge-promotion contract v1
- 一份面向 Stage 3 的 low-risk automation band model
- 一份 regression-asset writeback contract v1

## What This Baseline Does Not Claim

- `openclaw-task-system/.growware/` 已经开始消费这些合同
- `feishu6 -> Growware -> Project 1` 已经端到端跑通
- Stage 2 runtime 已经完成
- Stage 3 的低风险自动化已经开启
- 生产部署已经自治

## Stage 2 Paper Outcome

只有当仓库能集中指向下面这些 reviewable 合同时，Stage 2 才能算在纸面上被写清楚：

- incident intake 与 lifecycle
- verification payload 与结果处理
- deployment approval gate 与 rollback 规则
- close-out provenance，以及 `daemon-owned` / `terminal-takeover` 标记

## Stage 3 Paper Outcome

只有当仓库能集中指向下面这些 reviewable 合同时，Stage 3 才能算在纸面上被写清楚：

- judge promotion 规则
- low-risk automation bands
- regression-asset writeback 规则
- 自动执行场景下的 escalation 与 rollback 约束

## Ordered Workstreams

### WS1 - Incident Lifecycle

定义运行证据或人工反馈如何进入同一条 durable incident lifecycle。

### WS2 - Verification And Deploy Gate

定义必须验证什么、审批 payload 至少要有什么，以及 rollback 如何继续保持门禁。

### WS3 - Close-Out Provenance

定义每次 close-out 如何保留执行来源、验证证据和延期 writeback。

### WS4 - Judge Promotion

定义重复出现的人类判断以后如何被提升成可复用 judge 候选。

### WS5 - Automation Bands

定义什么属于 `manual-only`、`approval-gated` 或 `low-risk automatic`。

### WS6 - Regression Asset Writeback

定义修复之后如何沉淀测试、回放、fixture，或明确记录延期。

### WS7 - Machine Layer

把这些 source docs 编译成一层本地机器可读资产，方便后续 runtime 直接读取。

## Current Durable Source Pack

- [stage-2-3-contracts/README.zh-CN.md](stage-2-3-contracts/README.zh-CN.md) 是当前的人类可 review source pack
- `python3 scripts/growware_stage23_contract_sync.py --write --json` 会把它编译进 `.growware/stage-2-3/`
- `python3 scripts/growware_stage23_contract_sync.py --check --json` 会校验是否漂移

## Runtime-Only Remaining Work

- 教目标项目从它自己的项目级控制面里消费这些合同
- 把 channel host、project adapter 和 executor 接到同一套机器层上
- 真跑通一条本地 observe -> report -> repair -> verify -> deploy 链路
- 在真的看到重复 incident 之前，不开启任何 Stage 3 automation band

## Paper Exit Criteria

- `stage-2-3-baseline*` 已存在且可 review
- `stage-2-3-contracts/*` 已作为详细 source pack 存在
- `.growware/stage-2-3/*` 能从 source pack 稳定编译并通过校验
- roadmap、development plan、test plan 与 `.codex/*` 都指向同一个 Stage 2/3 paper-baseline checkpoint
- 仓库依然没有靠假设声称 runnable runtime 已完成

