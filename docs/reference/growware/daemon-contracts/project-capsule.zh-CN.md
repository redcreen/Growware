# Project Capsule Contract

[English](project-capsule.md) | [中文](project-capsule.zh-CN.md)

## Metadata

- id: `growware.project-capsule.minimum`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `project-capsule`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义 Growware 读取每个接入项目时所依赖的最小项目侧表面。

## Required Fields

- `project_id`：稳定的项目标识
- `project_label`：给 progress push 使用的人类可读名称
- `project_root`：项目所代表的仓库或工作区根路径
- `control_surface_root`：项目本地 durable 控制面根路径
- `phase`：当前项目阶段
- `execution_line`：当前活跃执行线
- `blockers`：当前 blocker 摘要，或空列表
- `approval_boundary`：风险动作对应的 review / approval 边界
- `policy_source_docs`：人类可读 policy source 引用
- `policy_machine_manifest`：机器层 policy manifest 引用
- `validation_entrypoints`：允许的验证命令或 adapter
- `deploy_entrypoints`：允许的部署命令或 adapter
- `rollback_entrypoints`：允许的回滚命令或 adapter
- `channel_bindings`：可用于 steering 或接收 push 更新的 channel 引用
- `executor_ref`：Growware 可以 handoff 给它的执行器或 adapter
- `status_updated_at`：最后一次 durable 状态更新时间

## State Rules

- 缺少任意必填字段的项目，不能作为 active capsule 接入
- 未知值必须显式记录，不能默默省略
- 在开始 `executor-required` 工作前，`approval_boundary`、`policy_machine_manifest`、`executor_ref` 必须已经存在
- Growware 可以只读 capsule 来回答进展问题，而不改动目标项目

## Approval Rules

- 修改 `project_root`、`control_surface_root`、`channel_bindings` 都需要明确 review
- 扩大任何 entrypoint 权限都需要明确批准
- 不经 review 就修改 deploy 或 rollback 边界是无效的

## Machine Notes

- 把 `required_fields` 编译为稳定顺序数组
- 字段名必须原样保留，方便 adapter 用同一套拼写做校验
