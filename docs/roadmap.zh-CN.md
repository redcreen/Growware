# 路线图

[English](roadmap.md) | [中文](roadmap.zh-CN.md)

## 范围

这份路线图描述的是：如何把 Growware 这个概念，推进成一条真实的本地优先 pilot。它故意停在实现细节之前。

这些阶段下面更细的维护者执行队列，请看 [reference/growware/development-plan.zh-CN.md](reference/growware/development-plan.zh-CN.md)。

## 总体进展

| 项目 | 当前值 |
| --- | --- |
| 主线进度 | Stage 0、Stage 1、Stage 1.5 和 readonly bridge checkpoint 已经足够收口，仓库已从纯纸面规划进入受限的真实项目桥接审查阶段 |
| 当前阶段 | experimental runtime v0 加 project-bound readonly executor bridge |
| 当前目标 | 保持 readonly bridge 真实可信，保持所有 machine layer 与文档源同步，且不夸大成 Project 1 已完成 runtime 接线 |
| 明确下一步动作 | 在绑定任何 write-capable executor 前，先审查 readonly bridge 边界到底还是太窄还是太宽 |
| 下一候选动作 | 只有在显式 follow-up approval 后，才进入第一条 write-capable 的 `single-project local semi-automatic loop` |

查看详细执行计划：[reference/growware/development-plan.zh-CN.md](reference/growware/development-plan.zh-CN.md)

## 阶段

| 阶段 | 状态 | 目标 | 解锁什么 | 退出条件 |
| --- | --- | --- | --- | --- |
| [Stage 0 - 起源归档与可行性基线](reference/growware/development-plan.zh-CN.md#stage-0-origin-capture-and-feasibility) | 已完成 | 保存起点对话、统一命名并发布基线文档集 | 共享上下文与真实文档基线 | transcript 已归档、文档已互链、活跃命名已收敛到 Growware |
| [Stage 1 - 项目 1 Pilot 基础长任务](reference/growware/development-plan.zh-CN.md#stage-1-project-1-pilot-foundation-long-task) | 纸面已完成 | 在纸面上明确 Project 1、`A/B` 路径、`.growware/` 边界、核心合同与 Stage 2 启动门 | Growware 自身 daemon-first 规划 | `pilot-loop-v1`、架构、开发计划和 policy source 对齐成同一套 pilot 合同包 |
| [Stage 1.5 - Growware 自身 / Daemon Foundation](reference/growware/development-plan.zh-CN.md#stage-15-growware-self--daemon-foundation) | 纸面已完成 / 基础已具备 | 在继续扩展目标项目执行前，先明确 Growware 自身的 daemon 边界、project capsule、channel-progress 合同与执行 handoff | Stage 2 / Stage 3 纸面基线 | `daemon-foundation-plan`、`daemon-contracts/*`、生成出的 `.growware/daemon-foundation/*`、roadmap、development plan 与 `.codex/*` 对齐成一条 Growware-self 主线 |
| [Stage 2 - 单项目本地半自动闭环](reference/growware/development-plan.zh-CN.md#stage-2-single-project-local-semi-automatic-loop) | experimental v0 进行中 / deploy 仍受门禁 | 在批准过的 Growware daemon 边界之下，于项目 1 上实现一条本地 observe -> report -> repair -> verify -> deploy baseline 链路 | 第一个可运行 Growware 基线 | `experiments/mock_runtime/` 已能消费现有机器层并跑一条本地 mock 闭环，同时 deploy 仍然保持 approval-gated 且非生产 |
| [Stage 3 - 检测器、门禁和低风险自动化](reference/growware/development-plan.zh-CN.md#stage-3-detectors-gates-and-low-risk-automation) | 纸面基线已完成 / experiment hookup 排队中 | 补齐第一版 judge、deploy gate 和低风险自动化层 | 更稳定的闭环 | Stage 3 的 judge、automation band 和 regression asset 规则已经显式且可编译，但尚未被生产 runtime 启用 |
| [Stage 4 - 多项目接入与隔离](reference/growware/development-plan.zh-CN.md#stage-4-multi-project-onboarding-and-isolation) | 更后 | 支持多个项目并保持 channel、日志、队列、部署的隔离 | Growware 变成可复用控制层 | 多项目并行接入时不发生状态与发布污染 |

## 当前 / 下一步 / 更后面

| 时间层级 | 重点 | 退出信号 |
| --- | --- | --- |
| 当前 | 保持 readonly bridge 真实可信、保持 machine layer 与文档源同步，并避免夸大成 Project 1 runtime 已完成 | bridge review 持续为绿、sync 输出持续对齐、入口文档仍然明确这是 readonly 边界 |
| 下一步 | 判断是否要为第一条 `single-project local semi-automatic loop` 绑定 write-capable executor | 已获得显式批准的 write-capable executor 边界，并定义出一条可重复的本地 loop 路径 |
| 更后面 | 再逐步打开 detector / automation 工作和多项目隔离 | 后续扩展不会跳过 approval gate，也不会破坏跨项目隔离规则 |

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

- 过早把实验层锁死成生产 runtime 或框架
- 承诺自治式生产部署
- 取代 development plan 里的详细执行队列
- 绕过 `docs/policy/` 这一层 policy source

## 当前焦点

当前焦点是先落一条隔离的 mock runtime，让它消费现有机器层，但不假装 `Project 1` 已经完成端到端接线。

当前焦点是把 Stage 2 / Stage 3 的合同保持成显式、可编译、可 review 的状态，同时让 `experiments/mock_runtime/` 在本地证明 daemon-side control flow。
