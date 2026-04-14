# Channel Command And Event Model

[English](channel-command-model.md) | [中文](channel-command-model.zh-CN.md)

## Metadata

- id: `growware.channel.command-model.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `channel-command-model`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.md`

## Purpose

This contract defines the minimal durable command and event model Growware accepts and emits through channel dialogue.

## Required Envelope

- `command`: stable command name
- `channel_ref`: channel identifier in host-local form
- `message_ref`: source message identifier when available
- `actor_ref`: actor identifier for the sender
- `observed_at`: event timestamp
- `project_ref`: explicit project ref or empty when routing must infer it
- `payload`: command-specific payload body

## Commands

- `status`: request the current project progress snapshot
- `continue`: request the next execution step under the current execution line
- `approve`: approve one pending gated action
- `block`: report a blocker or refusal to proceed
- `incident`: report a runtime or product problem that should enter the project loop
- `close`: acknowledge close-out and mark the channel-visible loop as received

## Emitted Events

- `progress-pushed`: Growware emitted a progress snapshot or next-step update
- `approval-requested`: Growware is waiting for explicit approval
- `incident-recorded`: a channel-side incident was accepted into durable project state
- `execution-delegated`: the request moved into executor-required work
- `close-out-pushed`: Growware emitted final outcome and provenance

## Routing Rules

- prefer explicit `project_ref`; otherwise resolve through the project's declared `channel_bindings`
- if routing is ambiguous, stop and ask for clarification instead of guessing
- commands that change execution state must be tied back to one resolved project capsule

## Approval Rules

- `approve` is valid only when it matches one pending approval wait
- a channel message cannot silently widen executor privileges
- channel-side free text does not override machine-loaded project policy

## Machine Notes

- compile `commands` and `emitted_events` as stable ordered arrays
- keep the envelope field spellings stable across compiled JSON
