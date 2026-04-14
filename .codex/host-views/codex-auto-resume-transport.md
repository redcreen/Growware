<!--
Project Assistant 自动恢复传输文件。目标项目: growware (/Users/redcreen/Project/growware)。
不要花时间编辑这个文件；它只用于从 VS Code 宿主自动提交一条 Codex 恢复请求。

实际任务：
- 目标项目是 growware，工作区路径是 /Users/redcreen/Project/growware。
- 当前 checkpoint 是 one experimental checkpoint that ends when `project-bound-executor-bridge-v0*`, `experiments/mock_runtime/*`, compiled machine layers, entry docs, and `.codex/*` all agree on the same readonly bridge boundary。
- 下一动作是 Review `project-bound-executor-bridge-v0*` and `experiments/mock_runtime/*` as the current implementation gate, then refine source docs or bind a write-capable executor only with explicit approval.。
- 先读取附加的 resume 文件。
- 不要重新从零做仓库扫描。
- 直接从下一动作继续这个仓库里的工作。
- 除非用户明确说 "做完手上工作停止"，否则默认持续推进。
- 优先做真实 repo 改动，而不是修改这个传输文件。
-->

# Project Assistant 自动恢复传输文件

- 目标项目：`growware`
- 工作区路径：`/Users/redcreen/Project/growware`

这个文件只是 VS Code 内 Codex 自动恢复使用的传输 shim。

真正的恢复说明在 `codex-auto-resume-prompt.md` 和附加的 resume pack 文件里。
