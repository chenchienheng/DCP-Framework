# Dispatch Validation Failure Lineage — World-Axis predecessor

**Lifecycle:** HISTORICAL_FAILURE_SPECIMEN  
**Current validator:** false  
**Runtime / Authority:** false

舊 audit 以 `MULTI_CHAIN_DISPATCH_GOVERNANCE` 為標準，要求 `WORLD_CHAIN_MASTER_AXIS` 補 entry／priority／review／return／AXIS-05／register fields。兩個被依賴的控制面皆已退休，因此本 report 的「minimal correction」本身已成為 zombie-reconstruction failure example。

## Retained lesson
- Validator／audit schema 必須先確認自己的 Current eligibility 與 successor relation。
- Missing field 只有在現行 contract 仍要求時才是 defect。
- 不得因 historical validator 命中缺口，就重建已退休 controller／axis／registry。
- Validation output 必須保留 claim ceiling：`historical mismatch ≠ current defect`。

## Current replacement
依 Need 驗證現行 `Identity / Dependency / Authority / Evidence / Action Effect / Return / Rebuild` contract；若 predecessor validator 已失權，結果轉為 lineage/failure evidence，不產生 remediation action。

舊欄位表與補回 World Axis 的指令留 Git history。
