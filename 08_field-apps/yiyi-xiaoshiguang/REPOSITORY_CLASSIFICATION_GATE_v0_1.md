# Yiyi / Xiaoshiguang｜Repository Classification Gate v0.1

Status: Candidate / Public-safe / No Customer Data / No Runtime / No External Writeback

## 0｜一句核心

小蒔光房況防錯 App 可以先在 Vitas 既有數位生態中開闢「去敏架構空間」，但正式 runtime、客戶資料、密鑰與營運主權必須與 public framework 倉分離，回到漪漪／小蒔光可授權與可撤回的邊界內。

---

## 1｜三倉分類

### A｜DCP-XLEN_XAFD_XLQY

Role: 翾靈／DCP 主結構與架構監督倉  
Visibility: Public  
Use For:
- 去敏架構契約
- 權限模型
- Gate 定義
- 回流格式
- W2 / W7 / W1 交接規則
- 小蒔光 App 的 public-safe fieldspace

Do Not Use For:
- 客戶資料
- 訂房資料
- 密鑰
- `.env`
- Supabase service key
- LINE Developers 憑證
- 未授權社群素材
- production runtime

### B｜XLQY_Qinyi_Flow_CoreTri

Role: 芹衣 Flow / CoreTri 監督與回流倉  
Expected Use:
- 芹衣維護規則
- 去敏回流
- 任務分類
- Return Packet
- Qinyi review gate

Current Note:
- 目前連接器對此倉寫入回傳 403，可能需要確認 GitHub App 是否已安裝或先建立初始 commit。
- 未確認前，不把它當可施工倉。

### C｜DCP-Framework

Role: 既有舊主倉／歷史承載  
Current Use:
- 已建立過 `feature/yiyi-xiaoshiguang-fieldspace-v0-7` 分支作初步 fieldspace

Forward Rule:
- 不再擴張小蒔光內容到舊主倉，以免三倉重複污染。
- 後續以 `DCP-XLEN_XAFD_XLQY` 為主結構倉。

---

## 2｜正式 App 倉原則

小蒔光正式 App runtime 不應放在 public framework 倉內。

Future Private Runtime Repo:
  suggested_name: "xiaoshiguang-booking-helper"
  visibility: "private"
  owner: "Yiyi / Xiaoshiguang-designated account"
  content:
    - app source code
    - deployment config without secrets
    - Supabase migration files
    - tests
    - public-safe docs
  forbidden:
    - customer data
    - API keys
    - service keys
    - raw LINE private messages
    - payment details

---

## 3｜污染防線

Hard_Boundaries:
  no_customer_data_in_public_repo: true
  no_credentials_in_repo: true
  no_runtime_secrets: true
  no_unapproved_social_import: true
  no_ai_generated_business_room_photos: true
  no_maintainer_default_pii_access: true

---

## 4｜Commit / PR Gate

Any PR touching this fieldspace must verify:

- No PII
- No secrets
- No `.env`
- No real booking exports
- No unapproved Facebook / Instagram content
- No automatic LINE sending
- No owner override by Vitas / Qinyi / maintainer
- Candidate / BuildReady / Runtime status clearly marked

---

## 5｜一句收尾

這個 fieldspace 的價值，是讓翾靈與芹衣能看見、監督、維護小蒔光 App 的架構邏輯；但它不能吞掉小蒔光的營運主權，也不能把 public framework 倉變成正式客戶資料倉。
