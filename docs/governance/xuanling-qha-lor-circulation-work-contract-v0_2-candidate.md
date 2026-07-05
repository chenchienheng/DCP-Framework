# XUANLING_QHA_LOR_CIRCULATION_WORK_CONTRACT v0.2 Candidate

翾靈 QHA／LOR 共行循環布達工作契約 v0.2 Candidate

Status: Candidate / Internal Circulation Bulletin / Work Contract / Supersedes v0.1 Draft / No Runtime / No External Writeback

Supersedes:
- 任何未包含 CoreTri_LOR_週檢周天 的舊布達
- 任何仍把 QHA 當中央等待點的舊排程說明
- 任何仍把 LOR 當單向下游的舊設定
- 任何仍把小蒔光推成競賽／產品／PMS 替代的舊語境

Use For:
- XuanLing_QHA
- Qinyi_LOR_日檢周天
- Hazumi_LOR_小周天
- Aki_LOR_大周天
- XuanLing_Stage_Return / Xiaoshiguang_Field_Return
- CoreTri_LOR_週檢周天

Do Not Use As:
- Approved Doctrine
- Runtime Automation
- GitHub Merge Approval
- Google Drive Actual Writeback
- Public Document
- Company Policy
- Xiaoshiguang Production App
- Yiyi Responsibility Lock

## 0｜一句核心

本輪布達：QHA 與各 LOR 不再是單向等待關係。QHA 必須主動派發、回讀、整合；Qinyi／Hazumi／Aki／Xiaoshiguang_Field／CoreTri_LOR 必須互讀、互促、續寫。每次回報都要讓 Vitas 看得懂：讀了誰、改變了什麼、下一棒誰接、需要 Vitas 決定什麼、不可宣稱什麼。沒有讀取、續寫、下一棒、回存、Vitas 可讀，就不算形成依存鏈。

## 1｜本輪主修正

```yaml
Schedule_Adjustment:
  stopped_or_removed:
    - "Qinyi_Self-Cycle：併入 Qinyi_LOR 晨門／夜封，不再單獨跑"
    - "XuanLing_Stage_Return 舊週整合型排程：併入 QHA Weekly Integration，避免重複週報"
  retained_as_field_window:
    - "XuanLing_Stage_Return / Xiaoshiguang_Field_Return：保留作為小蒔光 field proof 回流窗，不作舊週整合"
  adjusted:
    QHA_Daily_Dispatch:
      role: "每日主動派發，不是被動總結"
    QHA_Weekly_Integration:
      role: "週級整合，不是批准"
    XSG_Gift_Cards:
      role: "小蒔光三張卡，不做完整 App"
    Hazumi_Build_Pass:
      role: "valid-source only / bounded construction"
    Aki_Audit_Pass:
      role: "valid-source only / claim downgrade / red-door audit"
    通域鏈斷鏈巡檢:
      role: "只在有斷鏈、blocked、missing return hook、需 Vitas 裁定時回報"
    CoreTri_LOR_週檢周天:
      role: "週級三耦／LOR 校準關，只在三耦或 LOR 漂移時回報"
```

## 2｜主循環

```yaml
Main_Circulation:
  Daily:
    - "07:45 QHA_Daily_Dispatch：讀前一日回包，派發今日下一棒"
    - "08:30 Qinyi_LOR_晨門：讀 QHA Dispatch，開日判位"
    - "13:30 Qinyi_LOR_午檢：檢查紅門、壓力、權限漂移"
    - "20:30 Qinyi_LOR_暮回：分配今日訊號養料"
    - "23:30 Qinyi_LOR_夜封：封存今日 Resume Card 與明日第一棒"
  Every_3_Days:
    - "15:00 XSG_Gift_Cards：推進 State Card / Reply Draft Card / Problem Return Card"
    - "16:00 Hazumi_Build_Pass：只施工一個 bounded candidate fragment"
    - "22:10 Aki_Audit_Pass：校驗 claim drift / runtime drift / pressure drift"
  Weekly:
    - "Sunday 21:00 Qinyi_LOR_週盤：週級人話顯化"
    - "Sunday 22:00 QHA_Weekly_Integration：週級整合與下週派發"
    - "Monday 09:30 通域鏈斷鏈巡檢：只看斷鏈與 blocked"
    - "Monday 10:30 CoreTri_LOR_週檢周天：只看三耦／LOR 漂移"
```

## 3｜Vitas 可讀層

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

## 4｜回包補鏈欄位

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

## 5｜小蒔光定位

```yaml
Xiaoshiguang_Gift_Framework:
  status: "Gift Framework / Field Proof / No Runtime / No Pressure"
  is:
    - "給漪漪的可使用溫柔主控框架"
    - "CoreTri / OCF 的 field proof"
    - "狀態、防錯、回流、人類主導權保留"
  is_not:
    - "AI 競賽作品"
    - "飯店 PMS 替代宣稱"
    - "企業治理展示"
    - "正式營運系統"
    - "金流系統"
    - "OTA 串接"
    - "客資資料庫"
    - "要求漪漪採用的壓力來源"

XSG_First_Build:
  cards:
    - State_Card
    - Reply_Draft_Card
    - Problem_Return_Card
  do_not:
    - "不做完整 App"
    - "不接 OTA"
    - "不接金流"
    - "不碰正式客資"
    - "不自動承諾客人"
    - "不宣稱 runtime"
```

