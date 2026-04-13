# 架构

[English](architecture.md) | [中文](architecture.zh-CN.md)

## 目的

这份文档先回答一个比“怎么接 OpenClaw”更根的问题：Growware 到底是什么系统。

它基于完整起源对话，而不是只基于不完整的分享页转录。  
在这个前提下，再说明当前最推荐的 pilot 架构。

## 项目是什么

Growware 不是“让 AI 写代码”的聊天工具，也不是只会看日志和打补丁的自动修复脚本。

它更准确的系统定义是：

- `A 窗口` 是产品控制面
- `B 窗口` 是运行面和证据源
- 隐藏控制面是演化引擎

这个演化引擎持续维护三类共同演化的资产：

1. `spec`：软件应该做什么
2. `judge`：什么叫对，什么叫错
3. `code`：当前实现

所以 Growware 真正要自动化的，不只是“写代码”，而是这三条回路：

1. 造软件：从意图到规格、实现、验证、部署
2. 修软件：从运行证据到 incident、修复、验证、回发
3. 学软件：把一次反馈沉淀成规则、rubric、回归测试和约束

## 它不是什么

- 不是 OpenClaw 的替代品
- 不是 Codex 的替代品
- 不是 “A 说一句话 -> LLM 改代码 -> 直接部署” 的短链条
- 不是只围绕 bugfix 的守护进程

Growware 应该补的是 OpenClaw 和 Codex 之间缺失的那层项目级控制面。

## 当前推荐的系统分层

| 层 | 负责什么 | 不负责什么 |
| --- | --- | --- |
| OpenClaw | channel、gateway、plugin、hook、service、task 等宿主与生态基础设施 | 项目级 `judge`、修复记忆、软件演化规则 |
| Growware | 项目绑定、feedback intake、observer、judge、incident queue、verifier、deploy gate、状态机 | 重写 OpenClaw 宿主层，重写 Codex 本体 |
| Codex | 分析 incident、改代码、跑验证、产出修复结果 | 常驻承载 channel、维护长期项目状态、决定产品策略 |
| 目标项目 / 插件 | 真实运行、真实日志、run/test/deploy/rollback 钩子 | 跨项目调度与控制策略 |

## 当前推荐的 Pilot 形态

在第一条 pilot 里，建议保持现实收缩：

- `Project 1` 先锁定为 `openclaw-task-system`
- `A` 先收缩成 `human feedback ingress`
- `B` 表示真实使用通道和运行证据源
- `feishu6` 作为唯一默认的人类反馈、审批和通知入口
- `Telegram` 只作为备选或后续补充通知通道，不作为第一阶段主入口
- 所有默认挂载 `task system` 的使用 channel，都视为 `B` 面
- 不做动态 `A/B routing engine`
- 改用显式的 `project-channel binding`
- 每个项目先配一个轻量 `project daemon / sidecar`
- 项目级规则、合同和记忆落在目标项目根目录下的 `.growware/`
- `Codex` 作为按需拉起的执行器，而不是每项目常驻会话

## Pilot 拓扑

```mermaid
flowchart TD
    subgraph OpenClaw
        A[反馈 / 审批 / 通知 channel\nfeishu6]
        B[所有挂载 task system 的使用 channel]
        Adapter[Feedback adapter]
        GatewayLogs[Gateway logs]
        TG[Telegram fallback\n可选]
    end

    subgraph Growware
        Binding[静态 project-channel 绑定]
        Daemon[Project daemon / sidecar]
        Observer[Observer]
        Judge[Judge]
        Queue[Incident / repair queue]
        Verifier[Verifier]
        Gate[Deploy gate]
        Memory[Rules / Rubrics / Regression]
    end

    subgraph Target
        Plugin[目标插件或软件]
        PluginLogs[插件日志]
        Workspace[本地工作区 / repo]
    end

    Codex[Codex worker\n按需拉起]

    A --> Adapter
    Adapter --> Binding
    Binding --> Daemon
    TG -. optional .-> Adapter

    B --> Plugin
    Plugin --> PluginLogs
    GatewayLogs --> Observer
    PluginLogs --> Observer
    Daemon --> Observer

    Observer --> Judge
    Judge --> Queue
    Queue --> Codex
    Codex --> Workspace
    Workspace --> Verifier
    Verifier --> Gate
    Gate --> Daemon
    Daemon --> Adapter
    Adapter --> A

    A --> Memory
    Judge --> Memory
    Verifier --> Memory
    Workspace --> LocalRules[.growware/]
    LocalRules --> Daemon
```

## 当前推荐的 Pilot 绑定

这轮讨论后，第一条业务验证闭环建议先按下面的默认值收敛：

- `Project 1 = openclaw-task-system`
- `A channel = feishu6`
- `A channel` 同时承担：
  - 人类反馈入口
  - 审批入口
  - 决策和状态通知入口
- `B surfaces = 所有默认挂载 task system 的使用 channel`
- `Telegram` 暂时只保留为备选通道，不抢主流程

这组默认值的好处是：

- 先把人类裁判面收敛成单点
- 不把真实使用面和反馈面混在一起
- 让 `task system` 的所有真实使用都自动进入同一批运行证据范围
- 把项目级控制面和项目代码目录对齐，便于 Git 管理

## 三条主流

### 1. 反馈流

