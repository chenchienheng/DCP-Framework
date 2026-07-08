# Tri-Repo Linkage Index v0.1

Status: Candidate / Linkage Index / No Runtime / No External Writeback / No Physical Move
Use As: QHA index for linking DCP, XLQY, and Yiyi current-active files into a working chain ecology
Do Not Use As: file move approval, merge approval, public release, runtime proof, or closeout

## Core

A repo-network link is valid only when the source file, target file, bond type, return path, and boundary are visible. This index lists cross-repo links that should be read as active candidate bonds.

## Active Link Candidates

```yaml
Tri_Repo_Linkage:
  - id: "CORE-FLOW-001"
    from: "DCP/docs/governance/signal-intake-gate-v0_1.md"
    to: "XLQY/docs/dispatch/qha-daily-dispatch-template-v0_1.md"
    bond: "Signal Intake -> Daily Dispatch"
    return_path: "XLQY return packet -> DCP active pointer"
    red_door: "Dispatch != Approval"

  - id: "CORE-FLOW-002"
    from: "DCP/docs/router/production-router-v0_1-candidate.md"
    to: "XLQY/docs/returns/missing-return-hook-request-template-v0_1.md"
    bond: "Routing -> Missing Return Repair"
    return_path: "Missing hook patch -> Cross-Window Return Index"
    red_door: "Router Assignment != Execution Approval"

  - id: "FLOW-FIELD-001"
    from: "XLQY/docs/build-packets/hazumi-build-packet-coretri-ocf-v0_1.md"
    to: "Yiyi/docs/ui/field-card-spec-v0_1.md"
    bond: "Bounded Build Packet -> Field Card Proof"
    return_path: "Problem Return Card -> XLQY return packet"
    red_door: "Build Packet != Runtime"

  - id: "FIELD-FLOW-001"
    from: "Yiyi/docs/return/problem-return-form-v0_1.md"
    to: "XLQY/docs/audit/public-safe-output-checklist-v0_1.md"
    bond: "Field Problem Return -> Aki Public-Safe Review"
    return_path: "Audit note -> QHA Dispatch"
    red_door: "Problem Return != Closeout"

  - id: "FIELD-CORE-001"
    from: "Yiyi/docs/field/xiaoshiguang-gift-field-projection-intake-v0_1.md"
    to: "DCP/docs/governance/authority-ring-map-v0_1.md"
    bond: "Field Boundary -> Authority Ring Rule"
    return_path: "generalized pattern only -> DCP governance candidate"
    red_door: "Private Context != Open Core"

  - id: "CORE-FIELD-001"
    from: "DCP/docs/governance/small-build-loop-gate-v0_1.md"
    to: "Yiyi/docs/ui/field-card-spec-v0_1.md"
    bond: "Small Build Loop -> Three Field Cards"
    return_path: "Evidence / Return Check -> QHA Hub"
    red_door: "Field Proof != Runtime"
```

## Link Validation Fields

```yaml
Link_Validation:
  source_exists:
  target_exists:
  bond_type:
  allowed_action:
  forbidden_action:
  return_required:
  next_reader:
  red_door:
```

## Red Doors

- Link Exists != Handoff Completed.
- Cross-Repo Link != Merge Approval.
- Field-to-Core Link != Private Context Transfer.
- Core-to-Field Link != Runtime Command.
- Build Link != Build Approval.

## Final Rule

QHA should route through active links, not through memory of old conversations. Links must be reviewed when source or target files change.