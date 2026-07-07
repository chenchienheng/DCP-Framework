# Repo Cleanup and Migration Sprint v0.1

Status: Candidate / Cleanup Sprint / No Runtime / No External Writeback / No Deletion
Use As: stepwise cleanup plan for tri-repo alignment, migration, deduplication, and active-pointer stabilization
Do Not Use As: deletion approval, merge approval, public release, or automated migration instruction

## Core

Repository cleanup should proceed by classification before movement. Do not move or delete files until active, reference, superseded, fieldspace, archive, and output-candidate categories are visible.

## Sprint Goals

```yaml
Sprint_Goals:
  G1_Current_Active:
    meaning: "each repo has a current-active-index"
  G2_Superseded_Reference:
    meaning: "older or duplicate files are marked reference / superseded / archive"
  G3_Fieldspace_Containment:
    meaning: "private or field-specific files are prevented from contaminating root or output"
  G4_Output_Candidate:
    meaning: "public-safe modules are marked as output candidates, not released"
  G5_QHA_Read_Order:
    meaning: "QHA knows which index to read before expanding details"
```

## Sprint Phases

```yaml
Phases:
  Phase_1_Index:
    action:
      - "create current-active-index per repo"
      - "create superseded-reference-index per repo"
    no_move: true

  Phase_2_Classify:
    action:
      - "mark active / reference / superseded / archive / fieldspace / output_candidate"
    no_delete: true

  Phase_3_Pointer:
    action:
      - "create active pointers"
      - "replace long current links with essence and pointer"
    no_delete: true

  Phase_4_Migration_Candidate:
    action:
      - "propose file moves"
      - "list source path and target path"
      - "require Vitas approval"
    no_automatic_move: true

  Phase_5_Archive:
    action:
      - "move or park only after approval"
      - "keep lineage pointers"
    no_deletion_by_default: true
```

## Migration Row

```yaml
Migration_Row:
  file:
  current_repo:
  current_path:
  proposed_status: "active / reference / superseded / archive / fieldspace / output_candidate"
  proposed_target_repo:
  proposed_target_path:
  reason:
  risk:
  vitas_approval_required: true
```

## Red Doors

- Cleanup Plan != File Move Approval.
- Superseded != Deleted.
- Archive != Approved.
- Migration Candidate != Executed Move.
- Output Candidate != Public Release.
- Fieldspace Containment != Public-Safe.

## Final Rule

Clean by classification first, pointer second, migration third, archive fourth. Never delete by default.