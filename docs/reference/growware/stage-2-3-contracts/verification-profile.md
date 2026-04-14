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
  - `docs/reference/growware/pilot-loop-v1.md`
  - `docs/reference/growware/stage-2-3-baseline.md`

## Purpose

This contract defines what every Stage 2 verification record must carry before a repair may move toward deploy or close-out.

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

- verification scope must match the declared change scope
- `pass` without evidence refs is invalid
- `inconclusive` must explain what is still unknown
- if no regression asset was added, the record must say whether it was deferred or not applicable

## Failure Rules

- `fail` blocks deploy
- repeated inconclusive results require explicit human review before deploy
- verification cannot silently rewrite the incident summary or severity

## Close-Out Rules

- close-out must carry the latest verification record ref
- close-out must restate residual risk when the result is not a clean pass
- verification provenance must remain visible even when the repair is rejected or deferred

## Machine Notes

- compile `verification_modes`, `required_fields`, `matching_rules`, `failure_rules`, and `close_out_rules` as separate arrays

