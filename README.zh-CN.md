# Growware

[English](README.md) | [中文](README.zh-CN.md)

> Growware 是一个根据需求、使用与反馈，持续驱动软件演化的反馈驱动引擎。它要做的不是“让 AI 帮忙写代码”，而是把意图、判题和实现接成一个会持续生长的软件工厂。

## 它是什么

根据完整起源对话，Growware 的目标不是一个普通的 AI 编程助手，也不是一个只会自动修 bug 的闭环脚本。

它更准确的定义是：

- 一个自动反馈式的软件工厂
- 一个把 `A 窗口`、`B 窗口` 和隐藏控制面接起来的生长引擎
- 一个持续维护 `spec / judge / code` 一致性的项目级控制层

这里的核心不是“代码自己改”，而是：

- `A 窗口` 定义意图、边界和裁判标准
- `B 窗口` 提供真实使用中的证据
- 隐藏控制面把反馈沉淀成规则、测试、修复和部署决策

## 它不是什么

- 不是另一个聊天式“让 LLM 写代码”的前端
- 不是只盯日志然后猜哪里坏了的自动修复器
- 不是要重写 OpenClaw 的 gateway、channel、plugin 或 task 生态
- 不是要重写 Codex 这个 coding agent 本身

Growware 应该补的是中间缺失的那层：把需求、使用与反馈转成可以持续演化软件的项目级控制面。

## 核心模型

- `A 窗口`：产品控制面。负责提需求、给反馈、做裁判、做审批。
- `B 窗口`：运行面。真实的软件在这里被使用，并持续产出日志、行为、失败和满意度痕迹。
- 隐藏控制面：演化引擎。负责把 A/B 两侧的信号转成 `spec`、`judge`、`test`、`code change`、`deploy gate` 和可复用记忆。

这套系统真正要自动化的不是一条“写代码”动作，而是三条回路：

1. 造软件：从意图到规格、实现、验证、部署。
2. 修软件：从运行证据到 incident、修复、验证、回发。
3. 学软件：把一次反馈沉淀成以后可重复执行的 `judge`、规则和回归资产。

## 当前仓库状态

这个仓库现在已经切到 experimental runtime foundation mode。

当前仓库已经能保存起源材料、定义 policy source、把第一条 pilot loop 的进入条件写清楚，并跑一条隔离的本地 mock runtime；但它仍然不能被解读成 `Project 1` 的 runtime 接线已经真实落地。

当前已经完成的是：

- 用 [docs/reference/growware/origin.pdf](docs/reference/growware/origin.pdf) 保存完整起源对话
- 用 [docs/reference/growware/origin-raw-extract.zh-CN.md](docs/reference/growware/origin-raw-extract.zh-CN.md) 保存 PDF 的全文 Markdown 提取
- 从完整原始对话抽象出 [docs/reference/growware/origin.zh-CN.md](docs/reference/growware/origin.zh-CN.md)
- 用公开文档把项目重新定义为 `Growware`
- 在不提前锁死技术栈的前提下，给出可行性、架构和路线图基线
- 把 `openclaw-task-system` 记录成文档里的 `Project 1` pilot target
- 把人类可读 policy source 放进 [docs/policy/](docs/policy/README.zh-CN.md)，并补上本地 `.policy/` 编译 / 校验入口
- 在 [docs/reference/growware/pilot-loop-v1.zh-CN.md](docs/reference/growware/pilot-loop-v1.zh-CN.md) 里把第一条 pilot loop 的进入门写实
- 把当前 review 主线固定在 Growware 自身的 self-improvement stack，而不是目标项目扩展
- 在 [docs/reference/growware/daemon-foundation-plan.zh-CN.md](docs/reference/growware/daemon-foundation-plan.zh-CN.md) 里定义 daemon-first 规划
- 把 daemon foundation contract pack 落进 [docs/reference/growware/daemon-contracts/README.zh-CN.md](docs/reference/growware/daemon-contracts/README.zh-CN.md)，并补上本地 `.growware/daemon-foundation/` 编译 / 校验入口
- 把 Stage 2 / Stage 3 的 paper baseline 落进 [docs/reference/growware/stage-2-3-baseline.zh-CN.md](docs/reference/growware/stage-2-3-baseline.zh-CN.md)
- 把 Stage 2 / Stage 3 contract pack 落进 [docs/reference/growware/stage-2-3-contracts/README.zh-CN.md](docs/reference/growware/stage-2-3-contracts/README.zh-CN.md)，并补上本地 `.growware/stage-2-3/` 编译 / 校验入口
- 新增一个隔离的实验应用 [experiments/mock_runtime/README.md](experiments/mock_runtime/README.md)，用于消费现有机器层并跑 mock 闭环
- 实验 runtime 现在还带了一条 project-bound readonly executor bridge，说明在 [docs/reference/growware/project-bound-executor-bridge-v0.zh-CN.md](docs/reference/growware/project-bound-executor-bridge-v0.zh-CN.md)
- 用中等规模的 `.codex/*` 控制面把当前阶段对齐到 experimental runtime 状态

