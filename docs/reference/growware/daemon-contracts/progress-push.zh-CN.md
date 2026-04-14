# Progress Push Contract

[English](progress-push.md) | [中文](progress-push.zh-CN.md)

## Metadata

- id: `growware.progress-push.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `progress-push`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义 Growware 通过 channel 回推的结构化 payload，包括进展、审批、验证结果与 close-out。

## Message Types

- `progress-snapshot`：当前状态和下一步动作
- `approval-request`：带范围和理由的明确审批等待
- `verification-result`：带证据引用的验证结果
- `close-out`：最终结果、provenance 与 writeback 后续项

## Common Fields

- `message_type`：上述声明的消息类型之一
- `project_id`：接入项目标识
- `phase`：当前阶段
- `execution_line`：当前活跃执行线
- `summary`：channel 可见的简要说明
- `next_action`：下一步预期动作或等待状态
- `blockers`：当前 blockers，或空列表
- `approval_state`：相关动作的当前审批状态
- `provenance`：结果来自 daemon-owned 状态还是 terminal takeover

## Close-Out Fields

- `result`：最终结果摘要
- `validation_refs`：已执行检查的证据引用
- `execution_source`：daemon-owned 或 terminal-takeover 来源
- `writeback_refs`：这轮工作产出的 rule、judge、regression proposal
- `follow_up_needed`：明确的后续动作，或空值

## Delivery Rules

- 每次 push 都必须带上 `project_id` 与 `message_type`
- approval wait 必须写明它阻塞的是哪类 action scope
- close-out 必须保留 provenance，不能默认暗示已经完全 daemon-owned
- verification result 没有 evidence refs 时，不能宣称成功

## Machine Notes

- 把 `message_types`、`common_fields`、`close_out_fields` 分别编译为独立数组
- 机器层必须原样保留 `message_type` 的拼写
