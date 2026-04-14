# Project 1 Pilot Loop V1

[English](pilot-loop-v1.md) | [中文](pilot-loop-v1.zh-CN.md)

## Purpose

This document records the first pilot loop that must be explicit before runtime implementation begins.

It is the paper gate for Stage 1, not evidence that Stage 2 has already started.

## Status

- status: `draft / implementation-gate candidate`
- project mode: `discussion and documentation`
- last reviewed: `2026-04-14`

## Implementation Gate Coverage

| Required Item | Current Decision |
| --- | --- |
| One concrete pilot target | `Project 1 = openclaw-task-system` |
| One operator path | `feishu6 -> OpenClaw adapter -> Growware daemon -> approval / status reply back to feishu6` |
| One real usage path | all usage channels with `task system` mounted by default are the `B` surface |
| One incident contract | feedback / runtime evidence can be promoted into one shared incident record v0 |
| One verification contract | every proposed repair needs scoped checks, result evidence, and regression intent before deployment |
| One deployment approval boundary | deploy and rollback remain human-gated through `feishu6` for the first pilot |

## Pilot Target

- `Project 1` stays locked to `openclaw-task-system` until a human explicitly changes it.
- The Growware repository defines the method, policy source, and pilot boundary.
- The target project will own the future project-local control surface in `openclaw-task-system/.growware/` once Stage 2 is authorized.

## Operator Path

The first operator path is intentionally narrow:

1. A human reports intent, feedback, or approval in `feishu6`.
2. The OpenClaw adapter normalizes that message into a feedback event.
3. Growware binds the event to `Project 1`.
4. The daemon decides whether the event is only feedback, should open an incident, or requires approval handling.
5. If work is proposed, the same path returns status, approval requests, and close-out back to `feishu6`.

This path defines the human control surface for the first pilot. It does not yet claim that the runtime wiring is live.

## Real Usage Path

The real usage path is separate from the operator path:

- all usage channels with `task system` mounted by default belong to the `B` surface
- runtime evidence comes from gateway logs, target-project logs, daemon logs, and optional structured events
- collection alone does not create an incident; the judge layer decides whether the evidence crosses the incident threshold

## Incident Contract V0

An incident may start from either human feedback or runtime evidence, but both must converge on one record shape.

### Promotion Rules

- human feedback may be promoted when it reports a user-visible wrong behavior, a broken expectation, or a decision-worthy risk
- runtime evidence may be promoted when the judge classifies it as more than noise
- every promoted incident must keep provenance back to the original evidence

### Required Fields

| Field | Meaning |
| --- | --- |
| `project_id` | target project binding |
| `incident_id` | durable identifier |
| `source` | `human-feedback`, `gateway-log`, `plugin-log`, `daemon-log`, or structured event source |
| `summary` | short problem statement |
| `severity` | initial impact classification |
| `problem_type` | `spec-gap`, `runtime-observable`, or other approved category |
| `evidence` | references to logs, sessions, or feedback events |
| `approval_required` | whether the next action may proceed automatically |
| `status` | intake, triage, repair, verify, blocked, or closed |

## Verification Contract V0

No repair is eligible for deployment until the verifier can attach a scoped verification record.

The expanded Stage 2 and Stage 3 paper-delivery contracts now live in:

- [stage-2-3-baseline.md](stage-2-3-baseline.md)
- [stage-2-3-contracts/README.md](stage-2-3-contracts/README.md)

### Required Verification Record

| Field | Meaning |
| --- | --- |
| `incident_id` | the incident being checked |
| `change_scope` | what was changed |
| `checks_run` | the exact verification steps that were attempted |
| `result` | pass, fail, or inconclusive |
| `evidence` | output references, screenshots, logs, or notes |
| `regression_asset` | the rule, judge, or regression artifact created or explicitly deferred |
| `residual_risk` | what still is not proven |

### Pass Rule

- the proposed repair must be tied to one incident
- the checks must match the claimed change scope
- the result must be visible to a human reviewer
- if no durable regression asset is added yet, the close-out must say that explicitly

## Deployment Approval Boundary V0

For the first pilot, deployment remains human-gated.

| Action | Default Gate |
| --- | --- |
| user-visible behavior change | require approval in `feishu6` |
| deploy to the target runtime | require approval in `feishu6` |
| rollback in response to a bad deploy | require approval in `feishu6` unless emergency policy is defined later |
| policy or contract change that alters pilot semantics | require explicit human review before activation |

## Out Of Scope For This Stage

- choosing the final runtime form between sidecar and OpenClaw service
- claiming autonomous deployment
- claiming that `openclaw-task-system/.growware/` is already live from this repo alone
- treating `.policy/` compilation as proof that runtime execution already consumes it

## Stage 2 Start Gate

Stage 2 may start only when all of the following remain true in docs and `.codex/*`:

- the pilot target is explicit
- the operator path is explicit
- the real usage path is explicit
- the incident contract is explicit
- the verification contract is explicit
- the deployment approval boundary is explicit
- the user explicitly authorizes implementation to begin
