# Roadmap

[English](roadmap.md) | [中文](roadmap.zh-CN.md)

## Scope

This roadmap shows the milestone order for turning the Growware concept into a real local-first pilot. It is intentionally earlier than implementation detail.

For the detailed maintainer queue under these stages, use [reference/growware/development-plan.md](reference/growware/development-plan.md).

## Stages

| Stage | Status | Goal | Unlocks | Exit Criteria |
| --- | --- | --- | --- | --- |
| [Stage 0 - Origin Capture and Feasibility](reference/growware/development-plan.md#stage-0-origin-capture-and-feasibility) | completed | preserve the starting conversation, align naming, and publish the baseline docs set | shared context and truthful docs | transcript archived, docs linked, active naming converged to Growware |
| [Stage 1 - Project 1 Pilot Foundation Long Task](reference/growware/development-plan.md#stage-1-project-1-pilot-foundation-long-task) | completed | land Project 1, `feishu6` wiring, `.growware/` boundaries, daemon duties, contracts, and the start gate in the real project and host config | Stage 2 local loop | `openclaw-task-system/.growware/`, the `growware` agent, `feishu6-chat` binding, and v0 contracts are live |
| [Stage 2 - Single-Project Local Semi-Automatic Loop](reference/growware/development-plan.md#stage-2-single-project-local-semi-automatic-loop) | completed | implement the local observe -> report -> repair -> verify -> deploy baseline on Project 1 | first runnable Growware baseline | local deploy, Gateway restart, plugin smoke, and install-drift checks have run successfully |
| [Stage 3 - Detectors, Gates, and Low-Risk Automation](reference/growware/development-plan.md#stage-3-detectors-gates-and-low-risk-automation) | completed (baseline) | add the first judge, deploy-gate, and low-risk fallback automation layer | more stable loop | judge/deploy-gate v0 are versioned and installation-blocked deploys can fall back to runtime-sync safely |
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

## What This Roadmap Does Not Do

- pick a runtime or framework today
- promise autonomous production deployment
- replace the detailed queue in the development plan

## Current Focus

The current focus is no longer planning. It is accepting real human feedback through the live `feishu6-chat` path and continuing the pilot.
