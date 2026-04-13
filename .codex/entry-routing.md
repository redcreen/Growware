# Entry Routing

## Current Entry Direction

- Direction: `shared front door with repo-local durable state`
- Status: `active`
- Why Now: this repo has just been bootstrapped, so `继续 / 进展 / 交接` should resume from the shared `project-assistant` front door and read this repo's `.codex/*` state instead of reconstructing progress from chat memory.

## Entry Routing Contract

- `继续 / 进展 / 交接` must route through one shared front door before reading repo state.
- The front door must run version preflight against `.codex/control-surface.json` before it trusts `status.md` or `plan.md`.
- This repo currently owns durable state only; the front-door implementation lives in the shared `project-assistant` skill scripts, not in repo-local wrappers.
- The first screen for `continue / progress / handoff` should stay structured, not fall back to free-form prose.
- If this repo later adds a local CLI or automation wrapper, it should call the same shared front door rather than reimplementing the flow.

## Front Door Layers

| Layer | Current Implementation | Responsibility |
| --- | --- | --- |
| natural-language routing | `project-assistant` skill entry | Route `项目助手 继续 / 进展 / 交接` to the same shared front door |
| canonical tool front door | shared `project_assistant_entry.py` workflow | Normalize mode selection, run preflight, and dispatch to the right structured backend |
| mode backends | shared `continue_entry.py` / `progress_entry.py` / `handoff_entry.py` workflows | Render the first structured panel for each mode |
| durable repo state | `.codex/*` in this repo | Provide the truth source that the shared front door reads |

## Preflight Contract

| Mode | Preflight Rule | Why |
| --- | --- | --- |
| `continue` | verify the control-surface version first, then resume the active slice | avoid resuming from stale `.codex` structure |
| `progress` | verify the control-surface version first, then render the dashboard | avoid showing maintainers an out-of-date progress surface |
| `handoff` | verify the control-surface version first, then generate the resume pack | avoid carrying forward stale recovery instructions |

## Structured Output Contract

| Mode | First Output Must Be | Not Allowed First |
| --- | --- | --- |
| `continue` | structured continue snapshot | free-form prose summary |
| `progress` | structured maintainer dashboard | only a narrative paragraph |
| `handoff` | structured, copyable handoff panel | scattered recovery notes |

## Host / Tool Bridge Boundary

| Boundary | Repo Owns Today | Future Bridge |
| --- | --- | --- |
| tool-shaped entry | shared `project-assistant` front door | an optional repo-local wrapper may call the same shared entry later |
| business logic | shared skill-side entry scripts | vendor locally only if the repo intentionally adopts its own assistant runtime |
| durable truth | `.codex/*` files in this repo | stays repo-local regardless of host or wrapper choice |

## Next Entry Checks

1. On the next `项目助手 继续 / 进展 / 交接`, confirm the shared front door reads this repo's `.codex/control-surface.json` before rendering output.
2. If a repo-local CLI is added later, make it call the same shared front door instead of duplicating resume logic.
3. Keep structured first-screen behavior aligned with future control-surface changes in this repo.
