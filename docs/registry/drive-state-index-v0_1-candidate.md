# Drive State Index v0.1 Candidate

Status: Candidate / Drive Index / No Runtime / No External Writeback
Use As: read-only index for Drive as return carrier and review layer
Do Not Use As: write approval, closeout, company record policy, or public release

## Core

Drive is a human-readable working-memory surface. It is not current truth by default. QHA must know which folders are active, which hold returns, which hold decisions, and which are archive or reference layers.

## Row

```yaml
Drive_Index_Row:
  name:
  role:
  current_status: "active / candidate / archive / red_gate / reference"
  readable_by_qha: false
  write_target_candidate: false
  contains_current_returns: false
  contains_decision_items: false
  active_pointer_required: true
  red_doors: []
  next_probe:
  manual_needed:
```

## Roles

```yaml
Roles:
  Master_Index: "map and latest state"
  Return_Packets: "scheduled return lanes"
  Log_Cells: "structured logs"
  Red_Door_Registry: "boundary reminders"
  Weekly_Integration: "weekly summary"
  Decision_Queue: "items requiring Vitas decision"
  Repo_Returns: "GitHub return summaries"
  Archive: "parked, superseded, or historical material"
```

## Red Doors

- Drive File != Current Truth.
- Drive Folder != Governance Completion.
- Return Packet != Closeout.
- Decision Queue != Approved.
- Active Pointer != Approved Truth.
- Archive != Deletion.
- Drive Readable != Drive Authorized Write.

## Final Rule

QHA reads Drive as a state surface. It should prefer active pointers and decision queues, not full historical folders.