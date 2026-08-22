from __future__ import annotations

import json
import unittest
from pathlib import Path


class RootControlSurfaceRetirementTests(unittest.TestCase):
    def payload(self):
        root = Path(__file__).resolve().parents[1]
        return json.loads((root / "fixtures" / "repository" / "root-control-surface-retirement.json").read_text())

    def test_retired_root_surfaces_are_absent_and_successor_bound(self):
        payload = self.payload()
        self.assertEqual(len(payload["retired_surfaces"]), 5)
        for item in payload["retired_surfaces"]:
            self.assertEqual(item["physical_state_on_successor_branch"], "ABSENT")
            self.assertTrue(item["retired_semantics"])
            self.assertTrue(item["successor"])

    def test_retirement_does_not_recreate_central_controller(self):
        payload = self.payload()
        invariants = set(payload["invariants"])
        self.assertIn("SUCCESSOR_CAPABILITIES_DO_NOT_RECREATE_A_CENTRAL_CONTROLLER", invariants)
        self.assertIn("RETURN_RECONCILES_TO_NATIVE_RECEIVER_NOT_CENTRAL_REGISTRY", invariants)
        self.assertFalse(payload["runtime"])
        self.assertFalse(payload["promotion"])
        self.assertFalse(payload["destructive_reclaim_authorized"])


if __name__ == "__main__":
    unittest.main()
