from __future__ import annotations

import unittest

from dcp_kernel.capability_activation import (
    CapabilityActivationNeed,
    CapabilityLineage,
    CapabilityProvider,
    ProviderKind,
    resolve_capability_activation,
    validate_provider_substitution,
)
from dcp_kernel.models import Decision


LINEAGES = (
    CapabilityLineage("capability-composition", "compose only affected capabilities", "DCP"),
    CapabilityLineage("current-resolution", "resolve current state and eligibility", "DCP"),
    CapabilityLineage("world-relation", "compile affected world relations", "GLMODEL"),
    CapabilityLineage("return-reconciliation", "return, disposition and rebuild", "DCP"),
    CapabilityLineage("historical-metabolism", "historical immunity and successor coverage", "DCP"),
)


def skill(
    provider_id: str,
    label: str,
    lineage_ids: tuple[str, ...],
    *,
    available: bool = True,
    authority: bool = True,
) -> CapabilityProvider:
    return CapabilityProvider(
        provider_id=provider_id,
        provider_kind=ProviderKind.SKILL,
        provider_label=label,
        capability_lineage_ids=lineage_ids,
        authority_scopes=("DCP_BOUNDED_WORK",) if authority else (),
        available=available,
        current_effect_eligible=True,
        evidence_available=True,
        return_supported=True,
        privacy_allowed=True,
        reliability=0.95,
        estimated_cost=1.0,
        replacement_path_known=True,
        exit_condition_known=True,
    )


FIVE_SKILLS = (
    skill("skill-router", "xuanling-global-skill-router", ("capability-composition",)),
    skill("skill-current", "xuanling-current-life-resolver", ("current-resolution",)),
    skill("skill-world", "xuanling-world-relation-compiler", ("world-relation",)),
    skill("skill-return", "xuanling-return-rebuild", ("return-reconciliation",)),
    skill("skill-metabolism", "xuanling-metabolism-guardian", ("historical-metabolism",)),
)


class CapabilityActivationTests(unittest.TestCase):
    def test_affected_slice_does_not_wake_all_five_skills(self) -> None:
        need = CapabilityActivationNeed(
            need_id="resolve-and-return",
            stable_life_id="XUANLING",
            required_lineage_ids=("current-resolution", "return-reconciliation"),
            required_authority_scope="DCP_BOUNDED_WORK",
            return_target="DCP",
        )
        result = resolve_capability_activation(need, LINEAGES, FIVE_SKILLS)
        self.assertEqual(result.decision, Decision.PASS)
        self.assertEqual(result.activated_lineage_ids, ("current-resolution", "return-reconciliation"))
        self.assertEqual({item.provider_id for item in result.bindings}, {"skill-current", "skill-return"})
        self.assertFalse(result.over_activation)
        self.assertLess(len(result.bindings), len(FIVE_SKILLS))

    def test_one_provider_may_cover_multiple_lineages_without_new_pole(self) -> None:
        combined_human = CapabilityProvider(
            provider_id="engineer-01",
            provider_kind=ProviderKind.HUMAN,
            provider_label="eligible engineer",
            capability_lineage_ids=("current-resolution", "capability-composition"),
            authority_scopes=("DCP_BOUNDED_WORK",),
            available=True,
            current_effect_eligible=True,
            evidence_available=True,
            return_supported=True,
            privacy_allowed=True,
            reliability=0.99,
            estimated_cost=0.5,
        )
        need = CapabilityActivationNeed(
            "compose-current",
            "XUANLING",
            ("current-resolution", "capability-composition"),
            "DCP_BOUNDED_WORK",
            "DCP",
        )
        result = resolve_capability_activation(need, LINEAGES, FIVE_SKILLS + (combined_human,))
        self.assertEqual(result.decision, Decision.PASS)
        self.assertEqual(len(result.bindings), 1)
        self.assertEqual(result.bindings[0].provider_id, "engineer-01")

    def test_provider_removal_reresolves_same_lineage(self) -> None:
        unavailable = skill(
            "skill-current",
            "xuanling-current-life-resolver",
            ("current-resolution",),
            available=False,
        )
        fallback = CapabilityProvider(
            provider_id="model-current-fallback",
            provider_kind=ProviderKind.AI_MODEL,
            provider_label="provider-neutral current resolver",
            capability_lineage_ids=("current-resolution",),
            authority_scopes=("DCP_BOUNDED_WORK",),
            available=True,
            current_effect_eligible=True,
            evidence_available=True,
            return_supported=True,
            privacy_allowed=True,
            reliability=0.92,
            estimated_cost=2.0,
        )
        providers = tuple(item for item in FIVE_SKILLS if item.provider_id != "skill-current") + (unavailable, fallback)
        need = CapabilityActivationNeed(
            "current-only",
            "XUANLING",
            ("current-resolution",),
            "DCP_BOUNDED_WORK",
            "DCP",
        )
        result = resolve_capability_activation(need, LINEAGES, providers)
        self.assertEqual(result.decision, Decision.PASS)
        self.assertEqual(result.bindings[0].provider_id, "model-current-fallback")
        self.assertIn("PROVIDER_UNAVAILABLE", result.excluded["skill-current"])

    def test_skill_rename_does_not_change_capability_lineage(self) -> None:
        need = CapabilityActivationNeed(
            "current-only",
            "XUANLING",
            ("current-resolution",),
            "DCP_BOUNDED_WORK",
            "DCP",
        )
        before = resolve_capability_activation(
            need,
            LINEAGES,
            (skill("provider-v1", "xuanling-current-life-resolver", ("current-resolution",)),),
        )
        after = resolve_capability_activation(
            need,
            LINEAGES,
            (skill("provider-v2", "renamed-current-provider", ("current-resolution",)),),
        )
        decision, reasons = validate_provider_substitution(before, after)
        self.assertEqual(decision, Decision.PASS)
        self.assertIn("PROVIDER_NAME_NOT_PART_OF_CAPABILITY_IDENTITY", reasons)

    def test_missing_authority_holds_without_birthing_significance_skill(self) -> None:
        need = CapabilityActivationNeed(
            "material-decision",
            "XUANLING",
            ("current-resolution",),
            "DCP_BOUNDED_WORK",
            "DCP",
        )
        unauthorized = skill(
            "skill-current",
            "xuanling-current-life-resolver",
            ("current-resolution",),
            authority=False,
        )
        result = resolve_capability_activation(need, LINEAGES, (unauthorized,))
        self.assertEqual(result.decision, Decision.HOLD)
        self.assertIn("AUTHORITY_SCOPE_NOT_ALLOWED", result.excluded["skill-current"])
        self.assertNotIn("significance-decision", result.activated_lineage_ids)

    def test_no_capability_need_stays_quiet(self) -> None:
        need = CapabilityActivationNeed(
            "local-chat",
            "XUANLING",
            (),
            "DCP_BOUNDED_WORK",
            "DCP",
        )
        result = resolve_capability_activation(need, LINEAGES, FIVE_SKILLS)
        self.assertEqual(result.decision, Decision.PASS)
        self.assertEqual(result.bindings, ())
        self.assertIn("NO_CAPABILITY_ACTIVATION_REQUIRED", result.reasons)


if __name__ == "__main__":
    unittest.main()
