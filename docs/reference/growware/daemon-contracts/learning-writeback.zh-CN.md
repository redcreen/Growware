# Learning Writeback Contract

[English](learning-writeback.md) | [中文](learning-writeback.zh-CN.md)

## Metadata

- id: `growware.learning-writeback.v1`
- kind: `daemon-contract`
- status: `active-draft`
- contract_type: `learning-writeback`
- owners:
  - `growware`
- depends_on:
  - `docs/reference/growware/daemon-foundation-plan.zh-CN.md`

## Purpose

这份合同定义一次已解决的工作如何继续沉淀成可复用的 rule、judge 或 regression follow-up，而不是停留在一次性 chat 历史里。

## Proposal Types

- `rule-proposal`：候选可复用行为规则或审批规则
- `judge-proposal`：候选检查项或评估 rubric
- `regression-asset-proposal`：候选测试、回放或 fixture，用于未来预防

## Required Fields

- `proposal_id`：稳定的 proposal 标识
- `project_id`：接入项目标识
- `source_execution`：daemon-owned 或 terminal-takeover 来源
- `problem_summary`：已解决问题的简要描述
- `resolution_summary`：修复或决策的简要描述
- `candidate_asset`：提议沉淀的可复用资产
- `target_surface`：如果被接受，资产应该落在哪个表面
- `evidence_refs`：incident、validation 或 close-out 的支撑引用
- `approval_state`：该 proposal 是否仍需明确 review

## Trigger Rules

- 当一次 human-reported problem 被解决且结果具有复用性时，创建 writeback proposal
- 当一次审批或验证判断开始重复出现时，创建 writeback proposal
- 只有在工作纯机械且没有产生可复用规则时，才跳过 writeback

## Approval Rules

- proposal 只是 review 记录，不是静默生效的 policy
- 把 proposal 提升为 active rule 或 regression state，必须在目标表面被明确接受
- terminal-takeover 解决路径必须保留 provenance，不能假装 daemon 已经拥有了该行为

## Machine Notes

- 把 `proposal_types`、`required_fields`、`trigger_rules`、`approval_rules` 分别编译为独立数组
- 为未来 adapter 保持 proposal type 的稳定拼写
