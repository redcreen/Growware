# Automation Bands Contract

[English](automation-bands.md) | [中文](automation-bands.zh-CN.md)

## Metadata

- id: `growware.stage23.automation-bands.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `automation-bands`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/stage-2-3-baseline.md`
  - `docs/reference/growware/shared-policy-contract.md`

## Purpose

This contract defines the Stage 3 handling bands for manual-only, approval-gated, and low-risk automatic work.

## Automation Bands

- `manual-only`
- `approval-gated`
- `low-risk-automatic`

## Eligibility Rules

- user-visible semantic changes remain `manual-only`
- deploy and rollback remain at least `approval-gated` unless another explicit contract narrows the rule
- only repeated, reversible, low-blast-radius work may be considered for `low-risk-automatic`

## Guardrails

- every automatic path must preserve incident refs, verification refs, and close-out provenance
- every automatic path must still preserve a rollback path
- lack of fresh evidence moves the work back out of `low-risk-automatic`

## Approval Rules

- band promotion from `manual-only` to `approval-gated` or `low-risk-automatic` requires explicit review
- automation band changes may not be inferred from one successful repair

## Escalation Rules

- any band ambiguity falls back to the stricter band
- repeated verification failure immediately exits `low-risk-automatic`
- incidents involving approval-boundary drift immediately fall back to `manual-only`

## Machine Notes

- compile `automation_bands`, `eligibility_rules`, `guardrails`, `approval_rules`, and `escalation_rules` as separate arrays

