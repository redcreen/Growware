# 共享 Policy 合同

[English](shared-policy-contract.md) | [中文](shared-policy-contract.zh-CN.md)

## 目的

这份文档是 `人类`、`project-assistant`、`Growware` 三方共同遵守的合同。

它回答 5 个问题：

1. 项目规则到底归谁管
2. 人类应该把规则写在哪里
3. `project-assistant` 应该把这些规则编译成什么
4. Growware / daemon / terminal takeover 应该如何读取和执行这些规则
5. 如何在不把系统拖慢到不可用的前提下，把规则接到门禁上

这份文档本身不是运行时配置文件，但它定义了运行时配置文件应该如何存在、如何生成、如何校验、如何执行。

## 适用对象

- `人类`：项目 owner、维护者、产品负责人、批准者
- `project-assistant`：负责项目治理、文档治理、控制面、通用 gate 编排的上游系统
- `Growware`：负责 feedback intake、执行、验证、部署、通知的项目级闭环执行层
- `terminal takeover`：Codex 在终端中临时接管执行时，也必须遵守本合同

## 本仓库的当前落地方式

在 Growware 仓库里，第一层 policy source 放在 `docs/policy/`。

当前最小 source 集是：

- `docs/policy/README.md`
- `docs/policy/project-1.md`
- `docs/policy/README.zh-CN.md`
- `docs/policy/project-1.zh-CN.md`

这个仓库把这些文档当成 Project 1 的人类可读规则源。
同一份 source 现在可以通过 `python3 scripts/growware_policy_sync.py --write --json` 本地编译进 `.policy/`，并通过 `python3 scripts/growware_policy_sync.py --check --json` 做一致性校验。
Growware 应该读取编译后的机器层，而不是在运行时自己发明新规则。

## 当前遇到的问题

这份合同不是凭空设计出来的，而是为了解决当前已经真实出现的问题。

### 问题 1：执行器可能改了项目不该改的东西

项目里本来已经通过文档形成了约定，例如：

- 某些用户可见交互是稳定资产
- 某些行为允许修 bug，但不允许改语义
- 某些改动必须先走审批

但如果执行器只靠即时上下文判断，就可能在没有重新完整理解项目约定的情况下直接改掉这些行为。

### 问题 2：daemon 和记忆到的规则，不等于 terminal takeover 会天然遵守

项目运行一段时间后，daemon 可能已经通过 `.growware/`、测试、运行时规则沉淀了一部分能力。

但如果终端里的 Codex 接管执行，而没有受到同一套规则约束，就会出现：

- daemon 会遵守项目约定
- terminal takeover 却可能偏离项目约定

这会导致系统行为不一致。

### 问题 3：全文重读文档太慢，也不稳定

如果每次改代码前都要求执行器重新阅读整仓文档，会有两个问题：

- 太慢
- 仍然可能漏读关键约束

所以项目需要一个既来源于文档、又适合机器快速执行的中间层。

### 问题 4：规则必须属于项目，而不是属于某个工具

即使未来没有 Growware，项目也仍然需要：

- 防止乱改
- 在改动前校验边界
- 对文档与规则保持一致性

因此规则不能绑定到某个执行器品牌上，而必须绑定到项目本身。

## 这轮讨论的收敛过程

这份合同基于下面这组讨论结论收敛而来：

1. `project-assistant` 和 Growware 的职责不能混在一起  
   `project-assistant` 负责治理框架，Growware 负责执行闭环。

2. `哪些能改，哪些不能改` 不能由 Growware 自己解释  
   否则执行器会同时拥有执行权和立法权。

3. 规则内容应该属于项目  
   即使没有 Growware，项目也要有能力通过规则阻止乱改。

4. 人类不会直接维护机器 JSON  
   人类主要通过文档表达规则。

5. 机器不能直接啃全文文档  
   所以项目需要一个明确的机器 policy 执行层。

6. `project-assistant` 最适合承担“从文档编译 policy”的工作  
   因为它本来就负责项目治理、文档治理和通用 gate 编排。

7. Growware、daemon、terminal takeover 都必须执行同一套“当前有效机器 policy 层”
   不能出现“daemon 遵守、人工接管不遵守”的分裂状态。

## 最终决定

这轮讨论后，三方共同接受下面这些决定：

### 决定 1：规则内容归项目所有

规则不是 Growware 的私有配置，也不是 `project-assistant` 的全局常量。

