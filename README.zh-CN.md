# Growware

[English](README.md) | [中文](README.zh-CN.md)

> Growware 是一个文档先行的闭环软件演化项目：把真实使用、incident 与反馈转成可审阅的修复与验证。

## 它是什么

Growware 现在还不是一个已经完成的工具或框架。这个仓库当前做的事情，是先把一个本地优先的软件闭环边界定义清楚：软件被使用、被观测、被判定、被修复、被验证，然后才进入部署。

这个项目的起点，来自一段关于 Codex 与 OpenClaw 风格通道的对话。核心目标不是“AI 帮忙写点代码”，而是把“人发现问题再转述给 AI”逐步推进成“系统先发现、先提案、先验证，人只在风险边界介入”。

## 适用对象

- 正在构建自我改进插件、工具或软件闭环的维护者
- 希望从聊天式调试走向 incident 驱动修复的操作者
- 在实现开始前先审查项目可行性的协作者

## 当前项目状态

这个仓库现在处于“讨论与文档基线”阶段，不是“实现基线”阶段。

当前已经落下来的内容：

- 起源对话的 Markdown 原文归档
- 从项目角度给出的可行性评估
- 稳定的架构和路线图基线
- 一个停在实现之前的维护者开发计划

当前仍然故意不做决定的内容：

- 第一条真实 pilot loop 具体是什么
- 目标软件边界是什么
- 运行时和技术栈是什么
- incident 与验证的机器可判定合同是什么

## 快速开始

1. 先看起点对话：[docs/reference/growware/origin-transcript-2026-04-13.zh-CN.md](docs/reference/growware/origin-transcript-2026-04-13.zh-CN.md)
2. 再看项目判断：[docs/reference/growware/feasibility.zh-CN.md](docs/reference/growware/feasibility.zh-CN.md)
3. 再看稳定系统边界：[docs/architecture.zh-CN.md](docs/architecture.zh-CN.md)
4. 再看阶段顺序：[docs/roadmap.zh-CN.md](docs/roadmap.zh-CN.md)
5. 需要恢复维护者执行线时，看 [docs/reference/growware/development-plan.zh-CN.md](docs/reference/growware/development-plan.zh-CN.md)

## 核心概念

- `A 窗口`：需求、反馈、审批和人工裁判进入的位置
- `B 窗口`：真实使用产生证据、日志、incident 和行为轨迹的位置
- 隐藏控制面：把信号变成 incident、修复任务、验证步骤、部署决策和可复用记忆的地方

## 文档导航

- [文档首页](docs/README.zh-CN.md)
- [可行性评估](docs/reference/growware/feasibility.zh-CN.md)
- [架构](docs/architecture.zh-CN.md)
- [路线图](docs/roadmap.zh-CN.md)
- [开发计划](docs/reference/growware/development-plan.zh-CN.md)
- [测试计划](docs/test-plan.zh-CN.md)
- [起源对话原文](docs/reference/growware/origin-transcript-2026-04-13.zh-CN.md)
