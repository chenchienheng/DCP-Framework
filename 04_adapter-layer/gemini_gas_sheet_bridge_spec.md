# External Table Mutation Adapter Lineage Specimen

**Lifecycle:** HISTORICAL_IMPLEMENTATION_STUB  
**Current eligibility:** false  
**Executable authority:** none  
**Reclaim disposition:** HOLD_UNTIL_UNIQUE_IMPLEMENTATION_EVIDENCE_EXTRACTED

舊版 Gemini→Google Sheets／Apps Script 工程草稿不再作 CoreTri/DCP architecture，也不因 repo 公開而成為可執行部署指令。Vendor code 只保留 lineage/evidence value。

## Retained primitives
- External import 預設 read/report；mutation 需要 explicit authority。
- Non-destructive update、stable identity matching、evidence strength、provenance、rollback/error return 可泛化。
- Private/company data 需 Rights／Privacy／Purpose Gate。
- Adapter success ≠ Native absorption／Current／Release。
- API/schema/version 必須在實際接入時重新驗證。

## Successor binding
`Stable Existence → Mutation Intent → Source/Authority/Rights → Capability Binding → Schema/Fidelity Check → Bounded Mutation → Evidence/Return/Reconciliation`

舊 GAS code 與欄位 schema 留 Git history；若未來重建任一 table adapter，重新驗證當下 API、權限、資料 schema、安全與 rollback 條件。
