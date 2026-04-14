# Project-Bound Executor Bridge V0

[English](project-bound-executor-bridge-v0.md) | [中文](project-bound-executor-bridge-v0.zh-CN.md)

## 目的

这份文档记录的是 Growware 实验 runtime 现在第一次接到真实项目工作区的 executor bridge。

它回答一个很实际的问题：

`Growware 现在怎么在不直接跳到改代码或 deploy 的前提下，接触真实 Project 1 工作区？`

## 状态

- status: `active experimental bridge`
- last reviewed: `2026-04-14`
- implementation root: `experiments/mock_runtime/runtime.py`

## 当前允许的 Bridge 动作

- 从实验 capsule 里解析真实 `openclaw-task-system` 项目根目录
- 执行 `python3 scripts/runtime/growware_preflight.py --json`
- 执行 `python3 scripts/runtime/growware_openclaw_binding.py --json`
- 通过 `scripts/runtime/growware_project.py` 读取项目摘要
- 把命令结果作为 executor snapshot 落进实验 workspace

## 明确不在范围内

- 带 `--write` 或 `--restart` 的 binding 动作
- 本地 deploy
- rollback
- 修改目标项目文件
- 重启宿主

## 验证规则

只有在所有 readonly 命令都成功退出，且结果被保存在实验 runtime 状态里时，这条 bridge 才算健康。

只要任一 bridge 命令失败：

- incident flow 就必须停住或转成 blocked
- runtime 不得继续推进到 deploy-affecting work
- 失败原因必须保留在 executor snapshot 里

## 验证

```bash
python3 experiments/mock_runtime/runtime.py bridge-status --workspace /tmp/growware-mock-runtime
python3 experiments/mock_runtime/runtime.py demo --workspace /tmp/growware-mock-runtime
python3 -m unittest discover -s experiments/mock_runtime -p 'test_*.py'
```
