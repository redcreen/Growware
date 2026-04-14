# Project 1 Policy Source

[English](project-1.md) | [中文](project-1.zh-CN.md)

## Metadata

- id: `project-1.openclaw-task-system.policy-source`
- kind: `project-policy`
- status: `active`
- owners: `growware-maintainers`
- applies_to:
  - `README.md`
  - `README.zh-CN.md`
  - `docs/architecture.md`
  - `docs/architecture.zh-CN.md`
  - `docs/roadmap.md`
  - `docs/roadmap.zh-CN.md`
  - `docs/reference/growware/*`
  - `docs/policy/*`
  - `openclaw-task-system/.growware/`
- effect: `deny-without-approval`

## 规则

Project 1 先锁定为 `openclaw-task-system` pilot。

它的项目 policy 必须始终保留在可 review 的文档中；在任何行为被视为 durable 之前，相关规则都必须先是显式的。

当前默认的人类 ingress、审批和通知面是 `feishu6`。

当前项目级 durable 控制面属于 `openclaw-task-system/.growware/`，而这个仓库的人类可读 policy source 放在 `docs/policy/`。

任何会改变项目 target、channel 绑定、审批边界，或改变 pilot loop 用户可见语义的改动，都必须先经过明确 review，之后才可以当作正式 policy。

## 允许

- 澄清 policy 文案
- 补强让项目规则更易执行的文档
- 保持 policy source 中英文一致
- 未经人类明确变更前，保持 `openclaw-task-system` 为 Project 1
- 未经人类明确变更前，保持 `feishu6` 为默认的人类 ingress / 审批 / 通知路径
- 保持项目 durable 规则落在 `openclaw-task-system/.growware/`

## 禁止

- 未经明确批准就改 Project 1 target
- 未经明确批准就把主 human ingress 从 `feishu6` 移走
- 声称已经具备 autonomous production deployment
- 未经批准就改变 pilot 的用户可见语义
- 把 terminal takeover 当成规则豁免
- 只改聊天里的说法，却不让文档同步

## 需要审批

- 任何 Project 1 target 变更
- 任何 channel 绑定变更
- 任何 deploy / rollback 审批边界变更
- 任何重新定义 daemon-owned 与 terminal-takeover 的变更
- 任何新增默认 pilot surface 或 notification route 的变更

## 验证

- `README` / `roadmap` / `architecture` / `development-plan` / `test-plan` 与这份合同保持一致
- `docs/policy/README.md` 把这份文件列为当前 policy source
- `shared-policy-contract` 仍然说明文档是 source、`.policy/` 是机器层
- 当机器层存在时，执行前必须先做编译一致性检查

## Machine Notes

- 在 `.policy/` 生成之前，这份文档就是项目可读 source
- 编译出来的机器层不能扩大这份文档和 shared contract 允许的范围
