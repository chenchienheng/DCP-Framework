# Xiaoshiguang Fieldspace Index v0.1

Status: Candidate / Public-safe / No Customer Data / No Runtime

## 0｜一句核心

此目錄是小蒔光房況防錯 App 在翾靈／芹衣可見範圍內的「去敏 fieldspace」：只放架構、權限、Gate、施工與回流，不放客戶資料、密鑰或正式 runtime。

## 1｜目錄角色

This fieldspace is for:

- App architecture contracts
- GUI flow definitions
- authority boundaries
- privacy gates
- repository classification
- maintenance handoff
- sanitized learning return
- Codex / Hazumi construction preparation

This fieldspace is not for:

- production deployment
- customer database
- private bookings
- LINE private messages
- payment records
- API keys
- vendor credentials

## 2｜Key Documents

- `REPOSITORY_CLASSIFICATION_GATE_v0_1.md`  
  三倉分類與污染防線。

- `XIAOSHIGUANG_V0_7_AUTHORITY_LOCK_CONTRACT.md`  
  v0.7 權限、營運規則、Go-live Gate 補強契約。

- `XIAOSHIGUANG_CODEX_HANDOFF_v0_1.md`  
  給 Codex／和澄施工窗口的去敏交接規則。

## 3｜Authority

Highest Authority:
- Yiyi / Xiaoshiguang actual owner-side authority

Support Roles:
- Vitas: architecture and maintenance support
- Qinyi: sanitation, handoff, review, return calibration
- Codex / Hazumi: construction only after assignment

Rule:
- Support role is not owner authority.
- Maintainer permission is not customer-data permission.
- Public-safe is not public-approved.

## 4｜Runtime Boundary

Runtime must be separated into a future private repo or private deployment space before real use.

Runtime cannot live here if it includes:
- real customer PII
- booking exports
- `.env`
- database credentials
- LINE API secrets

## 5｜Current Status

- v0.6 App artifact exists outside repo as backend authority-safe candidate.
- v0.7 governance patch is being integrated into this fieldspace.
- No production deployment has been performed.
- No customer data has been written here.
