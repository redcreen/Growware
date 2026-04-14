# Judge Promotion Contract

[English](judge-promotion.md) | [中文](judge-promotion.zh-CN.md)

## Metadata

- id: `growware.stage23.judge-promotion.v1`
- kind: `stage-contract`
- status: `active-draft`
- contract_type: `judge-promotion`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/stage-2-3-baseline.md`
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines how repeated human judgments become durable judge candidates during Stage 3 preparation.

## Judge Classes

- `noise-vs-incident`
- `severity-band`
- `spec-gap-vs-runtime-observable`
- `approval-needed`
- `automation-eligibility`

## Promotion Triggers

- the same human judgment repeats across more than one incident
- the same approval decision repeats often enough to deserve a reusable rule
- the same verification pattern repeats and can be encoded as a judge or rubric

## Required Fields

- `judge_candidate_id`
- `judge_class`
- `source_incident_refs`
- `judgment_summary`
- `candidate_rule`
- `candidate_surface`
- `approval_state`

## Promotion Rules

- promotion creates a candidate, not active policy
- each candidate must point back to real incidents or close-outs
- candidates should describe both what they match and what they must not match

## Rejection Rules

- one-off ad hoc judgments should remain narrative, not forced into a judge candidate
- vague “seems useful” guesses do not qualify without evidence refs
- candidates that would broaden deploy authority by default require explicit rejection or review before activation

## Machine Notes

- compile `judge_classes`, `promotion_triggers`, `required_fields`, `promotion_rules`, and `rejection_rules` as separate arrays

