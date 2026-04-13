# 路线图

[English](roadmap.md) | [中文](roadmap.zh-CN.md)

## 范围

这份路线图描述的是：如何把 Growware 这个概念，推进成一条真实的本地优先 pilot。它故意停在实现细节之前。

这些阶段下面更细的维护者执行队列，请看 [reference/growware/development-plan.zh-CN.md](reference/growware/development-plan.zh-CN.md)。

## 阶段

| 阶段 | 状态 | 目标 | 解锁什么 | 退出条件 |
| --- | --- | --- | --- | --- |
| [Stage 0 - 起源归档与可行性基线](reference/growware/development-plan.zh-CN.md#stage-0-origin-capture-and-feasibility) | 已完成 | 保存起点对话、统一命名并发布基线文档集 | 共享上下文与真实文档基线 | transcript 已归档、文档已互链、活跃命名已收敛到 Growware |
| [Stage 1 - 项目 1 Pilot 基础长任务](reference/growware/development-plan.zh-CN.md#stage-1-project-1-pilot-foundation-long-task) | 已完成 | 把项目 1、`feishu6` 接线、`.growware/` 边界、daemon 职责、合同和启动条件压实到真实项目和宿主配置 | Stage 2 本地闭环 | `openclaw-task-system/.growware/`、`growware` agent、`feishu6-chat` 绑定和 v0 合同已落地 |
| [Stage 2 - 单项目本地半自动闭环](reference/growware/development-plan.zh-CN.md#stage-2-single-project-local-semi-automatic-loop) | 已完成 | 在项目 1 上实现一条本地 observe -> report -> repair -> verify -> deploy baseline 链路 | 第一个可运行 Growware 基线 | 本地 deploy、Gateway 重启、plugin smoke 和 install drift 校验已跑通 |
| [Stage 3 - 检测器、门禁和低风险自动化](reference/growware/development-plan.zh-CN.md#stage-3-detectors-gates-and-low-risk-automation) | 已完成（baseline） | 补齐 judge、deploy gate 和低风险 fallback 自动化的第一版 | 更稳定的闭环 | judge/deploy gate v0 已落盘，安装受阻时可自动走 runtime sync fallback |
| [Stage 4 - 多项目接入与隔离](reference/growware/development-plan.zh-CN.md#stage-4-multi-project-onboarding-and-isolation) | 更后 | 支持多个项目并保持 channel、日志、队列、部署的隔离 | Growware 变成可复用控制层 | 多项目并行接入时不发生状态与发布污染 |

## 推荐的第一条 Pilot

当前推荐把 `Project 1` 先定义为你现有的 `openclaw task system`。

这样做的原因：

- 它已经是一个真实项目，不需要虚构目标
- 你已经明确提出 `feishu6` 作为反馈 / 通知 / 审批入口
- 你已经明确所有默认挂载 `task system` 的使用 channel 都是运行面
- 你已经要求项目级控制面和项目路径保持一致，适合直接落在项目内 `.growware/`
- 它足够具体，适合拿来压实第一版合同

如果你后面指定别的项目，Growware 的总体路线不变，只替换 `Project 1` 的 target 即可。

## 当前推荐默认值

在真正开始 Stage 1 之前，当前文档已经先收敛到这些默认值：

- `Project 1 = openclaw-task-system`
- `A channel = feishu6`
- `A channel` 同时承载反馈、审批和通知
- `Telegram` 保留为备选通道
- 所有默认挂载 `task system` 的使用 channel 都视为 `B` 面
- 项目级 durable 配置和规则写入目标项目根目录下的 `.growware/`

## 这份路线图不做什么

- 今天就选定 runtime 或框架
- 承诺自治式生产部署
- 取代 development plan 里的详细执行队列

## 当前焦点

当前焦点已经从“规划 Stage 1”切换到“接受真实人类反馈并继续迭代”。

接下来默认入口已经变成：

- 你直接在 `feishu6-chat` 提想法或反馈
- Growware 通过 `growware` agent 进入 `openclaw-task-system` 工作区
- 本地先验证，再走 deploy baseline 和回发通知
