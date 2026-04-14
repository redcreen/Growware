# Incident Lifecycle Contract

[English](incident-lifecycle.md) | [中文](incident-lifecycle.zh-CN.md)

## Metadata

- id: `growware.stage23.incident-lifecycle.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `incident-lifecycle`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/pilot-loop-v1.md`
  - `docs/reference/growware/stage-2-3-baseline.md`

## Purpose

This contract defines how one Stage 2 incident is created, promoted, advanced, blocked, and closed.

## Intake Sources

- `human-feedback`
- `gateway-log`
- `plugin-log`
- `daemon-log`
- `structured-runtime-event`

## Lifecycle States

- `intake`
- `triage`
- `repair`
- `verify`
- `approval-wait`
- `blocked`
- `closed`

## Required Fields

- `project_id`
- `incident_id`
- `source`
- `summary`
- `severity`
- `problem_type`
- `evidence_refs`
- `current_state`
- `approval_required`
- `opened_at`
- `updated_at`

## Promotion Rules

- human feedback may promote directly when it describes a user-visible problem, expected-behavior gap, or decision-worthy risk
- runtime evidence may promote only after a judge path says it is not noise
- every promoted incident must preserve references back to its original evidence

## Closure Rules

- an incident may close only after verification reaches an explicit result and close-out provenance is written
- `closed` does not imply `daemon-owned`; provenance must state that separately
- if work stops without a fix, the incident must close as a blocked or deferred outcome rather than disappearing

## Approval Rules

- any transition into deploy-affecting work must obey the deployment gate contract
- any incident with ambiguous project binding must stop before repair
- severity escalation that changes deploy or rollback authority requires explicit review

## Machine Notes

- compile `intake_sources`, `lifecycle_states`, `required_fields`, `promotion_rules`, `closure_rules`, and `approval_rules` as separate arrays

