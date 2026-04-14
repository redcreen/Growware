# Roadmap

[English](roadmap.md) | [中文](roadmap.zh-CN.md)

## Scope

This roadmap shows the milestone order for turning the Growware concept into a real local-first pilot. It is intentionally earlier than implementation detail.

For the detailed maintainer queue under these stages, use [reference/growware/development-plan.md](reference/growware/development-plan.md).

## Stages

| Stage | Status | Goal | Unlocks | Exit Criteria |
| --- | --- | --- | --- | --- |
| [Stage 0 - Origin Capture and Feasibility](reference/growware/development-plan.md#stage-0-origin-capture-and-feasibility) | completed | preserve the starting conversation, align naming, and publish the baseline docs set | shared context and truthful docs | transcript archived, docs linked, active naming converged to Growware |
| [Stage 1 - Project 1 Pilot Foundation Long Task](reference/growware/development-plan.md#stage-1-project-1-pilot-foundation-long-task) | complete on paper | define Project 1, the `A/B` paths, `.growware/` boundary, core contracts, and the Stage 2 start gate on paper | daemon-first Growware planning | `pilot-loop-v1`, architecture, development plan, and policy source align on one explicit pilot contract pack |
| [Stage 1.5 - Growware Self / Daemon Foundation](reference/growware/development-plan.md#stage-15-growware-self--daemon-foundation) | paper complete / foundational | define Growware's own daemon boundary, project capsule, channel-progress contract, and execution handoff before broadening target-project execution | Stage 2 and Stage 3 paper baseline | `daemon-foundation-plan`, `daemon-contracts/*`, generated `.growware/daemon-foundation/*`, roadmap, development plan, and `.codex/*` align on one Growware-self mainline |
| [Stage 2 - Single-Project Local Semi-Automatic Loop](reference/growware/development-plan.md#stage-2-single-project-local-semi-automatic-loop) | experimental v0 in progress / deploy gated | implement the local observe -> report -> repair -> verify -> deploy baseline on Project 1 under the approved Growware daemon boundary | first runnable Growware baseline | `experiments/mock_runtime/` can consume the compiled machine layers and run a local mock loop while deploy remains approval-gated and non-production |
| [Stage 3 - Detectors, Gates, and Low-Risk Automation](reference/growware/development-plan.md#stage-3-detectors-gates-and-low-risk-automation) | paper baseline complete / experiment hookup queued | add the first judge, deploy-gate, and low-risk automation layer | more stable loop | the Stage 3 judge, automation-band, and regression-asset rules are explicit and machine-compilable before production activation |
| [Stage 4 - Multi-Project Onboarding and Isolation](reference/growware/development-plan.md#stage-4-multi-project-onboarding-and-isolation) | later | support more than one target project without cross-project contamination | reusable control layer | multiple projects can share Growware without channel, state, queue, or deploy collisions |

## Recommended First Pilot

The current recommended `Project 1` target is your existing `openclaw task system`.

Why:

- it is already a real project
- `feishu6` has already been proposed as the feedback / notification / approval entry
- all task-system-mounted usage channels are already being treated as the runtime surface
- you want the project-level control plane to live beside the project in `.growware/`
- it is concrete enough to force the first version of the contracts

If you choose another target later, the roadmap shape stays the same and only the `Project 1` target changes.

## Current Recommended Defaults

Before Stage 1 execution begins, the docs now assume these defaults:

- `Project 1 = openclaw-task-system`
- `A channel = feishu6`
- the `A channel` carries feedback, approvals, and notifications
- `Telegram` remains a fallback channel
- all usage channels with task system mounted by default are treated as `B` surfaces
- project-level durable configuration and rules live in `.growware/` at the target project root
- human-readable policy source lives in `docs/policy/` and is governed by `docs/reference/growware/shared-policy-contract.md`

## What This Roadmap Does Not Do

- lock a production runtime or framework too early
- promise autonomous production deployment
- replace the detailed queue in the development plan
- bypass the policy source layer in `docs/policy/`

## Current Focus

The current focus is to stand up one isolated mock runtime that consumes the compiled machine layers without pretending that Project 1 is already wired end to end.

The current focus is to keep the Stage 2 and Stage 3 contracts explicit, compiled, and reviewable while `experiments/mock_runtime/` proves the daemon-side control flow locally.
