# Policy Loading And Approval Contract

[English](policy-loading.md) | [中文](policy-loading.zh-CN.md)

## Metadata

- id: `growware.policy-loading.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `policy-loading`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/shared-policy-contract.md`
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines how Growware loads machine-readable project policy and applies approval checks before taking action.

## Inputs

- `project_id`: the resolved project capsule identifier
- `policy_source_docs`: human-readable source refs carried by the capsule
- `policy_machine_manifest`: machine-layer manifest ref carried by the capsule
- `policy_check_command`: declared validation command or adapter for the policy layer
- `action_kind`: the action Growware is evaluating
- `approval_boundary`: the project's declared approval boundary

## Loading Rules

- load policy only from the project capsule's declared machine-layer ref
- treat the human-readable policy source as review provenance, not as an implicit runtime fallback
- run the declared policy check path before executor-required work when freshness is uncertain
- evaluate the requested `action_kind` against the loaded policy and approval boundary before continuing

## Approval Rules

- if the loaded policy marks the action as approval-gated, Growware must stop at `approval-wait`
- if the action is not covered clearly enough by loaded policy, Growware must request review instead of inventing a rule from chat memory
- approval decisions must be traced back to the active project capsule and its current policy refs

## Failure Rules

- if the machine-layer manifest is missing, report `policy-unavailable` and stop
- if validation fails, report the failure and avoid continuing executor-required work
- if source docs and machine layer are known to drift, require review before acting

## Machine Notes

- compile `inputs`, `loading_rules`, `approval_rules`, and `failure_rules` as separate arrays
- keep `action_kind` and `policy-unavailable` spellings stable for later adapters
