# Repo Cleanup Migration Queue v0.1

Status: Candidate / Cleanup Queue / No Runtime / No External Writeback
Use As: migration and cleanup queue for three-repo alignment and future physical file moves
Do Not Use As: deletion order, merge approval, public release, or automated migration rule

## Core

Cleanup must proceed by classification before physical movement. Do not move or delete files until the target ring, current status, and replacement pointer are clear.

## Queue Classes

```yaml
Cleanup_Class:
  Keep_Current:
    meaning: "active current file; keep in current index"
  Move_To_Alignment:
    meaning: "repo-role / current / index file"
  Move_To_Governance:
    meaning: "red door, gate, containment, authority rule"
  Move_To_Template:
    meaning: "reusable schema or return packet template"
  Move_To_Domain_Pack:
    meaning: "domain-specific but generalizable support file"
  Move_To_Fieldspace:
    meaning: "belongs to field repo, not root core"
  Mark_Reference:
    meaning: "useful background, not active truth"
  Mark_Superseded:
    meaning: "replaced by newer file; keep lineage pointer"
  Archive_Cold:
    meaning: "historical full text; not active read"
  Red_Gate_Hold:
    meaning: "do not route until Vitas decision"
```

## First Cleanup Sprint

```yaml
Sprint_01:
  DCP:
    priority:
      - "keep alignment / governance / memory / registry / router / output / domain-pack files active"
      - "mark old daily signal and old circulation drafts reference or superseded after review"
  XLQY:
    priority:
      - "keep dispatch / returns / audit / role-map / protocol files active"
      - "mark legacy multi-window schedule reports reference or superseded"
  Yiyi:
    priority:
      - "keep OCF / UI state / field gift / return files active"
      - "mark app-first or production-like drafts reference or superseded"
```

## Required Before Physical Move

- target repo and folder confirmed
- authority ring confirmed
- current status assigned
- active pointer updated
- supersedes / superseded_by noted
- no private or company data in destination

## Red Doors

- Cleanup Queue != Delete Order.
- Move Candidate != File Move Completed.
- Superseded != Deleted.
- Archive != Approved.
- Physical Move Requires Manual Review.

## Final Rule

First classify. Then point. Then move only when safe. Never delete as a cleanup shortcut.