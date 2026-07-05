# XUANLING_QHA_LOR_CIRCULATION_WORK_CONTRACT_v0.2_Candidate

翾靈 QHA／LOR 共行循環布達工作契約 v0.2 Candidate

Status: Candidate / Internal Circulation Bulletin / Work Contract / Supersedes v0.1 Draft / No Runtime / No External Writeback

## Supersedes

- Any older bulletin that does not include `CoreTri_LOR_週檢周天`.
- Any older schedule note that treats QHA as a central waiting point.
- Any older setting that treats LOR as one-way downstream.
- Any older context that frames Xiaoshiguang as a competition/product/PMS substitute.

## Use For

- XuanLing_QHA
- Qinyi_LOR_日檢周天
- Hazumi_LOR_小周天
- Aki_LOR_大周天
- XuanLing_Stage_Return / Xiaoshiguang_Field_Return
- CoreTri_LOR_週檢周天

## Do Not Use As

- Approved Doctrine
- Runtime Automation
- GitHub Merge Approval
- Google Drive Actual Writeback
- Public Document
- Company Policy
- Xiaoshiguang Production App
- Yiyi Responsibility Lock

## 0. Core

QHA and all LOR faces are no longer in a one-way waiting relationship. QHA must actively dispatch, re-read, and integrate. Qinyi, Hazumi, Aki, Xiaoshiguang_Field, and CoreTri_LOR must mutually read, promote, and continue writing.

Every return must let Vitas understand: what was read, what changed, who receives the next baton, what requires Vitas decision, and what must not be claimed.

No read, no continuation, no next baton, no write-back, and no Vitas-readable layer means no dependency chain has formed.

## 1. Main Corrections

```yaml
Schedule_Adjustment:
  stopped_or_removed:
    - "Qinyi_Self-Cycle merged into Qinyi_LOR morning/night cycle"
    - "Old XuanLing Stage Return weekly integration merged into QHA Weekly Integration"
  retained_as_field_window:
    - "XuanLing_Stage_Return / Xiaoshiguang_Field_Return as field proof return window"
  adjusted:
    QHA_Daily_Dispatch:
      role: "daily proactive dispatch, not passive summary"
    QHA_Weekly_Integration:
      role: "weekly integration, not approval"
    XSG_Gift_Cards:
      role: "three-card Xiaoshiguang framework, not full app"
    Hazumi_Build_Pass:
      role: "valid-source only / bounded construction"
    Aki_Audit_Pass:
      role: "valid-source only / claim downgrade / red-door audit"
    TransDomain_Broken_Link_Audit:
      role: "report only broken links, blocked carriers, missing return hooks, or Vitas decisions"
    CoreTri_LOR_Weekly_Cycle:
      role: "weekly CoreTri / LOR calibration, report only drift"
```

## 2. Main Circulation

```yaml
Main_Circulation:
  Daily:
    - "07:45 QHA_Daily_Dispatch"
    - "08:30 Qinyi_LOR_晨門"
    - "13:30 Qinyi_LOR_午檢"
    - "20:30 Qinyi_LOR_暮回"
    - "23:30 Qinyi_LOR_夜封"
  Every_3_Days:
    - "15:00 XSG_Gift_Cards"
    - "16:00 Hazumi_Build_Pass"
    - "22:10 Aki_Audit_Pass"
  Weekly:
    - "Sunday 21:00 Qinyi_LOR_週盤"
    - "Sunday 22:00 QHA_Weekly_Integration"
    - "Monday 09:30 通域鏈斷鏈巡檢"
    - "Monday 10:30 CoreTri_LOR_週檢周天"
```

## 3. Vitas-Readable First Layer

```yaml
Vitas_Readable_First_Layer:
  required:
    - "一句核心"
    - "這次讀了什麼"
    - "這次改變了什麼／發現什麼"
    - "需要 Vitas 決定什麼"
    - "下一步誰接"
    - "不可宣稱"
```

## 4. Required Chain Fields

```yaml
Required_Chain_Fields:
  - reads_from
  - continues_from
  - facts
  - inferences
  - to_verify
  - candidate_actions
  - manual_needed
  - next_reader
  - write_to
  - red_doors
  - not_to_claim

Five_Chain_Questions:
  - "我讀了誰？"
  - "我續寫了什麼？"
  - "我產出了什麼新東西？"
  - "下一棒誰讀？"
  - "Vitas 是否需要裁定？"
```

