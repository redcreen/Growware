# Channel Command And Event Model

[English](channel-command-model.md) | [中文](channel-command-model.zh-CN.md)

## Metadata

- id: `growware.channel.command-model.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `channel-command-model`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义 Growware 通过 channel 对话接收与发出的最小 durable 命令 / 事件模型。

## Required Envelope

- `command`：稳定命令名
- `channel_ref`：host 本地形态的 channel 标识
- `message_ref`：可用时的源消息标识
- `actor_ref`：发送者标识
- `observed_at`：事件时间戳
- `project_ref`：显式项目引用；如果为空，则表示需要路由层推断
- `payload`：命令特定 payload

## Commands

- `status`：请求当前项目进展快照
- `continue`：请求按照当前执行线推进下一步
- `approve`：批准一个待处理 gated action
- `block`：报告 blocker 或明确拒绝继续
- `incident`：报告一个应当进入项目闭环的运行时或产品问题
- `close`：确认 close-out，表示 channel 可见这轮工作已收到

## Emitted Events

- `progress-pushed`：Growware 推送了进展快照或下一步更新
- `approval-requested`：Growware 正在等待明确批准
- `incident-recorded`：一条 channel 侧 incident 已经写入 durable 项目状态
- `execution-delegated`：请求已经转入 `executor-required` 工作
- `close-out-pushed`：Growware 推送了最终结果与 provenance

## Routing Rules

- 优先使用显式 `project_ref`；否则通过项目声明的 `channel_bindings` 做解析
- 如果路由有歧义，就停下来请求澄清，不能靠猜
- 任何会改变执行状态的命令，都必须回到一个已解析的 project capsule

## Approval Rules

- `approve` 只有在能匹配到一个待处理 approval wait 时才有效
- 一条 channel 消息不能悄悄扩大 executor 权限
- channel 自由文本不能覆盖机器加载的项目 policy

## Machine Notes

- 把 `commands` 与 `emitted_events` 编译为稳定顺序数组
- compiled JSON 中的 envelope 字段拼写必须保持稳定
