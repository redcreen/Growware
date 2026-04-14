# Automation Bands Contract

[English](automation-bands.md) | [中文](automation-bands.zh-CN.md)

## Metadata

- id: `growware.stage23.automation-bands.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `automation-bands`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`
  - `docs/reference/growware/shared-policy-contract.zh-CN.md`

## Purpose

这份合同定义 Stage 3 里的处理带宽：哪些只能人工、哪些需要审批、哪些才有资格进入低风险自动处理。

## Automation Bands

- `manual-only`
- `approval-gated`
- `low-risk-automatic`

## Eligibility Rules

- 用户可见语义变化始终属于 `manual-only`
- deploy 与 rollback 至少仍属于 `approval-gated`，除非以后有其他明确合同单独收紧规则
- 只有重复出现、可回滚、影响半径很小的工作，才可以考虑进入 `low-risk-automatic`

## Guardrails

- 每条自动路径都必须保留 incident refs、verification refs 和 close-out provenance
- 每条自动路径都必须继续保留 rollback path
- 缺少新鲜证据时，工作必须退出 `low-risk-automatic`

## Approval Rules

- 从 `manual-only` 提升到 `approval-gated` 或 `low-risk-automatic`，必须经过明确 review
- automation band 的变化不能只因为一次修复成功就被推断成立

## Escalation Rules

- 只要 band 有歧义，就回落到更严格的带宽
- 只要 verification 重复失败，就立刻退出 `low-risk-automatic`
- 只要 incident 涉及 approval-boundary 漂移，就立刻回落到 `manual-only`

## Machine Notes

- 把 `automation_bands`、`eligibility_rules`、`guardrails`、`approval_rules`、`escalation_rules` 分别编译为独立数组

