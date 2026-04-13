# Growware

[English](README.md) | [中文](README.zh-CN.md)

> Growware is a feedback-driven engine that continuously evolves software from intent, use, and feedback. It is not "AI helps write code"; it is a software factory that keeps intent, judgment, and implementation in a live loop.

## What It Is

Based on the full origin conversation, Growware is not just an AI coding helper and not just an automatic bug-fix loop.

It is more accurately:

- a feedback-driven software factory
- a growth engine that connects the `A window`, the `B window`, and a hidden control plane
- a project-level control layer that keeps `spec / judge / code` aligned over time

The core idea is not merely "code edits itself." The real shape is:

- the `A window` defines intent, boundaries, and judgment
- the `B window` provides evidence from real use
- the hidden control plane turns that evidence into rules, tests, repairs, and deployment decisions

## What It Is Not

- not another chat UI for asking an LLM to write code
- not a log-watcher that guesses where things broke
- not a rewrite of OpenClaw's gateway, channel, plugin, or task ecosystem
- not a rewrite of Codex as a coding agent

Growware should fill the missing middle layer: the project control plane that turns intent, use, and feedback into software evolution.

## Core Model

- `A window`: the product control plane for requirements, feedback, judgment, and approvals
- `B window`: the runtime surface where software is actually used and produces evidence
- hidden control plane: the evolution engine that turns A/B signals into `spec`, `judge`, `tests`, `code changes`, deploy gates, and reusable memory

The system is trying to automate three loops:

1. build software: intent to spec, implementation, verification, deployment
2. repair software: runtime evidence to incident, repair, verification, reply
3. learn software: turn one-off feedback into durable judges, rules, and regression assets

## Current Repository State

This repository has moved beyond the discussion-only baseline into a single-project pilot baseline.

What exists now:

- the full origin conversation is preserved in [docs/reference/growware/origin.pdf](docs/reference/growware/origin.pdf)
- the PDF has also been archived as full Markdown in [docs/reference/growware/origin-raw-extract.zh-CN.md](docs/reference/growware/origin-raw-extract.zh-CN.md)
- the extracted project definition lives in [docs/reference/growware/origin.md](docs/reference/growware/origin.md)
- public docs have been reframed around `Growware`
- feasibility, architecture, and roadmap are defined without prematurely locking the runtime stack
- `openclaw-task-system` is locked as `Project 1`
- the target project now contains a project-local `.growware/` control surface
- `feishu6-chat` is safely rebound to a dedicated `growware` agent in OpenClaw
- the local deploy baseline is real: if host install is blocked, deployment falls back to installed runtime sync, Gateway restart, smoke, and drift checks
- the `growware` agent has been verified inside the `openclaw-task-system` workspace

What remains intentionally not overstated:

- production-grade autonomous release
- multi-project isolation
- stronger detector / rubric / regression accumulation
- proactive cross-channel notification without an active conversation context

## Quick Start

1. Start from the canonical source: [docs/reference/growware/origin.pdf](docs/reference/growware/origin.pdf)
2. Read the extracted project definition: [docs/reference/growware/origin.md](docs/reference/growware/origin.md)
3. Review feasibility: [docs/reference/growware/feasibility.md](docs/reference/growware/feasibility.md)
4. Read the current architecture: [docs/architecture.md](docs/architecture.md)
5. Follow milestone order in [docs/roadmap.md](docs/roadmap.md)

## Documentation Map

- [Docs Home](docs/README.md)
- [Origin Summary](docs/reference/growware/origin.md)
- [Feasibility](docs/reference/growware/feasibility.md)
- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Development Plan](docs/reference/growware/development-plan.md)
- [Test Plan](docs/test-plan.md)
- [Share Transcript Capture](docs/reference/growware/origin-transcript-2026-04-13.md)
