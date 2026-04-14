#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DAEMON_CONTRACTS_DIR = REPO_ROOT / ".growware" / "daemon-foundation" / "contracts"
STAGE23_CONTRACTS_DIR = REPO_ROOT / ".growware" / "stage-2-3" / "contracts"
POLICY_RULES_DIR = REPO_ROOT / ".policy" / "rules"
STATE_FILENAME = "state.json"
CAPSULE_FILENAME = "project_capsule.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def next_id(state: dict, counter_name: str, prefix: str) -> str:
    counters = state["counters"]
    counters[counter_name] += 1
    return f"{prefix}-{counters[counter_name]:04d}"


def parse_contract_field(item: str) -> str:
    field = item.strip()
    if field.startswith("`"):
        return field.split("`", 2)[1]
    return field.split(":", 1)[0].strip()


def contract_field_names(contract: dict, section_name: str) -> list[str]:
    items = contract["sections"][section_name]["items"]
    return [parse_contract_field(item) for item in items]


def load_contracts() -> dict:
    contracts = {
        "project_capsule": load_json(DAEMON_CONTRACTS_DIR / "project-capsule.json"),
        "command_model": load_json(DAEMON_CONTRACTS_DIR / "channel-command-model.json"),
        "progress_push": load_json(DAEMON_CONTRACTS_DIR / "progress-push.json"),
        "policy_loading": load_json(DAEMON_CONTRACTS_DIR / "policy-loading.json"),
        "execution_handoff": load_json(DAEMON_CONTRACTS_DIR / "execution-handoff.json"),
        "learning_writeback": load_json(DAEMON_CONTRACTS_DIR / "learning-writeback.json"),
        "incident_lifecycle": load_json(STAGE23_CONTRACTS_DIR / "incident-lifecycle.json"),
        "verification_profile": load_json(STAGE23_CONTRACTS_DIR / "verification-profile.json"),
        "deployment_gate": load_json(STAGE23_CONTRACTS_DIR / "deployment-gate.json"),
        "close_out": load_json(STAGE23_CONTRACTS_DIR / "close-out-provenance.json"),
        "judge_promotion": load_json(STAGE23_CONTRACTS_DIR / "judge-promotion.json"),
        "automation_bands": load_json(STAGE23_CONTRACTS_DIR / "automation-bands.json"),
        "regression_assets": load_json(STAGE23_CONTRACTS_DIR / "regression-assets.json"),
        "policy_rule": load_json(next(POLICY_RULES_DIR.glob("*.json"))),
    }
    return contracts


def ensure_machine_layers() -> None:
    required_files = [
        REPO_ROOT / ".growware" / "daemon-foundation" / "manifest.json",
        REPO_ROOT / ".growware" / "stage-2-3" / "manifest.json",
        REPO_ROOT / ".policy" / "manifest.json",
    ]
    missing = [str(path) for path in required_files if not path.exists()]
    if missing:
        raise SystemExit(json.dumps({"ok": False, "error": "machine-layers-missing", "missing": missing}, indent=2))


