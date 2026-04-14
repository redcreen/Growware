# Deployment Gate Contract

[English](deployment-gate.md) | [中文](deployment-gate.zh-CN.md)

## Metadata

- id: `growware.stage23.deployment-gate.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `deployment-gate`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/pilot-loop-v1.zh-CN.md`
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`

## Purpose

这份合同定义 Stage 2 里的哪些动作可以自动继续，哪些必须停下来等审批，以及 rollback 如何继续保持受限。

## Action Classes

- `read-only-status`
- `verification-only`
- `user-visible-change`
- `deploy`
- `rollback`
- `policy-or-contract-change`

## Gate Decisions

- `read-only-status`：不需要 deploy 审批即可继续
- `verification-only`：当项目 policy 允许这些检查时可以继续
- `user-visible-change`：必须停下来等审批
- `deploy`：必须停下来等审批
- `rollback`：默认也必须停下来等审批，除非以后有明确的 emergency contract 单独收紧例外
- `policy-or-contract-change`：必须停下来等审批

## Required Approval Payload

- `project_id`
- `incident_id`
- `action_class`
- `requested_effect`
- `verification_ref`
- `risk_summary`
- `requested_at`

## Rollback Rules

- rollback 仍然必须带明确范围、证据和目标环境
- rollback 不会抹掉 close-out provenance 的要求
- 触发 rollback 的 incident 仍然必须保留原始 deploy 上下文

## Emergency Constraints

- 这个仓库里默认不存在 emergency exception
- 以后如果要有 emergency rule，必须单独定义，不能仅凭“很紧急”去推断

## Machine Notes

- 把 `action_classes`、`gate_decisions`、`required_approval_payload`、`rollback_rules`、`emergency_constraints` 分别编译为独立数组