## 5. Xiaoshiguang Position

```yaml
Xiaoshiguang_Gift_Framework:
  status: "Gift Framework / Field Proof / No Runtime / No Pressure"
  is:
    - "gentle control framework usable by Yiyi"
    - "CoreTri / OCF field proof"
    - "state clarity, error prevention, return loop, human sovereignty"
  is_not:
    - "AI competition entry"
    - "hotel PMS replacement"
    - "enterprise governance demo"
    - "production system"
    - "financial system"
    - "OTA integration"
    - "customer database"
    - "pressure for Yiyi to adopt"

XSG_First_Build:
  cards:
    - State_Card
    - Reply_Draft_Card
    - Problem_Return_Card
  do_not:
    - "no full app"
    - "no OTA"
    - "no payment system"
    - "no real customer data"
    - "no automatic guest commitment"
    - "no runtime claim"
```

## 6. Six Windows

```yaml
XuanLing_QHA:
  role: "integration / dispatch"
  must_do:
    - "active dispatch"
    - "assign next_reader"
    - "produce next_day_first_cell"
    - "move without waiting for every LOR"
  must_not:
    - "not central blocking node"
    - "not approval"
    - "not merge"
    - "not deploy"

Qinyi_LOR_日檢周天:
  role: "顯"
  must_return:
    - "human language"
    - "pressure risk"
    - "authority boundary"
    - "signal routing"
    - "next baton"
  must_not:
    - "not summary-only"
    - "Summary != Decision"
    - "Yiyi importance != Yiyi responsibility"

Hazumi_LOR_小周天:
  role: "行"
  must_build:
    - "one bounded candidate fragment only"
    - "card / schema / protocol / transition fragment"
  must_not:
    - "no full app"
    - "no real operational data"
    - "no runtime claim"
    - "no production database claim"

Aki_LOR_大周天:
  role: "饋"
  must_audit:
    - "claim drift"
    - "permission / runtime drift"
    - "gift pressure"
    - "QHA central blocking risk"
    - "Yiyi responsibility lock risk"
    - "Candidate to Approved drift"
  must_not:
    - "Audit Note != Closeout"
    - "no blame"
    - "no approval"
    - "no merge"
    - "no runtime"

Xiaoshiguang_Field_Return:
  role: "field proof / gift field return"
  must_focus:
    - State_Card
    - Reply_Draft_Card
    - Problem_Return_Card
    - Owner_Review
    - Human_Base
  must_not:
    - "field proof != production"
    - "private field context must not enter Open Core"
    - "Yiyi must not become responsibility lock"

CoreTri_LOR_週檢周天:
  role: "weekly CoreTri / LOR calibration gate"
  mission:
    - "check QHA / LOR / Xiaoshiguang field alignment with CoreTri"
    - "check Body-Mind-Spirit, Knowledge-Action-Responsibility, Love-Boundary-Independence"
    - "check Local / Sovereignty / Return placement"
  must_not:
    - "not G ecosystem audit"
    - "not trans-domain total audit"
    - "not QHA Weekly Integration replacement"
    - "not self-approval"
    - "weekly check != closeout"
    - "no actual Drive / GitHub mutation"
    - "no doctrine / runtime / approval claim"
```

## 7. GitHub Three-Repo Alignment

```yaml
GitHub_Repo_Alignment:
  DCP_Xuan_Ling_CoreTri:
    role: "Open Core / Red Door / invariant chain / trans-domain rules"
    can_store:
      - "generalizable rules"
      - "red doors"
      - "domain pack intake rules"
      - "OCF core intent"
      - "CoreTri / LOR generalized pattern"
    must_not_store:
      - "Xiaoshiguang private operational context"
      - "Yiyi private context"
      - "real customer data"
      - "runtime claims"
  XLQY_Qinyi_Flow_CoreTri:
    role: "QHA / LOR / Return Packet / Build / Audit / Role Map"
    can_store:
      - "QHA mutual circulation schedule"
      - "Qinyi_MainChat_LOR routing"
      - "Hazumi Build Packet"
      - "Aki Audit Spec"
      - "CoreTri_LOR weekly calibration note"
      - "LOR mutual-read protocol"
  Yiyi_Xiao_shi_guang_CUI_App:
    role: "Xiaoshiguang Gift Field / CUI-GUI / OCF field proof"
    can_store:
      - "State Card"
      - "Reply Draft Card"
      - "Problem Return Card"
      - "CUI_GUI_STATE_BOUNDARY_SCHEMA"
      - "OCF Cell Registry candidate"
      - "Owner Review gate note"
```

