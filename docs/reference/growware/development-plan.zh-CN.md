# Growware 开发计划

[English](development-plan.md) | [中文](development-plan.zh-CN.md)

## 目的

这份文档是给维护者看的 durable 详细执行计划，位置在 `docs/roadmap` 之下、`.codex/plan.md` 之上。

它回答的不是“今天聊天里说了什么”，而是：

`接下来先做什么、从哪里恢复、每个里程碑下面到底落什么细节。`

## 相关文档

- [../../roadmap.zh-CN.md](../../roadmap.zh-CN.md)
- [../../test-plan.zh-CN.md](../../test-plan.zh-CN.md)
- [feasibility.zh-CN.md](feasibility.zh-CN.md)
- [origin-transcript-2026-04-13.zh-CN.md](origin-transcript-2026-04-13.zh-CN.md)

## 怎么使用这份计划

1. 先看 roadmap，理解整体路线和当前里程碑。
2. 再看这里的“当前位置”和“顺序执行队列”，理解今天该从哪里恢复。
3. 需要具体约束时，再回到 `.codex/plan.md` 看实时执行控制面。

## 当前位置

| 项目 | 当前值 | 说明 |
| --- | --- | --- |
| 当前阶段 | Stage 2 experimental runtime v0 已启动；仓库现在已经能通过 readonly executor commands 接到真实 Project 1 工作区，但没有假装 `Project 1` 已完全接线。 | 当前维护者视角的阶段 |
| 当前切片 | `project-bound-readonly-executor-bridge-v0` | 当前执行线绑定的切片 |
| 当前执行线 | 扩展实验 runtime，让它在保持 deploy / rollback 继续受门禁的前提下，写下来自真实 Project 1 工作区的 readonly executor snapshot | 当前这轮真正要持续推进的工作 |
| 当前验证 | `experiments/mock_runtime/*`、bridge snapshots、`.growware/*`、`.policy/*`、architecture、roadmap、development plan、test plan 与 `.codex/*` 都描述同一个实验边界 | 当前线如何证明已经进入可执行状态 |

## 阶段总览

| 阶段 | 状态 | 目标 | 依赖 | 退出条件 |
| --- | --- | --- | --- | --- |
| Stage 0 | 已完成 | 保存起源对话、把项目统一命名为 Growware、建立真实文档基线 | 共享对话 | 对话已归档、命名已统一、基线文档已落下 |
| Stage 1 | 纸面已完成 | 用一条长任务把 Project 1 和第一版操作合同都定义清楚 | Stage 0 | target、channel 绑定、daemon 接口、核心合同和启动条件已明确 |
| Stage 1.5 | 纸面已完成 / 基础态 | 先定义 Growware 自身的 daemon 边界、project capsule、channel progress 合同与执行 handoff | Stage 1 | Growware 自身主线已显式化、可编译，并已足以支撑 Stage 2 / Stage 3 纸面基线 |
| Stage 2 | experimental v0 进行中 / deploy 仍受门禁 | 在批准过的 Growware daemon 边界之下，于项目 1 上实现一条带人工审批门的本地半自动闭环 baseline | Stage 1.5 | 一条隔离的 mock runtime 已能消费机器层，在本地走到 `approval-wait` / `close-out`，但不修改真实目标项目 |
| Stage 3 | 纸面基线已完成 / experiment hookup 排队中 | 扩展检测器、回归资产、门禁和低风险自动化的第一版 | Stage 2 | Stage 3 的 judge、automation band 和 regression 合同已显式且可编译，但尚未被生产 runtime 启用 |
| Stage 4 | 更后 | 支持多项目接入并保持隔离 | Stage 3 | 多项目并行时不发生 channel、状态、队列或部署污染 |

## 顺序执行队列

