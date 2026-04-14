# Execution Handoff Contract

[English](execution-handoff.md) | [中文](execution-handoff.zh-CN.md)

## Metadata

- id: `growware.execution-handoff.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `execution-handoff`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.md`
  - `docs/reference/growware/shared-policy-contract.md`

## Purpose

This contract defines when Growware answers from daemon-owned state, when it delegates, and when it must wait for approval.

## Handoff Modes

- `state-only`: answer from durable project state without code execution
- `coordination-only`: update project progress or planning state without entering executor-required work
- `executor-required`: hand work to the declared project executor or adapter
- `approval-wait`: stop because approval is required before the action may continue

## Required Handoff Record

- `project_id`: resolved attached project
- `requested_action`: action being asked for
- `handoff_mode`: one of the declared handoff modes
- `reason`: concise explanation for why this mode was chosen
- `policy_refs`: policy ids or manifests consulted before the decision
- `required_validation`: validation path expected before close-out
- `approval_state`: current approval state for the action

## Decision Rules

- prefer `state-only` when the answer already exists in durable project state
- use `coordination-only` when the work updates planning or progress but does not require code execution
- use `executor-required` only when the project capsule and policy layer both authorize the declared execution path
- move to `approval-wait` whenever the loaded policy or capsule boundary says the action is gated

## Approval Rules

- Growware must not invent an executor path outside the capsule's declared `executor_ref`
- a handoff record that changes action scope requires review
- final close-out must preserve the chosen `handoff_mode` as provenance

## Machine Notes

- compile `handoff_modes`, `required_handoff_record`, `decision_rules`, and `approval_rules` as separate arrays
- keep `handoff_mode` spellings stable for future daemon adapters
