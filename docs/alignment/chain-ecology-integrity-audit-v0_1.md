# Chain Ecology Integrity Audit v0.1

Status: Candidate / Integrity Audit / No Runtime / No External Writeback
Use As: QHA audit checklist for determining whether the repo-network, Drive layer, and LOR workfaces are truly circulating or only accumulating files
Do Not Use As: approval, merge gate, runtime proof, or public release claim

## Core

A chain ecology is real only when signals can be classified, routed, returned, indexed, and rebuilt without relying on Vitas manually copying every context block.

## Integrity Dimensions

```yaml
Integrity_Dimensions:
  Source_Continuity:
    question: "Does each return say what it read and what it continues from?"
  Carrier_Fit:
    question: "Is the content stored in the right carrier / repo / folder?"
  Authority_Clarity:
    question: "Is the decision owner visible?"
  Gate_Visibility:
    question: "Are red doors and manual-needed items explicit?"
  Return_Link:
    question: "Does it name next_reader and write_to?"
  Memory_Control:
    question: "Does it have active / superseded / archive handling?"
  Output_Boundary:
    question: "Does it distinguish internal core, workface, fieldspace, and output module?"
```

## Audit Scoring

```yaml
Audit_Score:
  L0_Pile:
    meaning: "files exist, but no active pointer or next_reader"
  L1_Indexed:
    meaning: "files are indexed and role-labeled"
  L2_Linked:
    meaning: "reads_from / continues_from / next_reader / write_to exist"
  L3_Circulating:
    meaning: "QHA can dispatch and receive returns without manual full-context paste"
  L4_Rebuildable:
    meaning: "new QHA window can reconstruct state from active pointers and alignment maps"
```

## Current Assessment Seed

```yaml
Current_Assessment_2026_07_07:
  GitHub_Three_Repos:
    score: "L1_Indexed moving toward L2_Linked"
  Google_Drive_Return_Layer:
    score: "L1_Indexed"
  QHA_One_Hub:
    score: "L1_Indexed / pending 3-day hub proof"
  Xiaoshiguang_Field:
    score: "L1_Indexed / field cards candidate started"
```

## Red Doors

- Many Files != Chain Ecology.
- Next Reader != ACK.
- Active Pointer != Approved Truth.
- Repo Alignment != Cleanup Completion.
- Hub Report != Runtime.

## Next Audit Need

- Three consecutive QHA Daily Hub logs.
- First real use of active pointer rows.
- First superseded/reference marking pass.
- First Xiaoshiguang three-card proof pass.
