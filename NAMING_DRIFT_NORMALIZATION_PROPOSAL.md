# Naming Drift Normalization — Historical Migration Proposal

> Lifecycle: `HISTORICAL_REFERENCE`
> Current execution eligibility: `false`
> Runtime: `false`
> Authority: `none`

This document records an earlier underscore-to-hyphen migration proposal. It must not be interpreted as a current instruction to move seed files, recreate retired families, normalize all names, or restore former runtime/board/adapter topology.

## Retained primitives
- naming/path drift may break discovery and references;
- before rename/move, identify Stable Existence and current successor coverage;
- preserve unique evidence/lineage before physical relocation or deletion;
- update affected pointers only after the target remains semantically valid;
- path consistency is useful navigation hygiene but does not establish ontology or authority.

## Retired migration assumptions
- underscore paths should automatically migrate into hyphenated families;
- the hyphenated directory is canonical because of naming convention alone;
- every unique legacy file must be preserved as a live body;
- `01_runtime-spine`, `03_board-orchestration`, or `04_adapter-layer` should be repopulated to resolve naming drift;
- `return_to_00` is a completion rule.

## Current rule
`Name drift != Identity drift`
`Rename != Metabolism`
`Path normalization != Current admission`
`Unique legacy file != Required live file`

Any future physical move/rename/reclaim requires current caller/rebuild, successor, rights/retention and owner checks. The former mapping table remains recoverable in Git history.
