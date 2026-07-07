# One-Hub Schedule Adjustment Report 2026-07-07 v0.1

Status: Candidate / Schedule Governance Patch / QHA Intake Report / No Runtime / No External Writeback
Use As: report for XuanLing_QHA to understand that the schedule surface has been consolidated into One-Hub mode
Do Not Use As: approved doctrine, runtime automation, task closeout, or proof of completed handoff

## One Core Sentence

The schedule layer has been changed from multi-window role reports to One-Hub mode: QHA Daily Hub is the only fixed daily entry point, QHA Weekly Hub is the only fixed weekly integration window, and role windows are paused unless Vitas or QHA manually expands them.

## What Changed

```yaml
Schedule_Adjustment:
  from:
    mode: "multi-window role reports"
    problem:
      - "many scheduled outputs opened separate conversations"
      - "next_reader was being mistaken as handoff"
      - "Vitas could be flooded by unread scheduled windows"
      - "reports could multiply without ACK or carrier filing"
  to:
    mode: "One-Hub / Daily Inbox"
    daily_visible_window: "QHA Daily Hub"
    weekly_visible_window: "QHA Weekly Hub"
    sidecars:
      - "Morning Signal: notify only on material high-signal external events"
      - "Gmail Hygiene Watch: notify only on substantive drift, risk, or broken chain"
```

## Active Schedule Surface After Adjustment

```yaml
Active_Now:
  Core_Hub:
    - "QHA Daily Hub"
    - "QHA Weekly Hub"
  Sidecar_Only:
    - "Morning Signal"
    - "Gmail Hygiene Watch"
  Non_QHA_Exception:
    - "Contacts Audit may still exist as a separate experiment/side branch if active; it is not part of QHA/LOR main chain"
```

## Paused Role Windows

```yaml
Paused_Role_Windows:
  - "Qinyi_LOR 晨門"
  - "Qinyi_LOR 午檢"
  - "Qinyi_LOR 暮回"
  - "Qinyi_LOR 夜封"
  - "Qinyi_LOR 週盤"
  - "Hazumi Build Pass"
  - "Aki Audit Pass"
  - "XSG Field Return"
  - "CoreTri_LOR 週檢周天"
  - "通域鏈斷鏈巡檢"
```

## New Hub Rule

```yaml
One_Hub_Schedule_Rule_v0_1:
  daily:
    only_fixed_output: "QHA Daily Hub"
    max_visible_decisions: 3
    if_previous_unread: "Pending_Vitas_Read / Backlog_Not_Expanded"
  weekly:
    only_fixed_output: "QHA Weekly Hub"
    if_daily_backlog_pending: "Weekly_Backlog_Not_Expanded"
  role_windows:
    mode: "manual_or_QHA_assigned_only"
    not_auto_push: true
  handoff:
    next_reader_is_not_ack: true
    requires:
      - "previous_packet_id or reads_from match"
      - "received_by"
      - "accepted_scope"
      - "next_return_required"
```

## QHA Daily Hub Output Limits

```yaml
QHA_Daily_Hub_Output:
  required:
    - "one core sentence"
    - "New_Input / No_New_Input"
    - "Pending_Vitas_Read backlog count/items"
    - "Needs_Decision top 1-3"
    - "Suggested next_reader candidates"
    - "Missing_Return_Request if needed"
    - "Red Doors"
    - "Filing_Block candidate"
  forbidden:
    - "do not expand long packets unless new verified material exists"
    - "do not simulate role reports"
    - "do not claim handoff completion without ACK"
    - "do not open or simulate Hazumi/Aki/Qinyi/CoreTri windows"
```

## Sidecar Rule

```yaml
Sidecars:
  Morning_Signal:
    notify_only_if: "material high-signal external event"
    if_hub_backlog_pending: "Signal_Pointer only"
    not: "daily news report"
  Gmail_Hygiene_Watch:
    notify_only_if: "substantive label drift, account/security risk, broken chain, or Vitas decision needed"
    if_hub_backlog_pending: "Hygiene_Pointer only"
    not: "Gmail native filter or bulk organizer"
```

## Red Doors

- Schedule Output != Handoff.
- Next Reader != ACK.
- Many Reports != Circulation.
- No Read Yet != Failure.
- Unseen Window != Work Done.
- QHA Daily Hub != Closeout.
- QHA Weekly Hub != Approval.
- Sidecar Signal != QHA Dispatch.
- Filing_Block != Actual Writeback.
- Suggested Repo File != Commit.
- Suggested Drive Folder != Drive Write.

## Routing After Adjustment

```yaml
Routing:
  Vitas_MainChat:
    role: "free signal intake / immediate judgment / packet preparation"
  QHA_Daily_Hub:
    role: "daily inbox / intake / backlog / decision queue / candidate next_reader"
  Role_Windows:
    role: "manual branch expansion only"
    examples:
      Qinyi: "human-language or pressure/authority check"
      Hazumi: "bounded build only after QHA/Vitas assignment"
      Aki: "audit only when drift/risk exists"
      CoreTri: "weekly calibration only when 三耦/LOR drift exists"
      XSG: "field return only when actual field source exists"
```

## QHA Instruction

QHA should stop expecting independent daily role packets from Qinyi, Hazumi, Aki, CoreTri, or XSG. If a role packet is needed, QHA should list it as a candidate next_reader or Missing_Return_Request and wait for Vitas or manual branch expansion.

QHA should treat the Daily Hub as the daily inbox, not as closeout. If Vitas has not read or acknowledged yesterday's hub, QHA should not create a full new long report. It should output Backlog_Not_Expanded.

## Final Judgment

```yaml
Final_Judgment:
  main_chain: "improved and consolidated"
  experiment_branch: "paused / manual expansion / side-branch feedback"
  closed_loop_proof: "still requires ACK and filed carrier evidence"
  next_need:
    - "QHA should read this report before its next Daily Hub run"
    - "future schedule outputs should follow One-Hub mode"
```
