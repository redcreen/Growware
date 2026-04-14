# 项目助手交接

## 摘要
| 项目 | 当前值 |
| --- | --- |
| 仓库 | `/Users/redcreen/Project/growware` |
| 层级 | `中型` |
| 当前阶段 | Stage 1.5 daemon-contract implementation 已建立 |
| 当前切片 | `growware-self daemon foundation` |
| 当前执行线 | compile Growware's daemon-first control contract into `docs/reference/growware/daemon-contracts/` and `.growware/daemon-foundation/`, then keep docs and machine layers aligned |
| 执行进度 | `4 / 4` |
| 架构信号 | `绿色` |
| 升级 Gate | `自动继续` |
| 当前主要风险 | 如果目标项目扩展再次被误写成 Growware 主线，或 `.growware/daemon-foundation/` 与 source docs 漂移，Growware 自身启动门会失真。 |

## Restore Order
1. `.codex/status.md`
2. `.codex/plan.md`
3. `.codex/brief.md`
4. `docs/reference/growware/daemon-foundation-plan.zh-CN.md`
5. `docs/reference/growware/daemon-contracts/README.zh-CN.md`
6. `docs/roadmap.zh-CN.md`
7. `docs/reference/growware/development-plan.zh-CN.md`
8. `docs/test-plan.zh-CN.md`

## Copy-Paste Commands

### Chinese
```text
项目助手 继续。先读取 .codex/status.md、.codex/plan.md、.codex/brief.md、docs/reference/growware/daemon-foundation-plan.zh-CN.md、docs/reference/growware/daemon-contracts/README.zh-CN.md、docs/roadmap.zh-CN.md、docs/reference/growware/development-plan.zh-CN.md、docs/test-plan.zh-CN.md；然后继续当前执行线：review Growware self daemon contracts, keep `.growware/daemon-foundation/` and `.policy/` aligned to doc source, and do not broaden target-project execution until runtime work is explicitly approved。
```

### English
```text
project assistant continue. Read .codex/status.md, .codex/plan.md, .codex/brief.md, docs/reference/growware/daemon-foundation-plan.md, docs/reference/growware/daemon-contracts/README.md, docs/roadmap.md, docs/reference/growware/development-plan.md, and docs/test-plan.md first; then continue the current execution line: review Growware self daemon contracts, keep `.growware/daemon-foundation/` and `.policy/` aligned to doc source, and do not broaden target-project execution until runtime work is explicitly approved.
```

## Next 3 Actions
1. Review `daemon-contracts/*` and `daemon-foundation-plan*` as the Growware-self implementation gate.
2. Refine contract fields or rules only through the doc source, then rerun both sync scripts.
3. Start runtime integration only with an explicit user decision after the contract pack is approved.
