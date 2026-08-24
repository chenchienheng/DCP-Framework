# Scheduling Reconciliation — Historical Topology Lineage

> Lifecycle: `HISTORICAL_REFERENCE`
> Current eligibility as scheduler topology: `false`
> Runtime: `false`
> Authority: `none`

This report records an earlier attempt to reconcile a 12-window schedule model with a later `00_ScheduleHub + 4 child windows` model. Neither topology is Current merely because this report compared them.

## Retained primitives
- a named cadence does not prove execution;
- changing scheduler topology can orphan expected effects unless receiver/effect/return dependencies are preserved;
- schedule migration must distinguish trigger/cadence from action authority;
- missed/stale effects need observable evidence and bounded recovery;
- carrier/topology migration should preserve stable schedule identity only where a real schedule still exists.

## Retired assumptions
- `00_ScheduleHub` is a master scheduler;
- `01_RT_Critical / 02_CVG_3D / 03_STAGE_W1 / 04_MANUAL_Doctrine` are required child windows;
- legacy 06–12 schedules must be remapped into 00–04;
- an empty named window is a topology gap requiring activation;
- `02_CVG_3D` should be activated as the next action.

## Current rule
`Named schedule != Effective schedule`
`Scheduler topology != Authority`
`Cadence mapping != Execution proof`
`Reconciliation report != Current state`

Use `SCHEDULING_EFFECT_REGISTER.md` and current evidence for any actual schedule/effect judgment. Full predecessor comparison remains in Git history.
