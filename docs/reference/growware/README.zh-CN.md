# Growware 参考资料包

[English](README.md) | [中文](README.zh-CN.md)

## 目的

这个目录存放 Growware 的长期参考真相源。这里不是实时控制面，而是项目定义、起源材料和阶段性判断的耐久文档层。

## 推荐阅读顺序

- [origin.pdf](origin.pdf)：完整起源对话的 PDF 原件，当前最权威的原始真相源
- [origin-raw-extract.zh-CN.md](origin-raw-extract.zh-CN.md)：从 PDF 直接提取的全文 Markdown 归档，便于人工 review
- [origin.zh-CN.md](origin.zh-CN.md)：从完整起源对话抽象出来的项目定义
- [origin-transcript-2026-04-13.zh-CN.md](origin-transcript-2026-04-13.zh-CN.md)：从分享页抓取的转录稿，只保留作来源痕迹；它已知不完整
- [feasibility.zh-CN.md](feasibility.zh-CN.md)：从项目角度对 Growware 的可行性、风险和进入条件做判断
- [pilot-loop-v1.zh-CN.md](pilot-loop-v1.zh-CN.md)：Project 1 第一条 pilot loop 的定义与实现入口门
- [daemon-foundation-plan.zh-CN.md](daemon-foundation-plan.zh-CN.md)：Growware 自身 daemon-first 规划主线，以及在继续扩展目标项目前必须先补齐的控制合同
- [daemon-contracts/README.zh-CN.md](daemon-contracts/README.zh-CN.md)：把这条规划主线继续落成机器可编译 source docs 的 daemon 合同包
- [stage-2-3-baseline.zh-CN.md](stage-2-3-baseline.zh-CN.md)：把 Stage 2 和 Stage 3 一次补齐到纸面完成、但不伪造 runtime 完成态的总基线
- [stage-2-3-contracts/README.zh-CN.md](stage-2-3-contracts/README.zh-CN.md)：incident、verification、deploy gate、provenance、automation 和 regression assets 的详细 source pack
- [shared-policy-contract.zh-CN.md](shared-policy-contract.zh-CN.md)：人类、`project-assistant`、Growware 共用的 policy 合同，定义当前 pilot 的 `.growware/*` 兼容态、长期 `docs/policy/` -> `.policy/` 目标态、编译责任、执行边界和门禁分层
- [../../policy/README.zh-CN.md](../../policy/README.zh-CN.md)：Project 1 的人类可读 policy source 入口
- [development-plan.zh-CN.md](development-plan.zh-CN.md)：路线图之下的详细执行队列

## 读取原则

- 项目“是什么”，以 `origin.pdf` 和 `origin*.md` 为准
- 项目“现在能不能做”，以 `feasibility*.md` 为准
- 项目“当前先怎么落”，以 `architecture*.md`、`roadmap*.md`、`development-plan*.md`、`pilot-loop-v1*.md`、`daemon-foundation-plan*.md`、`daemon-contracts/*`、`stage-2-3-baseline*.md` 和 `stage-2-3-contracts/*` 为准
