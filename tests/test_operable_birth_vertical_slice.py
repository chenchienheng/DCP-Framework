from __future__ import annotations

import unittest

from dcp_kernel.models import Decision
from dcp_kernel.operable_birth import BirthDisposition, OperableBirthInput, assess_operable_birth
from dcp_kernel.public_encounter import PublicEncounterInput, assess_public_encounter
from dcp_kernel.reception_gateway import GatewayDisposition, GatewayInput, assess_gateway_request
from dcp_kernel.relation_semantics import RelationInput, RelationState, assess_relation


class OperableBirthVerticalSliceTests(unittest.TestCase):
    def test_external_request_can_reach_bounded_projection_without_owner_as_api_gateway(self) -> None:
        gateway = assess_gateway_request(
            GatewayInput(
                request_id="EXT-1",
                source_identified=True,
                scope_bounded=True,
                rights_valid=True,
                material_event=True,
                affected_receivers=("DCP", "GLMODEL"),
            )
        )
        self.assertEqual(gateway.decision, Decision.PASS)
        self.assertEqual(gateway.disposition, GatewayDisposition.ROUTE)
        self.assertFalse(gateway.escalate_to_owner)

        relation = assess_relation(
            RelationInput(
                source_identity_resolved=True,
                target_identity_resolved=True,
                direction_known=True,
                reciprocity_relevant=True,
                reciprocity_defined=True,
                state_defined=True,
                time_defined=True,
                evidence_defined=True,
                authority_relevant=True,
                authority_defined=True,
                effect_defined=True,
                return_path_relevant=True,
                return_path_defined=True,
            )
        )
        self.assertEqual(relation.state, RelationState.MATERIAL_RELATION)

        encounter = assess_public_encounter(
            PublicEncounterInput(
                capability_id="RELATION-VIEW",
                material_public_delta=True,
                native_capability_evidence_present=True,
                lawful_source_rights=True,
                privacy_boundary_preserved=True,
                native_body_exposed=False,
                bounded_scope=True,
                claim_within_capability_evidence=True,
                authority_transfer_implied=False,
                revocable=True,
                external_evidence_return_path=True,
                release_approved=False,
            )
        )
        self.assertTrue(encounter.projection_candidate)
        self.assertFalse(encounter.release_authorized)

        birth_before_rebuild = assess_operable_birth(
            OperableBirthInput(
                existence_resolved=True,
                relation_resolved=True,
                event_materiality_resolved=True,
                judgment_before_capability=True,
                capability_bound=True,
                action_gated=True,
                evidence_recorded=True,
                receiver_disposition_observed=False,
                rebuild_applied=False,
                new_state_observed=False,
                retested=False,
            )
        )
        self.assertEqual(birth_before_rebuild.disposition, BirthDisposition.RETURN_NOT_REBUILT)

        birth_after_rebuild = assess_operable_birth(
            OperableBirthInput(
                existence_resolved=True,
                relation_resolved=True,
                event_materiality_resolved=True,
                judgment_before_capability=True,
                capability_bound=True,
                action_gated=True,
                evidence_recorded=True,
                receiver_disposition_observed=True,
                rebuild_applied=True,
                new_state_observed=True,
                retested=True,
            )
        )
        self.assertEqual(birth_after_rebuild.decision, Decision.PASS)
        self.assertEqual(birth_after_rebuild.disposition, BirthDisposition.OPERABLE_BIRTH_DELTA)


if __name__ == "__main__":
    unittest.main()
