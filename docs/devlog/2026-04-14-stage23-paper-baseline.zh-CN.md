# 2026-04-14 Stage 2 And Stage 3 Paper Baseline

[English](2026-04-14-stage23-paper-baseline.md) | [中文](2026-04-14-stage23-paper-baseline.zh-CN.md)

## 问题

仓库虽然已经有 pilot-loop gate、policy source 和 Growware 自身的 daemon-foundation 合同层，但 Stage 2 / Stage 3 仍然分散在 roadmap 级别的 prose 里。

这会留下三类风险：

- 用户要求“把 Stage 3 一口气做完”时，仓库在 documentation mode 下没有一条可真实收口的完成路径
- 后续 runtime 工作只能从分散文字里反推 incident、verification、deployment 和 automation 规则
- 入口文档和 `.codex/*` 容易漂移，并误导成“runtime 已经完成”

## 关键思路

- `AGENTS.md` 仍然把仓库限定在 discussion 和 documentation mode，所以“推到 Stage 3”为真时，只能指向最大真实边界内的 paper-complete 版本。
- 正确形态应当复用 policy source 和 daemon contracts 已建立的模式：文档保持可编辑真相源，本地编译器产出一层机器可读资产。
- Stage 2 / Stage 3 必须拆成更小的合同，review 才能围绕交付边界，而不是围绕一个过宽的 milestone 名字打转。

## 方案

- 新增 `docs/reference/growware/stage-2-3-baseline*`，把 Stage 2 / Stage 3 的 paper-baseline checkpoint 显式落盘。
- 新增 `docs/reference/growware/stage-2-3-contracts/`，作为 incident lifecycle、verification profile、deployment gate、close-out provenance、judge promotion、automation bands、regression assets 的 durable source pack。
- 实现 `scripts/growware_stage23_contract_sync.py`，把这些文档编译进 `.growware/stage-2-3/`，并校验 source 与 machine layer 是否漂移。
- 对齐 README、docs home、roadmap、development plan、test plan、`.codex/*` 和 host views，让它们都指向同一个 paper-baseline checkpoint，同时不把仓库写成 runnable runtime。

## 验证

```bash
python3 scripts/growware_stage23_contract_sync.py --write --json
python3 scripts/growware_stage23_contract_sync.py --check --json
python3 scripts/growware_daemon_contract_sync.py --check --json
python3 scripts/growware_policy_sync.py --check --json
```

## 后续

- 在启动 runtime integration 之前，继续 review Stage 2 / Stage 3 的合同是否过宽或过窄。
- 后续所有修改都继续经过文档 source，并在每次合同修订后重跑三条 sync 脚本。
- 不要把这套 paper baseline 误写成 runtime integration、low-risk automation 或 autonomous deployment 已经存在的证明。
