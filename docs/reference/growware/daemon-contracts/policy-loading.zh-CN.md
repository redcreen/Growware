# Policy Loading And Approval Contract

[English](policy-loading.md) | [中文](policy-loading.zh-CN.md)

## Metadata

- id: `growware.policy-loading.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `policy-loading`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/shared-policy-contract.zh-CN.md`
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义 Growware 在行动前如何加载机器可读项目 policy，并执行审批检查。

## Inputs

- `project_id`：已解析的 project capsule 标识
- `policy_source_docs`：capsule 中携带的人类可读 source 引用
- `policy_machine_manifest`：capsule 中携带的机器层 manifest 引用
- `policy_check_command`：policy 层声明的验证命令或 adapter
- `action_kind`：Growware 正在评估的动作类型
- `approval_boundary`：项目声明的审批边界

## Loading Rules

- 只能从 project capsule 声明的机器层引用加载 policy
- 人类可读 policy source 只作为 review provenance，不应被当成隐式运行时 fallback
- 当新鲜度不确定时，在开始 `executor-required` 工作前先跑声明的 policy check 路径
- 在继续执行前，必须先用已加载 policy 与 approval boundary 评估请求中的 `action_kind`

## Approval Rules

- 如果已加载 policy 把该动作标成 approval-gated，Growware 必须停在 `approval-wait`
- 如果已加载 policy 不能清楚覆盖该动作，Growware 必须请求 review，不能从 chat 记忆里临时发明规则
- 所有审批决定都必须能追溯到 active project capsule 及其当前 policy 引用

## Failure Rules

- 如果机器层 manifest 缺失，就报告 `policy-unavailable` 并停止
- 如果校验失败，就报告失败，不能继续 `executor-required` 工作
- 如果已知 source docs 与机器层发生漂移，必须先 review 再行动

## Machine Notes

- 把 `inputs`、`loading_rules`、`approval_rules`、`failure_rules` 分别编译为独立数组
- 为后续 adapter 保持 `action_kind` 与 `policy-unavailable` 的稳定拼写
