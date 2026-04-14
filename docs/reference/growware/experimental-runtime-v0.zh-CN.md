# Experimental Runtime V0

[English](experimental-runtime-v0.md) | [中文](experimental-runtime-v0.zh-CN.md)

## 目的

这份文档记录的是纸面基线之后，第一条已经被明确批准的 runtime 步子。

它回答一个很实际的问题：

`当前仓库现在允许做哪类 runtime 工作，哪些东西仍然明确不在范围内？`

## 状态

- status: `active experimental slice`
- last reviewed: `2026-04-14`
- implementation root: `experiments/mock_runtime/`

## 允许范围

- 实现一条仅限本地的 mock runtime
- 直接加载 `.policy/`、`.growware/daemon-foundation/` 和 `.growware/stage-2-3/`
- 通过一条 project-bound readonly executor bridge 接到 `openclaw-task-system`
- 先把控制闭环建成 command intake、project resolution、incident recording、verification、approval wait、approval、close-out
- 所有状态都写进隔离的实验 workspace
- 在接真实 target-project executor 之前，先证明 control-plane flow 本身成立

## 明确不在范围内

- 直接接 `feishu6` 宿主
- 修改真实 `openclaw-task-system` 工作区
- 执行 deploy
- 执行 rollback
- 声称生产就绪
- 声称自治发版

## 当前必须具备的 Runtime 行为

- 支持 `status`、`incident`、`continue`、`approve`、`block`、`close` 这些命令形态
- 按 project-capsule contract 校验实验 capsule
- 在动作决策前先加载 policy 机器层
- 遇到 approval-gated 动作时停住，而不是假装 deploy 已被允许
- 在进入 approval-wait 前，先从真实 Project 1 工作区写下一份 executor snapshot
- 发出结构化的 progress、approval 和 close-out payload
- 在 demo flow 里写出 close-out provenance，并至少落下一条 writeback proposal

## 验证

```bash
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## 退出条件

- mock runtime 能初始化一份隔离 workspace
- demo flow 能记录 incident、走到 `approval-wait`，并在显式 approval 后产出 close-out
- demo flow 不执行 deploy 或 rollback
- 真相源文档与 `.codex/*` 指向同一条实验边界