| 顺序 | 切片 | 当前状态 | 目标 | 验证 |
| --- | --- | --- | --- | --- |
| 1 | `bootstrap control surface` | 较早切片 | n/a | n/a |
| 2 | `origin capture and feasibility baseline` | 较早切片 | 保存共享对话并发布真实文档基线 | 对话归档、文档互链、命名收敛 |
| 3 | `stage-1 project-1 pilot foundation` | 支撑项 / 纸面已完成 | 把项目 1 合同、OpenClaw 绑定、daemon 接口和实现入口门写实 | `pilot-loop-v1` 与关联文档把第一条 pilot 写清楚，但不声称已 rollout |
| 4 | `growware-self daemon foundation` | 支撑项 / 纸面已完成 | 定义 Growware 自身 daemon 边界、project capsule、channel-progress 合同与 execution handoff | `daemon-foundation-plan`、`daemon-contracts/*` 与 `.growware/daemon-foundation/*` 让 Growware 自身主线既显式又可机器校验 |
| 5 | `stage-2-and-stage-3 paper baseline` | 支撑项 / 纸面已完成 | 定义 Stage 2 的 incident、verification、deploy、provenance，以及 Stage 3 的 judge、automation、regression 合同 | `stage-2-3-baseline`、`stage-2-3-contracts/*` 与 `.growware/stage-2-3/*` 让 Stage 2 / 3 主线既显式又可机器校验 |
| 6 | `experimental-mock-runtime-v0` | 当前 / 实现中 | 实现第一条隔离的本地 mock runtime，让它消费已编译机器层并在审批门前停住 | `experiments/mock_runtime/` 的 demo 与 smoke test 能通过，且不声称生产就绪 |
| 7 | `project-bound-readonly-executor-bridge-v0` | 当前 / 实现中 | 通过 readonly executor commands 把实验 runtime 接到真实 Project 1 工作区 | `bridge-status` 与 `demo` 能对真实 Project 1 工作区成功跑通，且不发生修改 |
| 8 | `single-project local semi-automatic loop` | 下一步 / runtime 排队中 | 在批准过的 Growware daemon 边界之下，于项目 1 上实现第一条本地 observe -> report -> repair -> verify -> deploy baseline 链路，并保留人工审批 | 一条 pilot 能在本地按可重复路径跑通 |
| 9 | `detectors, gates, and low-risk automation` | 更后 / runtime 排队中 | 把重复的人类纠正先沉淀成 v0 judge、门禁和 fallback 自动化 | 低风险自动化保持显式门禁且可回滚 |
| 10 | `multi-project onboarding and isolation` | 更后 | 支持第二个及更多目标项目接入 | 多项目不会互相污染 |
| 11 | `project-policy-source rollout` | 支撑项 / 已完成 | 把 `docs/policy/` 变成 Project 1 的可读规则源，并让入口文档都指向它 | 中英文成对的 policy source 已可见 |

## 里程碑细节

<a id="stage-0-origin-capture-and-feasibility"></a>
## Stage 0 - 起源归档与可行性基线

目标：

- 把起点对话完整保存成 Markdown
- 把临时占位名统一收敛为 `Growware`
- 发布能真实描述“实现前阶段”的 durable 文档

退出条件：

- 中英文 transcript Markdown 文件存在
- 对外文档都指向 Growware，而不是旧占位名
- feasibility、architecture、roadmap 和 test-plan 基线文档存在

<a id="stage-1-project-1-pilot-foundation-long-task"></a>
## Stage 1 - 项目 1 Pilot 基础长任务

推荐目标：

- `Project 1 = openclaw task system`

当前推荐默认值：

- `A channel = feishu6`
- `A channel` 同时承载反馈、审批和通知
- `Telegram` 作为备选通道
- 所有默认挂载 `task system` 的使用 channel 都视为 `B` 面
- 项目级 durable 配置与规则落在 `openclaw-task-system/.growware/`

这条长任务已经完成，相关结果已经落到：

这条长任务现在仍然停留在“先把启动门写清楚”的阶段，当前纸面汇总在 [pilot-loop-v1.zh-CN.md](pilot-loop-v1.zh-CN.md)。

### Stage 1 的长任务目标

- 锁定 `Project 1` 的目标对象
- 锁定 OpenClaw 的静态 channel 绑定
- 锁定 `feishu6` 和 `Telegram` 的主备策略
- 锁定 `feedback adapter -> project daemon` 的接线方式
- 锁定第一版 `feedback / incident / judge / verifier / deploy gate` 合同
- 锁定项目内 `.growware/` 的 durable 边界
- 锁定 daemon 需要暴露的本地接口
- 锁定什么情况下才允许进入 Stage 2

### Stage 1 的 6 条工作流

1. `WS1 - Project Lock`
   - 明确 `Project 1` 的目标项目、仓库、工作区和本地部署边界
   - 明确 `.growware/` 在项目根目录下的落盘原则

2. `WS2 - OpenClaw Binding`
   - 明确 `feishu6` 是人类反馈入口
   - 明确 `feishu6` 同时承担 approval / notification
   - 明确 `Telegram` 是否只做 fallback
   - 明确所有默认挂载 `task system` 的 channel 都属于真实使用证据面
   - 明确 watched plugin、log source 和 approval channel

3. `WS3 - Feedback And Incident Contract`
   - 定义 feedback event 的最小字段
   - 定义 incident record 的最小字段
   - 定义哪些证据能从 feedback 升级为 incident

4. `WS4 - Judge / Verifier / Deploy Gate V0`
   - 定义什么算正常噪声、异常、incident
   - 定义第一版本地验证路径
   - 定义哪些动作必须人工审批

5. `WS5 - Project Daemon Interface`
   - 明确 daemon 负责什么，不负责什么
   - 列出它必须暴露的 `run / test / deploy / rollback / logs` 接口
   - 明确 daemon 读写 `.growware/` 的哪些路径

6. `WS6 - Start Gate Review`
   - 用一份 review 清单确认 Stage 2 已经可以开始
   - 如果 review 不通过，就停在 Stage 1，不开工