def default_capsule(workspace: Path) -> dict:
    target_root = REPO_ROOT.parent / "openclaw-task-system"
    if target_root.exists():
        project_root = str(target_root.resolve())
        control_surface_root = str((target_root / ".growware").resolve())
    else:
        project_root = "UNBOUND-EXPERIMENTAL-PILOT"
        control_surface_root = "UNBOUND-EXPERIMENTAL-CONTROL-SURFACE"
    return {
        "project_id": "project-1.openclaw-task-system",
        "project_label": "Project 1 Experimental Capsule",
        "project_root": project_root,
        "control_surface_root": control_surface_root,
        "phase": "experimental-runtime-v0",
        "execution_line": "status -> incident -> verify -> approval-wait -> close-out",
        "blockers": [],
        "approval_boundary": {
            "deploy": "approval-required",
            "rollback": "approval-required",
            "user_visible_change": "approval-required",
        },
        "policy_source_docs": [
            "docs/policy/project-1.md",
            "docs/policy/project-1.zh-CN.md",
        ],
        "policy_machine_manifest": ".policy/manifest.json",
        "validation_entrypoints": [
            "python3 scripts/growware_daemon_contract_sync.py --check --json",
            "python3 scripts/growware_stage23_contract_sync.py --check --json",
            "python3 scripts/growware_policy_sync.py --check --json",
            "python3 scripts/runtime/growware_preflight.py --json",
            "python3 scripts/runtime/growware_openclaw_binding.py --json",
        ],
        "deploy_entrypoints": ["experimental-mock-runtime:no-deploy"],
        "rollback_entrypoints": ["experimental-mock-runtime:no-rollback"],
        "channel_bindings": ["feishu6", "mock://growware/demo"],
        "executor_ref": "project-bound-readonly-bridge",
        "executor_mode": "readonly-project-bridge",
        "status_updated_at": utc_now(),
        "workspace_root": str(workspace.resolve()),
    }


def default_state() -> dict:
    return {
        "schema": "growware.mock-runtime.state.v0",
        "phase": "experimental-runtime-v0",
        "execution_line": "status -> incident -> verify -> approval-wait -> close-out",
        "counters": {
            "incident": 0,
            "verification": 0,
            "approval": 0,
            "closeout": 0,
            "writeback": 0,
            "judge_candidate": 0,
            "executor_run": 0,
        },
        "incidents": [],
        "verifications": [],
        "approvals": [],
        "closeouts": [],
        "writebacks": [],
        "judge_candidates": [],
        "executor_runs": [],
        "events": [],
    }


def validate_capsule(capsule: dict, contracts: dict) -> None:
    required_fields = contract_field_names(contracts["project_capsule"], "required_fields")
    missing = [field for field in required_fields if field not in capsule]
    if missing:
        raise SystemExit(json.dumps({"ok": False, "error": "capsule-missing-fields", "missing": missing}, indent=2))


def load_workspace(workspace: Path, contracts: dict) -> tuple[dict, dict]:
    capsule_path = workspace / CAPSULE_FILENAME
    state_path = workspace / STATE_FILENAME
    if not capsule_path.exists() or not state_path.exists():
        raise SystemExit(
            json.dumps(
                {"ok": False, "error": "workspace-not-initialized", "workspace": str(workspace)},
                indent=2,
            )
        )
    capsule = load_json(capsule_path)
    validate_capsule(capsule, contracts)
    state = load_json(state_path)
    return capsule, state


def save_workspace(workspace: Path, capsule: dict, state: dict) -> None:
    capsule["status_updated_at"] = utc_now()
    write_json(workspace / CAPSULE_FILENAME, capsule)
    write_json(workspace / STATE_FILENAME, state)


def target_project_root(capsule: dict) -> Path | None:
    project_root = capsule.get("project_root")
    if not project_root or project_root.startswith("UNBOUND-"):
        return None
    return Path(project_root).resolve()


def executor_spec(capsule: dict) -> list[tuple[str, list[str]]]:
    return [
        ("growware-project-summary", ["python3", "-c", EXECUTOR_SUMMARY_SNIPPET]),
        ("growware-preflight", ["python3", "scripts/runtime/growware_preflight.py", "--json"]),
        ("growware-openclaw-binding-preview", ["python3", "scripts/runtime/growware_openclaw_binding.py", "--json"]),
    ]


EXECUTOR_SUMMARY_SNIPPET = (
    "import json; "
    "from scripts.runtime.growware_project import build_summary; "
    "print(json.dumps(build_summary(), ensure_ascii=True))"
)


