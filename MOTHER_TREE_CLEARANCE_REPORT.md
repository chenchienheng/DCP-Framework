# MotherTree Clearance Report — Historical Decision Stub

**Lifecycle:** HISTORICAL_DECISION_STUB  
**Current eligibility:** false

舊報告記錄一輪 PR/merge/hygiene 決策，包含 MotherTree、tri-coupled baseline、固定 merge order 與當時 PR 狀態。這些內容屬歷史決策證據，不得再當 Current governance 或現行 queue。

## 保留 Primitive
- PR hygiene 與 semantic review 應分開判斷。
- Mergeable ≠ Approved；Content-wise OK ≠ clean diff。
- 大量 unrelated deletion 應觸發 rebase/cleanup，而非直接吸收。
- Public/private boundary、Pending≠Fact、explicit write authorization、return trace 仍是有效檢查點。

現行 successor：Boundary-first review、Affected Scope、Release/Admission Gate、Receiver-owned Return。

完整舊 PR 編號、merge order 與 MotherTree decision checklist 保留於 Git history，只供 audit／lineage。
