# Deployment Gate Contract

[English](deployment-gate.md) | [中文](deployment-gate.zh-CN.md)

## Metadata

- id: `growware.stage23.deployment-gate.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `deployment-gate`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/pilot-loop-v1.md`
  - `docs/reference/growware/stage-2-3-baseline.md`

## Purpose

This contract defines what Stage 2 actions may continue automatically, which ones must stop for approval, and how rollback remains constrained.

## Action Classes

- `read-only-status`
- `verification-only`
- `user-visible-change`
- `deploy`
- `rollback`
- `policy-or-contract-change`

## Gate Decisions

- `read-only-status`: continue without deploy approval
- `verification-only`: continue when project policy allows the declared checks
- `user-visible-change`: stop for approval
- `deploy`: stop for approval
- `rollback`: stop for approval unless a later emergency contract explicitly narrows the exception
- `policy-or-contract-change`: stop for approval

## Required Approval Payload

- `project_id`
- `incident_id`
- `action_class`
- `requested_effect`
- `verification_ref`
- `risk_summary`
- `requested_at`

## Rollback Rules

- rollback still requires explicit scope, evidence, and target environment
- rollback does not erase the need for close-out provenance
- rollback-triggering incidents must still preserve the original deploy context

## Emergency Constraints

- no emergency exception exists by default in this repo
- future emergency rules must be defined explicitly rather than inferred from urgency alone

## Machine Notes

- compile `action_classes`, `gate_decisions`, `required_approval_payload`, `rollback_rules`, and `emergency_constraints` as separate arrays

