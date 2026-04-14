# Progress Push Contract

[English](progress-push.md) | [中文](progress-push.zh-CN.md)

## Metadata

- id: `growware.progress-push.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `progress-push`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines the structured payloads Growware sends back through channels for progress, approval, verification, and close-out.

## Message Types

- `progress-snapshot`: current status plus next action
- `approval-request`: explicit approval wait with scope and reason
- `verification-result`: validation outcome with evidence refs
- `close-out`: final result, provenance, and writeback follow-up

## Common Fields

- `message_type`: one of the declared message types
- `project_id`: attached-project identifier
- `phase`: current phase
- `execution_line`: current active execution line
- `summary`: concise channel-visible summary
- `next_action`: the next expected step or wait state
- `blockers`: current blockers or empty list
- `approval_state`: current approval status for the relevant action
- `provenance`: whether the result came from daemon-owned state or terminal takeover

## Close-Out Fields

- `result`: final outcome summary
- `validation_refs`: evidence refs for checks that were run
- `execution_source`: daemon-owned or terminal-takeover origin
- `writeback_refs`: rule, judge, or regression proposals created by the loop
- `follow_up_needed`: explicit next required follow-up or empty value

## Delivery Rules

- every push must identify its `project_id` and `message_type`
- approval waits must name the action scope they are blocking
- close-out must preserve provenance instead of implying fully daemon-owned execution by default
- verification results must not claim success without evidence refs

## Machine Notes

- compile `message_types`, `common_fields`, and `close_out_fields` as separate arrays
- the machine layer should preserve `message_type` spellings exactly