这条线对应你已经定义清楚的那种接法：

`feishu6 -> OpenClaw adapter -> project daemon`

如果 daemon 能把结果再回发回去，这条双向 feedback channel 就成立了。

```mermaid
sequenceDiagram
    participant Human as 人
    participant A as 反馈 channel
    participant Adapter as Feedback adapter
    participant Daemon as Project daemon

    Human->>A: 提需求 / 报问题 / 给裁定
    A->>Adapter: 投递消息
    Adapter->>Daemon: 归一化为 feedback event
    Daemon-->>Adapter: ack / 结果 / 后续动作
    Adapter-->>A: 回发同一 channel
```

### 2. 运行证据流

第一阶段不需要动态 `B` 路由器，但必须定义清楚证据源：

- OpenClaw gateway logs
- 目标插件日志
- daemon 自己的日志
- 目标项目主动上报的结构化事件

`Observer` 负责收集。  
`Judge` 负责回答“这是不是问题、属于哪一类问题、能不能自动修”。  
采集不能代替判定。

### 3. 演化流

完整起源对话里最重要的点不是“修一次”，而是“学一次”：

`A 窗口反馈 -> 更新 spec / rubric / detector / eval -> 改代码 -> 验证 -> 部署`

这条流决定了 Growware 是“软件工厂 / 生长引擎”，而不是一次次聊天修 bug。

## 为什么 `judge` 不能省

如果没有 `judge layer`，系统就会退化成：

`看日志 -> 猜是不是问题 -> 拉 Codex 试试`

这不是闭环，更不是演化。

`judge` 最少要回答：

- 这是正常噪声还是 incident
- 是规范缺失型问题还是运行可观测型问题
- 严重级别是什么
- 能不能自动修
- 是否必须人工审批

## 为什么第一阶段用静态绑定

当前 pilot 可以先不用动态 `A/B routing`，改成静态绑定配置：

```yaml
project_id: project-1
project_name: openclaw-task-system
feedback_channels:
  - feishu6
runtime_channels:
  - "*"
watched_plugins:
  - openclaw-task-system
log_sources:
  - openclaw-gateway
  - project-daemon
approval_channels:
  - feishu6
notification_channels:
  - feishu6
fallback_channels:
  - telegram
```

这样已经足够覆盖：

- 明确项目的人类反馈入口
- 明确项目的运行面和证据面
- 明确要观察哪些插件和日志源
- 明确所有决策通知默认回到 `feishu6`

只有以后多个项目共享 channel、日志源或部署边界时，才需要更强的 routing。

## `.growware/` 目录边界

第一阶段我同意把项目级 Growware 控制面放到目标项目目录里，而不是只放在 Growware 主仓库里。

对 `Project 1` 来说，推荐形态是：

```text
openclaw-task-system/
  .growware/
    project.yaml
    channels.yaml
    contracts/
    spec/
    judge/
    ops/
    memory/
```

这里建议区分两类内容：

应该进 Git：

- `project.yaml`
- channel 绑定配置
- `spec/`
- `judge/`
- 合同定义
- deploy / approval policy
- 人工沉淀下来的 durable 规则

不应该直接进 Git：

- 临时运行状态
- 本地队列
- 原始日志缓存
- 一次性的调试产物

如果要放在项目目录下，建议形态是：

```text
.growware/
  runtime/   # gitignore
  logs/      # gitignore
```

这样就能同时满足：

- 项目配置跟着项目仓库走
- Growware 的核心规则可以被代码审查和版本管理
- 运行态垃圾不会污染项目 Git 历史

## 最小事件合同

### Feedback Event

```json
{
  "project_id": "project-1",
  "channel_id": "feishu1",
  "message_id": "msg-123",
  "event_type": "human_feedback",
  "text": "the plugin output is wrong for task creation",
  "related_session_id": "sess-456",
  "related_plugin": "openclaw-task-system",
  "timestamp": "2026-04-13T18:00:00+08:00",
  "requires_reply": true
}
```

### Incident Record

```json
{
  "project_id": "project-1",
  "incident_id": "inc-001",
  "source": "gateway-log",
  "summary": "task creation fails after confirmation",
  "severity": "medium",
  "evidence": ["log excerpt", "session id", "feedback event"],
  "problem_type": "runtime-observable",
  "reproducible": false,
  "approval_required": true
}
```

## 部署形态建议

### 方案 1：嵌在 OpenClaw plugin / service 里

适合：

- pilot 明确只服务 OpenClaw 生态
- 想复用 OpenClaw 已有的 hooks、tasks、taskflow 和运行容器

### 方案 2：外挂 sidecar

适合：

- 未来可能不只接 OpenClaw
- 想把 Growware 保持成独立项目级控制层

无论选哪种，边界都应该保持一致：

- OpenClaw 负责宿主和接入
- Growware 负责项目控制面
- Codex 负责受控执行

当前对 `Project 1` 的建议更偏向：

- 运行上允许 sidecar 或 OpenClaw service 二选一
- 但项目级 durable 配置无论如何都放在 `openclaw-task-system/.growware/`

## 当前文档约束

只要 pilot 还没开始，文档可以先保守写“半自动、本地优先、人工门禁”。  
但项目定义不能再被写窄成“闭环修复脚本”或“文档先行的 AI coding 实验”。
