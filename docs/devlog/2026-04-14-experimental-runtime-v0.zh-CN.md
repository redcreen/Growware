# 2026-04-14 Experimental Runtime V0

[English](2026-04-14-experimental-runtime-v0.md) | [中文](2026-04-14-experimental-runtime-v0.zh-CN.md)

## 问题

仓库的纸面合同已经足够启动 runtime 工作，但还没有任何一层可执行实现会直接消费编译后的机器层。

这让“已批准合同”和“可执行行为”之间始终隔着一层空白。

## 关键思路

- 用户已经显式批准实现，所以继续把仓库维持在 paper-only mode 反而不真实。
- 第一条 runtime 仍然必须保持隔离、本地、approval-gated。
- 最安全的桥接方式是做一个零依赖 mock runtime，直接加载 `.policy/`、`.growware/daemon-foundation/` 和 `.growware/stage-2-3/`。

## 方案

- 把仓库边界从 paper-only mode 切到 experimental runtime foundation mode。
- 新增 `docs/reference/growware/experimental-runtime-v0*`，把已批准的 runtime 边界写实。
- 实现 `experiments/mock_runtime/`，作为本地 CLI harness 和 smoke-test 目标。
- 在保持 deploy / rollback 明确不在范围内的前提下，先把 incident、verification、approval、close-out、writeback 这条 flow 跑起来。

## 验证

```bash
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## 后续

- 只有在下一次显式批准后，才把这条 synthetic mock executor path 换成真实 project-bound executor。
- 继续让实验 runtime 直接消费编译后的机器层，不要再退回从 prose 猜规则。
- 不要把这套 harness 误写成 `Project 1` 的 deploy 接线已经真实落地。
