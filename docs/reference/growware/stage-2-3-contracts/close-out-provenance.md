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
  - `docs/reference/growware/daemon-foundation-plan.md`
  - `docs/reference/growware/stage-2-3-baseline.md`

## Purpose

This contract defines how every Stage 2 and Stage 3 close-out preserves execution source, verification evidence, and unresolved follow-up.

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

- every close-out must name one execution source
- `closed` must not imply that all capability was daemon-owned
- mixed execution must describe which part stayed manual

## Follow-Up Rules

- missing judge, rule, or regression work must be surfaced as deferred follow-up rather than omitted
- unresolved risk must stay visible in the close-out payload
- rejected or blocked work still needs close-out provenance

## Approval Rules

- close-out may not erase the approval history that allowed the action
- terminal takeover may not be represented as daemon-owned for convenience

## Machine Notes

- compile `execution_sources`, `required_fields`, `provenance_rules`, `follow_up_rules`, and `approval_rules` as separate arrays

