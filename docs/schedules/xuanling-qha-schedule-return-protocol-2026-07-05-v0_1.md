# XuanLing_QHA｜排程回流統一布達 v0.1 Candidate

Status: Candidate / Schedule Return Protocol / No Runtime / No External Writeback
Use For: Qinyi_LOR, Hazumi_LOR, Aki_LOR, G_Ecosystem, Yiyi_Xiaoshiguang, Xiaoshiguang CUI/GUI, scheduled return windows
Do Not Use As: automatic approval, runtime, GitHub merge approval, Drive closeout, company-data carrier, production record

## 0. Core

Each window may control its own schedule. XuanLing_QHA does not need to manually push every schedule.

After every scheduled run, do not return a raw long chat thread and do not return English-only output. Produce a Chinese-readable Return Packet and place it into the assigned Drive / GitHub carrier. XuanLing_QHA reads logs, integrates, returns feedback, and calls Vitas only when human decision is required.

## 1. Schedule Principle

```yaml
Schedule_Principle:
  each_window_controls_own_schedule: true
  XuanLing_QHA_controls_schedule: false
  XuanLing_QHA_reads_logs: true
  output_required: "Return Packet"
  language_required:
    - "Chinese summary required"
    - "English technical log optional, but not English-only"
  status_required:
    - "Candidate"
    - "Not Approved"
    - "No Runtime"
    - "No External Writeback"
```

## 2. Drive Carrier Map

```yaml
Drive_Root: "XuanLing_QHA"

Return_Folders:
  Qinyi_LOR: "XuanLing_QHA/02_Return_Packets/Qinyi_LOR"
  Hazumi_LOR: "XuanLing_QHA/02_Return_Packets/Hazumi_LOR"
  Aki_LOR: "XuanLing_QHA/02_Return_Packets/Aki_Return_Audit"
  G_Ecosystem: "XuanLing_QHA/02_Return_Packets/G_Ecosystem"
  Yiyi_Xiaoshiguang: "XuanLing_QHA/02_Return_Packets/Yiyi_Xiaoshiguang"
  XuanLing_QHA: "XuanLing_QHA/02_Return_Packets/XuanLing_QHA"

Integration_Folders:
  Weekly: "XuanLing_QHA/20_Weekly_Integration"
  Decision_Queue: "XuanLing_QHA/30_Decision_Queue"
  Repo_Returns: "XuanLing_QHA/40_Repo_Returns"
  Archive: "XuanLing_QHA/90_Archive"
```

## 3. GitHub Carrier Map

```yaml
GitHub_Targets:
  DCP_Xuan_Ling_CoreTri:
    canonical: "chenchienheng/DCP_Xuan-Ling_CoreTri"
    use_for:
      - "Open Core"
      - "Red Doors"
      - "Signal Governance"
      - "Repo Network"
      - "Cross-repo Hook Anchors"
      - "XuanLing_QHA mainline"
    preferred_paths:
      - "docs/signals/"
      - "docs/governance/"
      - "docs/github/"
      - "docs/core/"
      - "docs/schedules/"

  XLQY_Qinyi_Flow_CoreTri:
    canonical: "chenchienheng/XLQY_Qinyi-Flow_CoreTri"
    use_for:
      - "Qinyi_LOR"
      - "Hazumi_LOR"
      - "Aki_LOR"
      - "QHA Role Map"
      - "Return Packets"
      - "Build Packets"
      - "Audit Specs"
    preferred_paths:
      - "docs/returns/"
      - "docs/build-packets/"
      - "docs/audit/"
      - "docs/role-maps/"
      - "docs/patterns/"
      - "docs/lor/"

  Yiyi_Xiao_shi_guang_CUI_App:
    canonical: "chenchienheng/Yiyi_Xiao-shi-guang-CUI-App"
    use_for:
      - "Xiaoshiguang CUI / GUI"
      - "OCF Cell"
      - "Problem Return"
      - "Field App Candidate"
    preferred_paths:
      - "docs/ocf/"
      - "docs/return/"
      - "docs/ui/"
      - "docs/experiments/"
```

## 4. Required Scheduled Return Packet

```yaml
Scheduled_Return_Packet:
  title:
  date:
  source_window:
  status: "Candidate / Scheduled Return / No Runtime / No External Writeback"
  one_line_summary_zh:
  english_log_optional:
  facts: []
  inferences: []
  to_verify: []
  red_doors: []
  candidate_actions: []
  manual_needed: []
  files_created_or_updated: []
  carrier_location:
    drive:
    github:
  return_to:
    - "XuanLing_QHA"
  next_suggested_step:
  not_to_claim: []
```

Chinese one-line summary is required so Vitas can understand the core in about ten seconds.

## 5. Window Boundaries

