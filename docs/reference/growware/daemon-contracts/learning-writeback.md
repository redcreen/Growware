# Learning Writeback Contract

[English](learning-writeback.md) | [中文](learning-writeback.zh-CN.md)

## Metadata

- id: `growware.learning-writeback.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `learning-writeback`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines how resolved work later becomes reusable rule, judge, or regression follow-up instead of remaining one-off chat history.

## Proposal Types

- `rule-proposal`: candidate reusable behavioral or approval rule
- `judge-proposal`: candidate check or rubric for future evaluation
- `regression-asset-proposal`: candidate test, replay, or fixture for future prevention

## Required Fields

- `proposal_id`: stable proposal identifier
- `project_id`: attached project identifier
- `source_execution`: daemon-owned or terminal-takeover origin
- `problem_summary`: concise description of the resolved problem
- `resolution_summary`: concise description of the fix or decision
- `candidate_asset`: the proposed reusable asset
- `target_surface`: where the asset would live if accepted
- `evidence_refs`: supporting refs from incident, validation, or close-out
- `approval_state`: whether the proposal still needs explicit review

## Trigger Rules

- create a writeback proposal when a human-reported problem was resolved and the outcome appears reusable
- create a writeback proposal when a repeated approval or verification judgment surfaced
- skip writeback only when the work was purely mechanical and produced no reusable rule

## Approval Rules

- proposals are records for review, not silently activated policy
- promoting a proposal into active rule or regression state requires explicit acceptance in the target surface
- terminal-takeover resolutions must preserve provenance rather than pretending the daemon already owned the behavior

## Machine Notes

- compile `proposal_types`, `required_fields`, `trigger_rules`, and `approval_rules` as separate arrays
- keep proposal type spellings stable so future adapters can match them directly
