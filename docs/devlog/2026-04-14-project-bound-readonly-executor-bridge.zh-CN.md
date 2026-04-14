# 2026-04-14 Project-Bound Readonly Executor Bridge

[English](2026-04-14-project-bound-readonly-executor-bridge.md) | [中文](2026-04-14-project-bound-readonly-executor-bridge.zh-CN.md)

## 问题

隔离的 mock runtime 虽然已经能在本地证明 Growware 的 control flow，但它还没有真正碰到 `Project 1` 的真实工作区。

这让它始终停留在一条完全 synthetic 的 demo 和一条真实 runtime bridge 之间。

## 关键思路

- 下一层 bridge 仍然必须保持 readonly。
- 目标项目已经暴露出安全的 preview / preflight 入口。
- Growware 应该从自己的实验 runtime 里直接调用这些入口，并把结果落成 executor snapshot。

## 方案

- 在 `experiments/mock_runtime/runtime.py` 里新增 project-bound readonly bridge。
- 这条 bridge 现在会调用真实 `openclaw-task-system` 的 project summary、preflight 和 binding preview 入口。
- demo 和 smoke test 现在会验证 Growware 已能在不修改目标项目的前提下碰到真实 Project 1 工作区。

## 验证

```bash
python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```

## 后续

- 在下一次显式批准之前，这条 bridge 继续保持 readonly，不进入 write-capable executor。
- 继续把 executor snapshot 当成 durable provenance 落盘，而不是藏在终端输出里。
