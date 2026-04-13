# 测试计划

[English](test-plan.md) | [中文](test-plan.zh-CN.md)

## 范围与风险

这份测试计划验证的是 Growware 当前“文档先行”的基线。

当前阶段的主要风险：

- 起源对话保存不完整
- 活跃公开文档里还残留历史占位名
- 可行性判断说得太满，假装已经实现自治
- roadmap、development plan 和 `.codex/*` 之间出现漂移

## 验收用例
| 用例 | 前置条件 | 操作 | 预期结果 |
| --- | --- | --- | --- |
| 起源对话归档 | share 对话已经抓取 | 打开归档后的 Markdown transcript | 用户可见对话完整存在于 durable Markdown 文件中 |
| 命名收敛 | 公开文档最初用过占位名 | 搜索活跃文档里的已退役占位名 | Growware 的活跃文档不再使用旧名字 |
| 可行性判断真实 | feasibility 文档已存在 | 审看 verdict 和进入条件 | 仓库明确表达“分阶段可行”，而不是“已经自治可用” |
| 架构一致性 | architecture 和 roadmap 文档已存在 | 审看组件边界与阶段顺序 | `A 窗口`、`B 窗口` 和隐藏控制面在各文档里保持一致 |
| 控制面对齐 | `.codex/brief.md`、`.codex/plan.md`、`.codex/status.md` 已存在 | 对照 roadmap 和 development plan 审核 | 下一切片是 `pilot-loop definition`，而不是运行时代码实现 |

## 自动化覆盖

- `python3 <project-assistant>/scripts/validate_control_surface.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_docs_system.py <repo> --format text`
- `python3 <project-assistant>/scripts/validate_public_docs_i18n.py <repo> --format text`
- 搜索活跃文档里的历史占位名，并确认已无匹配

## 手工检查

- review 时把归档 transcript 和 share 页面对照一遍
- 确认可行性评估忠实于起点对话，而不是偷跑到未来假设
- 确认没有文档声称当前已经有 runnable baseline

## 测试数据与夹具

- `docs/reference/growware/` 下的起源 transcript
- `README*` 与 `docs/*.md` 构成的公开文档集合
- `.codex/*` 下的实时控制面

## 发布门禁

- 通过这份测试计划，只表示仓库已经具备真实的讨论基线。
- 这不表示运行时代码实现或自动部署已经就绪。