def parse_command_output(stdout: str) -> dict | None:
    text = stdout.strip()
    if not text:
        return None
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def run_project_executor_snapshot(capsule: dict, state: dict) -> dict:
    project_root = target_project_root(capsule)
    run_id = next_id(state, "executor_run", "EXR")
    snapshot = {
        "executor_run_id": run_id,
        "executor_ref": capsule.get("executor_ref"),
        "executor_mode": capsule.get("executor_mode", "readonly-project-bridge"),
        "project_id": capsule["project_id"],
        "project_root": str(project_root) if project_root else capsule.get("project_root"),
        "started_at": utc_now(),
        "commands": [],
        "ok": False,
    }
    if project_root is None or not project_root.exists():
        snapshot["finished_at"] = utc_now()
        snapshot["error"] = "project-root-unavailable"
        state["executor_runs"].append(snapshot)
        return snapshot

    for label, argv in executor_spec(capsule):
        completed = subprocess.run(
            argv,
            cwd=project_root,
            check=False,
            capture_output=True,
            text=True,
            timeout=120,
        )
        command_record = {
            "label": label,
            "argv": argv,
            "cwd": str(project_root),
            "exit_code": completed.returncode,
            "ok": completed.returncode == 0,
            "stdout": parse_command_output(completed.stdout),
            "stdout_text": completed.stdout.strip() if not parse_command_output(completed.stdout) else "",
            "stderr_text": completed.stderr.strip(),
            "finished_at": utc_now(),
        }
        snapshot["commands"].append(command_record)
        if completed.returncode != 0:
            snapshot["finished_at"] = utc_now()
            snapshot["ok"] = False
            snapshot["error"] = f"{label}-failed"
            state["executor_runs"].append(snapshot)
            return snapshot

    snapshot["finished_at"] = utc_now()
    snapshot["ok"] = True
    state["executor_runs"].append(snapshot)
    return snapshot


def gate_requires_approval(deployment_gate: dict, action_class: str) -> bool:
    gate_decisions = deployment_gate["sections"]["gate_decisions"]["items"]
    for decision in gate_decisions:
        if decision.startswith(f"`{action_class}`"):
            return "stop for approval" in decision
    return True


def emit_event(state: dict, event_name: str, payload: dict) -> dict:
    event = {"event": event_name, "emitted_at": utc_now(), "payload": payload}
    state["events"].append(event)
    return event


def counts_summary(state: dict) -> dict:
    return {
        "incidents_total": len(state["incidents"]),
        "incidents_open": sum(1 for item in state["incidents"] if item["current_state"] != "closed"),
        "approvals_pending": sum(1 for item in state["approvals"] if item["status"] == "pending"),
        "closeouts_total": len(state["closeouts"]),
    }


def status_payload(capsule: dict, state: dict) -> dict:
    counts = counts_summary(state)
    next_action = "report an incident"
    approval_state = "clear"
    pending = [item for item in state["approvals"] if item["status"] == "pending"]
    if pending:
        next_action = f"approve {pending[0]['incident_id']}"
        approval_state = "pending"
    elif counts["incidents_open"]:
        next_action = "continue the oldest open incident"
    return {
        "message_type": "progress-snapshot",
        "project_id": capsule["project_id"],
        "phase": capsule["phase"],
        "execution_line": capsule["execution_line"],
        "summary": f"{counts['incidents_open']} open incidents, {counts['approvals_pending']} pending approvals",
        "next_action": next_action,
        "blockers": capsule["blockers"],
        "approval_state": approval_state,
        "provenance": "daemon-owned",
        "counts": counts,
        "executor_ref": capsule.get("executor_ref"),
    }


def find_incident(state: dict, incident_id: str | None) -> dict:
    incidents = state["incidents"]
    if incident_id:
        for incident in incidents:
            if incident["incident_id"] == incident_id:
                return incident
        raise SystemExit(json.dumps({"ok": False, "error": "incident-not-found", "incident_id": incident_id}, indent=2))
    for incident in incidents:
        if incident["current_state"] not in {"closed", "blocked"}:
            return incident
    raise SystemExit(json.dumps({"ok": False, "error": "no-open-incident"}, indent=2))


