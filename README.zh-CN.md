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

这个仓库现在仍然处于“讨论与文档基线”阶段，还没有进入运行时代码阶段。

当前已经完成的是：

- 用 [docs/reference/growware/origin.pdf](docs/reference/growware/origin.pdf) 保存完整起源对话
- 用 [docs/reference/growware/origin-raw-extract.zh-CN.md](docs/reference/growware/origin-raw-extract.zh-CN.md) 保存 PDF 的全文 Markdown 提取
- 从完整原始对话抽象出 [docs/reference/growware/origin.zh-CN.md](docs/reference/growware/origin.zh-CN.md)
- 用公开文档把项目重新定义为 `Growware`
- 在不提前锁死技术栈的前提下，给出可行性、架构和路线图基线

当前仍然故意没有锁死的是：

- 第一条真实 pilot 接哪个具体项目
- 哪些判断可以自动做，哪些必须人工裁定
- 第一版 daemon、judge、verifier 的最小合同
- 多项目接入和并行隔离的边界

## 快速开始

1. 先看完整真相源：[docs/reference/growware/origin.pdf](docs/reference/growware/origin.pdf)
2. 再看项目起源抽象：[docs/reference/growware/origin.zh-CN.md](docs/reference/growware/origin.zh-CN.md)
3. 再看项目可行性：[docs/reference/growware/feasibility.zh-CN.md](docs/reference/growware/feasibility.zh-CN.md)
4. 再看当前架构：[docs/architecture.zh-CN.md](docs/architecture.zh-CN.md)
5. 最后看阶段顺序：[docs/roadmap.zh-CN.md](docs/roadmap.zh-CN.md)

## 文档导航

- [文档首页](docs/README.zh-CN.md)
- [项目起源抽象](docs/reference/growware/origin.zh-CN.md)
- [可行性评估](docs/reference/growware/feasibility.zh-CN.md)
- [架构](docs/architecture.zh-CN.md)
- [路线图](docs/roadmap.zh-CN.md)
- [开发计划](docs/reference/growware/development-plan.zh-CN.md)
- [测试计划](docs/test-plan.zh-CN.md)
- [分享页转录稿](docs/reference/growware/origin-transcript-2026-04-13.zh-CN.md)
