# 项目助手继续

## 现在在哪里
| 项目 | 当前值 |
| --- | --- |
| 层级 | `中型` |
| 当前判断 | 当前处于 Growware 自身合同包实现线的持续推进中。 |
| 当前阶段 | Stage 1.5 daemon-contract implementation 已建立；当前主线先完善 Growware 自身，而不是扩展目标项目。 |
| 当前切片 | `growware-self daemon foundation` |
| 当前执行线 | compile Growware's daemon-first control contract into `docs/reference/growware/daemon-contracts/` and `.growware/daemon-foundation/`, then keep docs and machine layers aligned |
| 执行进度 | `4 / 4` |
| 架构信号 | `绿色` |
| 自动触发 | 当前没有自动触发 |
| 升级 Gate | `自动继续` |
| 当前主要风险 | 如果目标项目扩展再次被误当成 Growware 主线，或者 `.growware/daemon-foundation/` 与 source docs 漂移，仓库会重新失真。 |
| 完整看板 | `项目助手 进展` / `project assistant progress` |

## 接下来先做什么
| 顺序 | 当前要做的事 |
| --- | --- |
| 1 | Review `daemon-contracts/*` and `daemon-foundation-plan*` as the Growware-self implementation gate. |
| 2 | Refine contract fields or rules only through the doc source, then rerun both sync scripts. |
| 3 | Start runtime integration only with an explicit user decision after the contract pack is approved. |

## 当前任务板
| 任务 | 类型 | 状态 |
| --- | --- | --- |
| create `daemon-contracts/*` and make the Growware-self daemon contracts explicit | 主线 | 已完成 |
| implement `scripts/growware_daemon_contract_sync.py` and compile the contract pack into `.growware/daemon-foundation/` | 主线 | 已完成 |
| align README, docs home, roadmap, development plan, test plan, and reference docs to the same contract-pack checkpoint | 主线 | 已完成 |
| rerun daemon and policy machine-layer validation after the contract-pack pass | 主线 | 已完成 |
