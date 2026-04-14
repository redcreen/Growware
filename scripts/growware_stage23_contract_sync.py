#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STAGE23_CONTRACT_SOURCE_DIR = Path("docs") / "reference" / "growware" / "stage-2-3-contracts"
STAGE23_DIR = Path(".growware") / "stage-2-3"
STAGE23_CONTRACTS_DIR = STAGE23_DIR / "contracts"
STAGE23_CONTRACT_VERSION = 1


@dataclass(frozen=True)
class Stage23ContractDocSpec:
    stem: str
    contract_id: str
    contract_type: str
    required_sections: tuple[str, ...]


DOC_SPECS: tuple[Stage23ContractDocSpec, ...] = (
    Stage23ContractDocSpec(
        stem="incident-lifecycle",
        contract_id="growware.stage23.incident-lifecycle.v1",
        contract_type="incident-lifecycle",
        required_sections=(
            "Purpose",
            "Intake Sources",
            "Lifecycle States",
            "Required Fields",
            "Promotion Rules",
            "Closure Rules",
            "Approval Rules",
            "Machine Notes",
        ),
    ),
    Stage23ContractDocSpec(
        stem="verification-profile",
        contract_id="growware.stage23.verification-profile.v1",
        contract_type="verification-profile",
        required_sections=(
            "Purpose",
            "Verification Modes",
            "Required Fields",
            "Matching Rules",
            "Failure Rules",
            "Close-Out Rules",
            "Machine Notes",
        ),
    ),
    Stage23ContractDocSpec(
        stem="deployment-gate",
        contract_id="growware.stage23.deployment-gate.v1",
        contract_type="deployment-gate",
        required_sections=(
            "Purpose",
            "Action Classes",
            "Gate Decisions",
            "Required Approval Payload",
            "Rollback Rules",
            "Emergency Constraints",
            "Machine Notes",
        ),
    ),
    Stage23ContractDocSpec(
        stem="close-out-provenance",
        contract_id="growware.stage23.close-out-provenance.v1",
        contract_type="close-out-provenance",
        required_sections=(
            "Purpose",
            "Execution Sources",
            "Required Fields",
            "Provenance Rules",
            "Follow-Up Rules",
            "Approval Rules",
            "Machine Notes",
        ),
    ),
    Stage23ContractDocSpec(
        stem="judge-promotion",
        contract_id="growware.stage23.judge-promotion.v1",
        contract_type="judge-promotion",
        required_sections=(
            "Purpose",
            "Judge Classes",
            "Promotion Triggers",
            "Required Fields",
            "Promotion Rules",
            "Rejection Rules",
            "Machine Notes",
        ),
    ),
    Stage23ContractDocSpec(
        stem="automation-bands",
        contract_id="growware.stage23.automation-bands.v1",
        contract_type="automation-bands",
        required_sections=(
            "Purpose",
            "Automation Bands",
            "Eligibility Rules",
            "Guardrails",
            "Approval Rules",
            "Escalation Rules",
            "Machine Notes",
        ),
    ),
    Stage23ContractDocSpec(
        stem="regression-assets",
        contract_id="growware.stage23.regression-assets.v1",
        contract_type="regression-assets",
        required_sections=(
            "Purpose",
            "Asset Types",
            "Required Fields",
            "Writeback Rules",
            "Coverage Rules",
            "Approval Rules",
            "Machine Notes",
        ),
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


def _normalize_section_name(name: str) -> str:
    normalized = []
    for char in name.strip().lower():
        if char.isalnum():
            normalized.append(char)
        else:
            normalized.append("_")
    value = "".join(normalized)
    while "__" in value:
        value = value.replace("__", "_")
    return value.strip("_")


def _parse_section_payload(lines: list[str]) -> dict[str, Any]:
    items = _parse_list_block(lines)
    text_lines: list[str] = []
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("- "):
            continue
        text_lines.append(stripped)
    return {
        "items": items,
        "text": "\n".join(text_lines).strip(),
    }


def _has_section_content(payload: dict[str, Any] | None) -> bool:
    if not payload:
        return False
    items = payload.get("items")
    text = payload.get("text")
    return bool(items or text)


def _parse_markdown_contract_doc(path: Path) -> dict[str, Any]:
    lines = _read_text(path).splitlines()
    title, sections = _split_sections(lines)
    metadata = _parse_metadata(sections.get("Metadata", []))
    parsed_sections: dict[str, dict[str, Any]] = {}
    for section_name, section_lines in sections.items():
        if section_name == "Metadata":
            continue
        parsed_sections[_normalize_section_name(section_name)] = {
            "title": section_name,
            **_parse_section_payload(section_lines),
        }
    return {
        "title": title,
        "metadata": metadata,
        "sections": parsed_sections,
    }


def _relative(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def _source_paths(root: Path, spec: Stage23ContractDocSpec) -> tuple[Path, Path]:
    en_path = root / STAGE23_CONTRACT_SOURCE_DIR / f"{spec.stem}.md"
    zh_path = root / STAGE23_CONTRACT_SOURCE_DIR / f"{spec.stem}.zh-CN.md"
    return en_path, zh_path


def build_stage23_contract_catalog(project_root: Path | None = None) -> dict[str, Any]:
    root = resolve_project_root(project_root)
    source_dir = root / STAGE23_CONTRACT_SOURCE_DIR
    compiled_dir = root / STAGE23_DIR
    contracts_dir = compiled_dir / "contracts"
    compiled_dir.mkdir(parents=True, exist_ok=True)
    contracts_dir.mkdir(parents=True, exist_ok=True)

    source_docs: list[dict[str, Any]] = []
    contracts: list[dict[str, Any]] = []
    warnings: list[str] = []
    files: list[dict[str, Any]] = []

    for spec in DOC_SPECS:
        en_path, zh_path = _source_paths(root, spec)
        if not en_path.exists():
            warnings.append(f"missing stage23 contract source: {_relative(en_path, root)}")
            continue
        if not zh_path.exists():
            warnings.append(f"missing stage23 contract translation: {_relative(zh_path, root)}")
        parsed = _parse_markdown_contract_doc(en_path)
        metadata = parsed["metadata"]

        contract_id = str(metadata.get("id") or spec.contract_id)
        kind = str(metadata.get("kind") or "stage-contract")
        status = str(metadata.get("status") or "active-draft")
        contract_type = str(metadata.get("contract_type") or spec.contract_type)
        owners = metadata.get("owners") if isinstance(metadata.get("owners"), list) else []
        depends_on = metadata.get("depends_on") if isinstance(metadata.get("depends_on"), list) else []

        if contract_id != spec.contract_id:
            warnings.append(
                f"contract id mismatch for {_relative(en_path, root)}: expected {spec.contract_id}, got {contract_id}"
            )
        if contract_type != spec.contract_type:
            warnings.append(
                f"contract type mismatch for {_relative(en_path, root)}: expected {spec.contract_type}, got {contract_type}"
            )

        missing_sections = [
            section
            for section in spec.required_sections
            if not _has_section_content(parsed["sections"].get(_normalize_section_name(section)))
        ]
        if missing_sections:
            warnings.append(
                f"missing required sections in {_relative(en_path, root)}: {', '.join(missing_sections)}"
            )

        contract = {
            "schema": "growware.stage23.contract.v1",
            "id": contract_id,
            "title": parsed["title"] or contract_id,
            "kind": kind,
            "status": status,
            "contract_type": contract_type,
            "owners": owners,
            "depends_on": depends_on,
            "required_sections": [_normalize_section_name(section) for section in spec.required_sections],
            "sections": parsed["sections"],
            "source_docs": [
                _relative(en_path, root),
                _relative(zh_path, root),
            ]
            if zh_path.exists()
            else [_relative(en_path, root)],
        }
        contracts.append(contract)
        source_docs.append(
            {
                "stem": spec.stem,
                "source": _relative(en_path, root),
                "translation": _relative(zh_path, root) if zh_path.exists() else None,
                "contract_id": contract_id,
                "contract_type": contract_type,
            }
        )
        files.append(
            {
                "path": str(contracts_dir / f"{spec.stem}.json"),
                "payload": contract,
            }
        )

    manifest = {
        "schema": "growware.stage23.manifest.v1",
        "contract_version": STAGE23_CONTRACT_VERSION,
        "generated_by": "growware/scripts/growware_stage23_contract_sync.py",
        "generated_at": datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "index": ".growware/stage-2-3/index.json",
        "contracts_dir": ".growware/stage-2-3/contracts",
    }
    index = {
        "schema": "growware.stage23.index.v1",
        "contracts": [
            {
                "id": contract["id"],
                "contract_type": contract["contract_type"],
                "status": contract["status"],
                "contract_file": f".growware/stage-2-3/contracts/{source_doc['stem']}.json",
                "source_docs": contract["source_docs"],
            }
            for contract, source_doc in zip(contracts, source_docs, strict=True)
        ],
    }
    provenance = {
        "schema": "growware.stage23.provenance.v1",
        "contract_version": STAGE23_CONTRACT_VERSION,
        "source_docs": source_docs,
        "warnings": warnings,
    }
    files = [
        {"path": str(compiled_dir / "manifest.json"), "payload": manifest},
        {"path": str(compiled_dir / "index.json"), "payload": index},
        {"path": str(compiled_dir / "provenance.json"), "payload": provenance},
        *files,
    ]

    return {
        "ok": not warnings and len(contracts) == len(DOC_SPECS),
        "projectRoot": str(root),
        "stage23ContractSourceDir": str(source_dir),
        "stage23Dir": str(compiled_dir),
        "contracts": contracts,
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


def write_stage23_contract_catalog(project_root: Path | None = None) -> dict[str, Any]:
    report = build_stage23_contract_catalog(project_root)
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


def validate_stage23_contract_catalog(project_root: Path | None = None) -> dict[str, Any]:
    report = build_stage23_contract_catalog(project_root)
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
    report.update(
        {
            "ok": not report["warnings"] and not missing and not mismatches and len(report["contracts"]) == len(DOC_SPECS),
            "missing": missing,
            "mismatches": mismatches,
        }
    )
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile or validate Growware Stage 2/3 contract docs into .growware.")
    parser.add_argument("--project-root", type=Path, default=resolve_project_root())
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def render_markdown(payload: dict[str, Any]) -> str:
    lines = ["# Growware Stage 2/3 Contract Sync", ""]
    lines.append(f"- ok: `{str(payload['ok']).lower()}`")
    lines.append(f"- changed: `{str(payload.get('changed', False)).lower()}`")
    lines.append(f"- project_root: `{payload['projectRoot']}`")
    lines.append(f"- stage23_contract_source_dir: `{payload['stage23ContractSourceDir']}`")
    lines.append(f"- stage23_dir: `{payload['stage23Dir']}`")
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
    lines.append("- contracts:")
    for contract in payload["contracts"]:
        lines.append(f"  - {contract['id']}: `{contract['contract_type']}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.check and args.write:
        raise SystemExit("--check and --write cannot be combined")
    payload = write_stage23_contract_catalog(args.project_root) if args.write else validate_stage23_contract_catalog(args.project_root)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(payload), end="")
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
