# Regression Asset Contract

[English](regression-assets.md) | [中文](regression-assets.zh-CN.md)

## Metadata

- id: `growware.stage23.regression-assets.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `regression-assets`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义 Stage 2 和 Stage 3 的工作如何回写 tests、replays、fixtures、rules，或者显式记录 deferred gaps。

## Asset Types

- `test`
- `replay`
- `fixture`
- `rule`
- `judge`
- `deferred-gap`

## Required Fields

- `asset_id`
- `asset_type`
- `project_id`
- `source_incident_ref`
- `target_surface`
- `asset_summary`
- `status`
- `approval_state`

## Writeback Rules

- 每一条 closed incident 都必须要么产出一个 asset，要么产出一条明确的 `deferred-gap`
- 所有 assets 都必须保留回到 incident 或 close-out 的 provenance
- deferred gaps 必须解释为什么它还没有被提升

## Coverage Rules

- 重复 incident 如果一直没有新增 assets，就应该触发 review
- 一个 asset 只有在共享范围明确时，才允许覆盖多条 incident
- regression assets 应该减少未来歧义，而不是只重复 incident summary

## Approval Rules

- 新增会改变 deploy 权限的 rule 或 judge，必须经过明确 review
- 删除或替换一条已经接受的 regression asset，必须保留明确 review 和 provenance

## Machine Notes

- 把 `asset_types`、`required_fields`、`writeback_rules`、`coverage_rules`、`approval_rules` 分别编译为独立数组

