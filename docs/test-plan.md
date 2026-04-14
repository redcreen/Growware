# Test Plan

[English](test-plan.md) | [中文](test-plan.zh-CN.md)

## Scope and Risk

This test plan verifies the current documentation-first baseline for Growware.

Main risks at this stage:

- the origin conversation is preserved incompletely
- legacy placeholder naming remains in active public docs
- the feasibility judgment overclaims autonomy or implementation readiness
- roadmap, development plan, and `.codex/*` drift away from each other
- the first pilot loop gate stays implicit or split across docs
- Growware's own daemon-first planning line stays vague and target-project work is mistaken for Growware progress
- the daemon contract pack drifts from the generated `.growware/daemon-foundation/` machine layer
- the compiled `.policy/` machine layer drifts from `docs/policy/`

## Acceptance Cases
| Case | Setup | Action | Expected Result |
| --- | --- | --- | --- |
| Origin transcript preservation | Shared conversation has been captured from the share page | Open the archived Markdown transcript | The user-visible conversation is present in durable Markdown files |
| Naming convergence | Public docs were bootstrapped under a placeholder name | Search active docs for the retired placeholder name | Active Growware docs no longer use the old name |
| Feasibility honesty | Feasibility doc exists | Review the verdict and preconditions | The repo states "phased and feasible", not "already autonomous" |
| Architecture consistency | Architecture and roadmap docs exist | Read component boundaries and staged delivery order | `A window`, `B window`, and hidden control plane stay consistent across docs |
| Pilot-loop definition | `reference/growware/pilot-loop-v1.md` exists | Review the implementation gate items | pilot target, operator path, real usage path, incident contract, verification contract, and deployment approval boundary are explicit |
| Daemon-foundation planning | `reference/growware/daemon-foundation-plan.md` exists | Review the daemon-first workstreams and boundaries | Growware's own daemon boundary, project capsule, progress push, and handoff model are explicit before broader project execution |
| Daemon contract pack compile | `reference/growware/daemon-contracts/*` and `scripts/growware_daemon_contract_sync.py` exist | Run the compiler and then validate the generated output | `.growware/daemon-foundation/manifest.json`, `.growware/daemon-foundation/index.json`, provenance, and contract files are generated and match the source docs |
| Control-surface alignment | `.codex/brief.md`, `.codex/plan.md`, and `.codex/status.md` exist | Compare them against roadmap and development plan | The current slice is `growware-self daemon foundation`, not target-project expansion |
| Policy source alignment | `docs/policy/README.md` and `docs/policy/project-1.md` exist | Read the policy source alongside the shared contract | The human-readable policy source is explicit, bilingual, and anchored to Project 1 |
| Policy machine-layer compile | `docs/policy/*` and `scripts/growware_policy_sync.py` exist | Run the compiler and then validate the generated output | `.policy/manifest.json`, `.policy/index.json`, provenance, and rule files are generated and match the source docs |

## Automation Coverage

- `python3 <project-assistant>/scripts/validate_control_surface.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_docs_system.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_public_docs_i18n.py <repo> --format text`
- `python3 scripts/growware_daemon_contract_sync.py --write --json`
- `python3 scripts/growware_daemon_contract_sync.py --check --json`
- `python3 scripts/growware_policy_sync.py --write --json`
- `python3 scripts/growware_policy_sync.py --check --json`
- search active docs for the retired placeholder name and confirm no matches remain
- confirm the active docs do not claim that Stage 2 or Stage 3 are already live
- confirm the daemon contract pack is linked from docs home, the reference pack, and the daemon-foundation plan
- confirm the policy source docs are linked from docs home and the reference pack
- confirm `pilot-loop-v1.md` is linked from the docs entry points
- confirm `daemon-foundation-plan.md` is linked from the docs entry points

## Manual Checks

- Compare the archived transcript against the shared page during review.
- Confirm that the feasibility assessment still reflects the shared conversation instead of future assumptions.
- Confirm that no doc claims a runnable autonomous baseline already exists.
- Confirm that the first pilot loop remains explicitly pre-implementation unless the user has approved Stage 2.
- Confirm that target-project expansion is not described as the current mainline while Growware's own daemon boundary is still under review.
- Confirm that the generated `.growware/daemon-foundation/` files still trace back to the same bilingual source docs.
- Confirm that the generated `.policy/` files still trace back to the same bilingual source docs.

## Test Data and Fixtures

- The archived origin transcript under `docs/reference/growware/`
- The public docs set under `README*` and `docs/*.md`
- The live control surface under `.codex/*`
- The generated daemon machine layer under `.growware/daemon-foundation/*`
- The compiled machine layer under `.policy/*`

## Release Gate

- Passing this test plan means the repo has a truthful discussion baseline.
- It also means the repo can compile and validate its current daemon contract source into `.growware/daemon-foundation/`.
- It also means the repo can compile and validate its current Project 1 policy source into `.policy/`.
- It does not mean runtime implementation or autonomous deployment is ready.
