# 测试计划

[English](test-plan.md) | [中文](test-plan.zh-CN.md)

## 范围与风险

这份测试计划验证的是 Growware 当前“文档先行”的基线。

当前阶段的主要风险：

- 起源对话保存不完整
- 活跃公开文档里还残留历史占位名
- 可行性判断说得太满，假装已经实现自治
- roadmap、development plan 和 `.codex/*` 之间出现漂移
- 第一条 pilot loop 的进入门仍然隐含在聊天里，没有集中落盘
- Growware 自身 daemon-first 主线仍然含糊不清，导致目标项目工作被误读成 Growware 本体进展
- daemon contract pack 与生成出来的 `.growware/daemon-foundation/` 机器层发生漂移
- 编译后的 `.policy/` 机器层与 `docs/policy/` 漂移

## 验收用例
| 用例 | 前置条件 | 操作 | 预期结果 |
| --- | --- | --- | --- |
| 起源对话归档 | share 对话已经抓取 | 打开归档后的 Markdown transcript | 用户可见对话完整存在于 durable Markdown 文件中 |
| 命名收敛 | 公开文档最初用过占位名 | 搜索活跃文档里的已退役占位名 | Growware 的活跃文档不再使用旧名字 |
| 可行性判断真实 | feasibility 文档已存在 | 审看 verdict 和进入条件 | 仓库明确表达“分阶段可行”，而不是“已经自治可用” |
| 架构一致性 | architecture 和 roadmap 文档已存在 | 审看组件边界与阶段顺序 | `A 窗口`、`B 窗口` 和隐藏控制面在各文档里保持一致 |
| Pilot Loop 定义 | `reference/growware/pilot-loop-v1.zh-CN.md` 已存在 | 审看实现入口门条目 | pilot target、operator path、real usage path、incident contract、verification contract 与 deployment approval boundary 都已显式写出 |
| Daemon Foundation 规划 | `reference/growware/daemon-foundation-plan.zh-CN.md` 已存在 | 审看 daemon-first 工作流和边界 | Growware 自身的 daemon 边界、project capsule、progress push 与 handoff model 都已在扩展目标项目之前显式写出 |
| Daemon contract pack 编译 | `reference/growware/daemon-contracts/*` 与 `scripts/growware_daemon_contract_sync.py` 已存在 | 先运行编译，再校验产物 | `.growware/daemon-foundation/manifest.json`、`.growware/daemon-foundation/index.json`、provenance 与 contract 文件被生成且与 source 文档一致 |
| 控制面对齐 | `.codex/brief.md`、`.codex/plan.md`、`.codex/status.md` 已存在 | 对照 roadmap 和 development plan 审核 | 当前切片已经切到 `growware-self daemon foundation`，而不是直接去扩展目标项目 |
| Policy source 对齐 | `docs/policy/README.md` 和 `docs/policy/project-1.md` 已存在 | 把 policy source 与 shared contract 一起阅读 | 人类可读 policy source 已显式存在，且中英文成对并锚定 Project 1 |
| Policy 机器层编译 | `docs/policy/*` 与 `scripts/growware_policy_sync.py` 已存在 | 先运行编译，再校验产物 | `.policy/manifest.json`、`.policy/index.json`、provenance 与 rule 文件被生成且与 source 文档一致 |

## 自动化覆盖

- `python3 <project-assistant>/scripts/validate_control_surface.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_docs_system.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_public_docs_i18n.py <repo> --format text`
- `python3 scripts/growware_daemon_contract_sync.py --write --json`
- `python3 scripts/growware_daemon_contract_sync.py --check --json`
- `python3 scripts/growware_policy_sync.py --write --json`
- `python3 scripts/growware_policy_sync.py --check --json`
- 搜索活跃文档里的历史占位名，并确认已无匹配
- 确认活跃文档没有把 Stage 2 或 Stage 3 写成已经上线
- 确认 daemon contract pack 已从 docs 首页、reference pack 和 daemon-foundation plan 可见地链接出去
- 确认 policy source 文档已从 docs 首页和 reference pack 可见地链接出去
- 确认 `pilot-loop-v1.zh-CN.md` 已从入口文档能直接点到
- 确认 `daemon-foundation-plan.zh-CN.md` 已从入口文档能直接点到

## 手工检查

- review 时把归档 transcript 和 share 页面对照一遍
- 确认可行性评估忠实于起点对话，而不是偷跑到未来假设
- 确认没有文档声称当前已经有 runnable autonomous baseline
- 确认在你明确批准 Stage 2 之前，第一条 pilot loop 仍然被写成实现前状态
- 确认在 Growware 自身 daemon 边界完成 review 之前，没有把目标项目扩展写成当前主线
- 确认生成出来的 `.growware/daemon-foundation/` 仍然能追溯回同一组中英文 source 文档
- 确认生成出来的 `.policy/` 仍然能追溯回同一组中英文 source 文档

## 测试数据与夹具

- `docs/reference/growware/` 下的起源 transcript
- `README*` 与 `docs/*.md` 构成的公开文档集合
- `.codex/*` 下的实时控制面
- `.growware/daemon-foundation/*` 下的 daemon 机器层产物
- `.policy/*` 下的机器层产物

## 发布门禁

- 通过这份测试计划，只表示仓库已经具备真实的讨论基线。
- 这也表示仓库已经能把当前 daemon contract source 编译并校验进 `.growware/daemon-foundation/`。
- 这也表示仓库已经能把当前 Project 1 policy source 编译并校验进 `.policy/`。
- 这不表示运行时代码实现或自动部署已经就绪。
