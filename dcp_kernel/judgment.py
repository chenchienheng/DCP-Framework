from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .models import Decision


class KnowledgeState(str, Enum):
    KNOWN = "KNOWN"
    INFERRED = "INFERRED"
    SUSPECTED = "SUSPECTED"
    UNKNOWN = "UNKNOWN"
    CONFLICT = "CONFLICT"


@dataclass(frozen=True)
class JudgmentInput:
    judgment_id: str
    source_classified: bool
    meaning_relevant: bool
    boundary_resolved: bool
    evidence_sufficient: bool
    alternatives_considered: bool
    consequence_assessed: bool
    responsibility_owner: str | None
    return_target: str | None
    rebuild_path_present: bool
    authority_valid: bool
    recommendation_present: bool = False
    expert_confidence: float | None = None
    model_confidence: float | None = None
    majority_agreement: bool = False
    counterexample_channel_open: bool = True
    execution_available: bool = False
    execution_requested: bool = False


@dataclass(frozen=True)
class JudgmentAssessment:
    decision: Decision
    knowledge_state: KnowledgeState
    execution_permitted_by_judgment: bool
    recommendation_is_decision: bool
    reasons: tuple[str, ...]


def assess_judgment(item: JudgmentInput) -> JudgmentAssessment:
    """Assess judgment without letting expertise, confidence or execution become authority."""

    reasons: list[str] = []

    if not item.source_classified:
        reasons.append("SOURCE_NOT_CLASSIFIED")
    if not item.meaning_relevant:
        reasons.append("MEANING_RELEVANCE_UNRESOLVED")
    if not item.boundary_resolved:
        reasons.append("BOUNDARY_UNRESOLVED")
    if not item.evidence_sufficient:
        reasons.append("EVIDENCE_INSUFFICIENT")
    if not item.alternatives_considered:
        reasons.append("ALTERNATIVES_NOT_CONSIDERED")
    if not item.consequence_assessed:
        reasons.append("CONSEQUENCE_NOT_ASSESSED")
    if not item.responsibility_owner:
        reasons.append("RESPONSIBILITY_OWNER_MISSING")
    if not item.return_target:
        reasons.append("RETURN_TARGET_MISSING")
    if not item.rebuild_path_present:
        reasons.append("REBUILD_PATH_MISSING")
    if not item.authority_valid:
        reasons.append("AUTHORITY_MISSING")
    if item.majority_agreement and not item.counterexample_channel_open:
        reasons.append("MAJORITY_WITHOUT_COUNTEREXAMPLE_CHANNEL")
    if item.execution_requested and not item.execution_available:
        reasons.append("EXECUTION_CAPABILITY_UNAVAILABLE")

    if not item.evidence_sufficient:
        knowledge = KnowledgeState.UNKNOWN
    elif not item.source_classified or not item.boundary_resolved:
        knowledge = KnowledgeState.INFERRED
    else:
        knowledge = KnowledgeState.KNOWN

    if reasons:
        return JudgmentAssessment(
            decision=Decision.HOLD,
            knowledge_state=knowledge,
            execution_permitted_by_judgment=False,
            recommendation_is_decision=False,
            reasons=tuple(reasons),
        )

    return JudgmentAssessment(
        decision=Decision.PASS,
        knowledge_state=knowledge,
        execution_permitted_by_judgment=item.execution_requested,
        recommendation_is_decision=False,
        reasons=(
            "JUDGMENT_CHAIN_COMPLETE",
            "EXPERTISE_CONFIDENCE_AND_RECOMMENDATION_DID_NOT_CREATE_AUTHORITY",
        ),
    )
