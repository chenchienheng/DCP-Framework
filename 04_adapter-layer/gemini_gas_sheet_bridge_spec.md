# Gemini → Google Sheet Bridge Spec — Historical Implementation Stub

**Lifecycle:** HISTORICAL_IMPLEMENTATION_STUB  
**Current eligibility:** false  
**Executable authority:** none

舊版包含 Gemini→Google Sheets／Apps Script 的具體工程草稿與寫入邏輯。該 vendor-specific code 不再作 CoreTri/DCP architecture，也不得因 repo 公開而被視為可執行部署指令。

## 保留 Primitive
- External import 預設 report/read-only；mutation 需要 explicit authority。
- Non-destructive update、stable identity matching、evidence strength、provenance、error return 是可重用 adapter 方法。
- Private/company-sensitive data 需先過 Rights／Privacy／Purpose Gate。
- Adapter success ≠ Native absorption／Current／Release。

現行 successor：Carrier-neutral adapter contract + 六維 Cloud binding + receiver-owned Return/Reconciliation。

完整 GAS code 與 Gemini/Sheet 欄位 schema 保留於 Git history；若未來重建 Google adapter，必須重新驗證 API、權限、資料 schema 與安全條件。
