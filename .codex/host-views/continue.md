# 项目助手继续

## 现在在哪里
| 项目 | 当前值 |
| --- | --- |
| 层级 | `中型` |
| 当前判断 | 当前处于 project-bound readonly executor bridge 的持续推进中。 |
| 当前阶段 | Growware 已能通过只读 bridge 接到真实 Project 1 工作区；当前主线是在保持非写入前提下扩展真实 executor 感知。 |
| 当前切片 | `project-bound-readonly-executor-bridge-v0` |
| 当前执行线 | run and refine the readonly project-bound bridge in `experiments/mock_runtime/` while keeping `.growware/*`、`.policy/*` and docs aligned |
| 执行进度 | `4 / 4` |
| 架构信号 | `绿色` |
| 自动触发 | 当前没有自动触发 |
| 升级 Gate | `自动继续` |
| 当前主要风险 | 如果实验层被误写成 `Project 1` 已 live，或者机器层与 source docs 漂移，仓库会重新失真。 |
| 完整看板 | `项目助手 进展` / `project assistant progress` |

## 接下来先做什么
| 顺序 | 当前要做的事 |
| --- | --- |
| 1 | Review `project-bound-executor-bridge-v0*` and `experiments/mock_runtime/*` as the current implementation gate. |
| 2 | Refine contracts only through the doc source, then rerun all three sync scripts plus bridge/runtime checks. |
| 3 | Bind a real write-capable executor only with an explicit user decision. |

## 当前任务板
| 任务 | 类型 | 状态 |
| --- | --- | --- |
| extend source-of-truth docs and control surface to the project-bound readonly executor bridge boundary | 主线 | 已完成 |
| implement readonly target-project bridge commands in `experiments/mock_runtime/` | 主线 | 已完成 |
| capture bridge snapshots in the demo flow and smoke test | 主线 | 已完成 |
| rerun bridge, runtime, and machine-layer verification | 验证 | 已完成 |
