# Active / Superseded / Archive Pointer Index v0.1

Status: Candidate / Memory Pointer Index / No Runtime / No External Writeback
Use As: pointer index for active returns, superseded returns, and archive retrieval
Do Not Use As: approved doctrine, auto deletion rule, legal record policy, or company retention policy

## Core

QHA should not read every full return packet by default. It should read active pointers first, then use superseded or archive pointers only when lineage, conflict, or rebuild requires it.

## Pointer Row

```yaml
Pointer_Row:
  pointer_id:
  title:
  current_status: "Active / Canonicalized / Superseded / Quarantined / Red_Gate"
  active_pointer:
  latest_essence_pointer:
  supersedes: []
  superseded_by:
  archive_pointer:
  canonical_repo_pointer:
  drive_pointer:
  cold_archive_candidate:
  human_base_candidate:
  last_reviewed_at:
  next_review_due:
  red_doors: []
  retrieval_conditions: []
```

## Sections

```yaml
Pointer_Index:
  Active_Current:
    purpose: "current working returns and latest valid summaries"
  Canonicalized:
    purpose: "essence promoted into repo-safe candidate"
  Superseded:
    purpose: "older return kept as lineage, not current truth"
  Quarantined:
    purpose: "contains private context or contamination risk"
  Red_Gate:
    purpose: "blocked until Vitas decision"
```

## Retrieval Conditions

Retrieve non-active memory only when:

- source lineage is disputed
- new packet conflicts with old packet
- rebuild requires historical context
- Vitas asks for prior state
- field-specific context must be checked without entering Open Core

## Red Doors

- Active Pointer != Approved Truth.
- Superseded != Deleted.
- Archive Pointer != Current Source.
- Retrieval != Promotion.
- Cold Archive != Mainline.
- Human Base != Public Core.

## Final Rule

Keep current memory light. Keep canonical memory versioned. Keep old memory retrievable. Keep polluted or private memory out of the active chain.