def find_approval(state: dict, incident_id: str) -> dict:
    for approval in state["approvals"]:
        if approval["incident_id"] == incident_id and approval["status"] == "pending":
            return approval
    raise SystemExit(json.dumps({"ok": False, "error": "approval-not-found", "incident_id": incident_id}, indent=2))


def init_workspace_command(args: argparse.Namespace) -> dict:
    workspace = Path(args.workspace).resolve()
    if workspace.exists() and args.reset:
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True, exist_ok=True)
    capsule = default_capsule(workspace)
    state = default_state()
    save_workspace(workspace, capsule, state)
    return {"ok": True, "workspace": str(workspace), "capsule": capsule}


def status_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    capsule, state = load_workspace(workspace, contracts)
    executor_snapshot = run_project_executor_snapshot(capsule, state)
    payload = status_payload(capsule, state)
    payload["executor_snapshot"] = executor_snapshot
    event = emit_event(state, "progress-pushed", payload)
    save_workspace(workspace, capsule, state)
    return {"ok": True, "workspace": str(workspace), **event}


def incident_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    capsule, state = load_workspace(workspace, contracts)
    incident_id = next_id(state, "incident", "INC")
    now = utc_now()
    action_class = args.action_class
    incident = {
        "project_id": capsule["project_id"],
        "incident_id": incident_id,
        "source": "human-feedback",
        "summary": args.summary,
        "severity": args.severity,
        "problem_type": args.problem_type,
        "evidence_refs": [f"mock-channel:{args.channel_ref}:{incident_id}"],
        "current_state": "intake",
        "approval_required": gate_requires_approval(contracts["deployment_gate"], action_class),
        "opened_at": now,
        "updated_at": now,
        "action_class": action_class,
        "requested_effect": args.requested_effect,
        "approval_state": "not-requested",
    }
    state["incidents"].append(incident)
    event = emit_event(state, "incident-recorded", incident)
    save_workspace(workspace, capsule, state)
    return {"ok": True, "workspace": str(workspace), **event}


def continue_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    capsule, state = load_workspace(workspace, contracts)
    incident = find_incident(state, args.incident_id)
    now = utc_now()
    incident["current_state"] = "verify"
    incident["updated_at"] = now
    executor_snapshot = run_project_executor_snapshot(capsule, state)
    if not executor_snapshot["ok"]:
        incident["current_state"] = "blocked"
        incident["approval_state"] = "clear"
        incident["blocked_reason"] = executor_snapshot.get("error", "executor-bridge-failed")
        payload = status_payload(capsule, state)
        payload["summary"] = f"{incident['incident_id']} blocked because the readonly project bridge failed"
        payload["next_action"] = "review executor bridge"
        payload["executor_snapshot"] = executor_snapshot
        event = emit_event(state, "progress-pushed", payload)
        save_workspace(workspace, capsule, state)
        return {"ok": True, "workspace": str(workspace), **event}

    verification_id = next_id(state, "verification", "VER")
    verification = {
        "verification_id": verification_id,
        "incident_id": incident["incident_id"],
        "change_scope": "readonly-project-bridge-and-state-transition",
        "checks_run": [
            "daemon-contract-load",
            "stage23-contract-load",
            "policy-load",
            "approval-gate-eval",
            "project-bound-readonly-bridge",
        ],
        "verification_mode": "scope-check",
        "result": "pass",
        "evidence_refs": [
            ".growware/daemon-foundation/manifest.json",
            ".growware/stage-2-3/manifest.json",
            ".policy/manifest.json",
            executor_snapshot["executor_run_id"],
        ],
        "residual_risk": "readonly project-bound bridge succeeded, but target-project mutation, deploy, and rollback remain unimplemented",
        "regression_asset_ref": "",
        "verified_at": now,
        "executor_snapshot": executor_snapshot,
    }
    state["verifications"].append(verification)

    if gate_requires_approval(contracts["deployment_gate"], incident["action_class"]):
        incident["current_state"] = "approval-wait"
        incident["approval_state"] = "pending"
        approval_id = next_id(state, "approval", "APR")
        approval = {
            "approval_id": approval_id,
            "project_id": capsule["project_id"],
            "incident_id": incident["incident_id"],
            "action_class": incident["action_class"],
            "requested_effect": incident["requested_effect"],
            "verification_ref": verification_id,
            "risk_summary": verification["residual_risk"],
            "requested_at": now,
            "status": "pending",
        }
        state["approvals"].append(approval)
        payload = {
            "message_type": "approval-request",
            "project_id": capsule["project_id"],
            "phase": capsule["phase"],
            "execution_line": capsule["execution_line"],
            "summary": f"{incident['incident_id']} requires approval before any deploy-affecting step",
            "next_action": f"approve {incident['incident_id']}",
            "blockers": capsule["blockers"],
            "approval_state": "pending",
            "provenance": "daemon-owned",
            "approval": approval,
            "verification": verification,
            "executor_snapshot": executor_snapshot,
        }
        event = emit_event(state, "approval-requested", payload)
    else:
        payload = status_payload(capsule, state)
        payload["executor_snapshot"] = executor_snapshot
        event = emit_event(state, "progress-pushed", payload)
    save_workspace(workspace, capsule, state)
    return {"ok": True, "workspace": str(workspace), **event}