规则属于 `目标项目`，并跟随项目 Git 管理。

### 决定 2：文档是人类真相源

人类通过项目文档表达规则。

推荐把规则型文档集中放在：

```text
docs/policy/
```

### 决定 3：项目需要一层“当前有效机器 policy 层”

机器执行层不取代文档，它是执行器在运行时真正加载的项目本地规则层。

允许两种形态：

- 当前 pilot 兼容态：`.growware/contracts/`、`.growware/policies/`、`.growware/ops/`
- 长期目标态：由 `docs/policy/` 编译出来的 `.policy/`

Growware、daemon、terminal takeover 在任一时刻都必须执行当前项目的同一套“当前有效机器 policy 层”。

### 决定 4：`project-assistant` 负责规范化落地

`project-assistant` 负责：

- 规范 policy 文档格式
- 从文档提炼规则
- 编译 `.policy/`
- 做一致性校验
- 把规则接入通用 gate

### 决定 5：Growware 只是执行器

Growware 负责：

- 读取 `.policy/`
- 判断是否允许执行
- 执行、验证、部署、通知

Growware 不负责最终解释项目规则。

### 决定 6：terminal takeover 不拥有规则豁免权

只要进入项目执行面，无论是 daemon 还是终端接管，都必须服从同一套 `.policy/`。

## 每个角色如何工作

### 人类

人类的工作方式是：

- 在文档中定义规则
- review 和批准规则变化
- 判断重大业务 tradeoff
- 不直接手工维护机器 policy 层

### `project-assistant`

`project-assistant` 的工作方式是：

- 读取项目文档中的 policy source
- 将规则抽象成稳定结构
- 生成或刷新当前有效机器 policy 层
- 检查文档与机器 policy 是否一致
- 把当前有效机器 policy 层变成可执行 gate 输入

### Growware

Growware 的工作方式是：

- 根据当前任务和 touched scope 读取当前有效机器 policy 层
- 决定这次执行是 `allow`、`deny` 还是 `require-approval`
- 按规则执行代码修改、验证、部署、通知
- 在 close-out 中说明命中的规则和执行来源

### terminal takeover

terminal takeover 的工作方式是：

- 接管时先读当前有效机器 policy 层
- 不允许跳过禁止项
- 不允许跳过审批项
- 执行结束后明确说明：这是 `terminal-takeover`，以及哪些能力已回灌

## 核心原则

### 1. 规则属于项目，不属于执行器

`哪些能改，哪些不能改`，归 `目标项目` 所有。

它们不是 Growware 的内部偏好，不是 `project-assistant` 的全局固定常量，也不是某一轮对话里的临时约定。

### 2. 人类只与文档交互

最终输入源始终是 `人类`。

但人类主要修改的是 `文档`，不是 `.policy/` 里的机器文件。

### 3. 当前有效机器 policy 层是执行真相源

给人看的规则，放在 `docs/`。

给机器执行的规则，放在当前有效机器 policy 层。

当前 pilot 兼容态使用的是 `.growware/contracts/`、`.growware/policies/`、`.growware/ops/`。

长期目标态则是 `docs/policy/` 加上编译后的 `.policy/`。

Growware、daemon、terminal takeover 都只应把当前有效机器 policy 层当作运行时约束输入，而不是直接靠全文阅读整仓文档做即时判断。

### 4. `project-assistant` 负责文档到 policy 的规范化落地

`project-assistant` 负责：

- 定义文档中的 policy source 应如何书写
- 从文档提炼和编译当前有效机器 policy 层
- 校验文档与机器 policy 是否一致
- 将 `.policy/` 接入通用 gate 框架

### 5. Growware 只执行，不立法

Growware 负责执行项目规则，不负责自创项目规则。

如果 Growware 认为某条规则需要变化，它只能：

- 产出提案
- 修改文档草案
- 等待人类批准

在批准前，Growware 不得把“建议”当成“已生效规则”。

## 真相源分层

从高到低，真相源分成 4 层：

1. `人类批准`
2. `项目文档中的 policy source`
3. 当前有效机器 policy 层
4. `运行时状态`

解释：

- `人类批准` 决定规则是否成立
- `文档` 负责让人类可读、可 review、可维护
- 当前有效机器 policy 层负责让机器可执行、可校验、可 gate
- `运行时状态` 只能消费规则，不能定义规则

如果出现冲突，优先级如下：

