# Project Brief

## Delivery Tier
- Tier: `medium`
- Why this tier: the repository now has three local machine-layer entrypoints, but it still needs multiple sessions before any real runtime loop is authorized
- Why this tier: the repository now has machine-layer contracts plus one isolated experimental runtime, but it still needs multiple sessions before any real target-project loop is authorized
- Last reviewed: 2026-04-14

## Outcome

Stand up `Growware` as a truthful documentation-first control layer plus one isolated experimental runtime. Preserve the full origin material, correct the public project definition, define the stable system boundary, make the Project 1 policy source reviewable in `docs/policy/`, compile that source into `.policy/`, record the first pilot loop explicitly, turn Growware's own daemon-first control contract into a reviewable contract pack compiled into `.growware/daemon-foundation/`, close Stage 2 and Stage 3 on paper through a reviewable source pack compiled into `.growware/stage-2-3/`, implement a local mock runtime under `experiments/mock_runtime/`, and bridge that runtime into the real Project 1 workspace only through readonly executor commands without claiming production readiness.

## Scope

- Keep the medium-tier `.codex` control surface aligned with the current discussion stage.
- Preserve the full origin source in `docs/reference/growware/origin.pdf` and extract its project definition into durable Markdown.
- Publish truthful public docs for origin, feasibility, architecture, roadmap, development plan, test plan, and policy source.
- Publish one durable first-pilot-loop spec that covers the implementation gate items.
- Publish one durable daemon-foundation plan that defines Growware's own control boundary, progress-push contract, and project handoff model.
- Publish one durable daemon contract pack under `docs/reference/growware/daemon-contracts/`.
- Publish one durable Stage 2 and Stage 3 paper baseline under `docs/reference/growware/stage-2-3-baseline*`.
- Publish one durable Stage 2 and Stage 3 contract pack under `docs/reference/growware/stage-2-3-contracts/`.
- Keep local compile / validate entrypoints for `.policy/`, `.growware/daemon-foundation/`, and `.growware/stage-2-3/`.
- Implement one isolated experimental runtime under `experiments/mock_runtime/`.
- Implement one project-bound readonly executor bridge under `experiments/mock_runtime/`.

## Non-Goals

- Expanding the experimental runtime into a production claim or live target-project binding.
- Claiming autonomous deployment or production readiness.

## Constraints

- The repository now allows only one isolated experimental runtime path under `experiments/mock_runtime/`.
- The runtime may call the real Project 1 workspace only through readonly bridge commands.
- The daemon contract pack and the Stage 2/3 pack are machine-readable control layers, not proof that Project 1 runtime wiring is live.
- The experimental runtime must not execute deploy or rollback and must keep production claims out of scope.
- Public docs must stay bilingual and use repository-relative links.

## Definition of Done

- `README*`, `docs/*`, and `docs/reference/growware/*` truthfully describe Growware as a feedback-driven software factory / growth engine in pre-runtime mode.
- `origin.pdf` is recognized as the canonical origin source and `origin*.md` captures the extracted project definition.
- `pilot-loop-v1*` records the first pilot target, paths, contracts, and approval boundary explicitly.
- `daemon-foundation-plan*` and `daemon-contracts/*` record Growware's own daemon boundary, capsule, channel, progress, policy-loading, handoff, and learning-writeback contracts explicitly.
- `stage-2-3-baseline*` and `stage-2-3-contracts/*` record the incident, verification, deploy, provenance, judge, automation-band, and regression-asset contracts explicitly.
- `scripts/growware_daemon_contract_sync.py` compiles and validates `.growware/daemon-foundation/`.
- `scripts/growware_stage23_contract_sync.py` compiles and validates `.growware/stage-2-3/`.
- `scripts/growware_policy_sync.py` compiles and validates `.policy/`.
- `experiments/mock_runtime/` consumes the compiled machine layers and exposes a reproducible local demo flow.
- `.codex/brief.md`, `.codex/plan.md`, and `.codex/status.md` stay aligned on the experimental runtime slice.
- The old public `auto-software` framing is removed from the active docs.
