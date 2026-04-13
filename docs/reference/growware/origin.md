# Growware Origin Summary

[English](origin.md) | [中文](origin.zh-CN.md)

## Source of Truth

- the full origin material is now preserved in [origin.pdf](origin.pdf)
- [origin-transcript-2026-04-13.md](origin-transcript-2026-04-13.md) comes from the share page and is retained only as provenance; it is no longer treated as the full source
- this document is not a verbatim transcript; it is the extracted project definition from the full original conversation

## One-Sentence Definition

Growware is a feedback-driven engine that continuously evolves software from intent, use, and feedback.

In the language of the original conversation, it is also:

- an automatic feedback-driven software system
- a feedback-driven software factory
- a growth engine that "raises" software instead of finishing it once

## What the Project Actually Is

The full origin conversation makes the project definition explicit:

- the `A window` is not a chat box for asking AI to write code; it is the product control console
- the `B window` is not just where humans inspect results; it is the evidence surface of the real world
- the background is not a naked LLM; it is a persistent control plane

That control plane is not only about code edits. It must keep three evolving artifacts aligned:

1. `spec`: what the software should do
2. `judge`: how correctness is decided
3. `code`: the current implementation

So Growware should not be described as a "closed-loop bug-fix tool" or merely a "document-first AI coding project." It is closer to:

- a project-level evolution control system
- a middle control layer attached between OpenClaw, Codex, and the target project
- a system that productizes human judgment into rules, tests, and gates over time

## The Three Core Loops

### 1. Build software

The `A window` expresses intent. The system turns that into specs, boundaries, and acceptance criteria, then implements, verifies, and deploys into the `B window`.

### 2. Repair software

Real use in the `B window` produces logs, failures, anomalies, and behavior drift. The system turns that evidence into incidents, then runs analysis, repair, verification, and deployment.

### 3. Learn software

When the `A window` gives feedback again, the system should not only patch code once. It should also convert that feedback into durable judges, rules, rubrics, regression tests, and constraints.

This loop is why Growware is not just "automatic coding." It is software evolution.

## What It Should Not Become

The most misleading shape would be:

`A window sentence -> LLM edits code -> deploy`

That path is short, but unstable. The full origin conversation repeatedly identifies the missing middle as the `judge layer`.

The more stable path is:

`A window feedback -> update spec / rubric / detector / eval -> edit code -> verify -> deploy`

In other words, teach the system what counts as wrong before asking it to fix things.

## Why the Name Growware Fits

In the naming discussion, `auto-software` was treated as a direction or concept label rather than a strong system name.

`Growware` won because it sounds like a distinct system while preserving the key idea: software is not merely written once; it grows through use and feedback.

The closest Chinese system-level wording in the same discussion was:

- 生长引擎
- a core system that continuously evolves software from intent, use, and feedback

## Direct Constraints On Repository Docs

Based on the full origin conversation, the repository docs should now stay within these boundaries:

- do not describe Growware as only an AI coding assistant
- do not describe it as only an automatic bug-fix daemon
- keep the `A window / B window / hidden control plane` split explicit
- treat `spec / judge / code` as the co-evolving target, not just `code`
- stage the implementation conservatively, but do not narrow the project definition itself
