# Growware Feasibility Assessment

[English](feasibility.md) | [中文](feasibility.zh-CN.md)

## Verdict

Growware is feasible as a staged engineering system.

It is not yet feasible as a fully autonomous product. The current gap is not "can an LLM write code" but "does the system have stable judge signals, contracts, and deployment boundaries."

## Why This Direction Is Realistic

- The origin conversation already identifies a stable split between `A window`, `B window`, and a hidden control plane.
- Existing coding agents are strong at reading code, triaging incidents, editing code, and running checks when the task boundary is explicit.
- A local-first pilot keeps secrets, deployment risk, and rollback simpler while the loop is still being proven.
- The project can start from one real pilot instead of solving generalized autonomy on day one.

## What Makes It Hard

- Human expectations are still mostly natural language, not machine-checkable judges.
- Passing local tests is weaker than proving real-world correctness.
- Automatic repair without explicit verification and deployment gates creates new incident risk.
- One successful pilot does not automatically generalize into a multi-project platform.

## Required Entry Conditions Before Implementation

| Condition | Why it matters |
| --- | --- |
| One concrete pilot target | Without a real target, the system boundary stays abstract |
| Clear `A window` and `B window` ownership | Feedback and runtime evidence must not collapse into one channel |
| Structured incident contract | Logs alone are not a stable repair input |
| Verification contract | The system needs a repeatable way to decide whether a fix is acceptable |
| Deployment and rollback boundary | Repair without release safety is not a usable loop |
| Human approval rule for early stages | The project should start as semi-automatic, not fully autonomous |

## Recommended Project Posture

1. Stay local-first before introducing cloud execution.
2. Prove one semi-automatic loop before designing for many targets.
3. Turn repeated human corrections into durable rules, judges, and regression assets.
4. Delay runtime and stack choice until the first pilot object is explicit.

## Decision For This Repository

As of `2026-04-13`, the right move for this repo is:

- preserve the origin transcript in Markdown
- align all active docs to the `Growware` name
- define the first pilot loop before writing runtime code
- keep autonomy claims behind explicit human approval and verification gates

## Source Context

- [origin-transcript-2026-04-13.md](origin-transcript-2026-04-13.md)
- [../../architecture.md](../../architecture.md)
- [../../roadmap.md](../../roadmap.md)
