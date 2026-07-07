# DCP Superseded / Reference Index v0.1

Status: Candidate / Superseded Reference Index / No Runtime / No External Writeback / No Deletion
Repo: chenchienheng/DCP_Xuan-Ling_CoreTri
Branch: qinyi/xuanling-cloud-workbench-v0.8

## Core

This index is the first pass for classifying older or duplicate DCP files. It does not delete, move, or invalidate any file. It marks cleanup targets for later review.

## Classification Rows

```yaml
DCP_Superseded_Reference:
  Reference_Pending:
    meaning: "still useful as lineage, not current reading layer"
    examples:
      - "older daily signal drafts"
      - "older schedule drafts before One-Hub"
      - "long analysis packets whose essence is now in active files"

  Superseded_Pending:
    meaning: "likely replaced by active current file, requires verification"
    examples:
      - "pre-v0.4 return packet templates"
      - "pre-One-Hub schedule deconfliction notes"
      - "older memory notes replaced by temporal retention and pointer index"

  Archive_Pending:
    meaning: "not needed for current reading layer, keep pointer only after review"
    examples:
      - "long full-packet historical material"
      - "duplicate signal summaries"
      - "old candidate reports already converted to index"

  Keep_Active:
    meaning: "listed in DCP Current Active Index"
    pointer: "docs/alignment/dcp-current-active-index-v0_1.md"
```

## Review Needed

QHA should later compare actual files against the active index and propose specific path-level classifications.

## Red Doors

- Superseded Pending != Superseded Confirmed.
- Reference != Current Truth.
- Archive Pending != Deletion.
- Classification != File Move.

## Final Rule

DCP cleanup starts with this index, then path-level review. No file movement or deletion is authorized by this document.