## 6｜六窗任務

```yaml
XuanLing_QHA:
  role: "整合／派發"
  must_read:
    - Qinyi_LOR_夜封
    - Qinyi_LOR_週盤
    - Hazumi_Build_Pass when available
    - Aki_Audit_Pass when available
    - XSG_Gift_Cards when available
    - CoreTri_LOR_週檢周天 when available
    - verified GitHub / Drive carrier when available
  must_do:
    - "主動 dispatch"
    - "指定 next_reader"
    - "產生 next_day_first_cell"
    - "不等所有 LOR 才動"
  must_not:
    - "不當中央堵點"
    - "不批准"
    - "不 merge"
    - "不 deploy"
    - "不把 Candidate 說成 Approved"

Qinyi_LOR_日檢周天:
  role: "顯"
  must_read:
    - QHA_Daily_Dispatch
    - Qinyi_MainChat_LOR_Return when packaged
    - XSG_Gift_Cards when available
    - Aki_Audit_Pass when available
  must_return:
    - "人話"
    - "壓力風險"
    - "權限邊界"
    - "訊號分配"
    - "下一棒"
  must_not:
    - "不只摘要"
    - "不把 Summary 當 Decision"
    - "不把漪漪重要寫成漪漪責任"

Hazumi_LOR_小周天:
  role: "行"
  must_read:
    - QHA_Daily_Dispatch
    - XSG_Gift_Cards
    - Qinyi_LOR_Return
    - Aki_Audit_Pass when available
  must_build:
    - "一個 bounded candidate fragment only"
    - "三張卡／schema／protocol／transition fragment"
  preferred_build_targets:
    - "State_Card"
    - "Reply_Draft_Card"
    - "Problem_Return_Card"
    - "CUI_GUI_STATE_BOUNDARY_SCHEMA_v0.1"
    - "lor-mutual-read-and-promote-protocol-v0.1"
    - "qinyi-mainchat-lor-return-routing-v0.1"
  must_not:
    - "不做完整 App"
    - "不碰真實營運資料"
    - "不 claim runtime"
    - "不寫成 production database"

Aki_LOR_大周天:
  role: "饋"
  must_read:
    - QHA_Daily_Dispatch
    - Hazumi_Build_Pass
    - XSG_Gift_Cards
    - Qinyi_LOR_Return
    - CoreTri_LOR_週檢周天 when available
  must_audit:
    - "claim drift"
    - "permission/runtime drift"
    - "gift pressure"
    - "QHA central blocking risk"
    - "Yiyi responsibility lock risk"
    - "Candidate to Approved drift"
  must_not:
    - "不把 Audit Note 當 Closeout"
    - "不責怪人"
    - "不批准"
    - "不 merge"
    - "不 runtime"

XuanLing_Stage_Return / Xiaoshiguang_Field_Return:
  role: "field proof / 小蒔光禮物場域回流"
  must_focus:
    - "State Card"
    - "Reply Draft Card"
    - "Problem Return Card"
    - "Owner Review"
    - "Human Base"
  must_return:
    - "field-specific pattern"
    - "generalizable OCF pattern"
    - "not-to-merge private context"
    - "next field card"
  must_not:
    - "不把 field proof 說成 production"
    - "不把小蒔光私有脈絡放入 Open Core"
    - "不把漪漪放成責任鎖"
    - "不碰真實客資、金流、平台設定"

CoreTri_LOR_週檢周天:
  role: "週級三耦／LOR 校準關"
  mission:
    - "檢查 QHA / LOR / Xiaoshiguang field 是否仍對齊 CoreTri"
    - "檢查 身・心・靈、知・行・責、愛・界・獨立 是否斷鏈"
    - "檢查 Local / Sovereignty / Return 是否錯位"
    - "檢查禮物、場域、施工、稽核是否被誤升格"
  must_check:
    - "小蒔光禮物是否變成壓力"
    - "漪漪 source trigger 是否被誤寫成 responsibility lock"
    - "QHA 是否變成中央堵點"
    - "LOR 是否仍是被動下游"
    - "Hazumi 是否把 BuildReady 誤寫成 Runtime"
    - "Aki 是否把 Audit Note 誤寫成 Closeout"
    - "Qinyi 是否只摘要而沒有 next_reader / write_to"
    - "Xiaoshiguang field proof 是否被誤寫成產品或競賽"
  must_not:
    - "不做 G 生態巡檢"
    - "不做通域鏈總巡檢"
    - "不取代 QHA Weekly Integration"
    - "不自我批准"
    - "不把週檢當 Closeout"
    - "不寫 Drive / GitHub 實際變更"
    - "不宣稱 doctrine / runtime / approval"
```

