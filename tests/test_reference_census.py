from __future__ import annotations

import unittest

from dcp_kernel.reference_census import (
    DependencySignal,
    ReferenceClass,
    classify_dependency_signal,
    classify_reference,
    has_proven_live_caller,
    has_rebuild_relevant_reference,
    has_unknown_hold,
    has_wake_routing_relevant_reference,
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
        self.assertFalse(has_rebuild_relevant_reference(observations, "01_runtime-spine"))
        self.assertFalse(has_wake_routing_relevant_reference(observations, "01_runtime-spine"))

    def test_unknown_reference_blocks_clean_audit_and_dependency_withdrawal(self) -> None:
        files = {"misc/map.md": "03_field-governance/CO_FIELD_DEPENDENCY_MODEL_v0_1.md"}
        observations = scan_text_map(files, ("03_field-governance",))
        self.assertTrue(has_unknown_hold(observations, "03_field-governance"))
        self.assertTrue(has_rebuild_relevant_reference(observations, "03_field-governance"))
        self.assertTrue(has_wake_routing_relevant_reference(observations, "03_field-governance"))

    def test_live_rebuild_reference_is_flagged_for_bounded_review(self) -> None:
        files = {
            "dcp_kernel/platform.py": "legacy fallback rebuild from 03_field-governance/RECOMPOSITION_ENGINE_v0_1.md"
        }
        observations = scan_text_map(files, ("03_field-governance",))
        self.assertTrue(has_proven_live_caller(observations, "03_field-governance"))
        self.assertTrue(has_rebuild_relevant_reference(observations, "03_field-governance"))
        self.assertEqual(observations[0].dependency_signal, DependencySignal.REBUILD_RELEVANT)

    def test_live_wake_reference_is_flagged_for_bounded_review(self) -> None:
        signal = classify_dependency_signal(
            caller_path="CURRENT-SURFACE-MANIFEST.json",
            classification=ReferenceClass.LIVE_CALLER,
            excerpt="reader routing points to 04_adapter-layer/activation_order.md",
        )
        self.assertEqual(signal, DependencySignal.WAKE_ROUTING_RELEVANT)

    def test_lineage_pointer_does_not_create_rebuild_or_wake_dependency(self) -> None:
        signal = classify_dependency_signal(
            caller_path="REPOSITORY_CORPUS_INDEX.md",
            classification=ReferenceClass.LINEAGE_POINTER,
            excerpt="rebuild history 01_runtime-spine/window_linking_logic_01_07.md",
        )
        self.assertEqual(signal, DependencySignal.NONE)


if __name__ == "__main__":
    unittest.main()