def create_writebacks(state: dict, capsule: dict, incident: dict, verification: dict) -> list[str]:
    now = utc_now()
    writeback_ids: list[str] = []

    writeback_id = next_id(state, "writeback", "WB")
    writeback = {
        "proposal_id": writeback_id,
        "proposal_type": "regression-asset-proposal",
        "project_id": capsule["project_id"],
        "source_execution": "daemon-owned",
        "problem_summary": incident["summary"],
        "resolution_summary": "synthetic close-out after explicit approval",
        "candidate_asset": "deferred-gap",
        "target_surface": ".growware/stage-2-3/contracts/regression-assets.json",
        "evidence_refs": [verification["verification_id"], incident["incident_id"]],
        "approval_state": "review-required",
        "created_at": now,
    }
    state["writebacks"].append(writeback)
    writeback_ids.append(writeback_id)

    similar_closed = [
        item
        for item in state["incidents"]
        if item["problem_type"] == incident["problem_type"]
        and item["current_state"] == "closed"
        and item["incident_id"] != incident["incident_id"]
    ]
    if similar_closed:
        judge_candidate_id = next_id(state, "judge_candidate", "JDG")
        candidate = {
            "judge_candidate_id": judge_candidate_id,
            "judge_class": "approval-needed",
            "source_incident_refs": [incident["incident_id"]] + [item["incident_id"] for item in similar_closed],
            "judgment_summary": "user-visible changes repeatedly require explicit approval",
            "candidate_rule": "keep deploy-affecting work approval-gated until a narrower contract exists",
            "candidate_surface": ".growware/stage-2-3/contracts/judge-promotion.json",
            "approval_state": "review-required",
            "created_at": now,
        }
        state["judge_candidates"].append(candidate)
        writeback_ids.append(judge_candidate_id)
    return writeback_ids


