# DCP Path Classification v0.1

Status: Candidate / Path Classification / No Runtime / No External Writeback / No Physical Move
Repo: chenchienheng/DCP_Xuan-Ling_CoreTri
Branch: qinyi/xuanling-cloud-workbench-v0.8

## Core

This is a first path-level classification pass for DCP. It marks the current reading layer and later review targets. It does not move files.

## Keep Current

```yaml
Keep_Current:
  alignment:
    - "docs/alignment/repo-internal-alignment-protocol-v0_1.md"
    - "docs/alignment/dcp-internal-alignment-map-v0_1.md"
    - "docs/alignment/dcp-current-active-index-v0_1.md"
    - "docs/alignment/tri-repo-identity-alignment-gate-v0_1.md"
    - "docs/alignment/chain-ecology-integrity-audit-v0_1.md"
    - "docs/alignment/repo-cleanup-and-migration-sprint-v0_1.md"
    - "docs/alignment/repo-cleanup-migration-queue-v0_1.md"
  governance:
    - "docs/governance/signal-intake-gate-v0_1.md"
    - "docs/governance/authority-ring-map-v0_1.md"
  memory_templates:
    - "docs/templates/return-packet-template-v0_4.md"
    - "docs/memory/active-superseded-archive-pointer-index-v0_1.md"
    - "docs/memory/active-pointer-rows-2026-07-07-v0_1.md"
    - "docs/returns/temporal-return-packet-retention-rule-v0_1.md"
  registry_router:
    - "docs/registry/carrier-registry-v0_2-candidate.md"
    - "docs/manifest/carrier-manifest-schema-v0_1.md"
    - "docs/router/production-router-v0_1-candidate.md"
    - "docs/router/production-router-output-surface-patch-v0_1.md"
    - "docs/registry/software-skills-carrier-registry-v0_2-candidate.md"
    - "docs/registry/drive-state-index-v0_1-candidate.md"
  output_domain:
    - "docs/output/output-module-index-v0_1-candidate.md"
    - "docs/output/output-repo-skeleton-v0_1-candidate.md"
    - "docs/domain-packs/bim-cad-open-host-bridge-v0_1.md"
    - "docs/domain-packs/aec-revit-parametric-carrier-gate-v0_1.md"
  signals:
    - "docs/signals/evidence-hygiene-signal-card-v0_1.md"
    - "docs/signals/signal-level-model-v0_1.md"
    - "docs/signals/external-message-signal-rule-v0_1.md"
```

## Later Review Targets

```yaml
Later_Review:
  Reference_Pending:
    - "older daily signal drafts"
    - "long signal extraction reports already converted to registry / signal card"
    - "old domain discussion files after domain-pack extraction"
  Superseded_Pending:
    - "pre-v0.4 return packet templates"
    - "pre-One-Hub schedule notes"
    - "older memory notes superseded by temporal retention / pointer index"
    - "any file implying output as fourth core repo"
  Archive_Pending:
    - "full long-packet history after essence extraction"
    - "duplicate signal summaries"
```

## Red Doors

- Classification != Physical Move.
- Review Target != Confirmed Superseded.
- Keep Current != Approved Doctrine.
- Path List != Closeout.

## Final Rule

DCP should first stabilize the active governance layer, then mark old drafts as reference or superseded after review.