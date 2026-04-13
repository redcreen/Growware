# Growware Feasibility Assessment

[English](feasibility.md) | [中文](feasibility.zh-CN.md)

## Verdict

Growware is feasible as a feedback-driven software factory or growth engine.

What is feasible now is a staged, project-level, local-first path with human gates.  
What is not feasible now is skipping `judge`, verification, and deployment boundaries and pretending that a fully autonomous software system already exists.

## What This Project Is Actually Building

The full origin conversation shows that Growware is not trying to add yet another coding agent. It is trying to add the missing project-level control plane that:

- structures intent, feedback, and judgment from the `A window`
- turns real runtime behavior and logs from the `B window` into actionable evidence
- evolves `spec / judge / code` together
- productizes human judgment into detectors, rubrics, regression tests, and deployment gates

So Growware is not:

- a replacement for OpenClaw
- a replacement for Codex
- only an automatic bug-fix daemon

It is better understood as the middle control layer between OpenClaw, Codex, and the target project.

## Why This Direction Is Realistic

- The origin discussion already defines the system clearly: `A window`, `B window`, hidden control plane, and the co-evolution of `spec / judge / code`.
- OpenClaw is a strong fit for channels, gateway behavior, plugins, hooks, and task infrastructure.
- Codex is a strong fit for controlled execution: read code, patch code, run checks, and produce repair output.
- A local-first pilot keeps the real logs, workspace, and deployment boundary close while the loop is still being proven.
- The project can first prove the three loops of building, repairing, and learning software on one real target before aiming for a generalized platform.

## What Makes It Hard

- The hardest problem is not whether an LLM can write code; it is who provides a stable error signal.
- Real-world correctness has at least three layers: runtime correctness, behavioral correctness, and business correctness. The latter two are weaker than local tests alone.
- If the system only edits `code` and does not evolve `judge` and `spec`, it will repeat the same classes of mistakes.
- If human feedback becomes one-off patches instead of durable rules and regression assets, Growware never develops a real learning loop.
- One successful pilot does not automatically become a multi-project operating system.

## Required Entry Conditions Before Implementation

| Condition | Why it matters |
| --- | --- |
| One real pilot object | Without a real target, `A/B` and runtime evidence stay abstract |
| Clear `A window` definition | The project must know who provides requirements, feedback, and approvals |
| Clear `B window` definition | The project must know where real use and evidence come from |
| A minimal `judge` contract | Without "what counts as wrong," the repair loop is unstable |
| Verification and regression contract | The system needs a repeatable way to know whether the fix is better |
| Deployment and rollback boundary | Automatic repair without release safety is automatic risk creation |
| Early-stage human judgment rules | The system should start semi-automatic, not pretend to be fully autonomous |

## Most Important Decision For This Repository

As of `2026-04-13`, the next correct move for this repository is not runtime code. It is to describe the project truthfully:

- treat [origin.pdf](origin.pdf) as the full source of truth
- correct the docs from "document-first closed-loop repair project" to "feedback-driven software factory / growth engine"
- keep Growware scoped to the project-level control layer instead of rewriting OpenClaw or Codex
- avoid locking the daemon shape, runtime, or multi-project bus before the first pilot is explicit

## Recommended Project Posture

1. Stay local-first before introducing cloud parallelism.
2. Prove one semi-automatic loop before widening autonomy.
3. Turn human feedback into `judge`, rules, and regression assets before claiming that software can "grow itself."
4. Start with one project or plugin before expanding into a multi-project platform.

## Current Concrete Viability Call

Given the current discussion, this default shape is reasonable:

- `Project 1 = openclaw-task-system`
- `feishu6` is the single default human feedback, approval, and notification entry for stage 1
- `Telegram` is kept as a fallback channel rather than the primary pilot surface
- all usage channels with `task system` mounted by default are treated as the runtime surface
- project-level durable rules and contracts live in `.growware/` at the target project root

This is a sensible default because it:

- narrows human judgment to one surface first
- keeps the real usage surface separate from the judgment surface
- aligns project-level control with the project repository for Git review and versioning
- keeps the Growware repository focused on architecture and method instead of replacing per-project control planes

## Source Context

- [origin.pdf](origin.pdf)
- [origin.md](origin.md)
- [../../architecture.md](../../architecture.md)
- [../../roadmap.md](../../roadmap.md)
