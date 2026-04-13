# Growware Development Plan

[English](development-plan.md) | [中文](development-plan.zh-CN.md)

## Purpose

This document is the durable maintainer-facing execution plan that sits below `docs/roadmap.md` and above `.codex/plan.md`.

It answers one practical question:

`what should happen next, where should maintainers resume, and what detail sits underneath each roadmap milestone?`

## Related Documents

- [../../roadmap.md](../../roadmap.md)
- [../../test-plan.md](../../test-plan.md)
- [feasibility.md](feasibility.md)
- [origin-transcript-2026-04-13.md](origin-transcript-2026-04-13.md)

## How To Use This Plan

1. Read the roadmap first to understand milestone order.
2. Read `Current Position` and `Ordered Execution Queue` here to know where to resume.
3. Drop into `.codex/plan.md` only when you need the live control-surface detail.

## Current Position

| Item | Current Value | Meaning |
| --- | --- | --- |
| Current Phase | Stage 3 baseline is complete and the pilot is now live for real feedback. | Current maintainer-facing phase |
| Active Slice | `real-feishu6 pilot operation` | The slice tied to the current execution line |
| Current Execution Line | accept real `feishu6-chat` feedback, enter the `openclaw-task-system` workspace through the `growware` agent, verify locally, then run the deploy baseline and send notifications back | What the repo is trying to continue now |
| Validation | `.growware/`, OpenClaw binding, local deploy fallback, Gateway restart, plugin smoke, and install drift are all live and verified | How this line proves itself now |

## Milestone Overview

| Milestone | Status | Goal | Depends On | Exit Criteria |
| --- | --- | --- | --- | --- |
| Stage 0 | completed | preserve the origin conversation, rename the project to Growware, and establish a truthful docs baseline | shared conversation | transcript archived, naming aligned, baseline docs exist |
| Stage 1 | planned / not started | use one long task to define Project 1 and all of its first operational contracts | Stage 0 | target, channel binding, daemon interface, core contracts, and the start gate are explicit |
| Stage 2 | queued | implement one local semi-automatic loop with human approval at deployment gates for Project 1 | Stage 1 | Project 1 can run through observe -> report -> repair -> verify -> deploy locally |
| Stage 3 | queued | expand detectors, gates, regression assets, and low-risk automation | Stage 2 | selected low-risk incidents can be auto-fixed behind explicit gates |
| Stage 4 | later | onboard more than one project without cross-project contamination | Stage 3 | multiple projects can share Growware without channel, state, queue, or deploy collisions |

## Ordered Execution Queue

| Order | Slice | Status | Objective | Validation |
| --- | --- | --- | --- | --- |
| 1 | `bootstrap control surface` | earlier slice | n/a | n/a |
| 2 | `origin capture and feasibility baseline` | earlier slice | preserve the shared conversation and publish truthful baseline docs | transcript archived, docs linked, and naming converged |
| 3 | `stage-1 project-1 pilot foundation` | current / planning only | fully define Project 1 contracts, OpenClaw bindings, and daemon interfaces | Stage 1 long task is complete and waiting for the user to start it |
| 4 | `single-project local semi-automatic loop` | next / queued | implement the first local observe -> report -> repair -> verify -> deploy loop with human approval for Project 1 | one pilot runs locally through a repeatable path |
| 5 | `detectors, gates, and low-risk automation` | later / queued | turn repeated human corrections into detectors, rules, gates, and regression assets | low-risk automation stays gated and reversible |
| 6 | `multi-project onboarding and isolation` | later | support a second and later target projects | multiple projects do not contaminate each other |

## Milestone Details

<a id="stage-0-origin-capture-and-feasibility"></a>
## Stage 0 - Origin Capture and Feasibility

Goal:

- preserve the exact user-visible starting conversation in Markdown
- replace the temporary placeholder naming with `Growware`
- publish durable docs that truthfully describe the repo as pre-implementation

Exit criteria:

- transcript exists in English and Chinese Markdown files
- public docs point to Growware, not the old placeholder name
- feasibility, architecture, roadmap, and test-plan baselines exist

<a id="stage-1-project-1-pilot-foundation-long-task"></a>
## Stage 1 - Project 1 Pilot Foundation Long Task

