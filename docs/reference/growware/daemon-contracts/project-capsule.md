# Project Capsule Contract

[English](project-capsule.md) | [中文](project-capsule.zh-CN.md)

## Metadata

- id: `growware.project-capsule.minimum`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `project-capsule`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines the minimum project-facing surface Growware reads from each attached project.

## Required Fields

- `project_id`: stable attached-project identifier
- `project_label`: human-facing name used in progress push
- `project_root`: repo or workspace root that the project represents
- `control_surface_root`: durable project-local control surface root
- `phase`: current project phase
- `execution_line`: current active execution line
- `blockers`: current blocker summary or empty list
- `approval_boundary`: review and approval boundary for risky actions
- `policy_source_docs`: human-readable policy source refs
- `policy_machine_manifest`: machine-layer policy manifest ref
- `validation_entrypoints`: allowed validation commands or adapters
- `deploy_entrypoints`: allowed deploy commands or adapters
- `rollback_entrypoints`: allowed rollback commands or adapters
- `channel_bindings`: attached channel refs that can steer or receive push updates
- `executor_ref`: declared executor or adapter Growware may hand work to
- `status_updated_at`: last durable state update timestamp

## State Rules

- a project missing any required field is not attachable as an active capsule
- unknown values must be recorded explicitly rather than omitted silently
- `approval_boundary`, `policy_machine_manifest`, and `executor_ref` must be present before executor-required work starts
- Growware may read the capsule for progress answers without mutating the target project

## Approval Rules

- changing `project_root`, `control_surface_root`, or `channel_bindings` requires explicit review
- widening any entrypoint privilege requires explicit approval
- changing the deploy or rollback boundary without review is invalid

## Machine Notes

- compile `required_fields` as a stable ordered array
- preserve field names exactly so adapters can validate against the same spellings
