# Growware

[English](README.md) | [中文](README.zh-CN.md)

> Growware is a document-first exploration of a closed-loop software evolution system that turns real-world usage, incidents, and feedback into reviewed fixes.

## What It Is

Growware is not a finished tool or framework yet. This repository currently defines the project boundary for a local-first loop where software is used, observed, judged, repaired, verified, and only then deployed.

The starting point comes from a shared conversation about using Codex and OpenClaw-style channels to move from "human notices a problem and reports it" toward "the system notices, proposes, verifies, and improves with humans only at risk boundaries."

## Who This Is For

- Maintainers building self-improving plugins, tools, or software around agent workflows
- Operators who want incident-driven repair instead of chat-only debugging
- Collaborators reviewing feasibility before implementation starts

## Current Project State

This repo is in a discussion and documentation baseline, not an implementation baseline.

What exists today:

- the origin conversation archived in Markdown
- a project-feasibility assessment
- a stable architecture and roadmap baseline
- a maintainer-facing development plan that stops before runtime implementation

What is still intentionally undecided:

- the first concrete pilot loop
- the target software boundary
- the runtime and stack
- the machine-checkable incident and verification contracts

## Quick Start

1. Read the exact starting conversation in [docs/reference/growware/origin-transcript-2026-04-13.md](docs/reference/growware/origin-transcript-2026-04-13.md).
2. Review the project-level judgment in [docs/reference/growware/feasibility.md](docs/reference/growware/feasibility.md).
3. Read the stable system shape in [docs/architecture.md](docs/architecture.md).
4. Check milestone order in [docs/roadmap.md](docs/roadmap.md).
5. Use [docs/reference/growware/development-plan.md](docs/reference/growware/development-plan.md) when resuming detailed maintainer work.

## Core Ideas

- `A window`: where requirements, feedback, approvals, and human judgment arrive
- `B window`: where real usage produces evidence, logs, incidents, and behavior traces
- hidden control plane: where signals become incidents, repair tasks, verification steps, deployment decisions, and reusable memory

## Documentation Map

- [Docs Home](docs/README.md)
- [Feasibility](docs/reference/growware/feasibility.md)
- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Development Plan](docs/reference/growware/development-plan.md)
- [Test Plan](docs/test-plan.md)
- [Origin Transcript](docs/reference/growware/origin-transcript-2026-04-13.md)
