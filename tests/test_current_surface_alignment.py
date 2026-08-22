from __future__ import annotations

import json
import unittest
from pathlib import Path


class CurrentSurfaceAlignmentTests(unittest.TestCase):
    def test_legacy_families_are_not_current_reader_surfaces(self) -> None:
        manifest = json.loads(Path("CURRENT-SURFACE-MANIFEST.json").read_text(encoding="utf-8"))
        legacy_prefixes = (
            "00_meta/",
            "00_mother-law/",
            "01_native-board/",
            "01_runtime-spine/",
            "02_runtime-ops/",
            "02_translation-layer/",
            "03_board-orchestration/",
            "03_field-governance/",
            "04_adapter-layer/",
            "04_interface-layer/",
            "05_XLEN_Reserve_Unenabled/",
            "05_topology/",
        )

        surfaces: list[str] = list(manifest["reader_priority"])
        for values in manifest["current_public_surfaces"].values():
            surfaces.extend(values)

        for surface in surfaces:
            self.assertFalse(
                surface.startswith(legacy_prefixes),
                f"legacy surface unexpectedly Current-readable: {surface}",
            )

    def test_manifest_declares_carrier_and_folder_non_ontology(self) -> None:
        manifest = json.loads(Path("CURRENT-SURFACE-MANIFEST.json").read_text(encoding="utf-8"))
        model = manifest["classification_model"]
        carrier = manifest["carrier_model"]
        self.assertTrue(model["do_not_treat_folder_as_ontology"])
        self.assertTrue(model["do_not_treat_carrier_as_identity"])
        self.assertTrue(carrier["carrier_change_does_not_change_identity"])
        self.assertTrue(carrier["extension_is_not_taxonomy"])

    def test_historical_reader_shield_blocks_stale_reactivation(self) -> None:
        manifest = json.loads(Path("CURRENT-SURFACE-MANIFEST.json").read_text(encoding="utf-8"))
        shield = manifest["historical_reader_shield"]
        self.assertTrue(shield["root_legacy_visibility_does_not_establish_current"])
        self.assertTrue(shield["stale_register_reference_does_not_reactivate_retired_artifact"])
        self.assertFalse(shield["whole_body_reread_as_current"])


if __name__ == "__main__":
    unittest.main()
