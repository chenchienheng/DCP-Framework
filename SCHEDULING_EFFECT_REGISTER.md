# Schedule Effect Contract

> Lifecycle: `PUBLIC_RESEARCH_REFERENCE`
> Runtime: `false`
> Native source root: `false`
> Authority: `none`

This document preserves carrier-neutral scheduling primitives. It does not define a fixed scheduler topology, a permanent schedule hub, or platform-specific ownership.

## 1. Core rule
A named schedule is not an effective schedule.

An effective schedule requires:
- a bounded trigger or cadence;
- a receiver or accountable owner;
- an expected effect/output;
- evidence that the effect occurred;
- visibility when the run is missed, stale, blocked, or invalid;
- explicit action authority for any mutation;
- a return/reconciliation path.

`Named schedule != Runtime`
`Cadence != execution proof`
`Automation capability != authority`
`Tool label != scheduler identity`

## 2. Minimum schedule fields
A material schedule should be representable with:

- `schedule_id`
- `receiver_or_owner`
- `trigger_type`
- `cadence_or_condition`
- `start_or_watch_boundary`
- `expected_effect`
- `evidence_or_proof_ref`
- `action_authority`
- `allowed_scope`
- `return_target`
- `last_valid_execution`
- `missed_or_stale_state`
- `hold_or_invalidation`
- `rebuild_or_reentry_ref`

## 3. Trigger classes
Schedules may be:
- event-driven;
- periodic;
- condition-watch;
- manual/adjudication-gated.

The trigger class does not establish authority. It only defines when evaluation or bounded action may occur.

## 4. Effect gate
A schedule is effective only when its expected effect can be proven. Proof may be a validated state transition, evidence record, return packet, bounded external confirmation, or other source-appropriate evidence.

A schedule is drifting when:
- cadence/condition is defined but no valid effect appears;
- evidence is missing or stale;
- the receiver/owner is unresolved;
- action occurred outside allowed scope;
- a carrier changed but the schedule still assumes the old carrier;
- the run produced output but no valid return/reconciliation occurred.

## 5. Carrier independence
Automation services, calendars, issue trackers, workflow engines, repositories, and human review are interchangeable carriers when they can satisfy the same bounded contract. Carrier replacement must preserve stable schedule identity, authority boundaries, evidence, and return semantics.

## 6. Action gate
Evaluation and notification may be permitted while mutation is not. Any write, send, merge, delete, schedule change, or external side effect requires the applicable action authority; scheduler existence does not grant it.

## 7. Return and rebuild
Material schedule effects should return to the appropriate receiver and be reconstructable from last-valid execution plus ordered evidence/delta. Missed runs, holds, invalidations, and carrier migration must remain visible during rebuild.

## 8. Historical compatibility
Earlier versions encoded fixed `00–12` windows and later `00_ScheduleHub + four child windows`, plus platform-specific tool naming. Those are historical implementation experiments, not universal invariants. Their lineage is preserved in Git history and `archive/scheduling-generation/README.md`.

## 9. Public-surface ceiling
This file is a public research/reference contract only. It does not prove that any schedule is currently active, automated, authorized, or executing.