`人类明确批准 > 文档中的 policy source > 当前有效机器 policy 层 > 运行时推断`

因此：

- 如果当前有效机器 policy 层与文档不一致，gate 必须报错
- 如果运行时行为与当前有效机器 policy 层不一致，执行必须被阻断或降级
- 如果文档没有批准更新，执行器不能擅自把新行为当成正式规则

## 当前 Pilot 兼容态

长期目标仍然是 `docs/policy/` 加编译后的 `.policy/`。

但当前 Growware pilot 还没有走到那一步。现在机器真正执行的是：

```text
.growware/
  contracts/
  policies/
  ops/
```

对当前 pilot 来说：

- `.growware/contracts/` 承载 event / incident schema
- `.growware/policies/` 承载 intake、judge、deploy 的机器可读规则
- `.growware/ops/` 承载 daemon 可执行入口和职责定义
- `docs/reference/growware/shared-policy-contract*.md` 则是解释这个仓库如何把 policy 写在 `docs/policy/`，并把它编译成 `.policy/` 的 durable 合同

这意味着当前 pilot **并不宣称** 每个接入项目现在都已经具备 `docs/policy/` 和 `.policy/`。

当前合同真正表达的是：

- 当前 pilot runtime：`.growware/*`
- 未来通用 policy 栈：`docs/policy/` -> `.policy/`
- 两种形态都必须保持同一个 ownership 原则：项目文档定义规则，执行器只消费规则

## 三方职责边界

| 角色 | 拥有什么 | 负责什么 | 不负责什么 |
| --- | --- | --- | --- |
| 人类 | 最终规则解释权、批准权、业务方向决定权 | 在文档中表达规则、批准规则变更、判断重大 tradeoff | 把手写机器 JSON 当成可 review 文档的替代 |
| `project-assistant` | 规则框架、文档治理、通用 gate 编排 | 定义文档格式、在可用时编译 `.policy/`、校验一致性，并把 pilot policy 栈逐步桥接到目标模型 | 替项目拍板业务规则、绕过审批改规则 |
| Growware | 执行权、反馈闭环、修复执行权 | 读取当前有效机器 policy 层、判断能不能做、执行、验证、通知 | 自主立法、越过规则边界修改项目行为 |
| terminal takeover | 过渡执行能力 | 在临时接管时仍遵守同一套当前有效机器 policy 层 | 以“人工接管”为理由绕开项目规则 |

## 长期目标目录约定

每个已经收敛完成的项目，长期应同时拥有两层规则目录：

```text
docs/
  policy/
    *.md

.policy/
  manifest.json
  index.json
  rules/
    *.json
  provenance.json
```

解释：

- `docs/policy/`：人类可读规则层
- `.policy/`：机器执行规则层

这是通用“文档 -> 机器 policy”编译链成熟后的目标形态。

在那之前，pilot 项目允许使用 `.growware/contracts/`、`.growware/policies/`、`.growware/ops/` 这种兼容态，只要满足：

- ownership 仍然从人类批准的文档开始
- 机器层仍然进入 Git 管理
- daemon 和 terminal takeover 执行的是同一套规则
- 仓库明确写清楚如何迁移到 `docs/policy/` + `.policy/`

## 文档层约定：`docs/policy/*.md`

### 目标

让人类可以自然阅读和修改规则，同时让 `project-assistant` 能稳定提取结构化含义。

### 文件粒度

推荐一条主题一个文件，而不是一个超大总表。

建议类别：

- `change-boundaries.md`
- `approval-boundaries.md`
- `interaction-contracts.md`
- `verification-rules.md`
- `protected-assets.md`

### 每个 policy 文档必须回答的问题

至少要明确：

1. 规则 ID 是什么
2. 这条规则属于哪一类
3. 作用范围是什么
4. 允许做什么
5. 禁止做什么
6. 哪些情况必须人工审批
7. 违反后应该拦截还是告警
8. 至少要跑哪些验证

### 推荐文档模板

每个 `docs/policy/*.md` 建议使用如下结构：

```md
# 规则标题

## Metadata

- id: `interaction.wd.first-reply`
- kind: `interaction-contract`
- status: `active`
- owners: `project-owner`
- applies_to:
  - `plugin/src/plugin/index.ts`
  - `scripts/runtime/lifecycle_coordinator.py`
- effect: `deny-without-approval`

## Rule

这条规则的自然语言定义。

## Allowed

- 允许的修改范围

## Forbidden

- 禁止的修改范围

## Approval Required

- 哪些修改必须经过人类批准

## Verification

- 至少需要跑哪些验证

## Machine Notes

- 给 `project-assistant` 和 Growware 的补充说明
```

