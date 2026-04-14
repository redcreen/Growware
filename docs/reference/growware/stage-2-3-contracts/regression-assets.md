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
  - `docs/reference/growware/stage-2-3-baseline.md`
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines how Stage 2 and Stage 3 work writes back tests, replays, fixtures, rules, or explicit deferrals.

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

- every closed incident must either create an asset or create an explicit `deferred-gap`
- assets must preserve provenance back to the incident or close-out that created them
- deferred gaps must explain why they were not yet promoted

## Coverage Rules

- repeated incidents without new assets should trigger review
- one asset may cover more than one incident only when the shared scope is explicit
- regression assets should narrow future ambiguity rather than merely restate the incident summary

## Approval Rules

- adding a rule or judge that changes deploy authority requires explicit review
- deleting or replacing an accepted regression asset requires explicit review and provenance

## Machine Notes

- compile `asset_types`, `required_fields`, `writeback_rules`, `coverage_rules`, and `approval_rules` as separate arrays

