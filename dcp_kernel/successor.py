from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .models import Decision


class CoverageState(str, Enum):
    COVERED = "COVERED"
    COVERED_EVIDENCE_ONLY = "COVERED_EVIDENCE_ONLY"
    PARTIAL_READER_WITHDRAWAL = "PARTIAL_READER_WITHDRAWAL"
    GAP = "GAP"
    ZOMBIE_DEPENDENCY = "ZOMBIE_DEPENDENCY"
    HOLD = "HOLD"


@dataclass(frozen=True)
class SuccessorCoverageInput:
    artifact_path: str
    successor_id: str | None
    successor_executable_or_machine: bool
    active_callers: tuple[str, ...] = ()
    rebuild_dependency: bool = False
    unique_evidence: bool = False
    normal_reader_wake: bool = False
    current_routing_reference: bool = False


@dataclass(frozen=True)
class SuccessorCoverageAssessment:
    decision: Decision
    state: CoverageState
    normal_reader_eligible: bool
    destructive_action_authorized: bool
    reasons: tuple[str, ...]


def assess_successor_coverage(item: SuccessorCoverageInput) -> SuccessorCoverageAssessment:
    """Evaluate semantic metabolism without equating rename/archive with completion."""

    has_live_dependency = bool(item.active_callers) or item.rebuild_dependency

    if has_live_dependency and not item.successor_id:
        return SuccessorCoverageAssessment(
            decision=Decision.FAIL,
            state=CoverageState.ZOMBIE_DEPENDENCY,
            normal_reader_eligible=True,
            destructive_action_authorized=False,
            reasons=("LIVE_DEPENDENCY_WITHOUT_SUCCESSOR",),
        )

    if has_live_dependency and not item.successor_executable_or_machine:
        return SuccessorCoverageAssessment(
            decision=Decision.HOLD,
            state=CoverageState.GAP,
            normal_reader_eligible=True,
            destructive_action_authorized=False,
            reasons=("SUCCESSOR_DOES_NOT_COVER_LIVE_BEHAVIOR",),
        )

    if not item.successor_id:
        if item.unique_evidence:
            return SuccessorCoverageAssessment(
                decision=Decision.HOLD,
                state=CoverageState.COVERED_EVIDENCE_ONLY,
                normal_reader_eligible=False,
                destructive_action_authorized=False,
                reasons=("UNIQUE_EVIDENCE_RETAIN_WITHOUT_NORMAL_WAKE",),
            )
        return SuccessorCoverageAssessment(
            decision=Decision.HOLD,
            state=CoverageState.GAP,
            normal_reader_eligible=False,
            destructive_action_authorized=False,
            reasons=("SUCCESSOR_COVERAGE_UNPROVEN",),
        )

    if item.normal_reader_wake or item.current_routing_reference:
        return SuccessorCoverageAssessment(
            decision=Decision.HOLD,
            state=CoverageState.PARTIAL_READER_WITHDRAWAL,
            normal_reader_eligible=True,
            destructive_action_authorized=False,
            reasons=("SUCCESSOR_EXISTS_BUT_OLD_READER_OR_ROUTING_WAKE_REMAINS",),
        )

    if item.unique_evidence:
        return SuccessorCoverageAssessment(
            decision=Decision.PASS,
            state=CoverageState.COVERED_EVIDENCE_ONLY,
            normal_reader_eligible=False,
            destructive_action_authorized=False,
            reasons=("SUCCESSOR_COVERS_BEHAVIOR_RETAIN_UNIQUE_LINEAGE",),
        )

    return SuccessorCoverageAssessment(
        decision=Decision.PASS,
        state=CoverageState.COVERED,
        normal_reader_eligible=False,
        destructive_action_authorized=False,
        reasons=("SUCCESSOR_COVERS_BEHAVIOR_AND_READER_WAKE_WITHDRAWN",),
    )
