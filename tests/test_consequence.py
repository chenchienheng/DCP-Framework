from __future__ import annotations

import unittest

from dcp_kernel.consequence import (
    ConsequenceInput,
    compile_action_responsibility,
    derive_next_condition,
)
from dcp_kernel.models import (
    AffectedCone,
    CapabilityBinding,
    CapabilityResolution,
    CurrentResolution,
    CurrentResolutionStatus,
    Decision,
    ReturnState,
    TransitionEvaluation,
)
from dcp_kernel.platform import PlatformPlan, WorkContract


class ConsequenceTests(unittest.TestCase):
    def test_return_written_without_rebuild_is_not_next_condition_ready(self) -> None:
        result = derive_next_condition(
            ConsequenceInput(
                transition_id="T-1",
                observed_effect="mobility intrusion observed",
                impact=("vehicle_envelope",),
                evidence_refs=("E-1",),
                affected_receivers=("GLMODEL",),
                responsibility_owner="PARAMETRIC-ACTOR",
                return_state=ReturnState.PRODUCED,
            )
        )
        self.assertEqual(result.decision, Decision.HOLD)
        self.assertFalse(result.next_condition_ready)
        self.assertIn("RETURN_NOT_AT_NATIVE_DISPOSITION", result.reasons)
        self.assertIn("BEHAVIOR_DELTA_NOT_OBSERVED", result.reasons)
        self.assertIn("RETEST_NOT_OBSERVED", result.reasons)

    def test_failure_can_become_next_condition_when_responsibility_loop_closes(self) -> None:
        result = derive_next_condition(
            ConsequenceInput(
                transition_id="T-2",
                observed_effect="maintenance path conflicts with landscape",
                impact=("maintenance_access", "landscape_clearance"),
                cost=("rework",),
                side_effects=("service_route_shift",),
                evidence_refs=("E-FAIL-2",),
                affected_receivers=("GLMODEL", "PARAMETRIC"),
                responsibility_owner="PARAMETRIC-ACTOR",
                return_state=ReturnState.RETESTED,
                receiver_disposition="PATCH",
                rebuild_revision="WORLD-R3",
                behavior_delta="pre-task clearance check added",
                retest_result="original conflict no longer reproduced",
            )
        )
        self.assertEqual(result.decision, Decision.PASS)
        self.assertTrue(result.next_condition_ready)
        self.assertIn("impact:maintenance_access", result.next_dependencies)
        self.assertIn("side_effect:service_route_shift", result.next_dependencies)
        self.assertIn("RESULT_COMPILED_AS_NEXT_CONDITION", result.reasons)

    def test_action_responsibility_contract_binds_same_transition_and_blast_radius(self) -> None:
        binding = CapabilityBinding(
            capability_id="PARAMETRIC",
            actor_id="PARAMETRIC-ACTOR",
            carrier_id="BIM",
            authority_granted=True,
            rights_allowed=True,
            evidence_available=True,
            return_target="GLMODEL",
        )
        plan = PlatformPlan(
            decision=Decision.PASS,
            current=CurrentResolution(
                status=CurrentResolutionStatus.CURRENT,
                selected_revision="WORLD-R2",
            ),
            capability=CapabilityResolution(
                decision=Decision.PASS,
                binding=binding,
            ),
            affected_cone=AffectedCone(
                affected=("GLMODEL", "PARAMETRIC"),
                excluded={},
            ),
            transition=TransitionEvaluation(
                transition_id="T-3",
                decision=Decision.PASS,
                observations=(),
            ),
            work_contract=WorkContract(
                contract_id="WORK-T-3",
                stable_life_id="GUI-LU",
                transition_id="T-3",
                capability_id="PARAMETRIC",
                actor_id="PARAMETRIC-ACTOR",
                carrier_id="BIM",
                receiver="GLMODEL",
                affected_receivers=("GLMODEL", "PARAMETRIC"),
            ),
        )

        contract = compile_action_responsibility(plan)
        self.assertEqual(contract.transition_id, "T-3")
        self.assertEqual(contract.responsibility_owner, "PARAMETRIC-ACTOR")
        self.assertEqual(contract.return_target, "GLMODEL")
        self.assertEqual(contract.rebuild_target, "GLMODEL")
        self.assertEqual(contract.blast_radius, ("GLMODEL", "PARAMETRIC"))


if __name__ == "__main__":
    unittest.main()