当前仍然没有被夸大承诺的是：

- 由这个仓库直接拥有并验证过的 `openclaw-task-system/.growware/` 控制面
- 已验证的 `feishu6-chat -> growware` 运行时绑定
- 一条已经可跑的本地 observe -> report -> repair -> verify -> deploy 闭环
- 一个已经对真实 `openclaw-task-system` 工作区完成接线验证的本地执行器
- 生产级自治发布
- 多项目并行隔离
- 更强的 detector / rubric / regression 自动沉淀
- 没有会话上下文时的跨通道主动通知策略
- 直接接到运行时执行链路里的 `.growware/daemon-foundation/` 机器层
- 直接接到运行时执行链路里的 `.growware/stage-2-3/` 机器层
- 直接接到运行时执行链路里的 `.policy/` 机器层
- 从实验层直接触发的生产部署

## 快速开始

1. 先看完整真相源：[docs/reference/growware/origin.pdf](docs/reference/growware/origin.pdf)
2. 再看项目起源抽象：[docs/reference/growware/origin.zh-CN.md](docs/reference/growware/origin.zh-CN.md)
3. 再看项目可行性：[docs/reference/growware/feasibility.zh-CN.md](docs/reference/growware/feasibility.zh-CN.md)
4. 再看当前架构：[docs/architecture.zh-CN.md](docs/architecture.zh-CN.md)
5. 再看第一条 pilot loop 定义：[docs/reference/growware/pilot-loop-v1.zh-CN.md](docs/reference/growware/pilot-loop-v1.zh-CN.md)
6. 再看当前 daemon-first 规划：[docs/reference/growware/daemon-foundation-plan.zh-CN.md](docs/reference/growware/daemon-foundation-plan.zh-CN.md)
7. 再看 Stage 2 / Stage 3 的 paper baseline：[docs/reference/growware/stage-2-3-baseline.zh-CN.md](docs/reference/growware/stage-2-3-baseline.zh-CN.md)
8. 最后看阶段顺序：[docs/roadmap.zh-CN.md](docs/roadmap.zh-CN.md)
9. 查看 daemon contract pack：[docs/reference/growware/daemon-contracts/README.zh-CN.md](docs/reference/growware/daemon-contracts/README.zh-CN.md)
10. 查看 Stage 2 / Stage 3 contract pack：[docs/reference/growware/stage-2-3-contracts/README.zh-CN.md](docs/reference/growware/stage-2-3-contracts/README.zh-CN.md)
11. 查看 policy source：[docs/policy/README.zh-CN.md](docs/policy/README.zh-CN.md) 和 [docs/reference/growware/shared-policy-contract.zh-CN.md](docs/reference/growware/shared-policy-contract.zh-CN.md)
12. 查看实验 runtime 说明：[docs/reference/growware/experimental-runtime-v0.zh-CN.md](docs/reference/growware/experimental-runtime-v0.zh-CN.md)
13. 生成并校验机器层，再跑 mock runtime：

```bash
python3 scripts/growware_daemon_contract_sync.py --write --json
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_stage23_contract_sync.py --write --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --write --json
python3 scripts/growware_policy_sync.py --check --json
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## 文档导航

- [文档首页](docs/README.zh-CN.md)
- [项目起源抽象](docs/reference/growware/origin.zh-CN.md)
- [可行性评估](docs/reference/growware/feasibility.zh-CN.md)
- [架构](docs/architecture.zh-CN.md)
- [Pilot Loop V1](docs/reference/growware/pilot-loop-v1.zh-CN.md)
- [Daemon Foundation Plan](docs/reference/growware/daemon-foundation-plan.zh-CN.md)
- [Daemon Contract Pack](docs/reference/growware/daemon-contracts/README.zh-CN.md)
- [Stage 2 And Stage 3 Baseline](docs/reference/growware/stage-2-3-baseline.zh-CN.md)
- [Stage 2 And Stage 3 Contract Pack](docs/reference/growware/stage-2-3-contracts/README.zh-CN.md)
- [Experimental Runtime V0](docs/reference/growware/experimental-runtime-v0.zh-CN.md)
- [Project-Bound Executor Bridge V0](docs/reference/growware/project-bound-executor-bridge-v0.zh-CN.md)
- [路线图](docs/roadmap.zh-CN.md)
- [开发计划](docs/reference/growware/development-plan.zh-CN.md)
- [测试计划](docs/test-plan.zh-CN.md)
- [分享页转录稿](docs/reference/growware/origin-transcript-2026-04-13.zh-CN.md)
- [Policy Source](docs/policy/README.zh-CN.md)
- [Mock Runtime App](experiments/mock_runtime/README.md)
