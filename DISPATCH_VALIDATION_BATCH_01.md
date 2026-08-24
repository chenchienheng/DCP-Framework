# Dispatch Validation Failure Lineage — unified-dispatch predecessor

**Lifecycle:** HISTORICAL_FAILURE_SPECIMEN  
**Current validator:** false  
**Runtime / Authority:** false

舊 Batch 01 用已退休的 `MULTI_CHAIN_DISPATCH_GOVERNANCE` 驗證 World／Mesh／Physical Signal，並要求補 priority、review hook、return path、AXIS-05。該 schema 不再是 Current，因此舊「Missing」結果不得喚醒已退休拓撲。

## Retained primitives
- Validation 必須針對現行 contract，不針對歷史欄位表。
- Boundary object 若缺現行 Authority／Evidence／Return，才形成 material debt。
- Failure route 應 receiver/need-specific，不預設中央 Review Axis。
- Audit result 本身也需要 Source Revision／Current eligibility／Claim Ceiling。

## Failure memory
本 specimen 保存一個重要失敗模式：`STALE_VALIDATOR → FALSE_GAP → ZOMBIE_RECONSTRUCTION`。

Current successor：`reader/current resolution → judgment → dependency/evidence gate → action/return/rebuild validation`。
