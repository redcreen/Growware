# Growware Daemon Boundary Contract

[English](daemon-boundary.md) | [中文](daemon-boundary.zh-CN.md)

## Metadata

- id: `growware.daemon.boundary`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `daemon-boundary`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`
  - `docs/reference/growware/shared-policy-contract.zh-CN.md`

## Purpose

这份合同在继续扩展目标项目执行之前，先固定 Growware daemon 自己的职责边界。

## Owns

- 把 channel 对话归一成 Growware 侧 durable 命令与事件
- 解析一条请求属于哪个已接入项目
- 通过 project capsule 合同读取 durable 项目状态
- 在行动前加载机器可读 policy 与审批规则
- 判断请求属于 `state-only`、`coordination-only`、`executor-required` 或 `approval-wait`
- 组装 progress push、approval request、verification 与 close-out payload
- 在工作解决后产出 learning-writeback proposal

## Does Not Own

- 目标项目业务逻辑
- channel host 的传输层内部实现
- 项目本地运行时实现细节
- 超出批准边界的静默部署
- 靠猜测去重写其他项目路线图

## Decision Rules

- 如果一条请求可以直接由 durable 项目状态回答，就不要把它委派给目标项目
- 如果一条请求需要改仓库、跑验证或部署，就必须先形成 executor handoff record
- 如果审批状态缺失或有歧义，必须停下来请求 review，不能靠猜
- 如果 policy loading 失败，daemon 必须先报告失败，不能继续执行

## Approval Rules

- 改项目绑定、审批边界、执行器权限，都需要明确批准
- deploy 与 rollback 必须服从 project capsule 中声明的 approval boundary
- 把临时人工 workaround 提升为 daemon-owned 行为，必须有可 review 的 writeback

## Machine Notes

- 把这份文档编译成一个带稳定 `id` 的机器合同
- 生成记录时，`owns`、`does_not_own`、`decision_rules`、`approval_rules` 应保持为独立数组
