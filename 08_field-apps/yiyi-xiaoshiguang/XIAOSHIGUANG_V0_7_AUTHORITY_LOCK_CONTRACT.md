# 小蒔光房況防錯 App｜v0.7 Authority Lock Contract

Status: Candidate / Authority Lock / Operation Rules / Go-live Gate / No Runtime / No Customer Data

## 0｜一句核心

v0.7 的任務不是增加功能，而是把小蒔光 App 從「可做的後台原型」補強成「權限清楚、資料回到小蒔光、維護可撤回、正式上線前有 Gate」的營運防錯工具。

---

## 1｜房務規則缺漏

Owner Decision Required:

- 實際四間房房號
- 房名對外名稱
- 房名對內名稱
- 標準二人房／和室二人房實際對應
- 每間房可住人數
- 哪些房可加床
- 加床上限
- 包棟與單房入住是否都接受
- 包棟時是否鎖定全部房間
- 包棟與散住房況是否要分開看
- 維修、自用、平台保留的判斷方式

Status: To Verify / Owner Decision Required

---

## 2｜價格與檔期缺漏

Pending Pricing Table:

- 平日價格
- 假日價格
- 旺季價格
- 連續假期價格
- 春節／跨年價格
- 包棟價格
- 加床價格
- 押金規則
- 訂金比例
- 特殊日期人工報價 Gate

Rule:

- App can suggest a price field.
- App must not auto-quote before owner-approved pricing rules.
- Special dates must be marked as owner review required.

---

## 3｜暫保留到期 Gate

Expired_Hold_Gate:
  expired_hold:
    show_warning: true
    auto_release: false
    require_human_review: true
    release_requires_operator: true
    release_log_required: true

Rule:

- 暫保留到期後，不自動釋出。
- 到期後顯示提醒。
- 釋出需人工確認並留痕。

---

## 4｜取消與延期 Gate

Cancellation_And_Reschedule:
  cancellation_required:
    - cancel_reason
    - cancelled_by
    - cancelled_at
    - customer_notified_status
  reschedule_required:
    - original_booking_reference
    - new_checkin
    - new_checkout
    - availability_rechecked

Rule:

- 取消不能只按一下完成。
- 改期需重新跑房況 Gate。
- 涉及訂金／付款時只記錄狀態，不自動退款。

---

## 5｜付款與訂金邊界

Allowed:

- 未收
- 已收
- 免訂金
- 待確認
- 匯款後五碼，若 owner 批准

Forbidden By Default:

- full payment screenshots
- raw bank account private notes
- customer financial details in public repo
- maintainer access to payment details

---

## 6｜維護臨時授權

Temporary_Maintenance_Access:
  default: "no customer PII access"
  allowed_only_if:
    - Yiyi approves
    - scope is defined
    - time window is defined
    - reason is recorded
    - access is revoked after fix
    - audit log is retained

Maintainer may see:

- system errors
- redacted screenshots
- room ID
- date range
- non-PII logs

Maintainer must not see by default:

- guest name
- phone
- LINE ID
- private message
- payment data
- full booking export

---

## 7｜Repo 權限 Gate

Repo_State:
  name: "future private runtime repo"
  visibility: "private"
  owner: "Yiyi / Xiaoshiguang-designated account"
  maintainer_default_pii_access: false

Public Framework Repo Rule:

- This public repo may only store sanitized contracts and architecture.
- Runtime and customer data must not be stored here.

---

## 8｜照片與素材 Gate

Photo_Record:
  file_name: ""
  source: "official_site / facebook / instagram / uploaded_by_owner"
  authorized_by: "Yiyi"
  usage: "hero / room / gallery / internal_app"
  date_added: ""
  note: ""

Forbidden:

- AI-generated room photos as business presentation
- unapproved social media photos
- misleading beautified photos
- third-party stock photos pretending to be the B&B

---

## 9｜LINE 入口 Gate

LINE_Entry:
  phase_1: "Rich Menu / management link opens App URL"
  phase_2: "LIFF optional"
  still_forbidden:
    - auto_send_message
    - auto_confirm_booking
    - auto_payment
    - customer_direct_admin_access

Rule:

- LINE is entry, not authority.
- App must require login.
- Hidden URL alone is not security.

---

## 10｜Backup / Rollback Gate

Required Before Runtime:

- backup strategy
- export procedure
- disable-app procedure
- manual fallback procedure
- rollback procedure
- owner notification rule

---

## 11｜Mode Split

Mom_Mode:
  show:
    - 今日房況
    - 查房況
    - LINE 草稿
    - 暫保留
    - 確認訂房
  hide:
    - 系統設定
    - 資料庫
    - 權限
    - 匯出
    - 技術錯誤
    - API
    - GitHub
    - Supabase

Yiyi_Mode:
  show:
    - Mom_Mode all
    - 取消訂房
    - 封鎖日期
    - 錯誤紀錄
    - 權限批准
    - 維護授權

Maintainer_Mode:
  show:
    - system settings
    - redacted errors
    - schema / deployment status
    - logs without PII
  hide_by_default:
    - guest name
    - phone
    - private booking notes
    - payment data

---

## 12｜v0.7 Definition of Done

- 房務規則待確認清單完成
- 價格規則待確認清單完成
- 暫保留到期規則完成
- 取消／延期規則完成
- 訂金狀態邊界完成
- 維護臨時授權流程完成
- GitHub repo 權限規則完成
- 官方照片匯入規則完成
- LINE 入口 Gate 完成
- 備份與回滾規則完成
- 權限測試清單完成
- 媽媽模式／漪漪模式／維護模式完成
- 所有內容不含客戶個資
- 仍標記 Candidate / Not Runtime

---

## 13｜一句收尾

v0.7 的重點，是把「好用的 GUI App」補成「權限不亂、資料不外流、維護不黑箱、漪漪可掌權、媽媽不增加壓力」的小民宿營運防錯系統。
