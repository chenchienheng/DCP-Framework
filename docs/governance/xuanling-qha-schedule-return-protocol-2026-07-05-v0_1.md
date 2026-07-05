# XuanLing_QHA｜排程回流統一布達 v0.1 Candidate

Status: Candidate / Schedule Return Protocol / No Runtime / No External Writeback
Use For: Qinyi_LOR, Hazumi_LOR, Aki_LOR, G_Ecosystem, Yiyi_Xiaoshiguang, Xiaoshiguang CUI/GUI, and other scheduled return windows
Do Not Use As: automatic approval, runtime, GitHub merge, Drive closeout, company-data carrier, or official operation record

## Core

Each scheduled window may control its own schedule. XuanLing_QHA does not need to push every run manually. However, after every run, the window must not return only an English summary or a full raw chat transcript. It must output a Chinese-readable Return Packet and place or route it to the designated Drive / GitHub carrier so XuanLing_QHA can read logs, integrate, infer feedback, and call Vitas only when human decision is required.

```text
Schedule Trigger -> Scheduled_Return_Packet -> Drive/GitHub Candidate Carrier -> XuanLing_QHA Absorption -> Weekly Integration -> Vitas Decision Queue when needed
```

## Schedule Principle

```yaml
Schedule_Principle:
  each_window_controls_own_schedule: true
  XuanLing_QHA_controls_schedule: false
  XuanLing_QHA_reads_logs: true
  output_required: "Return Packet"
  language_required:
    - "中文摘要必須有"
    - "英文 technical log 可附，但不能只有英文"
  status_required:
    - "Candidate"
    - "Not Approved"
    - "No Runtime"
    - "No External Writeback"
```

## Drive Carrier Map

```yaml
Drive_Return_Root: "XuanLing_QHA/02_Return_Packets/"
Return_Folders:
  Qinyi_LOR: "XuanLing_QHA/02_Return_Packets/Qinyi_LOR"
  Hazumi_LOR: "XuanLing_QHA/02_Return_Packets/Hazumi_LOR"
  Aki_LOR: "XuanLing_QHA/02_Return_Packets/Aki_LOR"
  G_Ecosystem: "XuanLing_QHA/02_Return_Packets/G_Ecosystem"
  Yiyi_Xiaoshiguang: "XuanLing_QHA/02_Return_Packets/Yiyi_Xiaoshiguang"
  XuanLing_QHA: "XuanLing_QHA/02_Return_Packets/XuanLing_QHA"
Weekly_Integration: "XuanLing_QHA/20_Weekly_Integration/"
Decision_Queue: "XuanLing_QHA/30_Decision_Queue/"
Repo_Returns: "XuanLing_QHA/40_Repo_Returns/"
Archive: "XuanLing_QHA/90_Archive/"
```

## GitHub Carrier Map

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

## Required Scheduled Return Packet Format

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

Rule: `one_line_summary_zh` is required. Vitas must be able to understand the core of the packet in ten seconds.

## Window Boundaries

```yaml
Qinyi_LOR:
  role: "顯 / human translation / signal positioning / pressure and authority visibility"
  do_not:
    - "不施工"
    - "不批准"
    - "不宣稱 runtime"
    - "不把摘要當決策"

Hazumi_LOR:
  role: "行 / build decomposition / schema / docs / GUI Flow / Build Packet"
  do_not:
    - "不部署 production"
    - "不接真實資料"
    - "不碰外部平台正式設定"
    - "不把 BuildReady Candidate 說成 Runtime"

Aki_LOR:
  role: "饋 / error audit / claim downgrade / Return Audit / Rule Patch"
  do_not:
    - "不 closeout"
    - "不把錯誤變責備"
    - "不把 audit note 當最終裁定"

G_Ecosystem:
  role: "Gmail / Drive / Gemini / Calendar / Contacts carrier governance"
  do_not:
    - "不把 Gmail Signal 當 Task Approval"
    - "不把 Drive File 當 Closeout"
    - "不把 Gemini Review 當 Approval"
    - "不把 Calendar Event 當 Execution"

Yiyi_Xiaoshiguang:
  role: "Xiaoshiguang CUI / GUI / OCF field projection"
  do_not:
    - "不自動訂房"
    - "不自動付款"
    - "不接外部平台"
    - "不放真實營運資料"
    - "不把 CUI reply 當 confirmation"
```

## Call Vitas / Decision Queue

```yaml
Call_Vitas_When:
  - "需要 merge"
  - "需要 close"
  - "需要 public release"
  - "需要 runtime"
  - "需要 external writeback"
  - "需要 GitHub / Drive / M365 權限變更"
  - "涉及公司資料"
  - "涉及小蒔光真實營運"
  - "涉及付款、客戶、官方平台"
  - "Candidate 要升 Approved"
  - "field pattern 要升 Open Core"
  - "Red Gate 要解除"
```

```yaml
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

## Small / Large Circuit

```yaml
Small_Circuit_Daily:
  goal: "不要讓訊號散掉"
  output: "每窗一份 Daily Return Packet"
  preferred_flow:
    - "G_Ecosystem"
    - "Qinyi_LOR"
    - "Aki_LOR"
    - "Hazumi_LOR"
    - "XuanLing_QHA"

Large_Circuit_Weekly:
  goal: "把日檢轉成可治理脈絡"
  output: "Weekly Integration Return"
  tasks:
    - "合併一週 Return Packets"
    - "找重複點與依存勾錨"
    - "判 Keep / Park / Supersede / Red Gate"
    - "建立 Vitas Decision Queue"
    - "更新 Repo / Drive / Issue routing candidate"
```

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

## Common Red Doors

- Schedule Created != Follow-through
- Push Notification != Decision
- Daily Return != Closeout
- Weekly Integration != Approval
- Return Packet != Final Decision
- Candidate Action != Approved Action
- Build Packet != Runtime
- Audit Note != Closeout
- Drive Folder != Governance Completion
- GitHub File != Merge Approval
- CUI Reply != Booking Confirmation
- GUI Button != Owner Approval

## Short Instruction for Any Window

```text
以後排程回報請不要回整串聊天，也不要只給英文。
請輸出 Return Packet，放到：
XuanLing_QHA/02_Return_Packets/{你的窗口名}/
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
全部標：
Candidate / Not Approved / No Runtime / No External Writeback。
不要把摘要當決策，不要把回包當 closeout，不要把候選當批准。
遇到 merge、runtime、權限、公司資料、小蒔光真實營運、付款、官方平台、外部寫回，全部列 Manual Needed / Vitas Decision。
```

## XuanLing_QHA Work Mode

```yaml
XuanLing_QHA_Work_Mode:
  read:
    - "Drive Return Packets"
    - "GitHub repo files"
    - "GitHub issue / PR logs"
  integrate:
    - "日檢小周天"
    - "週檢大周天"
    - "重複點 / 勾錨"
    - "Red Door drift"
    - "Vitas Decision Queue"
  write_back:
    - "候選整合包"
    - "repo-safe markdown"
    - "Decision Queue"
    - "Weekly Integration"
  do_not:
    - "不自動批准"
    - "不自動 merge"
    - "不自動 runtime"
    - "不替 Vitas 做 final decision"
```

## Not To Claim

This protocol creates a shared return format and candidate carrier map. It does not mean Drive folders were physically created, GitHub files were merged, scheduled outputs were approved, or any runtime automation was deployed.
