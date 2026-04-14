# Verification Profile Contract

[English](verification-profile.md) | [中文](verification-profile.zh-CN.md)

## Metadata

- id: `growware.stage23.verification-profile.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `verification-profile`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/pilot-loop-v1.zh-CN.md`
  - `docs/reference/growware/stage-2-3-baseline.zh-CN.md`

## Purpose

这份合同定义每一条 Stage 2 verification record 在修复被允许进入 deploy 或 close-out 之前，至少必须携带什么。

## Verification Modes

- `scope-check`
- `targeted-test`
- `manual-observation`
- `log-confirmation`
- `regression-asset-added`

## Required Fields

- `incident_id`
- `change_scope`
- `checks_run`
- `verification_mode`
- `result`
- `evidence_refs`
- `residual_risk`
- `regression_asset_ref`
- `verified_at`

## Matching Rules

- verification 范围必须和声明的 change scope 对得上
- 没有 evidence refs 的 `pass` 结果无效
- `inconclusive` 必须说明还有什么未确定
- 如果没有新增 regression asset，记录里必须明确它是 deferred 还是 not applicable

## Failure Rules

- `fail` 会阻塞 deploy
- 重复出现的 inconclusive 结果，在 deploy 前必须显式经过人工 review
- verification 不能悄悄重写 incident 的 summary 或 severity

## Close-Out Rules

- close-out 必须带上最新 verification record 的引用
- 只要结果不是干净的 pass，close-out 就必须再次写明 residual risk
- 即使修复最后被拒绝或延期，verification provenance 也必须保留可见

## Machine Notes

- 把 `verification_modes`、`required_fields`、`matching_rules`、`failure_rules`、`close_out_rules` 分别编译为独立数组

