# 项目进展

## 一眼总览
| 问题 | 当前答案 |
| --- | --- |
| 项目 | `Growware` |
| 当前判断 | 当前处于 project-bound readonly executor bridge 的持续推进中。 |
| 当前阶段 | project-bound readonly executor bridge v0 |
| 当前工作域 | readonly project bridge plus machine-layer contracts |
| 当前切片 | `project-bound-readonly-executor-bridge-v0` |
| 当前执行进度 | `4 / 4` |
| 架构信号 | `绿色` |
| 直接价值 | 让 Growware 在不修改目标项目的前提下，第一次真实接到 `openclaw-task-system` 工作区并记录 executor snapshot。 |
| 当前主要风险 | 如果实验层被误写成 `Project 1` 已 live，或者机器层与 source docs 漂移，仓库会重新失真。 |

## 当前定位
| 维度 | 当前状态 | 说明 | 入口 |
| --- | --- | --- | --- |
| 主线状态 | project-bound readonly bridge 已落地 | 当前主线不再只是 isolated mock，而是受限的真实项目只读桥接层 | [路线图](/Users/redcreen/Project/growware/docs/roadmap.zh-CN.md) |
| 当前阶段 | `project-bound-executor-bridge-v0*` 与 `experiments/mock_runtime/*` 已建立 | 入口文档、路线图、开发计划、测试计划和 `.codex/*` 已对齐 | [当前阶段](/Users/redcreen/Project/growware/docs/reference/growware/project-bound-executor-bridge-v0.zh-CN.md) |
| 当前工作域 | project-bound readonly executor bridge | 继续保持 readonly / approval-gated truthfulness | [实验说明](/Users/redcreen/Project/growware/experiments/mock_runtime/README.md) |
| 当前切片 | `project-bound-readonly-executor-bridge-v0` | 下一步是 review bridge、按 source 修订、或显式绑定写能力 executor | [状态](/Users/redcreen/Project/growware/.codex/status.md) |

## 当前这轮到底在做什么
| 当前工作 | 类型 | 对维护者的直接价值 | 当前状态 | 对应任务 |
| --- | --- | --- | --- | --- |
| extend source-of-truth docs and control surface to the readonly bridge boundary | 主线 | 让 repo 真实反映“已批准真实项目只读桥接” | 已完成 | `EL-1` |
| implement readonly target-project bridge commands | 主线 | 让 Growware 首次从真实 Project 1 工作区拿到 executor snapshot | 已完成 | `EL-2` |
| capture bridge snapshots in demo flow and smoke test | 主线 | 让 bridge 行为可重复验证，而不是一次性终端表演 | 已完成 | `EL-3` |
| rerun bridge, runtime, and machine-layer validation | 验证 | 确认 `.growware/*`、`.policy/*`、bridge 和实验层没有彼此打架 | 已完成 | `EL-4` |

## 架构监督
| 项目 | 当前值 |
| --- | --- |
| 信号 | `绿色` |
| 根因假设 | isolated mock runtime 已经够用，但还没有真实项目侧的只读接触面 |
| 正确落层 | 先通过 readonly bridge 验证真实项目感知，再决定何时绑定写能力 executor |
| 升级 Gate | `自动继续` |

## 接下来要做什么
| 下一步 | 为什么做 |
| --- | --- |
| Review `project-bound-executor-bridge-v0*` and `experiments/mock_runtime/*` as the current implementation gate | 这是当前 bridge 层的集中真相 |
| Refine contracts only through the doc source, then rerun all three sync scripts plus bridge/runtime checks | 避免机器层、bridge、实验层和 source docs 分叉 |
| Bind a real write-capable executor only with explicit approval | 当前 runtime 仍然是 readonly bridge，不是写能力接线 |
