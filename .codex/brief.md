# Project Brief

## Delivery Tier
- Tier: `medium`
- Why this tier: the repository now has a documentation baseline, but it still requires multiple sessions to move from project definition into a first real pilot loop
- Last reviewed: 2026-04-13

## Outcome

Stand up `Growware` as a document-first baseline for a feedback-driven engine that continuously evolves software from intent, use, and feedback. Preserve the full origin material, correct the public project definition, define the stable system boundary, and prepare the discussion needed to choose the first pilot loop without inventing runtime details too early.

## Scope

- Keep the medium-tier `.codex` control surface aligned with the current discussion stage.
- Preserve the full origin source in `docs/reference/growware/origin.pdf` and extract its project definition into durable Markdown.
- Publish truthful public docs for origin, feasibility, architecture, roadmap, development plan, and test plan.
- Define Stage 1 as a planned long task for `Project 1`, not as runtime implementation.

## Non-Goals

- Picking a runtime, framework, or deployment target before the first pilot loop is explicit.
- Generating app scaffolding before the pilot boundary and `judge` signals are defined.
- Claiming autonomous deployment or production readiness.

## Constraints

- The repository is still pre-implementation.
- The first pilot target, operator path, and real usage path are still undecided.
- The incident, verification, and deployment-approval contracts are still undecided.
- Public docs must stay bilingual and use repository-relative links.

## Definition of Done

- `README*`, `docs/*`, and `docs/reference/growware/*` truthfully describe Growware as a feedback-driven software factory / growth engine.
- `origin.pdf` is recognized as the canonical origin source and `origin*.md` captures the extracted project definition.
- `.codex/brief.md`, `.codex/plan.md`, and `.codex/status.md` stay aligned on the Stage 1 long task as the next slice.
- The old public `auto-software` framing is removed from the active docs.
