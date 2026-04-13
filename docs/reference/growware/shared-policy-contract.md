# Shared Policy Contract

[English](shared-policy-contract.md) | [中文](shared-policy-contract.zh-CN.md)

## Purpose

This document is the shared contract for `humans`, `project-assistant`, and `Growware`.

It answers five questions:

1. who owns project rules
2. where humans should write those rules
3. what `project-assistant` must compile from those rules
4. how Growware / the daemon / terminal takeover must read and execute them
5. how to connect rules to gates without making the system unacceptably slow

This document is not itself a runtime config file. It defines how runtime policy files must exist, be generated, be validated, and be executed.

## Audience

- `human`: project owner, maintainer, product owner, approver
- `project-assistant`: the upstream project-governance and gate-orchestration system
- `Growware`: the project-level execution loop for feedback, implementation, verification, deploy, and notification
- `terminal takeover`: Codex working directly in the terminal must also obey this contract

## Current Problems This Contract Solves

This contract is not speculative. It exists because these problems have already appeared in practice.

### Problem 1: executors may change things the project did not authorize

The project may already have documented rules such as:

- some user-visible interactions are stable assets
- some behaviors may be bug-fixed but not semantically rewritten
- some changes require approval before implementation

If an executor works from immediate context alone, it may still change those behaviors without fully reloading the project's standing constraints.

### Problem 2: daemon memory does not guarantee terminal-takeover discipline

Over time, the daemon may already have learned part of the project through `.growware/`, tests, and runtime rules.

But if terminal Codex takes over without the same execution constraints, the system can split:

- the daemon follows project rules
- terminal takeover drifts from project rules

That creates inconsistent behavior.

### Problem 3: full-document rereads are too slow and still unreliable

If every code change requires rereading the full repo documentation, the system becomes:

- slow
- still vulnerable to missing key constraints

So the project needs an intermediate layer that comes from docs but is optimized for machine execution.

### Problem 4: rules must belong to the project, not to a tool brand

Even without Growware, the project still needs:

- protection against random edits
- boundary checks before changes
- consistency between docs and machine-readable rules

Therefore the rules must belong to the project itself.

## How This Discussion Converged

This contract is based on the following conclusions from the discussion:

1. `project-assistant` and Growware must not own the same layer  
   `project-assistant` owns the governance framework; Growware owns the execution loop.

2. Growware must not define `what may change` on its own  
   Otherwise the executor would also become the legislator.

3. Rule content belongs to the target project  
   Even without Growware, the project still needs rule-based protection.

4. Humans will not maintain machine JSON directly  
   Humans primarily express rules through docs.

5. Machines should not depend on rereading the full docs every time  
   That is why `.policy/` is needed.

6. `project-assistant` is the right place to compile policy from docs  
   It already owns project governance, doc governance, and generic gates.

7. Growware, the daemon, and terminal takeover must all execute the same `.policy/`  
   The system cannot allow daemon-owned execution and manual takeover to follow different rules.

## Final Decisions

The three parties now share the following decisions:

### Decision 1: rule content belongs to the project

Rules are not private Growware config and not `project-assistant` global constants.

Rules belong to the `target project` and are versioned with the project in Git.

### Decision 2: docs are the human source of truth

Humans express rules through project docs.

The recommended home is:

```text
docs/policy/
```

### Decision 3: `.policy/` is the machine execution source of truth

`.policy/` does not replace docs. It is the machine execution layer compiled from docs.

Growware, the daemon, and terminal takeover should execute `.policy/` at runtime.

### Decision 4: `project-assistant` owns normalization and compilation

`project-assistant` is responsible for:

- policy doc conventions
- extracting rules from docs
- compiling `.policy/`
- validating consistency
- wiring policy into generic gates

### Decision 5: Growware is an executor

Growware is responsible for:

- reading `.policy/`
- deciding whether execution is allowed
- implementing, verifying, deploying, and notifying

Growware is not the final interpreter of project rules.

### Decision 6: terminal takeover has no rule exemption

Once execution enters the project layer, daemon-owned execution and terminal takeover must obey the same `.policy/`.

## How Each Role Works

### Human

The human:

- defines rules in docs
- reviews and approves rule changes
- decides major business tradeoffs
- does not directly maintain machine `.policy/`

### `project-assistant`

`project-assistant`:

- reads policy source from project docs
- normalizes it into stable structure
- generates `.policy/`
- checks doc / policy consistency
- turns `.policy/` into executable gate inputs

### Growware

Growware:

- reads `.policy/` for the current task and touched scope
- decides whether the change is `allow`, `deny`, or `require-approval`
- executes implementation, verification, deploy, and notification under those rules
- reports triggered rules and execution source in close-out

### terminal takeover

terminal takeover:

- must read `.policy/` before executing
- may not bypass forbidden changes
- may not bypass approval-required changes
- must state that the result was `terminal-takeover` and which capabilities were fed back into durable assets

## Core Principles

### 1. Rules belong to the project, not to the executor