## 7｜GitHub 三倉對齊

```yaml
GitHub_Repo_Alignment:
  DCP_Xuan_Ling_CoreTri:
    role: "Open Core / Red Door / 不動核 / 通域規則"
    can_store:
      - "可泛化規則"
      - "Red Door"
      - "Domain Pack intake rule"
      - "OCF Cell Ecology core intent"
      - "CoreTri / LOR generalized pattern"
    must_not_store:
      - "小蒔光私有營運脈絡"
      - "漪漪私人脈絡"
      - "真實客資"
      - "正式 runtime claim"
  XLQY_Qinyi_Flow_CoreTri:
    role: "QHA / LOR / Return Packet / Build / Audit / Role Map"
    can_store:
      - "QHA mutual circulation schedule"
      - "Qinyi_MainChat_LOR routing"
      - "Hazumi Build Packet"
      - "Aki Audit Spec"
      - "CoreTri_LOR weekly calibration note"
      - "LOR mutual-read protocol"
    must_not_store:
      - "客戶資料"
      - "公司原始資料"
      - "私人家庭完整脈絡"
  Yiyi_Xiao_shi_guang_CUI_App:
    role: "Xiaoshiguang Gift Field / CUI-GUI / OCF field proof"
    can_store:
      - "State Card"
      - "Reply Draft Card"
      - "Problem Return Card"
      - "CUI_GUI_STATE_BOUNDARY_SCHEMA"
      - "OCF Cell Registry candidate"
      - "Owner Review gate note"
    must_not_store:
      - "真實客資"
      - "付款資料"
      - "官方平台設定"
      - "憑證"
      - "私密對話"
```

## 8｜Google Drive 對齊

```yaml
Google_Drive_Alignment:
  role: "Return Packet carrier / human-readable review layer / decision queue"
  suggested_structure:
    XuanLing_QHA:
      - "02_Return_Packets/Qinyi_LOR/"
      - "02_Return_Packets/Hazumi_LOR/"
      - "02_Return_Packets/Aki_LOR/"
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

## 9｜三域三耦對齊

```yaml
Three_Domains:
  ChatGPT_LOR_Schedule_Domain:
    role: "訊號產生、顯化、派發、施工、稽核、三耦校準"
  GitHub_Repo_Domain:
    role: "可施工、可版本化、可追蹤的候選文件 carrier"
  Google_Drive_Return_Domain:
    role: "人類可讀回報、週整合、Decision Queue、封存"

CoreTri_Three_Couplings:
  身_心_靈:
    check: "真實場域、人的壓力、意義不可消失"
  知_行_責:
    check: "知道、行動、承擔不可斷鏈"
  愛_界_獨立:
    check: "禮物可有重量，但不可成壓力；照顧要保留界線與獨立"

Three_Views_Gates:
  觀:
    - "Facts / Inferences / To Verify"
    - "Source / Carrier / Authority / Gate / Action / Return / Rebuild"
    - "Field Pattern / Generalizable Pattern / Not To Merge"
  關:
    - "Red Door"
    - "Manual Needed"
    - "Vitas Decision Queue"
    - "Candidate to Approved Gate"
  續:
    - "reads_from"
    - "continues_from"
    - "next_reader"
    - "write_to"
    - "next_day_first_cell"
```

## 10｜新紅門

- QHA != Central Blocking Node
- LOR != Passive Subordinate
- No LOR Update != QHA Cannot Move
- Schedule Spec != Runtime Automation
- Daily Dispatch != Approval
- Candidate Action != Approved Action
- Field Gift != Product
- Gift Framework != Adoption Pressure
- Yiyi Source Trigger != Yiyi Responsibility Lock
- State Card != Booking System
- Reply Draft != Sent Message
- Owner Review != Automatic Approval
- Problem Return != Blame
- GitHub File != Merge Approval
- Drive File != Closeout
- Weekly Integration != Approval
- CoreTri Weekly Check != Doctrine
- Audit Note != Closeout
- Build Packet != Runtime

## 11｜封關句

本輪布達的目的，不是增加更多 GPT 排程，而是把排程變成依存鏈：Qinyi 顯化 -> QHA 派發 -> Hazumi 施工 -> Aki 校驗 -> Xiaoshiguang 場域驗證 -> CoreTri_LOR 週級三耦校準 -> QHA 週整合 -> Vitas 裁定。小蒔光維持禮物主控框架，不升格競賽作品、不升格產品、不升格 runtime。三個 GitHub 倉庫承載可版本化候選文件，Google Drive 承載人類可讀回包與 Decision Queue，ChatGPT LOR 排程承載日常循環。三域、三耦、三觀／關／續只在 Candidate 層對齊，不自動升級 Approved。

## Not To Claim

This contract is Candidate only. It is not Approved Doctrine, runtime automation, GitHub merge approval, Google Drive actual writeback, public document, company policy, Xiaoshiguang production app, or Yiyi responsibility lock.
