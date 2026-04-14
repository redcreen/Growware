# Growware Daemon Foundation Plan

[English](daemon-foundation-plan.md) | [中文](daemon-foundation-plan.zh-CN.md)

## 目的

这份文档记录的是：在继续扩展目标项目执行线之前，Growware 自身需要先补齐哪条规划主线。

它回答一个实际问题：

`如果希望用户通过 channel 对话来推动项目进展，Growware 自己必须先拥有哪套 daemon-first 控制合同？`

## 当前状态

- status: `draft / review required`
- project mode: `discussion and documentation`
- current line: `Growware self-improvement before broader project execution`
- last reviewed: `2026-04-14`

## 为什么这才是当前主线

这个仓库现在已经有：

- 起源材料
- 第一条 pilot loop 的纸面启动门
- policy source 基线

但它还没有足够清楚地定义 Growware 自身的 daemon-first 控制合同。

如果缺了这层，主线就会跑偏：

- 目标项目的 feature work 会被误当成 Growware 的进展
- channel 对话仍然依赖 repo-local 的人工接管
- 项目进展不是 daemon-owned
- `Project 1` 会被误当成主线本体，而不是一个验证对象

所以当前下一条规划主线应该是完善 Growware 自身，而不是继续放大别的项目。

## 目标结果

Growware 最终应该成为一个 daemon-owned 的项目控制层，至少能做到：

1. 把 channel 对话接成结构化的项目驱动输入
2. 判断输入属于哪个项目
3. 在临时聊天记忆之外维护项目进展状态
4. 决定当前应该 steer、report、approve，还是 delegate execution
5. 把进展和 close-out 再推回 channel
6. 让 daemon-owned execution 和 terminal takeover 遵守同一套 policy / approval 规则

## Growware 自己必须拥有的能力

### 1. Channel Dialogue Ingress

Growware 需要一条 daemon-owned 的入口合同，把 channel 对话归一化成耐久事件，例如：

- project steering
- progress query
- approval
- incident report
- continue / resume
- close-out acknowledgement

### 2. Project Registry And Binding

Growware 需要一套项目注册与绑定层，回答：

- 现在挂了哪些项目
- 哪些 channel 可以推进它们
- 哪些审批是有效的
- 每个项目对应哪份 project-local control surface
- 哪些 validation / deploy 入口可以调用

### 3. Project Capsule

每个被 Growware 管理的项目，对 Growware 来说都应该是一个稳定的 project capsule，而不是任意散落的 repo 状态。

至少应该暴露：

- project identity
- current phase
- current execution line
- current blockers
- approval boundary
- policy source 与 machine layer 入口
- validation 入口
- deploy / rollback 入口

### 4. Daemon State Machine

Growware 需要自己的状态机，覆盖：

- intake
- triage
- project selection
- planning
- delegation
- verification review
- approval wait
- close-out
- learning writeback

### 5. Progress Push Contract

Growware 应该能把项目进展结构化地推回 channel。

至少要覆盖：

- current progress snapshot
- next action
- blocker summary
- approval request
- verification result
- close-out provenance

### 6. Execution Handoff Boundary

Growware 自己必须明确判断什么时候：

- 只靠 daemon-owned project state 回答
- 只更新项目进展而不触发代码执行
- 委托给目标项目执行器
- 停下来等待审批

这条 handoff boundary 必须显式存在，不然 Growware 很容易再次退化成“继续去改 Project 1”。

### 7. Policy And Rule Consumption

Growware 必须从 machine layer 读取当前项目规则，而不是从聊天上下文里临时猜。

至少包括：

- project policy source 位置
- compiled machine policy 加载路径
- approval checks
- daemon-owned 与 terminal-takeover 的一致性

### 8. Durable Learning Capture

Growware 需要落实那条 durable rule：每个被解决的人类问题，以后都应该成为可复用资产。

所以 daemon 规划里必须包含 close-out 如何回写：

- rule proposals
- judge proposals
- regression assets
- execution source provenance

## Growware 不应该拥有的东西

- 目标项目的业务逻辑
- OpenClaw 宿主内部实现
- 任意 per-project 的实现细节
- 通过假设直接改写别的项目 roadmap
- 未经审批就许诺自治部署

## 当前规划工作流

### WS1 - Daemon Responsibility Boundary

明确 Growware daemon 负责什么，不负责什么；并与下面几层分开：

- channel host
- target-project adapter
- target-project runtime
- terminal takeover

### WS2 - Channel Command And Event Model

定义 Growware 能耐久接收的最小 channel 输入，例如：

- `status`
- `continue`
- `approve`
- `block`
- `incident`
- `close`

### WS3 - Project Capsule Contract

定义 Growware 面向每个已挂项目读取的稳定合同。

### WS4 - Progress Push And Close-Out Contract

定义 Growware 如何回报：

- current status
- next action
- blockers
- verification result
- approval wait
- final close-out

### WS5 - Policy Loading And Gate Evaluation

定义 Growware 在采取动作前，如何读取 `.policy/` 或批准过的兼容层。

### WS6 - Executor / Adapter Handoff

定义 Growware 如何把工作委托进目标项目，而不让目标项目默认变成当前 roadmap 主线。

### WS7 - Learning Writeback

定义已解决工作如何沉淀成 rule / judge / regression asset proposal。

## 顺序规划队列

1. 定义 daemon boundary 和 non-goals。
2. 定义 project capsule schema 与最小字段。
3. 定义 channel command / event model。
4. 定义 progress push payload 与 close-out payload。
5. 定义 policy-loading 与 approval-check 路径。
6. 定义 executor / adapter handoff contract。
7. 定义 learning-writeback contract。

## 和 `Project 1` 的关系

`Project 1` 继续是 pilot target，也是验证对象。

但它不是当前默认的 feature expansion 主线。

当前建议顺序是：

1. 先把 Growware 自身的 daemon-owned control contract 写清楚
2. 经 review 批准这套合同
3. 再在这套边界之下收紧或实现目标项目集成

## Review Gates

在这条线开始实现之前，仓库里应明确记录：

- 一份经批准的 daemon responsibility boundary
- 一份经批准的 project capsule contract
- 一份经批准的 channel command / event model
- 一份经批准的 progress push contract
- 一份经批准的 execution handoff rule
- 一份经批准的 learning-writeback rule

## Current Durable Source Pack

- [daemon-contracts/README.zh-CN.md](daemon-contracts/README.zh-CN.md) 是当前这些合同的人类可 review source pack
- `python3 scripts/growware_daemon_contract_sync.py --write --json` 会把这些已 review 文档编译到 `.growware/daemon-foundation/`
- `python3 scripts/growware_daemon_contract_sync.py --check --json` 会校验机器层是否仍与合同文档保持一致

## 退出条件

- roadmap、development plan 与 `.codex/*` 都指向 Growware-self daemon foundation 这条主线
- daemon foundation 的工作流已经显式化
- daemon contract pack 已经作为可 review source 存在，并能稳定编译进 `.growware/daemon-foundation/`
- `Project 1` 被明确当成验证对象，而不是当前扩展主线
- 你已经 review 这些规划文档，并明确批准开始实现
