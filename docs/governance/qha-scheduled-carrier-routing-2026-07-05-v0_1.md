# QHA Scheduled Carrier Routing｜2026-07-05 v0.1

Status: Candidate / Scheduling Carrier Routing / Not Approved / No Runtime / No External Writeback
Owner: Vitas
Carrier: DCP_Xuan-Ling_CoreTri
Source: Hazumi_LOR scheduled task + QHA Daily Big Cycle task setup on 2026-07-05 Asia/Taipei
Do Not Use As: Approved doctrine, runtime spec, GitHub merge approval, Drive write confirmation, or closeout.

## Core

Hazumi_LOR scheduled output becomes useful only when it has a stable carrier route. This routing note defines how scheduled Cycle Logs should move from chat output into QHA-readable candidate positions without confusing schedule triggers with authorization or repo visibility with approval.

```text
Hazumi Scheduled Task
  -> Hazumi_LOR_Cycle_Log
  -> QHA Import Key
  -> XLQY Import Index
  -> QHA Daily Absorption
  -> Aki Audit / Vitas Decision / Parked Next Cell
```

## Authority Boundary

```yaml
Authority_Boundary:
  Vitas:
    role: "owner / decision authority"
  Scheduled_Chat_Task:
    role: "log generator"
    cannot:
      - "approve"
      - "merge"
      - "write external systems unless explicitly authorized and tool-executed"
  XuanLing_QHA:
    role: "daily absorption and routing"
    cannot:
      - "turn repeated pattern into doctrine"
      - "convert suggested repo file into commit claim"
  GitHub:
    role: "candidate carrier / visible repo record"
    cannot:
      - "mean merge approval by itself"
  Drive:
    role: "working inbox / human-readable import index"
    cannot:
      - "mean closeout by itself"
```

## Repo Chain

```yaml
Repo_Chain:
  DCP_Xuan_Ling_CoreTri:
    role: "root routing / open core / red-door registry"
    candidate_paths:
      - "docs/governance/qha-scheduled-carrier-routing-YYYY-MM-DD-v0_1.md"
      - "docs/signals/"
      - "docs/github/"
  XLQY_Qinyi_Flow_CoreTri:
    role: "QHA / Qinyi-Hazumi-Aki return flow"
    candidate_paths:
      - "docs/returns/qha-cycle-log-import-index-YYYY-MM-DD.md"
      - "docs/build-packets/"
      - "docs/audit/"
  Yiyi_Xiao_shi_guang_CUI_App:
    role: "field projection only when Xiaoshiguang source is active"
    candidate_paths:
      - "docs/experiments/"
      - "docs/ocf/"
      - "docs/return/"
```

## Drive Chain

```yaml
Drive_Chain:
  working_inbox_folder: "XuanLing_QHA_Cycle_Log_Inbox"
  import_index_doc: "XuanLing_QHA_Hazumi_Cycle_Log_Import_Index_v0.1_Candidate"
  purpose:
    - "human-readable intake"
    - "manual import queue"
    - "QHA daily review target"
  boundary:
    - "Drive File ≠ Closeout"
    - "Drive-visible Output ≠ Vitas Approval"
    - "Folder Exists ≠ Runtime"
```

## Required Cycle Log Placement Field

```yaml
Hazumi_LOR_Cycle_Log_Extension:
  qha_import_key:
  suggested_carrier_placement:
    drive_working_inbox:
    github_xlqy_candidate_path:
    github_dcp_routing_path:
    xiaoshiguang_candidate_path_if_active:
```

## Red Doors

- Build Packet ≠ Runtime
- Cycle Log ≠ Closeout
- Schedule Trigger ≠ Authorization
- Spec Written ≠ Deployed
- Return Packet ≠ Approved
- GitHub-visible Output ≠ Merge Approval
- Drive File ≠ Closeout
- Tool Capability ≠ Permission
- Scheduled Chat Output ≠ Repo File
- Suggested Carrier Placement ≠ External Writeback
- Repo File ≠ Approved Mainline

## Not To Claim

This routing note is a candidate carrier map. It does not claim that all future Hazumi logs will be automatically written to GitHub or Drive. It only defines the chain by which scheduled output can be imported, reviewed, routed, and rebuilt under Vitas authority.
