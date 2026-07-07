# DCP Current Active Index v0.1

Status: Candidate / Current Active Index / No Runtime / No External Writeback
Use As: current active map for QHA reading and cleanup planning
Do Not Use As: approved truth, release approval, merge approval, or closeout

## Core

This index lists the currently active DCP governance files for QHA reading. It does not delete or invalidate older files; it marks the current reading layer.

## Active Current

```yaml
DCP_Current_Active:
  alignment:
    - "docs/alignment/repo-internal-alignment-protocol-v0_1.md"
    - "docs/alignment/dcp-internal-alignment-map-v0_1.md"
    - "docs/alignment/dcp-current-active-index-v0_1.md"
  governance:
    - "docs/governance/signal-intake-gate-v0_1.md"
    - "docs/governance/semantic-topological-firewall-v0_1-candidate.md"
  memory:
    - "docs/templates/return-packet-template-v0_4.md"
    - "docs/memory/active-superseded-archive-pointer-index-v0_1.md"
    - "docs/memory/active-pointer-rows-2026-07-07-v0_1.md"
    - "docs/returns/temporal-return-packet-retention-rule-v0_1.md"
  registry_router:
    - "docs/registry/carrier-registry-v0_2-candidate.md"
    - "docs/manifest/carrier-manifest-schema-v0_1.md"
    - "docs/router/production-router-v0_1-candidate.md"
    - "docs/registry/software-skills-carrier-registry-v0_2-candidate.md"
    - "docs/registry/drive-state-index-v0_1-candidate.md"
  output:
    - "docs/output/output-module-index-v0_1-candidate.md"
    - "docs/output/output-repo-skeleton-v0_1-candidate.md"
  domain_packs:
    - "docs/domain-packs/bim-cad-open-host-bridge-v0_1.md"
    - "docs/domain-packs/aec-revit-parametric-carrier-gate-v0_1.md"
  signals:
    - "docs/signals/evidence-hygiene-signal-card-v0_1.md"
    - "docs/signals/signal-level-model-v0_1.md"
```

## Superseded / Reference Pending

Older v0.1-v0.3 return packets, schedule drafts, and duplicated circulation notes must be reviewed later and marked Active / Reference / Superseded / Archive.

## Red Doors

- Current Active != Approved Truth.
- Missing From Index != Deleted.
- Superseded Pending != Invalid.
- Active Index != Closeout.

## Final Rule

QHA should read this index first, then follow pointers. Do not re-read the full repository unless conflict, audit, or rebuild requires it.