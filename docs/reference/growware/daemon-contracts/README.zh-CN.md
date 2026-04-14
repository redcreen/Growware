# Growware Daemon Contract Pack

[English](README.md) | [中文](README.zh-CN.md)

## 目的

这个目录保存 Growware 自身 daemon foundation 的 durable 合同包。

这里的文档是给人 review 的 source of truth；本地机器层会从这些文档编译到 `.growware/daemon-foundation/`。

## 合同列表

- [daemon-boundary.zh-CN.md](daemon-boundary.zh-CN.md)：Growware daemon 自己拥有的职责，以及它明确不应该拥有的职责
- [project-capsule.zh-CN.md](project-capsule.zh-CN.md)：Growware 读取每个接入项目时所依赖的最小项目合同
- [channel-command-model.zh-CN.md](channel-command-model.zh-CN.md)：稳定的 channel 侧命令与事件模型
- [progress-push.zh-CN.md](progress-push.zh-CN.md)：结构化进展、审批、验证结果与 close-out payload 合同
- [policy-loading.zh-CN.md](policy-loading.zh-CN.md)：Growware 在行动前如何加载机器可读项目规则
- [execution-handoff.zh-CN.md](execution-handoff.zh-CN.md)：Growware 何时从自身状态回答、何时委派、何时停下来等待审批
- [learning-writeback.zh-CN.md](learning-writeback.zh-CN.md)：已解决工作如何变成可复用后续资产

## 编译与校验

```bash
python3 scripts/growware_daemon_contract_sync.py --write --json
python3 scripts/growware_daemon_contract_sync.py --check --json
```

## 阅读规则

- 先读 [../daemon-foundation-plan.zh-CN.md](../daemon-foundation-plan.zh-CN.md) 理解当前规划主线
- 当实现需要稳定边界和接口时，再读这个合同包
- 生成出来的 `.growware/daemon-foundation/` 只视为机器可读输出，不是可编辑 source
