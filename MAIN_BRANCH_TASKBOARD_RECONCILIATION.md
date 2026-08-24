# Taskboard Reconciliation Lineage — predecessor control-surface specimen

**Lifecycle:** METABOLIZED_HISTORICAL_SPECIMEN  
**Current control surface:** false  
**Runtime / Authority:** false

舊版將本檔宣告為 taskboard reality 的 single control surface，並以 AXIS-01～05 吸收 Issues／execution traces。該 Master-Axis／single-taskboard topology 已退休。

## Retained primitives
- Work-item UI state 不足以表示 semantic Current／absorption。
- Issue／PR／branch／task 的歷史 execution trace 可保留 provenance。
- 關閉、合併、開啟狀態必須與 dependency／receiver debt／evidence 分開判斷。
- 不應因 cleanup convenience 刪掉仍承載 unique evidence／failure／lineage 的 work item。

## Current interpretation
Work-item 只是一種 Carrier／metadata surface。Current task state 應由 owning Project/Lane contract、Need、dependency、authority、evidence、Return/Rebuild 判定；不存在單一 repository taskboard sovereignty。

`Issue state ≠ Current`  
`Open forever ≠ lineage preservation requirement`  
`Merged ≠ absorbed`  
`Taskboard entry ≠ authority`

舊 AXIS mapping 與 must-remain-open instructions 留 Git history，不得由本 specimen 重新喚醒。
