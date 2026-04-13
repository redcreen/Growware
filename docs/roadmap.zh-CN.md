# 路线图

[English](roadmap.md) | [中文](roadmap.zh-CN.md)

## 范围

这份路线图描述的是：如何把 Growware 这个概念，推进成一条真实的本地优先 pilot。它故意停在实现细节之前。

这些阶段下面更细的维护者执行队列，请看 [reference/growware/development-plan.zh-CN.md](reference/growware/development-plan.zh-CN.md)。

## 阶段

| 阶段 | 状态 | 目标 | 解锁什么 | 退出条件 |
| --- | --- | --- | --- | --- |
| [Stage 0 - 起源归档与可行性基线](reference/growware/development-plan.zh-CN.md#stage-0-origin-capture-and-feasibility) | 已完成 | 保存起点对话、统一命名并发布基线文档集 | 共享上下文与真实文档基线 | transcript 已归档、文档已互链、活跃命名已收敛到 Growware |
| [Stage 1 - 项目 1 Pilot 基础长任务](reference/growware/development-plan.zh-CN.md#stage-1-的长任务目标) | 已规划 / 待启动 | 用一个长任务把项目 1 的目标、OpenClaw 接线、daemon 边界、合同和启动条件一次定清楚 | Stage 2 的实现进入门 | target、channel 绑定、feedback/incident/judge/verifier/deploy 合同、daemon 接口全部明确 |
| [Stage 2 - 单项目本地半自动闭环](reference/growware/development-plan.zh-CN.md#stage-2-single-project-local-semi-automatic-loop) | 已排队 | 在项目 1 上实现一条带人工审批的本地 observe -> report -> repair -> verify -> deploy 链路 | 第一个可运行 Growware 基线 | 项目 1 能在本地按固定流程跑通一条真实闭环 |
| [Stage 3 - 检测器、门禁和低风险自动化](reference/growware/development-plan.zh-CN.md#stage-3-detectors-gates-and-low-risk-automation) | 已排队 | 扩展 judge、回归资产、门禁和低风险自动化 | 更稳定的闭环 | 部分低风险 incident 可以在显式门禁下自动修复 |
| [Stage 4 - 多项目接入与隔离](reference/growware/development-plan.zh-CN.md#stage-4-multi-project-onboarding-and-isolation) | 更后 | 支持多个项目并保持 channel、日志、队列、部署的隔离 | Growware 变成可复用控制层 | 多项目并行接入时不发生状态与发布污染 |

## 推荐的第一条 Pilot

当前推荐把 `Project 1` 先定义为你现有的 `openclaw task system`。

这样做的原因：

- 它已经是一个真实项目，不需要虚构目标
- 你已经在讨论它的 A/B channel、daemon 和反馈闭环
- 它足够具体，适合拿来压实第一版合同

如果你后面指定别的项目，Growware 的总体路线不变，只替换 `Project 1` 的 target 即可。

## 这份路线图不做什么

- 今天就选定 runtime 或框架
- 承诺自治式生产部署
- 取代 development plan 里的详细执行队列

## 当前焦点

当前焦点是：把 `Stage 1` 作为一个完整长任务规划好，但先不启动执行。

只有在你明确下达“开始”指令之后，仓库才进入这个长任务的实际推进。
