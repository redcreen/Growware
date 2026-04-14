# Execution Handoff Contract

[English](execution-handoff.md) | [中文](execution-handoff.zh-CN.md)

## Metadata

- id: `growware.execution-handoff.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `execution-handoff`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`
  - `docs/reference/growware/shared-policy-contract.zh-CN.md`

## Purpose

这份合同定义 Growware 何时从 daemon-owned 状态回答，何时委派执行，以及何时必须等待审批。

## Handoff Modes

- `state-only`：只从 durable 项目状态回答，不进行代码执行
- `coordination-only`：只更新项目进展或规划状态，不进入 `executor-required` 工作
- `executor-required`：把工作移交给声明好的项目执行器或 adapter
- `approval-wait`：因为该动作需要批准，所以暂停在等待态

## Required Handoff Record

- `project_id`：已解析的接入项目
- `requested_action`：当前请求的动作
- `handoff_mode`：上述声明的 handoff mode 之一
- `reason`：为何选择这个模式的简要说明
- `policy_refs`：做决定前查阅的 policy id 或 manifest
- `required_validation`：close-out 之前预期需要跑的验证路径
- `approval_state`：该动作当前的审批状态

## Decision Rules

- 如果答案已经存在于 durable 项目状态中，优先使用 `state-only`
- 如果工作只是更新规划或进展，不需要代码执行，就用 `coordination-only`
- 只有在 project capsule 与 policy layer 都授权时，才能进入 `executor-required`
- 只要已加载的 policy 或 capsule 边界表明该动作被 gate，立刻切到 `approval-wait`

## Approval Rules

- Growware 不能在 capsule 声明的 `executor_ref` 之外临时发明执行路径
- 任何会改变 action scope 的 handoff record 都需要 review
- 最终 close-out 必须把选中的 `handoff_mode` 保留下来作为 provenance

## Machine Notes

- 把 `handoff_modes`、`required_handoff_record`、`decision_rules`、`approval_rules` 分别编译为独立数组
- 为未来 daemon adapter 保持 `handoff_mode` 的稳定拼写
