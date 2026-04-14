# 路线图

[English](roadmap.md) | [中文](roadmap.zh-CN.md)

## 范围

这份路线图描述的是：如何把 Growware 这个概念，推进成一条真实的本地优先 pilot。它故意停在实现细节之前。

这些阶段下面更细的维护者执行队列，请看 [reference/growware/development-plan.zh-CN.md](reference/growware/development-plan.zh-CN.md)。

## 阶段

| 阶段 | 状态 | 目标 | 解锁什么 | 退出条件 |
| --- | --- | --- | --- | --- |
| [Stage 0 - 起源归档与可行性基线](reference/growware/development-plan.zh-CN.md#stage-0-origin-capture-and-feasibility) | 已完成 | 保存起点对话、统一命名并发布基线文档集 | 共享上下文与真实文档基线 | transcript 已归档、文档已互链、活跃命名已收敛到 Growware |
| [Stage 1 - 项目 1 Pilot 基础长任务](reference/growware/development-plan.zh-CN.md#stage-1-project-1-pilot-foundation-long-task) | 纸面已完成 | 在纸面上明确 Project 1、`A/B` 路径、`.growware/` 边界、核心合同与 Stage 2 启动门 | Growware 自身 daemon-first 规划 | `pilot-loop-v1`、架构、开发计划和 policy source 对齐成同一套 pilot 合同包 |
| [Stage 1.5 - Growware 自身 / Daemon Foundation](reference/growware/development-plan.zh-CN.md#stage-15-growware-self--daemon-foundation) | 进行中 / 合同包实现态 | 在继续扩展目标项目执行前，先明确 Growware 自身的 daemon 边界、project capsule、channel-progress 合同与执行 handoff | Stage 2 本地闭环 | `daemon-foundation-plan`、`daemon-contracts/*`、生成出的 `.growware/daemon-foundation/*`、roadmap、development plan 与 `.codex/*` 对齐成一条 Growware-self 主线 |
| [Stage 2 - 单项目本地半自动闭环](reference/growware/development-plan.zh-CN.md#stage-2-single-project-local-semi-automatic-loop) | 排队中 | 在批准过的 Growware daemon 边界之下，于项目 1 上实现一条本地 observe -> report -> repair -> verify -> deploy baseline 链路 | 第一个可运行 Growware 基线 | 一条本地闭环在人工审批门之后能够端到端跑通 |
| [Stage 3 - 检测器、门禁和低风险自动化](reference/growware/development-plan.zh-CN.md#stage-3-detectors-gates-and-low-risk-automation) | 更后 | 补齐第一版 judge、deploy gate 和低风险自动化层 | 更稳定的闭环 | 重复 incident 开始沉淀成可复用的 judge、规则和回归资产 |
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
- 人类可读 policy source 落在 `docs/policy/`，并受 `docs/reference/growware/shared-policy-contract.zh-CN.md` 管辖

## 这份路线图不做什么

- 今天就选定 runtime 或框架
- 承诺自治式生产部署
- 取代 development plan 里的详细执行队列
- 绕过 `docs/policy/` 这一层 policy source

## 当前焦点

当前焦点不再是直接去扩展 `Project 1`。

当前焦点是先定义并编译 Growware 自身的 daemon-first 主线，让 channel 对话能够推动项目进展，而不是把每个目标项目都误当成当前 roadmap 主线。
