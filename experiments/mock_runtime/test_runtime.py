from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNTIME = REPO_ROOT / "experiments" / "mock_runtime" / "runtime.py"


class MockRuntimeSmokeTest(unittest.TestCase):
    def test_demo_flow(self) -> None:
        with tempfile.TemporaryDirectory(prefix="growware-mock-runtime-") as tmpdir:
            completed = subprocess.run(
                [sys.executable, str(RUNTIME), "demo", "--workspace", tmpdir],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(completed.stdout)
            self.assertTrue(payload["ok"])
            self.assertEqual(payload["steps"][0]["event"], "progress-pushed")
            self.assertEqual(payload["steps"][1]["event"], "incident-recorded")
            self.assertEqual(payload["steps"][2]["event"], "approval-requested")
            self.assertEqual(payload["steps"][3]["event"], "close-out-pushed")
            self.assertEqual(payload["steps"][4]["event"], "close-out-pushed")
            self.assertEqual(payload["state"]["incidents"][0]["current_state"], "closed")
            self.assertEqual(payload["state"]["approvals"][0]["status"], "approved")
            self.assertEqual(payload["final_status"]["approval_state"], "clear")
            executor_snapshot = payload["steps"][0]["payload"]["executor_snapshot"]
            self.assertTrue(executor_snapshot["ok"])
            self.assertEqual(
                [item["label"] for item in executor_snapshot["commands"]],
                [
                    "growware-project-summary",
                    "growware-preflight",
                    "growware-openclaw-binding-preview",
                ],
            )
            verification_snapshot = payload["steps"][2]["payload"]["executor_snapshot"]
            self.assertTrue(verification_snapshot["ok"])
            self.assertEqual(payload["state"]["verifications"][0]["executor_snapshot"]["executor_ref"], "project-bound-readonly-bridge")
            self.assertEqual(payload["state"]["counters"]["executor_run"], 2)

    def test_bridge_status_command(self) -> None:
        with tempfile.TemporaryDirectory(prefix="growware-mock-runtime-") as tmpdir:
            subprocess.run(
                [sys.executable, str(RUNTIME), "init", "--workspace", tmpdir],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            completed = subprocess.run(
                [sys.executable, str(RUNTIME), "bridge-status", "--workspace", tmpdir],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(completed.stdout)
            self.assertTrue(payload["ok"])
            self.assertEqual(payload["executor_snapshot"]["executor_mode"], "readonly-project-bridge")
            self.assertTrue(payload["executor_snapshot"]["commands"][1]["stdout"]["ok"])


if __name__ == "__main__":
    unittest.main()
