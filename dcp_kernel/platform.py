from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Iterable, Mapping, Sequence

from .models import (
    AffectedCone,
    CapabilityBinding,
    CapabilityResolution,
    CurrentCandidate,
    CurrentResolution,
    CurrentResolutionStatus,
    Decision,
    Need,
    ReentryState,
    ReturnState,
    StableLife,
    Transition,
    TransitionEvaluation,
    TriRootState,
)
from .resolution import (
    compute_affected_cone,
    resolve_capability_binding,
    resolve_current,
)
from .return_state import ReturnClosure
from .transition import evaluate_transition


@dataclass(frozen=True)
class WorkContract:
    contract_id: str
    stable_life_id: str
    transition_id: str
    capability_id: str
    actor_id: str
    carrier_id: str
    receiver: str
    affected_receivers: tuple[str, ...]
    state: str = "CANDIDATE"


@dataclass(frozen=True)
class PlatformPlan:
    decision: Decision
    current: CurrentResolution
    capability: CapabilityResolution
    affected_cone: AffectedCone
    transition: TransitionEvaluation | None
    work_contract: WorkContract | None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class PlatformLoopResult:
    decision: Decision
    plan: PlatformPlan
    closure: ReturnClosure
    reentry: ReentryState | None
    reasons: tuple[str, ...] = ()


def compile_work_contract(
    *,
    stable_life: StableLife,
    tri_root: TriRootState,
    need: Need,
    capability_candidates: Iterable[CapabilityBinding],
    current_candidates: Sequence[CurrentCandidate],
    changed_nodes: Iterable[str],
    dependency_graph: Mapping[str, Sequence[str]],
    eligible_receivers: set[str],
    transition: Transition,
) -> PlatformPlan:
    """Compile a bounded candidate contract; never execute or approve the work."""

    current = resolve_current(
        stable_life_id=stable_life.life_id,
        last_good_revision=stable_life.last_good_revision,
        candidates=current_candidates,
    )
    empty_capability = CapabilityResolution(
        decision=Decision.HOLD,
        binding=None,
        reasons=("CURRENT_NOT_RESOLVED",),
    )
    empty_cone = AffectedCone(affected=(), excluded={})

    if current.status is not CurrentResolutionStatus.CURRENT:
        return PlatformPlan(
            decision=Decision.HOLD,
            current=current,
            capability=empty_capability,
            affected_cone=empty_cone,
            transition=None,
            work_contract=None,
            reasons=("CURRENT_NOT_RESOLVED",),
        )

    capability = resolve_capability_binding(need, capability_candidates)
    if capability.decision is not Decision.PASS or capability.binding is None:
        return PlatformPlan(
            decision=capability.decision,
            current=current,
            capability=capability,
            affected_cone=empty_cone,
            transition=None,
            work_contract=None,
            reasons=capability.reasons,
        )

    affected_cone = compute_affected_cone(
        changed_nodes=changed_nodes,
        dependency_graph=dependency_graph,
        eligible_receivers=eligible_receivers,
    )
    if need.receiver not in affected_cone.affected:
        return PlatformPlan(
            decision=Decision.HOLD,
            current=current,
            capability=capability,
            affected_cone=affected_cone,
            transition=None,
            work_contract=None,
            reasons=("RETURN_RECEIVER_NOT_IN_AFFECTED_CONE",),
        )

    effective_life = replace(
        stable_life,
        current_revision=current.selected_revision or stable_life.current_revision,
    )
    transition_evaluation = evaluate_transition(
        effective_life,
        tri_root,
        capability.binding,
        transition,
    )
    if transition_evaluation.decision is not Decision.PASS:
        return PlatformPlan(
            decision=transition_evaluation.decision,
            current=current,
            capability=capability,
            affected_cone=affected_cone,
            transition=transition_evaluation,
            work_contract=None,
            reasons=(
                transition_evaluation.first_material_break.motion.value
                if transition_evaluation.first_material_break
                else "TRANSITION_NOT_PASS",
            ),
        )

    contract = WorkContract(
        contract_id=f"WORK-{transition.transition_id}",
        stable_life_id=stable_life.life_id,
        transition_id=transition.transition_id,
        capability_id=capability.binding.capability_id,
        actor_id=capability.binding.actor_id,
        carrier_id=capability.binding.carrier_id,
        receiver=need.receiver,
        affected_receivers=affected_cone.affected,
    )
    return PlatformPlan(
        decision=Decision.PASS,
        current=current,
        capability=capability,
        affected_cone=affected_cone,
        transition=transition_evaluation,
        work_contract=contract,
    )


