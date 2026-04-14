# Incident Lifecycle Contract

[English](incident-lifecycle.md) | [中文](incident-lifecycle.zh-CN.md)

## Metadata

- id: `growware.stage23.incident-lifecycle.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `incident-lifecycle`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/pilot-loop-v1.zh-CN.md`
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`

## Purpose

这份合同定义一条 Stage 2 incident 如何被创建、提升、推进、阻塞和关闭。

## Intake Sources

- `human-feedback`
- `gateway-log`
- `plugin-log`
- `daemon-log`
- `structured-runtime-event`

## Lifecycle States

- `intake`
- `triage`
- `repair`
- `verify`
- `approval-wait`
- `blocked`
- `closed`

## Required Fields

- `project_id`
- `incident_id`
- `source`
- `summary`
- `severity`
- `problem_type`
- `evidence_refs`
- `current_state`
- `approval_required`
- `opened_at`
- `updated_at`

## Promotion Rules

- 只要 human feedback 描述了用户可见问题、预期偏差或值得裁决的风险，就可以直接提升
- runtime 证据只能在 judge 路径明确它不是噪声之后，才允许提升
- 每一条被提升的 incident 都必须保留回到原始证据的引用

## Closure Rules

- 只有在 verification 得到明确结果、且 close-out provenance 已写入之后，incident 才能关闭
- `closed` 不等于 `daemon-owned`；执行来源必须另行写明
- 如果工作中止但没有修复，incident 必须以 blocked 或 deferred 结果关闭，不能直接消失

## Approval Rules

- 任何会进入 deploy 影响范围的状态迁移，都必须服从 deployment gate contract
- 项目绑定有歧义的 incident，在进入 repair 之前必须停下
- 会改变 deploy 或 rollback 权限的严重级别升级，必须经过明确 review

## Machine Notes

- 把 `intake_sources`、`lifecycle_states`、`required_fields`、`promotion_rules`、`closure_rules`、`approval_rules` 分别编译为独立数组