### 语义要求

`project-assistant` 在编译时，必须把这些段落理解为：

- `Metadata`：结构化入口
- `Rule`：对外的人类定义
- `Allowed`：白名单
- `Forbidden`：红线
- `Approval Required`：人工 gate
- `Verification`：验证门禁
- `Machine Notes`：非用户文案层的机器解释辅助

如果某个文档只有长篇描述，没有明确的 `Allowed / Forbidden / Approval Required / Verification`，则只能算“可读说明”，不能算“完整 policy source”。

## 机器层约定：`.policy/`

`.policy/` 不是人类优先编辑层，而是 `project-assistant` 编译后的机器执行层。

### 必需文件

#### `.policy/manifest.json`

记录 policy 版本、合同版本、生成时间、生成器信息。

最小字段：

```json
{
  "schema": "growware.policy.manifest.v1",
  "contract_version": 1,
  "generated_by": "project-assistant",
  "generated_at": "2026-04-13T00:00:00Z",
  "index": ".policy/index.json",
  "rules_dir": ".policy/rules"
}
```

#### `.policy/index.json`

记录所有 rule 的摘要索引，供执行时快速加载。

最小字段：

```json
{
  "schema": "growware.policy.index.v1",
  "rules": [
    {
      "id": "interaction.wd.first-reply",
      "kind": "interaction-contract",
      "status": "active",
      "effect": "deny-without-approval",
      "applies_to": [
        "plugin/src/plugin/index.ts",
        "scripts/runtime/lifecycle_coordinator.py"
      ],
      "rule_file": ".policy/rules/interaction.wd.first-reply.json",
      "source_docs": [
        "docs/policy/interaction-contracts.md"
      ]
    }
  ]
}
```

#### `.policy/rules/*.json`

每条规则一个文件，供 Growware、daemon、terminal takeover 精确读取。

最小字段：

```json
{
  "schema": "growware.policy.rule.v1",
  "id": "interaction.wd.first-reply",
  "title": "WD 首轮回复交互合同",
  "kind": "interaction-contract",
  "status": "active",
  "effect": "deny-without-approval",
  "owners": ["project-owner"],
  "applies_to": [
    "plugin/src/plugin/index.ts",
    "scripts/runtime/lifecycle_coordinator.py"
  ],
  "allowed": [
    "修复明显 bug",
    "补测试",
    "不改变既有交互语义的内部重构"
  ],
  "forbidden": [
    "未批准的用户可见语义改写",
    "删除首轮 wd 回复",
    "把稳定交互资产改成新的默认风格"
  ],
  "approval_required": [
    "任何改动用户可见首轮 wd 文案语义的变更"
  ],
  "required_checks": [
    "node --test plugin/tests/pre-register-and-ack.test.mjs",
    "PYTHONPATH=tests python3 -m unittest tests.test_openclaw_hooks"
  ],
  "source_docs": [
    "docs/policy/interaction-contracts.md"
  ]
}
```

#### `.policy/provenance.json`

记录这批 policy 是从哪些文档编译来的，以及是否存在警告或未解析项。

## `project-assistant` 编译合同

`project-assistant` 必须承担文档到 `.policy/` 的编译责任。

### 输入

- `docs/policy/*.md`
- 其他被标记为 policy source 的文档段落
- 当前项目的目录布局和模块边界

### 输出

- `.policy/manifest.json`
- `.policy/index.json`
- `.policy/rules/*.json`
- `.policy/provenance.json`

### 编译要求

1. 编译必须可重复
2. 编译结果必须可提交到 Git
3. 编译必须显式记录来源文档
4. 编译失败时不得生成“看似成功”的半成品 policy
5. 如果文档含义不完整，只能报 warning 或 fail，不得擅自脑补成强规则

### 一致性要求

`project-assistant` 必须校验：

- 文档存在，但 `.policy/` 缺失：失败
- `.policy/` 存在，但来源文档不存在：失败
- 文档变更后 `.policy/` 未更新：失败
- `.policy/` 含义与文档冲突：失败

## Growware 执行合同

Growware、daemon、terminal takeover 都必须遵守同一套执行合同。