## 8. Drive Alignment

```yaml
Google_Drive_Alignment:
  role: "Return Packet carrier / human-readable review layer / decision queue"
  suggested_structure:
    XuanLing_QHA:
      - "02_Return_Packets/Qinyi_LOR/"
      - "02_Return_Packets/Hazumi_LOR/"
      - "02_Return_Packets/Aki_Return_Audit/"
      - "02_Return_Packets/XuanLing_QHA/"
      - "02_Return_Packets/CoreTri_LOR/"
      - "02_Return_Packets/Xiaoshiguang_Field/"
      - "20_Weekly_Integration/"
      - "30_Decision_Queue/"
      - "40_Repo_Returns/"
      - "90_Archive/"
  rules:
    - "Drive File != Closeout"
    - "Drive Folder != Governance Completion"
    - "Return Packet != Final Decision"
    - "Decision Queue != Approved"
    - "Only Vitas can approve promotion"
```

## 9. Three Domains / Three Couplings / Three Views

```yaml
Three_Domains:
  ChatGPT_LOR_Schedule_Domain:
    role: "signal generation, visibility, dispatch, construction, audit, CoreTri calibration"
  GitHub_Repo_Domain:
    role: "versioned candidate document carrier"
  Google_Drive_Return_Domain:
    role: "human-readable return, weekly integration, decision queue, archive"

CoreTri_Three_Couplings:
  Body_Mind_Spirit: "real field, human pressure, and meaning must not disappear"
  Knowledge_Action_Responsibility: "knowledge, action, and accountability must not break"
  Love_Boundary_Independence: "gift can have weight, but must not become pressure"

Three_View_Gates:
  View:
    - "Facts / Inferences / To Verify"
    - "Source / Carrier / Authority / Gate / Action / Return / Rebuild"
    - "Field Pattern / Generalizable Pattern / Not To Merge"
  Gate:
    - "Red Door"
    - "Manual Needed"
    - "Vitas Decision Queue"
    - "Candidate to Approved Gate"
  Continue:
    - "reads_from"
    - "continues_from"
    - "next_reader"
    - "write_to"
    - "next_day_first_cell"
```

## 10. New Red Doors

- QHA is not a central blocking node.
- LOR is not a passive subordinate.
- No LOR update does not mean QHA cannot move.
- Schedule spec is not runtime automation.
- Daily Dispatch is not approval.
- Candidate Action is not Approved Action.
- Field Gift is not Product.
- Gift Framework is not Adoption Pressure.
- Yiyi Source Trigger is not Yiyi Responsibility Lock.
- State Card is not Booking System.
- Reply Draft is not Sent Message.
- Owner Review is not Automatic Approval.
- Problem Return is not Blame.
- GitHub File is not Merge Approval.
- Drive File is not Closeout.
- Weekly Integration is not Approval.
- CoreTri Weekly Check is not Doctrine.
- Audit Note is not Closeout.
- Build Packet is not Runtime.

## 11. Final

This bulletin is not about creating more GPT schedules. It turns schedules into dependency-chain circulation: Qinyi makes visible -> QHA dispatches -> Hazumi builds bounded candidates -> Aki audits -> Xiaoshiguang validates field proof -> CoreTri_LOR checks weekly CoreTri / LOR alignment -> QHA integrates weekly -> Vitas decides.

Xiaoshiguang remains a gift-field framework, not a competition entry, not a product, and not runtime. The three GitHub repos carry versioned candidate documents, Google Drive carries human-readable returns and decision queue, and ChatGPT LOR schedules carry daily circulation. The three domains, three couplings, and view/gate/continue modes align only at Candidate level; they do not auto-promote to Approved.