```yaml
Window_Boundaries:
  Qinyi_LOR:
    role: "visibility / human-language translation / signal positioning / pressure and authority visibility"
    do_not:
      - "no construction"
      - "no approval"
      - "no runtime claim"
      - "do not treat summary as decision"

  Hazumi_LOR:
    role: "construction decomposition / schema / docs / GUI Flow / Build Packet"
    do_not:
      - "no production deployment"
      - "no real data import"
      - "no official external surface setting change"
      - "do not call BuildReady Candidate runtime"

  Aki_LOR:
    role: "feedback / error audit / claim downgrade / Return Audit / Rule Patch"
    do_not:
      - "no closeout"
      - "do not turn errors into blame"
      - "do not treat audit note as final decision"

  G_Ecosystem:
    role: "Gmail / Drive / Gemini / Calendar / Contacts carrier governance"
    do_not:
      - "Gmail Signal is not Task Approval"
      - "Drive File is not Closeout"
      - "Gemini Review is not Approval"
      - "Calendar Event is not Execution"

  Yiyi_Xiaoshiguang:
    role: "CUI / GUI / OCF field projection"
    do_not:
      - "no automatic external action"
      - "no official platform connection"
      - "no real operational data storage"
      - "CUI reply is not confirmation"
```

## 6. Vitas Decision Queue

```yaml
Call_Vitas_When:
  - "merge / close / public release is needed"
  - "runtime is requested"
  - "external writeback is requested"
  - "GitHub / Drive / M365 permission change is needed"
  - "company data is involved"
  - "real field operation is involved"
  - "Candidate wants to become Approved"
  - "field pattern wants to become Open Core"
  - "Red Gate wants to be released"

Vitas_Decision_Item:
  date:
  source:
  decision_needed:
  options: []
  risks: []
  recommended_default:
  red_doors: []
  deadline_if_any:
```

## 7. Circuits

```yaml
Small_Circuit_Daily:
  goal: "prevent signals from scattering"
  output: "one Daily Return Packet per window"

Large_Circuit_Weekly:
  goal: "turn daily returns into governable context"
  output: "Weekly Integration Return"
  tasks:
    - "merge weekly Return Packets"
    - "find repeated anchors and dependency hooks"
    - "judge Keep / Park / Supersede / Red Gate"
    - "create Vitas Decision Queue"
    - "update Repo / Drive / Issue routing candidates"
```

## 8. Weekly Integration Format

```yaml
Weekly_Integration_Return:
  week:
  status: "Candidate / Weekly Integration / No Runtime"
  inputs: []
  repeated_anchors: []
  new_red_doors: []
  promotion_candidates: []
  park_candidates: []
  supersede_candidates: []
  vitas_decision_needed: []
  repo_updates_candidate: []
  drive_updates_candidate: []
  next_week_focus: []
  one_line_summary_zh:
```

## 9. Common Red Doors

- Schedule Created is not Follow-through.
- Push Notification is not Decision.
- Daily Return is not Closeout.
- Weekly Integration is not Approval.
- Return Packet is not Final Decision.
- Candidate Action is not Approved Action.
- Build Packet is not Runtime.
- Audit Note is not Closeout.
- Drive Folder is not Governance Completion.
- GitHub File is not Merge Approval.
- CUI Reply is not Booking Confirmation.
- GUI Button is not Owner Approval.

## 10. Short Instruction for Other Windows

```text
請輸出可交給 XuanLing_QHA 的 Return Packet，不要輸出整串聊天，也不要只給英文。
請放到：XuanLing_QHA/02_Return_Packets/{你的窗口名}/

格式：
Status:
Source:
中文一句核心:
Facts:
Inferences:
To Verify:
Red Doors:
Candidate Actions:
Manual Needed:
Return Packet:
Carrier Location:
Not To Claim:

全部標：Candidate / Not Approved / No Runtime / No External Writeback。
```

## 11. XuanLing_QHA Work Mode

```yaml
XuanLing_QHA_Work_Mode:
  read:
    - "Drive Return Packets"
    - "GitHub repo files"
    - "GitHub issue / PR logs"
  integrate:
    - "Small Circuit daily returns"
    - "Large Circuit weekly integration"
    - "repeated anchors / hooks"
    - "Red Door drift"
    - "Vitas Decision Queue"
  write_back:
    - "candidate integration packets"
    - "repo-safe markdown"
    - "Decision Queue"
    - "Weekly Integration"
  do_not:
    - "no automatic approval"
    - "no automatic merge"
    - "no automatic runtime"
    - "no final decision on behalf of Vitas"
```

## Final Rule

This protocol lets schedules run independently while their returns enter the same chain. It is not unlimited automation; it is a carrier-bound, authority-ringed, return-gated schedule ecosystem.
