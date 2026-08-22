from __future__ import annotations

import unittest

from dcp_kernel.reference_census import (
    ReferenceClass,
    classify_reference,
    has_proven_live_caller,
    has_unknown_hold,
    scan_text_map,
)


class ReferenceCensusTests(unittest.TestCase):
    def test_current_surface_reference_is_live(self) -> None:
        self.assertEqual(
            classify_reference("CURRENT-SURFACE-MANIFEST.json", "01_runtime-spine"),
            ReferenceClass.LIVE_CALLER,
        )

    def test_executable_reference_is_live(self) -> None:
        self.assertEqual(
            classify_reference("dcp_kernel/platform.py", "03_field-governance"),
            ReferenceClass.LIVE_CALLER,
        )

    def test_legacy_family_self_reference_is_not_live_caller(self) -> None:
        self.assertEqual(
            classify_reference("04_adapter-layer/README.md", "04_adapter-layer"),
            ReferenceClass.SELF_REFERENCE,
        )

    def test_historical_index_reference_is_lineage_pointer(self) -> None:
        self.assertEqual(
            classify_reference("REPOSITORY_CORPUS_INDEX.md", "04_adapter-layer"),
            ReferenceClass.LINEAGE_POINTER,
        )

    def test_unknown_surface_stays_hold(self) -> None:
        self.assertEqual(
            classify_reference("misc/unclassified-map.md", "03_field-governance"),
            ReferenceClass.UNKNOWN_HOLD,
        )

    def test_search_hit_is_not_implicitly_live(self) -> None:
        files = {
            "REPOSITORY_CORPUS_INDEX.md": "legacy path: 01_runtime-spine/",
            "CURRENT-SURFACE-MANIFEST.json": "no legacy reference here",
        }
        observations = scan_text_map(files, ("01_runtime-spine",))
        self.assertFalse(has_proven_live_caller(observations, "01_runtime-spine"))
        self.assertFalse(has_unknown_hold(observations, "01_runtime-spine"))

    def test_unknown_reference_blocks_clean_audit(self) -> None:
        files = {"misc/map.md": "03_field-governance/CO_FIELD_DEPENDENCY_MODEL_v0_1.md"}
        observations = scan_text_map(files, ("03_field-governance",))
        self.assertTrue(has_unknown_hold(observations, "03_field-governance"))


if __name__ == "__main__":
    unittest.main()