`what may change and what may not change` belongs to the `target project`.

These rules are not Growware preferences, not `project-assistant` global constants, and not temporary chat agreements.

### 2. Humans interact with documents

The final input source is always the `human`.

Humans primarily edit `documents`, not `.policy/` machine files.

### 3. `.policy/` is the machine execution source of truth

Human-readable rules live in `docs/`.

Machine-executable rules live in `.policy/`.

Growware, the daemon, and terminal takeover should treat `.policy/` as the runtime constraint input rather than re-reading the full repo documentation on every task.

### 4. `project-assistant` turns documents into normalized policy

`project-assistant` is responsible for:

- defining how policy source should be written in docs
- extracting and compiling `.policy/`
- validating document and `.policy/` consistency
- attaching policy to the generic gate framework

### 5. Growware executes policy; it does not legislate policy

Growware executes project rules. It does not invent them.

If Growware believes a rule should change, it may only:

- produce a proposal
- draft document updates
- wait for human approval

Before approval, Growware may not treat a recommendation as an active rule.

## Source-of-Truth Layers

From highest to lowest priority:

1. `human approval`
2. `policy source in project docs`
3. `.policy/` machine execution layer
4. `runtime state`

That means:

- `human approval` determines whether a rule is valid
- `docs` make rules reviewable and maintainable by humans
- `.policy/` makes rules executable and gateable by machines
- `runtime state` may consume rules but may not define them

If there is a conflict, precedence is:

`explicit human approval > policy source in docs > .policy/ > runtime inference`

Therefore:

- if `.policy/` conflicts with docs, the gate must fail
- if runtime behavior conflicts with `.policy/`, execution must be blocked or downgraded
- if docs were not approved, executors may not silently treat new behavior as official policy

## Responsibility Boundaries

| Role | Owns | Responsible For | Must Not Do |
| --- | --- | --- | --- |
| Human | final rule interpretation, approval, business direction | expressing rules in docs, approving rule changes, deciding major tradeoffs | hand-authoring machine JSON in `.policy/` |
| `project-assistant` | rule framework, docs governance, generic gate orchestration | defining doc format, compiling `.policy/`, validating consistency, wiring rules into gates | deciding project business rules on its own |
| Growware | execution, feedback loop, repair flow | reading `.policy/`, deciding whether execution is allowed, implementing, verifying, notifying | self-legislating project rules or bypassing approvals |
| terminal takeover | temporary execution path | obeying `.policy/` during direct execution | treating manual takeover as a rule exemption |

## Directory Convention

Every onboarded project should have two policy layers:

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

- `docs/policy/`: human-readable rule layer
- `.policy/`: machine-executable rule layer

## Document Layer Contract: `docs/policy/*.md`

### Goal

Humans must be able to read and edit rules naturally, while `project-assistant` must be able to extract stable machine meaning from them.

### File Granularity

Prefer one topic per file instead of one giant policy table.

Suggested categories:

- `change-boundaries.md`
- `approval-boundaries.md`
- `interaction-contracts.md`
- `verification-rules.md`
- `protected-assets.md`

### Every policy document must answer

At minimum:

1. what the rule ID is
2. what kind of rule it is
3. what scope it applies to
4. what is allowed
5. what is forbidden
6. what requires human approval
7. whether violations must block or only warn
8. which verification is mandatory

### Recommended Markdown Template

```md
# Rule Title

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

Natural-language definition of the rule.

## Allowed

- allowed change surface

## Forbidden

- forbidden change surface

## Approval Required

- changes that require human approval

## Verification

- minimum required checks

## Machine Notes

- additional notes for `project-assistant` and Growware
```

### Semantic Requirements

`project-assistant` must interpret these sections as:

- `Metadata`: structured entry point
- `Rule`: external human definition
- `Allowed`: allowlist
- `Forbidden`: red lines
- `Approval Required`: approval gate
- `Verification`: verification gate
- `Machine Notes`: machine-focused clarifications

If a doc only contains descriptive prose and does not clearly expose `Allowed / Forbidden / Approval Required / Verification`, it is only readable guidance, not a complete policy source.

## Machine Layer Contract: `.policy/`

`.policy/` is the compiled machine execution layer created by `project-assistant`.

### Required Files

#### `.policy/manifest.json`

Tracks policy version, contract version, generation time, and generator metadata.

Minimal shape:

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

Provides a fast runtime index of all rules.

Minimal shape:

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

One file per rule, for Growware, the daemon, and terminal takeover.

Minimal shape:

```json
{
  "schema": "growware.policy.rule.v1",
  "id": "interaction.wd.first-reply",
  "title": "WD first-reply interaction contract",
  "kind": "interaction-contract",
  "status": "active",
  "effect": "deny-without-approval",
  "owners": ["project-owner"],
  "applies_to": [
    "plugin/src/plugin/index.ts",
    "scripts/runtime/lifecycle_coordinator.py"
  ],
  "allowed": [
    "obvious bug fixes",
    "test additions",
    "internal refactors without user-visible semantic change"
  ],
  "forbidden": [
    "unapproved user-visible semantic rewrite",
    "removing the first wd reply",
    "changing a stable interaction asset into a new default style"
  ],
  "approval_required": [
    "any change to the user-visible semantics of the first wd reply"
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

Records which docs produced the current policy set and whether any warnings or unresolved items remain.

## `project-assistant` Compile Contract

`project-assistant` owns the document-to-policy compile step.

### Inputs

- `docs/policy/*.md`
- other explicitly marked policy-source sections in docs
- the project's module and directory layout

### Outputs

- `.policy/manifest.json`
- `.policy/index.json`
- `.policy/rules/*.json`
- `.policy/provenance.json`

### Compile Requirements

1. compilation must be repeatable
2. compiled output must be committable to Git
3. compiled policy must explicitly record source docs
4. failed compilation must not leave a fake-success half-state
5. if docs are incomplete, the compiler may warn or fail, but must not silently invent strong rules

### Consistency Requirements

`project-assistant` must fail when:

- docs exist but `.policy/` is missing
- `.policy/` exists but source docs do not
- docs changed but `.policy/` was not refreshed
- `.policy/` meaning conflicts with docs

## Growware Execution Contract

Growware, the daemon, and terminal takeover must obey the same execution contract.

### Minimum Read Set Per Task

Executors should not re-read every project document on every task. They should load:

1. global immutable rules
2. rules matching the current touched files
3. rules that require approval for the current change
4. the minimum required verification set

### Growware must

1. read `.policy/`
2. map touched files and task intent to relevant rules
3. classify the change as:
   - `allow`
   - `require-approval`
   - `deny`
   - `advisory`
4. state in close-out:
   - which rules were triggered
   - which checks were run
   - whether an approval boundary was crossed

### Growware must not

- replace rules with its own preference
- bypass `.policy/` and rewrite user-visible behavior from context alone
- use `terminal takeover` as an excuse to bypass forbidden changes
- treat a proposal as an active rule before approval

## Terminal Takeover Contract

`terminal takeover` is an execution source, not a rule exemption.

Therefore:

- it must read `.policy/` first
- it must stop on `deny`
- it must wait on `require-approval`
- it must still report:
  - whether the result is `daemon-owned` or `terminal-takeover`
  - which capabilities were fed back into daemon-owned assets

## Layered Gate Contract

To avoid making the system too slow, gates must be layered instead of running every rule on every change.

### Layer 1: always-on light gates

Always run. Must be fast.

Responsibilities:

- `.policy/` exists
- `.policy/` is consistent with docs
- touched files match the relevant rules
- detect `deny` and `require-approval`
- compute the minimum required checks

### Layer 2: targeted gates

Only load rule families relevant to the touched scope.

Examples:

- interaction changes -> `interaction-contract`
- deploy changes -> `ops-boundary`
- schema changes -> `compatibility-contract`

### Layer 3: deep gates

Only run on high-risk changes.

Examples:

- user-visible semantic changes
- compatibility boundary changes
- deployment boundary changes
- security policy changes

The system should be designed around `rule families + scope mapping`, not raw rule count.

## Recommended Rule Kinds

Keep the first version small:

- `immutable-rule`
- `approval-required`
- `interaction-contract`
- `behavior-contract`
- `verification-rule`
- `ops-boundary`

## Change Workflow Contract

Rule changes should flow like this:

1. human updates `docs/policy/*.md`
2. `project-assistant` compiles `.policy/`
3. consistency gates pass
4. Growware executes under the new rule set

This order is not allowed:

1. executor changes behavior first
2. docs are updated later
3. the change is retroactively treated as established policy

## Conservative Default

The system must be conservative when:

- docs exist but rule meaning is unclear
- `.policy/` is missing
- touched files hit a protected area but no rule exists
- rules conflict
- approval is required but approval state is unclear

Conservative behavior means:

- do not auto-change
- do not pretend compliance
- produce a proposal for human confirmation

## Minimum Adoption Requirements

To adopt this contract, a project needs at least:

1. a `docs/policy/` directory
2. a `.policy/` directory
3. at least one `interaction-contract`
4. at least one `verification-rule`
5. a `project-assistant` compile / validate entrypoint
6. a Growware `.policy/` read path

## WD First-Reply Example

If the project treats the `wd` first reply as a stable interaction asset, docs and `.policy/` should encode the following meaning:

- bug fixes are allowed
- tests may be added
- internal implementation may change
- user-visible semantic changes to the first reply are not allowed without approval
- any user-visible semantic rewrite requires explicit human approval

Then:

- `project-assistant` compiles that into `.policy/`
- Growware triggers that rule before execution
- terminal takeover cannot casually rewrite it either

## Final Authority

The final meaning of this contract is determined by `human approval`.

`project-assistant` is responsible for compiling approved rules clearly.  
Growware is responsible for executing them clearly.  
No executor may replace the project owner's rule authority.