### 执行前最少加载什么

每次任务开始前，不应全文重读全部文档，而应读取：

1. 全局 `immutable` 规则
2. 本次 touched files 命中的相关 rule
3. 本次需要审批的 rule
4. 本次必须执行的最小验证集

### Growware 必须做到

1. 只读取 `.policy/`
2. 根据 touched files 和任务目标映射相关规则
3. 在执行前判断：
   - `allow`
   - `require-approval`
   - `deny`
   - `advisory`
4. 在 close-out 时说明：
   - 哪些规则被命中
   - 哪些验证被执行
   - 是否触发审批边界

### Growware 不得做到

- 不得把“我觉得应该这样”当成规则
- 不得跳过 `.policy/` 直接凭上下文改用户可见行为
- 不得因为 `terminal takeover` 就绕过禁止项
- 不得在未批准的情况下把提案写成已生效规则

## terminal takeover 合同

`terminal takeover` 只是执行来源，不是规则豁免来源。

因此：

- `terminal takeover` 必须先读 `.policy/`
- `terminal takeover` 命中 `deny` 时必须停止
- `terminal takeover` 命中 `require-approval` 时必须等批准
- `terminal takeover` 完成后也必须说明：
  - 结果是 `daemon-owned` 还是 `terminal-takeover`
  - 哪些能力已回灌给 daemon

## 门禁分层合同

为了避免“规则越多，系统越慢”，门禁必须分层，而不是所有规则每次全跑。

### Layer 1: 常驻轻门禁

每次都跑，必须快。

负责：

- `.policy/` 是否存在
- `.policy/` 是否与文档一致
- touched files 命中了哪些 rule
- 是否命中 `deny` 或 `require-approval`
- 本次最小验证集是什么

### Layer 2: 目标化门禁

只按 touched scope 加载。

例如：

- 改用户可见回复，才加载 `interaction-contract`
- 改 deploy，才加载 `ops-boundary`
- 改 schema，才加载 `compatibility-contract`

### Layer 3: 深门禁

只在高风险变更时触发。

例如：

- 发布语义变化
- 兼容性边界变化
- 自动部署边界变化
- 安全策略变化

结论：

门禁不应按“规则条数”设计，而应按“规则类别 + 影响范围”设计。

## 推荐 rule kind

建议先限制在少数 rule kind，避免爆炸式复杂化：

- `immutable-rule`
- `approval-required`
- `interaction-contract`
- `behavior-contract`
- `verification-rule`
- `ops-boundary`

## 变更流程合同

规则变更应该走下面这条链：

1. 人类修改 `docs/policy/*.md`
2. `project-assistant` 编译 `.policy/`
3. 一致性 gate 通过
4. Growware 开始按新规则执行

不允许的顺序：

1. 执行器先改行为
2. 事后再补文档
3. 再假装这是既定 policy

## 默认保守原则

如果出现下列情况，系统必须保守：

- 文档存在，但规则含义不清
- `.policy/` 缺失
- touched files 命中了受保护区域，但无对应 rule
- 规则之间互相冲突
- 规则要求审批，但审批状态不明确

保守策略：

- 不自动改
- 不假装合规
- 产出需要人类确认的提案

## 最小落地要求

一个项目要接入本合同，最少需要：

1. `docs/policy/` 目录
2. `docs/policy/README.md` 入口文件
3. `docs/policy/project-1.md` 或等价的项目 policy source
4. `.policy/` 目录
5. 至少 1 条 `interaction-contract`
6. 至少 1 条 `verification-rule`
7. `project-assistant` 的 compile / validate 入口
8. Growware 的 `.policy/` 读取入口

## WD 首轮回复示例

如果项目认定 `wd` 首轮回复是稳定交互资产，那么文档和 `.policy/` 应表达成类似下面的含义：

- 可以修 bug
- 可以补测试
- 可以优化内部实现
- 不可以在未批准的情况下改变第一轮回复的用户可见语义
- 任何用户可见语义变化都必须经过人类批准

这样：

- `project-assistant` 会把它编译进 `.policy/`
- Growware 会在执行前命中这条 rule
- terminal takeover 也不能随手改掉

## 最终裁决

这份合同的最终含义以 `人类批准` 为准。

`project-assistant` 负责把批准后的规则编译清楚。  
Growware 负责按规则执行清楚。  
任何执行器都不能取代项目 owner 的规则裁决权。
