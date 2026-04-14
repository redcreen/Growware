# Policy 源

[English](README.md) | [中文](README.zh-CN.md)

## 目的

这个目录是 Growware Project 1 的人类可读 policy source。

`docs/reference/growware/shared-policy-contract.zh-CN.md` 负责定义这些文档应该如何编写、编译和执行。

## 当前 source 集

- [project-1.zh-CN.md](project-1.zh-CN.md)：`openclaw-task-system` 的初始 policy source

## 使用方式

1. 先读 shared policy contract。
2. 保持中英文 policy 文件同步。
3. 把这些文档当成经过 review 的项目规则源。
4. 用 `python3 scripts/growware_policy_sync.py --write --json` 把它们编译进 `.policy/`。
5. 用 `python3 scripts/growware_policy_sync.py --check --json` 校验机器层是否和文档保持一致。

## 编译与校验

```bash
python3 scripts/growware_policy_sync.py --write --json
python3 scripts/growware_policy_sync.py --check --json
```

## 阅读顺序

- [../reference/growware/shared-policy-contract.zh-CN.md](../reference/growware/shared-policy-contract.zh-CN.md)
- [project-1.zh-CN.md](project-1.zh-CN.md)
