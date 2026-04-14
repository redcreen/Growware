# 2026-04-14 Daemon Contract Pack

[English](2026-04-14-daemon-contract-pack.md) | [中文](2026-04-14-daemon-contract-pack.zh-CN.md)

## 问题

Growware 自身主线虽然已经在规划文档里显式化了，但它还没有属于自己的机器可读 daemon 合同层。

这个缺口会带来两类风险：

- 仓库容易再次把目标项目扩展误当成 Growware 自身进展
- 后续 runtime 工作只能从大段 prose 里猜 daemon 边界，而不是加载一套稳定合同包

## 关键思路

- 仓库仍处于 discussion / documentation mode，所以这条长任务不该去猜 runtime 形态，也不该提前脚手架 app 代码。
- 正确桥接方式应当复用 policy source 已经建立的模式：文档保持可编辑真相源，本地脚本把它编译成机器层。
- daemon 边界必须拆成更小的 durable 合同，后续 runtime 才能消费，而不用反复重读一整份规划 memo。

## 方案

- 新增 `docs/reference/growware/daemon-contracts/` 作为 Growware 自身 daemon 合同的 durable source pack。
- 定义七份合同文档，分别覆盖 daemon boundary、project capsule、channel command model、progress push、policy loading、execution handoff、learning writeback。
- 实现 `scripts/growware_daemon_contract_sync.py`，把这些文档编译进 `.growware/daemon-foundation/`，并校验是否漂移。
- 把 README、docs home、roadmap、development plan、test plan、`.codex/*` 和 host views 全部对齐到新的 contract-pack checkpoint。

## 验证

```bash
python3 scripts/growware_daemon_contract_sync.py --write --json
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
```

## 后续

- 在启动 runtime 集成前，继续 review 这些合同字段是不是过宽或过窄。
- 所有修订都继续经过文档 source，再重新跑两条 sync 脚本。
- 不要把这套合同包误当成 Growware runtime 接线已经实现的证明。