Recommended target:

- `Project 1 = openclaw task system`

Current recommended defaults:

- `A channel = feishu6`
- the `A channel` carries feedback, approvals, and notifications
- `Telegram` is the fallback channel
- all usage channels with `task system` mounted by default are treated as `B` surfaces
- project-level durable configuration and rules live in `openclaw-task-system/.growware/`

This long task is not for runtime implementation yet. It exists to lock down the boundaries that must be true before implementation begins.

### Stage 1 Objectives

- lock the `Project 1` target
- lock the OpenClaw static channel binding
- lock the `feishu6` / `Telegram` primary-fallback strategy
- lock the `feedback adapter -> project daemon` integration shape
- lock the first `feedback / incident / judge / verifier / deploy gate` contracts
- lock the durable `.growware/` boundary inside the target project
- lock the local interfaces the daemon must expose
- lock the start gate for Stage 2

### Stage 1 Workstreams

1. `WS1 - Project Lock`
   - define the target project, repo, workspace, and local deploy boundary
   - define the on-repo `.growware/` persistence boundary

2. `WS2 - OpenClaw Binding`
   - define `feishu6` as the human feedback entry
   - define `feishu6` as the approval / notification route
   - define whether `Telegram` stays fallback-only
   - define all task-system-mounted channels as the real usage evidence surface
   - define watched plugins, log sources, and approval channels

3. `WS3 - Feedback And Incident Contract`
   - define the minimum feedback event
   - define the minimum incident record
   - define how feedback can be promoted into an incident

4. `WS4 - Judge / Verifier / Deploy Gate V0`
   - define noise versus anomaly versus incident
   - define the first local verification path
   - define which actions require human approval

5. `WS5 - Project Daemon Interface`
   - define what the daemon owns and what it does not own
   - list the required `run / test / deploy / rollback / logs` interfaces
   - define which `.growware/` paths the daemon reads and writes

6. `WS6 - Start Gate Review`
   - review whether Stage 2 is actually ready to begin
   - if the review fails, stop here instead of starting execution

### Stage 1 Deliverables

- updated architecture docs
- Project 1 static binding draft
- `.growware/` directory layout draft
- feedback event v0
- incident record v0
- judge / verifier / deploy gate v0
- project daemon interface v0
- Stage 2 start-gate checklist

### Stage 1 Exit Criteria

- `Project 1` is explicit
- the `feishu6` and `Telegram fallback` ownership model is explicit
- the in-project `.growware/` boundary is explicit
- daemon boundaries are explicit
- the feedback, incident, judge, verifier, and deploy gate contracts are explicit
- the user has explicitly authorized the transition into Stage 2

### Stage 1 Start Condition

- planning is complete
- execution remains paused until the user explicitly says to start

<a id="stage-2-single-project-local-semi-automatic-loop"></a>
## Stage 2 - Single-Project Local Semi-Automatic Loop

Goal:

- implement one local-first loop with structured observation, incident generation, repair execution, verification, and gated deployment for `Project 1`

Expected result:

- Growware can prove one end-to-end loop on `Project 1` without claiming generalized autonomy
- `feishu6` can reliably carry feedback, notifications, and approvals
- `openclaw-task-system/.growware/` works as the project-level durable control surface

<a id="stage-3-detectors-gates-and-low-risk-automation"></a>
## Stage 3 - Detectors, Gates, and Low-Risk Automation

Goal:

- accumulate detectors, judges, rules, regression assets, and rollback-safe automation from repeated incidents

Expected result:

- some low-risk repairs can move from human-triggered to gated automatic execution

<a id="stage-4-multi-project-onboarding-and-isolation"></a>
## Stage 4 - Multi-Project Onboarding and Isolation

Goal:

- support a second and later target projects
- keep channels, logs, state, queues, and deployment boundaries isolated

Expected result:

- Growware starts becoming a reusable project control layer rather than a single-project control loop

## Current Next Step

| Next Move | Why |
| --- | --- |
| Wait for the user to start `Stage 1 - Project 1 Pilot Foundation Long Task` | this round defines the long task completely, but does not start execution |
