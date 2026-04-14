# Growware Daemon Boundary Contract

[English](daemon-boundary.md) | [中文](daemon-boundary.zh-CN.md)

## Metadata

- id: `growware.daemon.boundary`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `daemon-boundary`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.md`
  - `docs/reference/growware/shared-policy-contract.md`

## Purpose

This contract fixes the ownership boundary of the Growware daemon before broader project execution begins.

## Owns

- normalize channel dialogue into durable Growware-side commands and events
- resolve which attached project a request belongs to
- read durable project state through the project capsule contract
- load machine-readable policy and approval rules before acting
- decide whether the request is state-only, coordination-only, executor-required, or approval-wait
- assemble progress push, approval request, verification, and close-out payloads
- emit learning-writeback proposals after resolved work

## Does Not Own

- target-project business logic
- channel-host transport internals
- project-local runtime implementation details
- silent deployment beyond the approved boundary
- rewriting another project's roadmap by assumption

## Decision Rules

- if a request can be answered from durable project state, do not delegate it to a target project
- if a request needs repo mutation, validation, or deployment activity, require an executor handoff record
- if approval state is missing or ambiguous, stop and request review instead of guessing
- if policy loading fails, the daemon must report the failure and avoid continuing execution

## Approval Rules

- changing project binding, approval boundary, or executor privileges requires explicit approval
- deployment and rollback actions must obey the project capsule's declared approval boundary
- promoting a temporary manual workaround into daemon-owned behavior requires reviewable writeback

## Machine Notes

- compile this doc into one machine contract with the same stable `id`
- the generated record should expose `owns`, `does_not_own`, `decision_rules`, and `approval_rules` as separate arrays
