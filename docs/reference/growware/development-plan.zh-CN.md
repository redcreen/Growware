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
| 当前阶段 | Stage 3 baseline 已完成，进入真实反馈运行期。 | 来自当前 pilot 的实际执行状态 |
| 当前切片 | `real-feishu6 pilot operation` | 当前执行线绑定的切片 |
| 当前执行线 | 接收 `feishu6-chat` 的真实反馈，通过 `growware` agent 进入 `openclaw-task-system` 工作区，先本地验证再走 deploy baseline 和通知回发 | 当前这轮真正要持续推进的工作 |
| 当前验证 | `.growware/`、OpenClaw 绑定、本地 deploy fallback、Gateway 重启、plugin smoke、install drift 已经落地并验证 | 当前线如何证明已经进入可运行状态 |

## 阶段总览

| 阶段 | 状态 | 目标 | 依赖 | 退出条件 |
| --- | --- | --- | --- | --- |
| Stage 0 | 已完成 | 保存起源对话、把项目统一命名为 Growware、建立真实文档基线 | 共享对话 | 对话已归档、命名已统一、基线文档已落下 |
| Stage 1 | 已完成 | 把项目 1 的基础合同和边界全部压实到真实仓库和宿主配置 | Stage 0 | target、channel 绑定、daemon 接口、核心合同和启动条件已落地 |
| Stage 2 | 已完成 | 在项目 1 上实现一条带人工审批门的本地半自动闭环 baseline | Stage 1 | 一条本地 observe -> report -> repair -> verify -> deploy 链路已实际跑通 |
| Stage 3 | 已完成（baseline） | 扩展检测器、回归资产、门禁和低风险自动化的第一版 | Stage 2 | 部分低风险 fallback 自动化已可运行，并保留显式门禁 |
| Stage 4 | 更后 | 支持多项目接入并保持隔离 | Stage 3 | 多项目并行时不发生 channel、状态、队列或部署污染 |

## 顺序执行队列

| 顺序 | 切片 | 当前状态 | 目标 | 验证 |
| --- | --- | --- | --- | --- |
| 1 | `bootstrap control surface` | 较早切片 | n/a | n/a |
| 2 | `origin capture and feasibility baseline` | 较早切片 | 保存共享对话并发布真实文档基线 | 对话归档、文档互链、命名收敛 |
| 3 | `stage-1 project-1 pilot foundation` | 已完成 | 把项目 1 的基础合同、OpenClaw 接线和 daemon 接口一次规划并落地 | `.growware/` 与 `growware` agent 已生效 |
| 4 | `single-project local semi-automatic loop` | 已完成 | 在项目 1 上实现第一条本地 observe -> report -> repair -> verify -> deploy baseline 链路，并保留人工审批 | 本地 deploy、重启、smoke、drift 已验证 |
| 5 | `detectors, gates, and low-risk automation` | 已完成（baseline） | 把重复的人类纠正先沉淀成 v0 judge、门禁和 fallback 自动化 | 低风险 fallback 自动化保持显式门禁且可回滚 |
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

当前推荐默认值：

- `A channel = feishu6`
- `A channel` 同时承载反馈、审批和通知
- `Telegram` 作为备选通道
- 所有默认挂载 `task system` 的使用 channel 都视为 `B` 面
- 项目级 durable 配置与规则落在 `openclaw-task-system/.growware/`

这条长任务已经完成，相关结果已经落到：

- `openclaw-task-system/.growware/`
- `scripts/runtime/growware_preflight.py`
- `scripts/runtime/growware_openclaw_binding.py`
- `scripts/runtime/growware_local_deploy.py`
- OpenClaw `feishu6-chat -> growware` 真实绑定

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

<a id="stage-2-single-project-local-semi-automatic-loop"></a>
## Stage 2 - 单项目本地半自动闭环

目标：

- 在 `Project 1` 上实现一条本地优先的闭环，包含结构化观测、incident 生成、修复执行、验证和带门禁部署

预期结果：

- Growware 能在 `Project 1` 上证明端到端链路，但不夸大成“通用自治系统”
- `feishu6` 能稳定承接反馈、通知和审批
- `openclaw-task-system/.growware/` 能作为项目级 durable 控制面生效

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
| 在 `feishu6-chat` 接收真实反馈并继续迭代 | 规划、接线和 deploy baseline 已经完成，接下来应进入真实人类反馈闭环 |
