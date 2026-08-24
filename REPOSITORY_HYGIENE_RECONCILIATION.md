# Repository Hygiene Reconciliation — Historical Review Lineage

> Lifecycle: `HISTORICAL_REFERENCE`
> Current eligibility: `false`
> Runtime: `false`
> Authority: `none`

This report records a past GitHub hygiene review over issues, PRs and branches. Its issue numbers, branch classifications, canonical-task claims, dependency order and cleanup recommendations are observations from that earlier state only.

## Retained primitives
- repository UI state can drift from semantic/current state;
- duplicate/stale branches or issues should be verified before closure/deletion;
- branch/issue cleanup must not erase unique provenance or live dependencies;
- repository hygiene should reduce confusion without promoting a taskboard or issue into architecture authority;
- destructive actions require current evidence and explicit authority.

## Retired claims/actions
- Issue #44 is the canonical consolidation surface;
- specific issues `must remain open` as structural anchors;
- PRs must resolve in the predecessor dependency order;
- `main`/named branches form a current task ontology;
- a human should now close/delete the specifically named historical issues/branches;
- old taskboard reconciliation is a current next action.

## Current rule
`Issue state != Architecture state`
`Branch label != Current work`
`Historical cleanup recommendation != Current authority`
`Merged/stale guess != Delete authority`

Any present hygiene action must re-read current repository evidence, affected caller/rebuild dependencies, retention/provenance needs and applicable action authority. Full predecessor issue/branch inventory remains in Git history.
