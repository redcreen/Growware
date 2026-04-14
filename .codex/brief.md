# Project Brief

## Delivery Tier
- Tier: `medium`
- Why this tier: the repository now has two local machine-layer entrypoints, but it still needs multiple sessions before any real runtime loop is authorized
- Last reviewed: 2026-04-14

## Outcome

Stand up `Growware` as a document-first baseline for a feedback-driven engine that continuously evolves software from intent, use, and feedback. Preserve the full origin material, correct the public project definition, define the stable system boundary, make the Project 1 policy source reviewable in `docs/policy/`, compile that source into `.policy/`, record the first pilot loop explicitly before runtime implementation begins, and turn Growware's own daemon-first control contract into a reviewable contract pack that compiles into `.growware/daemon-foundation/`.

## Scope

- Keep the medium-tier `.codex` control surface aligned with the current discussion stage.
- Preserve the full origin source in `docs/reference/growware/origin.pdf` and extract its project definition into durable Markdown.
- Publish truthful public docs for origin, feasibility, architecture, roadmap, development plan, test plan, and policy source.
- Publish one durable first-pilot-loop spec that covers the implementation gate items.
- Publish one durable daemon-foundation plan that defines Growware's own control boundary, progress-push contract, and project handoff model.
- Publish one durable daemon contract pack under `docs/reference/growware/daemon-contracts/`.
- Keep local compile / validate entrypoints for both `.policy/` and `.growware/daemon-foundation/`.

## Non-Goals

- Picking a runtime, framework, or deployment target before the first pilot loop is explicit.
- Generating app scaffolding before the pilot boundary and `judge` signals are defined.
- Claiming autonomous deployment or production readiness.

## Constraints

- The repository is still pre-runtime and remains in discussion / documentation mode.
- The daemon contract pack is a machine-readable control layer, not proof that Growware runtime wiring is live.
- Runtime execution still does not consume the compiled machine layers directly.
- The incident, verification, and deployment-approval contracts must stay explicit in docs before Stage 2 can start.
- Growware should improve itself before broadening any attached target project's feature work.
- Public docs must stay bilingual and use repository-relative links.

## Definition of Done

- `README*`, `docs/*`, and `docs/reference/growware/*` truthfully describe Growware as a feedback-driven software factory / growth engine in pre-runtime mode.
- `origin.pdf` is recognized as the canonical origin source and `origin*.md` captures the extracted project definition.
- `pilot-loop-v1*` records the first pilot target, paths, contracts, and approval boundary explicitly.
- `daemon-foundation-plan*` records Growware's own daemon boundary, project capsule, progress-push contract, and handoff model explicitly.
- `daemon-contracts/*` records the daemon boundary, capsule, channel, progress, policy-loading, handoff, and learning-writeback contracts explicitly.
- `scripts/growware_daemon_contract_sync.py` compiles and validates that contract pack into `.growware/daemon-foundation/`.
- `.codex/brief.md`, `.codex/plan.md`, and `.codex/status.md` stay aligned on the Growware-self daemon-foundation slice.
- The old public `auto-software` framing is removed from the active docs.
