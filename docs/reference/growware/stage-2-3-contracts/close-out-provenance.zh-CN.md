# Close-Out Provenance Contract

[English](close-out-provenance.md) | [中文](close-out-provenance.zh-CN.md)

## Metadata

- id: `growware.stage23.close-out-provenance.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `close-out-provenance`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`

## Purpose

这份合同定义每一次 Stage 2 和 Stage 3 close-out 如何保留执行来源、验证证据和未解决 follow-up。

## Execution Sources

- `daemon-owned`
- `terminal-takeover`
- `mixed`

## Required Fields

- `project_id`
- `incident_id`
- `execution_source`
- `result_summary`
- `verification_refs`
- `writeback_refs`
- `residual_risk`
- `follow_up_needed`
- `closed_at`

## Provenance Rules

- 每次 close-out 都必须明确一个 execution source
- `closed` 不得被写成“所有能力都已经 daemon-owned”的隐含说法
- mixed execution 必须说明哪一部分仍然是手动完成的

## Follow-Up Rules

- 缺失的 judge、rule 或 regression 工作必须作为 deferred follow-up 写出来，不能省略
- 未解决风险必须继续保留在 close-out payload 里
- 就算工作最后是 rejected 或 blocked，也仍然需要 close-out provenance

## Approval Rules

- close-out 不能抹掉这次动作曾经依赖过的 approval history
- terminal takeover 不能为了方便而被写成 daemon-owned

## Machine Notes

- 把 `execution_sources`、`required_fields`、`provenance_rules`、`follow_up_rules`、`approval_rules` 分别编译为独立数组

