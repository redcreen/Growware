# Test Plan

[English](test-plan.md) | [中文](test-plan.zh-CN.md)

## Scope and Risk

This test plan verifies the current documentation-first baseline for Growware.

Main risks at this stage:

- the origin conversation is preserved incompletely
- legacy placeholder naming remains in active public docs
- the feasibility judgment overclaims autonomy or implementation readiness
- roadmap, development plan, and `.codex/*` drift away from each other

## Acceptance Cases
| Case | Setup | Action | Expected Result |
| --- | --- | --- | --- |
| Origin transcript preservation | Shared conversation has been captured from the share page | Open the archived Markdown transcript | The user-visible conversation is present in durable Markdown files |
| Naming convergence | Public docs were bootstrapped under a placeholder name | Search active docs for the retired placeholder name | Active Growware docs no longer use the old name |
| Feasibility honesty | Feasibility doc exists | Review the verdict and preconditions | The repo states "phased and feasible", not "already autonomous" |
| Architecture consistency | Architecture and roadmap docs exist | Read component boundaries and staged delivery order | `A window`, `B window`, and hidden control plane stay consistent across docs |
| Control-surface alignment | `.codex/brief.md`, `.codex/plan.md`, and `.codex/status.md` exist | Compare them against roadmap and development plan | The next slice is `pilot-loop definition`, not runtime implementation |

## Automation Coverage

- `python3 <project-assistant>/scripts/validate_control_surface.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_docs_system.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_public_docs_i18n.py <repo> --format text`
- search active docs for the retired placeholder name and confirm no matches remain

## Manual Checks

- Compare the archived transcript against the shared page during review.
- Confirm that the feasibility assessment still reflects the shared conversation instead of future assumptions.
- Confirm that no doc claims a runnable baseline already exists.

## Test Data and Fixtures

- The archived origin transcript under `docs/reference/growware/`
- The public docs set under `README*` and `docs/*.md`
- The live control surface under `.codex/*`

## Release Gate

- Passing this test plan means the repo has a truthful discussion baseline.
- It does not mean runtime implementation or autonomous deployment is ready.
