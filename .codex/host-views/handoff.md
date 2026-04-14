# 项目助手交接

## 摘要
| 项目 | 当前值 |
| --- | --- |
| 仓库 | `/Users/redcreen/Project/growware` |
| 层级 | `中型` |
| 当前阶段 | project-bound readonly executor bridge v0 已建立 |
| 当前切片 | `project-bound-readonly-executor-bridge-v0` |
| 当前执行线 | run and refine the readonly bridge in `experiments/mock_runtime/` while keeping docs and machine layers aligned |
| 执行进度 | `4 / 4` |
| 架构信号 | `绿色` |
| 升级 Gate | `自动继续` |
| 当前主要风险 | 如果实验层被误写成 `Project 1` 已 live，或机器层与 source docs 漂移，仓库会失真。 |

## Restore Order
1. `.codex/status.md`
2. `.codex/plan.md`
3. `.codex/brief.md`
4. `docs/reference/growware/project-bound-executor-bridge-v0.zh-CN.md`
5. `experiments/mock_runtime/README.md`
6. `docs/reference/growware/daemon-foundation-plan.zh-CN.md`
7. `docs/roadmap.zh-CN.md`
8. `docs/reference/growware/development-plan.zh-CN.md`
9. `docs/test-plan.zh-CN.md`

## Copy-Paste Commands

### Chinese
```text
项目助手 继续。先读取 .codex/status.md、.codex/plan.md、.codex/brief.md、docs/reference/growware/project-bound-executor-bridge-v0.zh-CN.md、experiments/mock_runtime/README.md、docs/reference/growware/daemon-foundation-plan.zh-CN.md、docs/roadmap.zh-CN.md、docs/reference/growware/development-plan.zh-CN.md、docs/test-plan.zh-CN.md；然后继续当前执行线：review the readonly project bridge, keep `.growware/stage-2-3/`、`.growware/daemon-foundation/`、`.policy/` and `experiments/mock_runtime/` aligned to doc source, and do not claim Project 1 runtime completion until a write-capable executor is explicitly approved。
```

### English
```text
project assistant continue. Read .codex/status.md, .codex/plan.md, .codex/brief.md, docs/reference/growware/project-bound-executor-bridge-v0.md, experiments/mock_runtime/README.md, docs/reference/growware/daemon-foundation-plan.md, docs/roadmap.md, docs/reference/growware/development-plan.md, and docs/test-plan.md first; then continue the current execution line: review the readonly project bridge, keep `.growware/stage-2-3/`, `.growware/daemon-foundation/`, `.policy/`, and `experiments/mock_runtime/` aligned to doc source, and do not claim Project 1 runtime completion until a write-capable executor is explicitly approved.
```

## Next 3 Actions
1. Review `project-bound-executor-bridge-v0*` and `experiments/mock_runtime/*` as the current implementation gate.
2. Refine contracts only through the doc source, then rerun all three sync scripts plus bridge/runtime checks.
3. Bind a real write-capable executor only with an explicit user decision.
