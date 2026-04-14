# Judge Promotion Contract

[English](judge-promotion.md) | [中文](judge-promotion.zh-CN.md)

## Metadata

- id: `growware.stage23.judge-promotion.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `judge-promotion`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义在 Stage 3 准备阶段里，重复出现的人类判断如何被提升成 durable judge candidates。

## Judge Classes

- `noise-vs-incident`
- `severity-band`
- `spec-gap-vs-runtime-observable`
- `approval-needed`
- `automation-eligibility`

## Promotion Triggers

- 同一种人类判断在多条 incident 里重复出现
- 同一种 approval 决策重复到值得沉淀成可复用规则
- 同一种 verification 模式反复出现，并且可以编码为 judge 或 rubric

## Required Fields

- `judge_candidate_id`
- `judge_class`
- `source_incident_refs`
- `judgment_summary`
- `candidate_rule`
- `candidate_surface`
- `approval_state`

## Promotion Rules

- promotion 产生的是 candidate，不是已经生效的 policy
- 每个 candidate 都必须能回到真实的 incidents 或 close-outs
- candidate 既要说明它匹配什么，也要说明它不应该误匹配什么

## Rejection Rules

- 一次性的 ad hoc judgment 应该继续保持叙事态，不要强行升成 judge candidate
- 没有证据引用的“看起来有用”猜测，不够资格
- 任何默认会扩大 deploy 权限的 candidate，在激活前都必须先被明确拒绝或 review

## Machine Notes

- 把 `judge_classes`、`promotion_triggers`、`required_fields`、`promotion_rules`、`rejection_rules` 分别编译为独立数组

