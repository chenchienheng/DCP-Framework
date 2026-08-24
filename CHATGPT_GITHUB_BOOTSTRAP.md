# Repository Re-entry Surface

> Lifecycle: `PUBLIC_RESEARCH_REFERENCE`
> Runtime: `false`
> Native source root: `false`
> Authority: `none`

Purpose: provide a minimal, low-read re-entry surface for this repository without treating GitHub, a repository name, or a historical map as the system identity.

## Current carrier identity
- canonical_repository_full_name: `chenchienheng/DCP-Pole-Projection`
- observed_historical_or_alias_reference: `chenchienheng/XuanLing-00-Foundation-DCP`
- connector_resolution: observed to resolve to the same repository identity at this review point
- default_branch: `main`
- repository_role: `PUBLIC_FOUNDATION_RESEARCH_SURFACE`

A repository alias/name change does not create a second DCP, second Native Source, second Current, or second Authority. Re-entry should prefer the connector-resolved canonical repository identity and preserve historical aliases only for provenance/navigation.

## Reader entry
Read in this order unless an affected pointer says otherwise:
1. `README.md`
2. `CURRENT-SURFACE-MANIFEST.json`
3. `LIFECYCLE_DEPENDENCY_CHAIN_KERNEL.md`
4. `PUBLIC-SURFACE-POLICY.md`
5. `STATUS.md`
6. only the affected public/reference artifact

Do not use file recency, root location, repository naming, alias naming, or historical cross-links to infer Current state or Native authority.

## Re-entry rules
- verify actual connector/repository access when repository work is required;
- resolve the canonical carrier identity from the connector/repository object rather than trusting a historical display name;
- resolve Current through `CURRENT-SURFACE-MANIFEST.json`, not through historical maps;
- treat this repository as a replaceable public carrier/reference surface;
- use stable identity, source authority, evidence, dependency, return/reconciliation, and rebuild/re-entry relations to continue work;
- historical artifacts may be re-materialized only for provenance, audit, failure learning, regression, or rebuild.

## Not to claim
- repository access does not establish authority;
- repository durability does not make GitHub a Native Source Root;
- repository alias equality does not establish semantic equality outside the observed carrier identity;
- successful write does not prove Runtime capability;
- public-safe content is not public-approved unless the release gate says so.

## Historical compatibility
Earlier versions referenced `chenchienheng/DCP-Framework`, a GitHub chain master map, GitHub as a primary writeback/bone candidate, and later the `XuanLing-00-Foundation-DCP` naming surface. Those are carrier/history references, not architecture invariants. Historical detail remains recoverable from Git history and lineage indexes.
