# Policy Source

[English](README.md) | [中文](README.zh-CN.md)

## Purpose

This directory is the human-readable policy source for Growware Project 1.

The shared contract in `docs/reference/growware/shared-policy-contract.md` defines how these docs are written, compiled, and executed.

## Current Source Set

- [project-1.md](project-1.md): the initial policy source for `openclaw-task-system`

## How To Use It

1. Read the shared policy contract first.
2. Keep the English and Chinese policy files aligned.
3. Treat these docs as the reviewed project rule source.
4. Compile them into `.policy/` with `python3 scripts/growware_policy_sync.py --write --json`.
5. Validate the generated machine layer with `python3 scripts/growware_policy_sync.py --check --json`.

## Compile And Validate

```bash
python3 scripts/growware_policy_sync.py --write --json
python3 scripts/growware_policy_sync.py --check --json
```

## Reading Order

- [../reference/growware/shared-policy-contract.md](../reference/growware/shared-policy-contract.md)
- [project-1.md](project-1.md)
