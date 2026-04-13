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
| 当前阶段 | Stage 1 已规划，等待开始指令。 | 来自 `.codex/plan.md` 的当前维护阶段 |
| 当前切片 | `stage-1 project-1 pilot foundation` | 当前执行线绑定的切片 |
| 当前执行线 | 把项目 1 的 target、OpenClaw 接线、daemon 职责、feedback/incident/judge/verifier/deploy 合同和启动条件一次规划完整，但先不执行 | 当前这轮真正要收口的工作 |
| 当前验证 | Stage 1 长任务的 workstreams、交付件、退出条件和启动门都已经明确 | 继续前如何证明这条线已收口 |

## 阶段总览

| 阶段 | 状态 | 目标 | 依赖 | 退出条件 |
| --- | --- | --- | --- | --- |
| Stage 0 | 已完成 | 保存起源对话、把项目统一命名为 Growware、建立真实文档基线 | 共享对话 | 对话已归档、命名已统一、基线文档已落下 |
| Stage 1 | 已规划 / 待启动 | 用一个长任务把项目 1 的基础合同和边界全部压实 | Stage 0 | target、channel 绑定、daemon 接口、核心合同和启动条件明确 |
| Stage 2 | 已排队 | 在项目 1 上实现一条带人工审批门的本地半自动闭环 | Stage 1 | 一条本地 observe -> report -> repair -> verify -> deploy 链路可跑通 |
| Stage 3 | 已排队 | 扩展检测器、回归资产、门禁和低风险自动化 | Stage 2 | 部分低风险 incident 可以在显式门禁下自动修复 |
| Stage 4 | 更后 | 支持多项目接入并保持隔离 | Stage 3 | 多项目并行时不发生 channel、状态、队列或部署污染 |

## 顺序执行队列

| 顺序 | 切片 | 当前状态 | 目标 | 验证 |
| --- | --- | --- | --- | --- |
| 1 | `bootstrap control surface` | 较早切片 | n/a | n/a |
| 2 | `origin capture and feasibility baseline` | 较早切片 | 保存共享对话并发布真实文档基线 | 对话归档、文档互链、命名收敛 |
| 3 | `stage-1 project-1 pilot foundation` | 当前 / 仅规划 | 把项目 1 的基础合同、OpenClaw 接线和 daemon 接口一次规划清楚 | Stage 1 长任务文档已明确，等待开始指令 |
| 4 | `single-project local semi-automatic loop` | 下一步 / 已排队 | 在项目 1 上实现第一条本地 observe -> report -> repair -> verify -> deploy 链路，并保留人工审批 | 一条真实 pilot 能按固定路径本地跑通 |
| 5 | `detectors, gates, and low-risk automation` | 更后 / 已排队 | 把重复的人类纠正沉淀成检测器、规则、门禁和回归资产 | 低风险自动化保持有显式门禁且可回滚 |
| 6 | `multi-project onboarding and isolation` | 更后 | 支持第二个及更多目标项目接入 | 多项目不会互相污染 |

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

这个长任务的目的不是写运行时代码，而是把真正开工前必须压实的边界一次定义完整。

### Stage 1 的长任务目标

- 锁定 `Project 1` 的目标对象
- 锁定 OpenClaw 的静态 channel 绑定
- 锁定 `feedback adapter -> project daemon` 的接线方式
- 锁定第一版 `feedback / incident / judge / verifier / deploy gate` 合同
- 锁定 daemon 需要暴露的本地接口
- 锁定什么情况下才允许进入 Stage 2

### Stage 1 的 6 条工作流

1. `WS1 - Project Lock`
   - 明确 `Project 1` 的目标项目、仓库、工作区和本地部署边界

2. `WS2 - OpenClaw Binding`
   - 明确哪个 channel 是人类反馈入口
   - 明确哪个 channel 或日志来源属于真实使用证据
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

6. `WS6 - Start Gate Review`
   - 用一份 review 清单确认 Stage 2 已经可以开始
   - 如果 review 不通过，就停在 Stage 1，不开工

### Stage 1 的交付件

- 更新后的架构文档
- `Project 1` 静态绑定配置草案
- feedback event v0
- incident record v0
- judge / verifier / deploy gate v0
- project daemon interface v0
- Stage 2 启动门清单

### Stage 1 的退出条件

- `Project 1` 已明确
- A/B 对应的 channel 与证据来源已明确
- daemon 边界已明确
- feedback、incident、judge、verifier、deploy gate 合同已明确
- 你明确下达开始指令，允许进入 Stage 2

### Stage 1 的开始条件

- 当前只完成“规划”
- 真正开始执行，必须等待你的明确命令

<a id="stage-2-single-project-local-semi-automatic-loop"></a>
## Stage 2 - 单项目本地半自动闭环

目标：

- 在 `Project 1` 上实现一条本地优先的闭环，包含结构化观测、incident 生成、修复执行、验证和带门禁部署

预期结果：

- Growware 能在 `Project 1` 上证明端到端链路，但不夸大成“通用自治系统”

<a id="stage-3-detectors-gates-and-low-risk-automation"></a>
## Stage 3 - 检测器、门禁和低风险自动化

目标：

- 从重复 incident 中沉淀检测器、规则、回归资产和可回滚的自动化能力

预期结果：

- 一部分低风险修复可以从“人工触发”迁移到“带门禁的自动执行”

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
| 等待你的开始指令，然后启动 `Stage 1 - 项目 1 Pilot 基础长任务` | 这轮先把长任务规划完整，但不自动开工 |
