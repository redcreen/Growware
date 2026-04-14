# Growware Stage 2 And Stage 3 Contract Pack

[English](README.md) | [中文](README.zh-CN.md)

## Purpose

这个目录保存的是 Stage 2 和 Stage 3 paper baseline 的详细 source contracts。

这里的文档是人类可 review 的 source of truth；本地机器层会从这些文档编译到 `.growware/stage-2-3/`。

## Contracts

- [incident-lifecycle.zh-CN.md](incident-lifecycle.zh-CN.md)：incident 如何创建、提升、推进和关闭
- [verification-profile.zh-CN.md](verification-profile.zh-CN.md)：每次修复的 verification record 至少必须带什么
- [deployment-gate.zh-CN.md](deployment-gate.zh-CN.md)：哪些动作必须审批、禁止继续，或只能 rollback
- [close-out-provenance.zh-CN.md](close-out-provenance.zh-CN.md)：close-out 如何保留 provenance 和未完成 follow-up
- [judge-promotion.zh-CN.md](judge-promotion.zh-CN.md)：重复判断如何被提升成 durable judge candidates
- [automation-bands.zh-CN.md](automation-bands.zh-CN.md)：什么情况下只能人工、需要审批，或允许低风险自动处理
- [regression-assets.zh-CN.md](regression-assets.zh-CN.md)：regression assets 如何提议、接受、延期，或明确缺失

## Compile And Validate

```bash
python3 scripts/growware_stage23_contract_sync.py --write --json
python3 scripts/growware_stage23_contract_sync.py --check --json
```

## Reading Rule

- 先读 [../stage-2-3-baseline.zh-CN.md](../stage-2-3-baseline.zh-CN.md) 理解高层边界
- 当实现需要稳定字段和规则时，再读这个合同包
- 生成出来的 `.growware/stage-2-3/` 只是机器可读输出，不是可编辑 source