def approve_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    capsule, state = load_workspace(workspace, contracts)
    incident = find_incident(state, args.incident_id)
    approval = find_approval(state, incident["incident_id"])
    verification = next(item for item in reversed(state["verifications"]) if item["incident_id"] == incident["incident_id"])
    now = utc_now()

    approval["status"] = "approved"
    approval["approved_at"] = now
    incident["current_state"] = "closed"
    incident["approval_state"] = "approved"
    incident["updated_at"] = now
    writeback_refs = create_writebacks(state, capsule, incident, verification)
    closeout_id = next_id(state, "closeout", "CLS")
    closeout = {
        "closeout_id": closeout_id,
        "project_id": capsule["project_id"],
        "incident_id": incident["incident_id"],
        "execution_source": "daemon-owned",
        "result_summary": "mock runtime completed a synthetic close-out after explicit approval; no deploy was executed",
        "verification_refs": [verification["verification_id"]],
        "writeback_refs": writeback_refs,
        "residual_risk": "readonly bridge reached the real project workspace, but target-project mutation, deploy, and rollback remain unimplemented",
        "follow_up_needed": "widen the readonly bridge into a project-bound executor only with explicit approval",
        "closed_at": now,
        "channel_close_received_at": "",
    }
    state["closeouts"].append(closeout)
    payload = {
        "message_type": "close-out",
        "project_id": capsule["project_id"],
        "phase": capsule["phase"],
        "execution_line": capsule["execution_line"],
        "summary": f"{incident['incident_id']} closed in mock runtime after explicit approval",
        "next_action": "review writeback proposals",
        "blockers": capsule["blockers"],
        "approval_state": "approved",
        "provenance": "daemon-owned",
        "result": closeout["result_summary"],
        "validation_refs": closeout["verification_refs"],
        "execution_source": closeout["execution_source"],
        "writeback_refs": closeout["writeback_refs"],
        "follow_up_needed": closeout["follow_up_needed"],
        "closeout": closeout,
        "executor_snapshot": verification.get("executor_snapshot"),
    }
    event = emit_event(state, "close-out-pushed", payload)
    save_workspace(workspace, capsule, state)
    return {"ok": True, "workspace": str(workspace), **event}


def block_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    capsule, state = load_workspace(workspace, contracts)
    incident = find_incident(state, args.incident_id)
    incident["current_state"] = "blocked"
    incident["blocked_reason"] = args.reason
    incident["updated_at"] = utc_now()
    payload = status_payload(capsule, state)
    payload["summary"] = f"{incident['incident_id']} blocked: {args.reason}"
    payload["next_action"] = "review blocker"
    payload["approval_state"] = incident.get("approval_state", "clear")
    event = emit_event(state, "progress-pushed", payload)
    save_workspace(workspace, capsule, state)
    return {"ok": True, "workspace": str(workspace), **event}


def close_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    capsule, state = load_workspace(workspace, contracts)
    for closeout in state["closeouts"]:
        if closeout["incident_id"] == args.incident_id:
            closeout["channel_close_received_at"] = utc_now()
            payload = {
                "message_type": "close-out",
                "project_id": capsule["project_id"],
                "phase": capsule["phase"],
                "execution_line": capsule["execution_line"],
                "summary": f"{args.incident_id} close-out acknowledged by the channel side",
                "next_action": "none",
                "blockers": capsule["blockers"],
                "approval_state": "approved",
                "provenance": "daemon-owned",
                "result": closeout["result_summary"],
                "validation_refs": closeout["verification_refs"],
                "execution_source": closeout["execution_source"],
                "writeback_refs": closeout["writeback_refs"],
                "follow_up_needed": closeout["follow_up_needed"],
                "closeout": closeout,
            }
            event = emit_event(state, "close-out-pushed", payload)
            save_workspace(workspace, capsule, state)
            return {"ok": True, "workspace": str(workspace), **event}
    raise SystemExit(json.dumps({"ok": False, "error": "closeout-not-found", "incident_id": args.incident_id}, indent=2))


