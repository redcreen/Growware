#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
POLICY_SOURCE_DIR = Path("docs") / "policy"
POLICY_DIR = Path(".policy")
POLICY_RULES_DIR = POLICY_DIR / "rules"
POLICY_CONTRACT_VERSION = 1


@dataclass(frozen=True)
class PolicyDocSpec:
    stem: str
    rule_id: str
    kind: str
    effect: str


DOC_SPECS: tuple[PolicyDocSpec, ...] = (
    PolicyDocSpec(
        stem="project-1",
        rule_id="project-1.openclaw-task-system.policy-source",
        kind="project-policy",
        effect="deny-without-approval",
    ),
)


def resolve_project_root(project_root: Path | None = None) -> Path:
    return (project_root or PROJECT_ROOT).resolve()


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _strip_inline_markup(value: str) -> str:
    return value.strip().strip("`").strip()


def _strip_wrapped_code_span(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and text.startswith("`") and text.endswith("`"):
        inner = text[1:-1]
        if "`" not in inner:
            return inner.strip()
    return text


def _split_sections(lines: list[str]) -> tuple[str, dict[str, list[str]]]:
    title = ""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    buffer: list[str] = []
    for raw in lines:
        line = raw.rstrip("\n")
        if line.startswith("# "):
            title = line[2:].strip()
            continue
        if line.startswith("## "):
            if current is not None:
                sections[current] = buffer
            current = line[3:].strip()
            buffer = []
            continue
        if current is not None:
            buffer.append(line)
    if current is not None:
        sections[current] = buffer
    return title, sections


def _parse_list_block(lines: list[str]) -> list[str]:
    values: list[str] = []
    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            values.append(_strip_wrapped_code_span(stripped[2:].strip()))
    return values


def _parse_metadata(lines: list[str]) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        stripped = raw.strip()
        if not stripped:
            i += 1
            continue
        if not stripped.startswith("- "):
            i += 1
            continue
        key_part = stripped[2:]
        if ":" not in key_part:
            i += 1
            continue
        key, remainder = key_part.split(":", 1)
        key = key.strip().replace("-", "_").replace(" ", "_")
        value = remainder.strip()
        if value:
            metadata[key] = _strip_inline_markup(value)
            i += 1
            continue
        values: list[str] = []
        i += 1
        while i < len(lines):
            nested = lines[i]
            nested_stripped = nested.strip()
            if not nested_stripped:
                i += 1
                continue
            if nested.startswith("  - "):
                values.append(_strip_inline_markup(nested_stripped[2:].strip()))
                i += 1
                continue
            break
        metadata[key] = values
    return metadata


def _parse_markdown_policy_doc(path: Path) -> dict[str, Any]:
    lines = _read_text(path).splitlines()
    title, sections = _split_sections(lines)
    metadata = _parse_metadata(sections.get("Metadata", []))
    rule_text = "\n".join(line.strip() for line in sections.get("Rule", []) if line.strip()).strip()
    return {
        "title": title,
        "metadata": metadata,
        "rule": rule_text,
        "allowed": _parse_list_block(sections.get("Allowed", [])),
        "forbidden": _parse_list_block(sections.get("Forbidden", [])),
        "approval_required": _parse_list_block(sections.get("Approval Required", [])),
        "required_checks": _parse_list_block(sections.get("Verification", [])),
        "machine_notes": _parse_list_block(sections.get("Machine Notes", [])),
    }


def _relative(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def _policy_source_paths(root: Path, spec: PolicyDocSpec) -> tuple[Path, Path]:
    en_path = root / POLICY_SOURCE_DIR / f"{spec.stem}.md"
    zh_path = root / POLICY_SOURCE_DIR / f"{spec.stem}.zh-CN.md"
    return en_path, zh_path


def build_policy_catalog(project_root: Path | None = None) -> dict[str, Any]:
    root = resolve_project_root(project_root)
    source_dir = root / POLICY_SOURCE_DIR
    compiled_dir = root / POLICY_DIR
    rules_dir = compiled_dir / "rules"
    compiled_dir.mkdir(parents=True, exist_ok=True)
    rules_dir.mkdir(parents=True, exist_ok=True)

    source_docs: list[dict[str, Any]] = []
    rules: list[dict[str, Any]] = []
    warnings: list[str] = []

    for spec in DOC_SPECS:
        en_path, zh_path = _policy_source_paths(root, spec)
        if not en_path.exists():
            warnings.append(f"missing policy source: {_relative(en_path, root)}")
            continue
        if not zh_path.exists():
            warnings.append(f"missing policy translation: {_relative(zh_path, root)}")
        parsed = _parse_markdown_policy_doc(en_path)
        metadata = parsed["metadata"]
        rule_id = str(metadata.get("id") or spec.rule_id)
        kind = str(metadata.get("kind") or spec.kind)
        status = str(metadata.get("status") or "active")
        effect = str(metadata.get("effect") or spec.effect)
        owners = metadata.get("owners") if isinstance(metadata.get("owners"), list) else []
        applies_to = metadata.get("applies_to") if isinstance(metadata.get("applies_to"), list) else []

        rule = {
            "schema": "growware.policy.rule.v1",
            "id": rule_id,
            "title": parsed["title"] or rule_id,
            "kind": kind,
            "status": status,
            "effect": effect,
            "owners": owners,
            "applies_to": applies_to,
            "rule": parsed["rule"],
            "allowed": parsed["allowed"],
            "forbidden": parsed["forbidden"],
            "approval_required": parsed["approval_required"],
            "required_checks": parsed["required_checks"],
            "machine_notes": parsed["machine_notes"],
            "source_docs": [
                _relative(en_path, root),
                _relative(zh_path, root),
            ] if zh_path.exists() else [_relative(en_path, root)],
        }
        rules.append(rule)
        source_docs.append(
            {
                "source": _relative(en_path, root),
                "translation": _relative(zh_path, root) if zh_path.exists() else None,
                "rule_id": rule_id,
                "kind": kind,
            }
        )

    manifest = {
        "schema": "growware.policy.manifest.v1",
        "contract_version": POLICY_CONTRACT_VERSION,
        "generated_by": "growware/scripts/growware_policy_sync.py",
        "generated_at": datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "index": ".policy/index.json",
        "rules_dir": ".policy/rules",
    }
    index = {
        "schema": "growware.policy.index.v1",
        "rules": [
            {
                "id": rule["id"],
                "kind": rule["kind"],
                "status": rule["status"],
                "effect": rule["effect"],
                "applies_to": rule["applies_to"],
                "rule_file": f".policy/rules/{rule['id']}.json",
                "source_docs": rule["source_docs"],
            }
            for rule in rules
        ],
    }
    provenance = {
        "schema": "growware.policy.provenance.v1",
        "contract_version": POLICY_CONTRACT_VERSION,
        "source_docs": source_docs,
        "warnings": warnings,
    }
    files: list[dict[str, Any]] = [
        {"path": str(compiled_dir / "manifest.json"), "payload": manifest},
        {"path": str(compiled_dir / "index.json"), "payload": index},
        {"path": str(compiled_dir / "provenance.json"), "payload": provenance},
    ]
    for rule in rules:
        files.append({"path": str(rules_dir / f"{rule['id']}.json"), "payload": rule})

    return {
        "ok": not warnings and len(rules) == len(DOC_SPECS),
        "projectRoot": str(root),
        "policySourceDir": str(source_dir),
        "policyDir": str(compiled_dir),
        "rules": rules,
        "warnings": warnings,
        "files": files,
    }


def _dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_for_compare(path: Path, payload: Any) -> Any:
    if path.name == "manifest.json" and isinstance(payload, dict):
        normalized = dict(payload)
        normalized["generated_at"] = "<normalized>"
        return normalized
    return payload


def _compare_payloads(existing: Any, desired: Any, *, path: Path) -> bool:
    return _normalize_for_compare(path, existing) == _normalize_for_compare(path, desired)


def write_policy_catalog(project_root: Path | None = None) -> dict[str, Any]:
    report = build_policy_catalog(project_root)
    changed = False
    for entry in report["files"]:
        path = Path(entry["path"])
        payload = entry["payload"]
        current = _load_json(path) if path.exists() else None
        if current is None or not _compare_payloads(current, payload, path=path):
            _dump_json(path, payload)
            changed = True
    report["changed"] = changed
    return report


def validate_policy_catalog(project_root: Path | None = None) -> dict[str, Any]:
    report = build_policy_catalog(project_root)
    root = resolve_project_root(project_root)
    missing: list[str] = []
    mismatches: list[str] = []
    for entry in report["files"]:
        path = Path(entry["path"])
        payload = entry["payload"]
        if not path.exists():
            missing.append(_relative(path, root))
            continue
        current = _load_json(path)
        if not _compare_payloads(current, payload, path=path):
            mismatches.append(_relative(path, root))
    report.update({
        "ok": not report["warnings"] and not missing and not mismatches and len(report["rules"]) == len(DOC_SPECS),
        "missing": missing,
        "mismatches": mismatches,
    })
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile or validate Growware policy docs into .policy.")
    parser.add_argument("--project-root", type=Path, default=resolve_project_root())
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def render_markdown(payload: dict[str, Any]) -> str:
    lines = ["# Growware Policy Sync", ""]
    lines.append(f"- ok: `{str(payload['ok']).lower()}`")
    lines.append(f"- changed: `{str(payload.get('changed', False)).lower()}`")
    lines.append(f"- project_root: `{payload['projectRoot']}`")
    lines.append(f"- policy_source_dir: `{payload['policySourceDir']}`")
    lines.append(f"- policy_dir: `{payload['policyDir']}`")
    if payload.get("warnings"):
        lines.append("- warnings:")
        for warning in payload["warnings"]:
            lines.append(f"  - {warning}")
    if payload.get("missing"):
        lines.append("- missing:")
        for item in payload["missing"]:
            lines.append(f"  - {item}")
    if payload.get("mismatches"):
        lines.append("- mismatches:")
        for item in payload["mismatches"]:
            lines.append(f"  - {item}")
    lines.append("- rules:")
    for rule in payload["rules"]:
        lines.append(f"  - {rule['id']}: `{rule['kind']}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.check and args.write:
        raise SystemExit("--check and --write cannot be combined")
    payload = write_policy_catalog(args.project_root) if args.write else validate_policy_catalog(args.project_root)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(payload), end="")
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
