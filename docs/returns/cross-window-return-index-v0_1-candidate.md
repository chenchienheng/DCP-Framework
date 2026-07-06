# Cross-Window Return Index v0.1 Candidate

Status: Candidate / Cross-Window Return Index / No Runtime / No External Writeback
Use As: index for QHA/LOR/MainChat/field return packets and next-reader continuity
Do Not Use As: closeout, approval, task completion proof, or runtime schedule

## Core

A return becomes useful only when it is linked: reads_from, continues_from, next_reader, write_to, red_doors, and not_to_claim must be visible.

## Return Index Row

```yaml
Cross_Window_Return_Row:
  return_id:
  source_window:
  reads_from: []
  continues_from: []
  facts: []
  inferences: []
  to_verify: []
  candidate_actions: []
  manual_needed: []
  next_reader: []
  write_to:
  red_doors: []
  not_to_claim: []
  retention_class:
  active_pointer:
  archive_pointer:
```

## Window Types

```yaml
Window_Types:
  Qinyi_LOR: "human-readable signal and pressure boundary"
  Hazumi_LOR: "bounded build packet"
  Aki_LOR: "audit / drift / red-door patch"
  XuanLing_QHA: "dispatch / integration / decision queue"
  Qinyi_MainChat_LOR: "daily conversation signal entrance"
  CoreTri_LOR: "weekly CoreTri / LOR calibration"
  Xiaoshiguang_Field: "field gift / OCF CUI-GUI return"
```

## Red Doors

- Return Index != Closeout.
- Next Reader != Approval.
- Active Pointer != Approved Truth.
- Missing Return Hook != Failure.
- Filed Return != Read Return.

## Final Rule

QHA should use this index to read active returns, detect missing hooks, and dispatch the next reader without re-reading every full packet.