def demo_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    init_workspace_command(argparse.Namespace(workspace=str(workspace), reset=True))
    steps = [
        status_command(argparse.Namespace(workspace=str(workspace)), contracts),
        incident_command(
            argparse.Namespace(
                workspace=str(workspace),
                summary="Channel reply missing after task completion",
                severity="medium",
                problem_type="user-visible-gap",
                action_class="user-visible-change",
                requested_effect="restore user-visible completion reply",
                channel_ref="mock://growware/demo",
            ),
            contracts,
        ),
        continue_command(argparse.Namespace(workspace=str(workspace), incident_id=None), contracts),
        approve_command(argparse.Namespace(workspace=str(workspace), incident_id="INC-0001"), contracts),
        close_command(argparse.Namespace(workspace=str(workspace), incident_id="INC-0001"), contracts),
    ]
    capsule, state = load_workspace(workspace, contracts)
    return {
        "ok": True,
        "workspace": str(workspace),
        "steps": steps,
        "final_status": status_payload(capsule, state),
        "state": state,
    }


def bridge_status_command(args: argparse.Namespace, contracts: dict) -> dict:
    workspace = Path(args.workspace).resolve()
    if not (workspace / CAPSULE_FILENAME).exists() or not (workspace / STATE_FILENAME).exists():
        init_workspace_command(argparse.Namespace(workspace=str(workspace), reset=False))
    capsule, state = load_workspace(workspace, contracts)
    snapshot = run_project_executor_snapshot(capsule, state)
    save_workspace(workspace, capsule, state)
    return {"ok": snapshot["ok"], "workspace": str(workspace), "executor_snapshot": snapshot}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Growware experimental mock runtime")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="initialize an isolated experimental workspace")
    init_parser.add_argument("--workspace", required=True)
    init_parser.add_argument("--reset", action="store_true")

    status_parser = subparsers.add_parser("status", help="emit a progress snapshot")
    status_parser.add_argument("--workspace", required=True)

    incident_parser = subparsers.add_parser("incident", help="record a mock incident")
    incident_parser.add_argument("--workspace", required=True)
    incident_parser.add_argument("--summary", required=True)
    incident_parser.add_argument("--severity", default="medium")
    incident_parser.add_argument("--problem-type", default="user-visible-gap")
    incident_parser.add_argument("--action-class", default="user-visible-change")
    incident_parser.add_argument("--requested-effect", default="restore user-visible behavior")
    incident_parser.add_argument("--channel-ref", default="mock://growware/demo")

    continue_parser = subparsers.add_parser("continue", help="advance the oldest open incident")
    continue_parser.add_argument("--workspace", required=True)
    continue_parser.add_argument("--incident-id")

    approve_parser = subparsers.add_parser("approve", help="approve a pending incident")
    approve_parser.add_argument("--workspace", required=True)
    approve_parser.add_argument("--incident-id", required=True)

    block_parser = subparsers.add_parser("block", help="block an open incident")
    block_parser.add_argument("--workspace", required=True)
    block_parser.add_argument("--incident-id", required=True)
    block_parser.add_argument("--reason", required=True)

    close_parser = subparsers.add_parser("close", help="acknowledge a close-out")
    close_parser.add_argument("--workspace", required=True)
    close_parser.add_argument("--incident-id", required=True)

    bridge_parser = subparsers.add_parser("bridge-status", help="run the readonly project-bound executor bridge")
    bridge_parser.add_argument("--workspace", required=True)

    demo_parser = subparsers.add_parser("demo", help="run the full isolated demo flow")
    demo_parser.add_argument("--workspace", required=True)
    return parser


def main() -> int:
    ensure_machine_layers()
    parser = build_parser()
    args = parser.parse_args()
    contracts = load_contracts()

    command_handlers = {
        "init": lambda: init_workspace_command(args),
        "status": lambda: status_command(args, contracts),
        "incident": lambda: incident_command(args, contracts),
        "continue": lambda: continue_command(args, contracts),
        "approve": lambda: approve_command(args, contracts),
        "block": lambda: block_command(args, contracts),
        "close": lambda: close_command(args, contracts),
        "bridge-status": lambda: bridge_status_command(args, contracts),
        "demo": lambda: demo_command(args, contracts),
    }
    payload = command_handlers[args.command]()
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