def build_reentry_state(
    *,
    stable_life: StableLife,
    tri_root: TriRootState,
    closure: ReturnClosure,
    receiver_rebuild_revision: str,
    receiver_tri_root_revision: str | None = None,
    last_good_revision: str | None = None,
    active_need: str | None = None,
    blockers: tuple[str, ...] = (),
    cursor: str | None = None,
    ack_owner: str | None = None,
) -> ReentryState:
    """Build typed re-entry only after receiver-owned rebuild resolution exists."""

    rebuild_resolved_states = {
        ReturnState.REBUILD_APPLIED_OR_NO_REBUILD_WITH_REASON,
        ReturnState.BEHAVIOR_DELTA_OBSERVED,
        ReturnState.RETESTED,
    }
    if closure.state not in rebuild_resolved_states:
        raise ValueError("REENTRY_REQUIRES_RECEIVER_REBUILD_RESOLUTION")

    return ReentryState(
        stable_life_id=stable_life.life_id,
        invariant_core_id=stable_life.invariant_core.identity_anchor,
        tri_root_revision=receiver_tri_root_revision or tri_root.source_revision,
        current_revision=receiver_rebuild_revision,
        last_good_revision=last_good_revision or stable_life.current_revision,
        active_need=active_need,
        blockers=blockers,
        pending_returns=() if closure.state is ReturnState.RETESTED else (closure.return_id,),
        cursor=cursor,
        ack_owner=ack_owner,
    )


def complete_fixture_loop(
    *,
    plan: PlatformPlan,
    stable_life: StableLife,
    tri_root: TriRootState,
    closure: ReturnClosure,
    receiver_rebuild_revision: str,
    receiver_tri_root_revision: str,
    cursor: str,
    ack_owner: str,
) -> PlatformLoopResult:
    """Verify an end-to-end deterministic fixture; never impersonate external execution."""

    if plan.decision is not Decision.PASS or plan.work_contract is None:
        return PlatformLoopResult(
            decision=Decision.FAIL,
            plan=plan,
            closure=closure,
            reentry=None,
            reasons=("WORK_CONTRACT_NOT_COMPILED",),
        )

    if closure.receiver != plan.work_contract.receiver:
        return PlatformLoopResult(
            decision=Decision.FAIL,
            plan=plan,
            closure=closure,
            reentry=None,
            reasons=("RETURN_RECEIVER_MISMATCH",),
        )

    if closure.state is not ReturnState.RETESTED:
        return PlatformLoopResult(
            decision=Decision.HOLD,
            plan=plan,
            closure=closure,
            reentry=None,
            reasons=("RETURN_REBUILD_BEHAVIOR_RETEST_LOOP_INCOMPLETE",),
        )

    reentry = build_reentry_state(
        stable_life=stable_life,
        tri_root=tri_root,
        closure=closure,
        receiver_rebuild_revision=receiver_rebuild_revision,
        receiver_tri_root_revision=receiver_tri_root_revision,
        last_good_revision=plan.current.selected_revision,
        cursor=cursor,
        ack_owner=ack_owner,
    )
    return PlatformLoopResult(
        decision=Decision.PASS,
        plan=plan,
        closure=closure,
        reentry=reentry,
    )
