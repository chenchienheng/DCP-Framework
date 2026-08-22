import unittest

from dcp_kernel import (
    ActionGateInput, CapabilityBinding, CoexistenceInput, CurrentCandidate, Decision,
    EffectClass, InvariantCore, JudgmentInput, LifecycleState, MeaningCompileInput,
    NativeModel, Need, RiskLevel, StableLife, Transition, TriRootState,
    assess_action_gate, assess_coexistence, assess_decision_chain, assess_judgment,
    compile_governed_work_contract, compile_meaning,
)


class GovernedPlatformTests(unittest.TestCase):
    def setup_chain(self, evidence_sufficient=True):
        meaning = compile_meaning(MeaningCompileInput(
            source_id="R1-00-03",
            meaning_statement="判斷不可外包且抽象需凝實",
            primitive="JUDGMENT_SOVEREIGNTY",
            relation="meaning constrains action selection",
            constraint="no action without evidence/authority/responsibility",
            gate="pre-action decision chain",
            action_delta="block work contract when judgment is incomplete",
            evidence_requirement="typed evidence",
            return_target="Receiver",
            rebuild_effect="next decision changes from receiver evidence",
        ))
        judgment = assess_judgment(JudgmentInput(
            judgment_id="J-GOV",
            source_classified=True,
            meaning_relevant=True,
            boundary_resolved=True,
            evidence_sufficient=evidence_sufficient,
            alternatives_considered=True,
            consequence_assessed=True,
            responsibility_owner="DCP",
            return_target="Receiver",
            rebuild_path_present=True,
            authority_valid=True,
            counterexample_channel_open=True,
            execution_available=True,
            execution_requested=False,
        ))
        coexistence = assess_coexistence(CoexistenceInput(
            left=NativeModel("A", "Ideas", "LIFE-1", "MEANING", "MEANING", "prose"),
            right=NativeModel("B", "DCP", "LIFE-1", "DEPENDENCY", "DEPENDENCY", "graph"),
            common_source_id="SHARED-R",
            translation_available=True,
            compatibility_conditions_known=True,
            shared_evidence_interface=True,
        ))
        action_gate = assess_action_gate(ActionGateInput(
            transition_id="T-GOV",
            required_effect=EffectClass.BOUNDED_MUTATION,
            proposed_effect=EffectClass.BOUNDED_MUTATION,
            risk_level=RiskLevel.MEDIUM,
            authority_valid=True,
            affected_scope_resolved=True,
            evidence_sufficient=True,
            responsibility_owner="DCP",
            return_target="Receiver",
        ))
        return assess_decision_chain(
            meaning=meaning,
            judgment=judgment,
            coexistence=coexistence,
            action_gate=action_gate,
        )

    def base_inputs(self):
        life = StableLife(
            life_id="LIFE-1",
            invariant_core=InvariantCore("LIFE-1", "Preserve meaning", "WORLD-1"),
            native_owner="Vitas",
            current_revision="R1",
            last_good_revision="R1",
        )
        tri = TriRootState(True, True, "WORLD-1", "R1")
        need = Need("N-1", "MODEL", "Receiver")
        capability = CapabilityBinding("MODEL", "Actor", "Carrier", True, True, True, "Receiver", True)
        current = CurrentCandidate("LIFE-1", "R1", LifecycleState.CURRENT, None, True, True, True, True, "2026-08-22")
        transition = Transition(
            transition_id="T-GOV",
            stable_life_id="LIFE-1",
            need="N-1",
            state_before=LifecycleState.CURRENT,
            proposed_effect="bounded change",
            capability_id="MODEL",
            source_revision="R1",
            world_id_before="WORLD-1",
            world_id_after="WORLD-1",
        )
        return life, tri, need, capability, current, transition

    def test_incomplete_judgment_blocks_work_contract(self):
        life, tri, need, capability, current, transition = self.base_inputs()
        result = compile_governed_work_contract(
            decision_chain=self.setup_chain(evidence_sufficient=False),
            stable_life=life,
            tri_root=tri,
            need=need,
            capability_candidates=[capability],
            current_candidates=[current],
            changed_nodes=["Source"],
            dependency_graph={"Source": ["Receiver"]},
            eligible_receivers={"Receiver"},
            transition=transition,
        )
        self.assertEqual(result.decision, Decision.HOLD)
        self.assertIsNone(result.work_contract)

    def test_complete_decision_chain_allows_candidate_contract(self):
        life, tri, need, capability, current, transition = self.base_inputs()
        result = compile_governed_work_contract(
            decision_chain=self.setup_chain(),
            stable_life=life,
            tri_root=tri,
            need=need,
            capability_candidates=[capability],
            current_candidates=[current],
            changed_nodes=["Source"],
            dependency_graph={"Source": ["Receiver"]},
            eligible_receivers={"Receiver"},
            transition=transition,
        )
        self.assertEqual(result.decision, Decision.PASS)
        self.assertIsNotNone(result.work_contract)
        self.assertEqual(result.work_contract.state, "CANDIDATE")


if __name__ == "__main__":
    unittest.main()