### Stage 1 的交付件

- 更新后的架构文档
- `Project 1` 静态绑定配置草案
- `.growware/` 目录结构草案
- feedback event v0
- incident record v0
- judge / verifier / deploy gate v0
- project daemon interface v0
- Stage 2 启动门清单

### Stage 1 的退出条件

- `Project 1` 已明确
- `feishu6`、`Telegram fallback` 与 A/B 对应关系已明确
- 项目内 `.growware/` 边界已明确
- daemon 边界已明确
- feedback、incident、judge、verifier、deploy gate 合同已明确
- 你明确下达开始指令，允许进入 Stage 2

### Stage 1 的开始条件

- 当前只完成“规划”
- 真正开始执行，必须等待你的明确命令

<a id="stage-15-growware-self--daemon-foundation"></a>
## Stage 1.5 - Growware 自身 / Daemon Foundation

目标：

- 在继续扩展目标项目执行线之前，先定义 Growware 自身的 daemon-first 控制层

当前主线判断：

- Growware 应先补齐自己作为 daemon-owned 项目控制面的合同
- 目标项目应作为挂接验证对象存在，而不是默认成为当前 roadmap 主线
- channel 对话应该先能通过 Growware 推动项目进展，而不是继续依赖 repo-local 的人工接续

当前参考文档：

- [daemon-foundation-plan.zh-CN.md](daemon-foundation-plan.zh-CN.md)

### Stage 1.5 的目标

- 定义 daemon responsibility boundary
- 定义 project capsule contract
- 定义 channel command / event model
- 定义 progress push / close-out contract
- 定义 policy loading 与 approval-check 路径
- 定义 executor / adapter handoff boundary
- 定义 learning-writeback contract

### Stage 1.5 的退出条件

- `daemon-foundation-plan*` 已显式存在并可 review
- `daemon-contracts/*` 已作为已批准合同的可 review source pack 存在
- `.growware/daemon-foundation/*` 能稳定从 source pack 编译并通过校验
- roadmap、development plan、test plan 与 `.codex/*` 都指向同一条 Growware-self 主线
- `Project 1` 被明确当成验证对象，而不是当前扩展主线
- 你明确批准这条线开始实现

当前结果：

- 这一阶段已经纸面完成，并成为 Stage 2 / Stage 3 纸面基线的前置基础

<a id="stage-2-single-project-local-semi-automatic-loop"></a>
## Stage 2 - 单项目本地半自动闭环

目标：

- 在 `Project 1` 上实现一条本地优先的闭环，包含结构化观测、incident 生成、修复执行、验证和带门禁部署

当前纸面基线：

- [stage-2-3-baseline.zh-CN.md](stage-2-3-baseline.zh-CN.md)
- [stage-2-3-contracts/README.zh-CN.md](stage-2-3-contracts/README.zh-CN.md)

预期结果：

- Growware 能在 `Project 1` 上证明端到端链路，但不夸大成“通用自治系统”
- `feishu6` 能稳定承接反馈、通知和审批
- `openclaw-task-system/.growware/` 能作为项目级 durable 控制面生效
- `growware` agent 的完成态会主动回发 `feishu6`
- close-out 会明确标记 `daemon-owned` / `terminal-takeover`
- 自然语言反馈可以先经项目本地 classifier 进入 runtime-owned executable intake

当前真实状态：

- 交付合同已经纸面完成
- runtime 集成仍然排队中

<a id="stage-3-detectors-gates-and-low-risk-automation"></a>
## Stage 3 - 检测器、门禁和低风险自动化

目标：

- 从重复 incident 中沉淀检测器、规则、回归资产和可回滚的自动化能力

当前纸面基线：

- [stage-2-3-baseline.zh-CN.md](stage-2-3-baseline.zh-CN.md)
- [stage-2-3-contracts/README.zh-CN.md](stage-2-3-contracts/README.zh-CN.md)

预期结果：

- 一部分低风险修复可以从“人工触发”迁移到“带门禁的自动执行”

当前真实状态：

- Stage 3 的 judge、automation band 和 regression 合同已经纸面完成
- 没有任何 runtime automation band 已被启用

<a id="stage-4-multi-project-onboarding-and-isolation"></a>
## Stage 4 - 多项目接入与隔离

目标：

- 支持第二个及更多项目接入 Growware
- 保持 channel、日志、状态、队列和部署边界隔离

预期结果：

- Growware 开始从“单项目控制层”变成“可复用项目控制层”

## 当前下一步

| 下一步 | 为什么做 |
| --- | --- |
| Review `stage-2-3-baseline*` 与 `stage-2-3-contracts/*`，并持续保持 `.growware/stage-2-3/*`、`.growware/daemon-foundation/*`、入口文档和 `.codex/*` 对齐 | 当前纸面完成态的关键问题，已经变成如何在 runtime 开工前保持 Stage 2 / 3 基线真实不漂移 |
