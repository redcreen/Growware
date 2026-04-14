# Project 1 Pilot Loop V1

[English](pilot-loop-v1.md) | [中文](pilot-loop-v1.zh-CN.md)

## 目的

这份文档把“开始运行时实现之前，第一条 pilot loop 必须先明确什么”集中写清楚。

它是 Stage 1 的纸面启动门，不是 Stage 2 已经开始的证明。

## 当前状态

- status: `draft / implementation-gate candidate`
- project mode: `discussion and documentation`
- last reviewed: `2026-04-14`

## 实现入口门覆盖项

| 必需项 | 当前决定 |
| --- | --- |
| 一个具体 pilot target | `Project 1 = openclaw-task-system` |
| 一条 operator path | `feishu6 -> OpenClaw adapter -> Growware daemon -> 再回到 feishu6 做审批 / 状态回发` |
| 一条 real usage path | 所有默认挂载 `task system` 的使用 channel 都属于 `B` 面 |
| 一份 incident contract | 人工反馈和运行时证据都能提升为同一种 incident record v0 |
| 一份 verification contract | 每次拟议修复都必须先附带范围化校验、结果证据和回归沉淀意图 |
| 一条 deployment approval boundary | 第一条 pilot 的 deploy / rollback 都继续通过 `feishu6` 走人工审批 |

## Pilot Target

- `Project 1` 继续锁定为 `openclaw-task-system`，除非人类明确改动。
- Growware 仓库负责方法、policy source 和 pilot 边界定义。
- 目标项目会在 Stage 2 获批后拥有自己的 `openclaw-task-system/.growware/` 控制面。

## Operator Path

第一条 operator path 故意保持收缩：

1. 人类在 `feishu6` 里提交意图、反馈或审批。
2. OpenClaw adapter 把消息归一化成 feedback event。
3. Growware 把事件绑定到 `Project 1`。
4. daemon 判断这条事件只是反馈、应该立 incident，还是属于审批处理。
5. 一旦有后续动作，状态、审批请求和 close-out 仍然回到 `feishu6`。

这条路径定义的是第一条 pilot 的人类控制面，不等于 runtime 接线已经真实跑通。

## Real Usage Path

真实使用路径与 operator path 分开定义：

- 所有默认挂载 `task system` 的使用 channel 都属于 `B` 面
- 运行证据来自 gateway logs、目标项目日志、daemon 日志，以及可选结构化事件
- 采集本身不自动生成 incident；是否越过 incident 阈值由 judge layer 决定

## Incident Contract V0

incident 可以从人工反馈发起，也可以从运行证据发起，但两者都必须收敛成同一种记录结构。

### 提升规则

- 人工反馈只要描述了用户可见错误、预期落差或需要裁决的风险，就可以被提升
- 运行证据只有在 judge 判定它不是噪声时，才可以被提升
- 每个被提升的 incident 都必须保留回到原始证据的 provenance

### 必备字段

| 字段 | 含义 |
| --- | --- |
| `project_id` | 目标项目绑定 |
| `incident_id` | durable 标识符 |
| `source` | `human-feedback`、`gateway-log`、`plugin-log`、`daemon-log` 或结构化事件来源 |
| `summary` | 简短问题陈述 |
| `severity` | 初始影响级别 |
| `problem_type` | `spec-gap`、`runtime-observable` 或其他批准类别 |
| `evidence` | 指向日志、session 或 feedback event 的引用 |
| `approval_required` | 下一步动作是否允许自动继续 |
| `status` | intake、triage、repair、verify、blocked 或 closed |

## Verification Contract V0

任何修复在 verifier 产出范围化验证记录之前，都没有资格进入部署。

更细的 Stage 2 / Stage 3 纸面交付合同现在统一落在：

- [stage-2-3-baseline.zh-CN.md](stage-2-3-baseline.zh-CN.md)
- [stage-2-3-contracts/README.zh-CN.md](stage-2-3-contracts/README.zh-CN.md)

### 必备验证记录

| 字段 | 含义 |
| --- | --- |
| `incident_id` | 正在验证的 incident |
| `change_scope` | 本次改动的范围 |
| `checks_run` | 实际尝试过哪些验证步骤 |
| `result` | pass、fail 或 inconclusive |
| `evidence` | 输出引用、截图、日志或说明 |
| `regression_asset` | 本次新增或明确延期的规则、judge 或回归资产 |
| `residual_risk` | 还有哪些部分没有被证明 |

### 通过规则

- 拟议修复必须对应一个 incident
- 校验步骤必须和改动范围匹配
- 结果必须能被人类 reviewer 看见
- 如果暂时没有新增 durable 回归资产，close-out 里必须明说

## Deployment Approval Boundary V0

第一条 pilot 继续保持人工门禁部署。

| 动作 | 默认门禁 |
| --- | --- |
| 用户可见行为变化 | 必须先在 `feishu6` 获批 |
| 部署到目标运行面 | 必须先在 `feishu6` 获批 |
| 因坏部署触发 rollback | 默认也必须先在 `feishu6` 获批，除非以后单独定义紧急策略 |
| 会改变 pilot 语义的 policy 或合同变更 | 启用前必须先有人类显式 review |

## 本阶段明确不做的事

- 现在就决定最终 runtime 是 sidecar 还是 OpenClaw service
- 声称已经具备自治部署能力
- 仅凭这个仓库就声称 `openclaw-task-system/.growware/` 已经真实落地
- 把 `.policy/` 编译能力误写成 runtime 已经直接消费 `.policy/`

## Stage 2 启动门

只有当下面几项同时在文档和 `.codex/*` 里保持成立时，Stage 2 才允许开始：

- pilot target 已明确
- operator path 已明确
- real usage path 已明确
- incident contract 已明确
- verification contract 已明确
- deployment approval boundary 已明确
- 你明确下达开始实现的指令
