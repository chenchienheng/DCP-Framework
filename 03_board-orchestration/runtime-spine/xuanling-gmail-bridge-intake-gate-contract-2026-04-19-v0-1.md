# External Intake Gate Lineage Contract — Gmail predecessor specimen

**Lifecycle:** HISTORICAL_IMPLEMENTATION_SPECIMEN / PRIMITIVES_RETAINED  
**Current eligibility as Gmail mother-gate:** false  
**Executable authority:** none

舊版以 Gmail 為首個 reusable mother-gate，並綁定 `return_to_00`、固定 reserve path、cross-window route 與當時的 inbox taxonomy。這些 vendor/path/topology assumptions 已退休。

## Retained intake primitives
- External message/event/file/API payload 先是 Source/Signal Candidate，不因進入介面就成 Truth／Current／Authority。
- Intake 先做 source/context identification，再做 purpose/scope、rights/privacy/risk、contamination/evidence screen，最後才決定 action/hold/no-action/return。
- Unknown、suspicious、noise-heavy、route-breaking input 可局部 HOLD；不得直接 promotion。
- Low-priority/no-action 與 contamination/high-risk 必須分離。
- Actionable intake 需要 stable target、authority、evidence role、return route。
- Adapter/API/quota/label/archive/write assumptions 屬 Carrier-specific profile，接入時重新驗證。

## Carrier-neutral successor
`External Source/Signal → Identity/Context → Purpose/Rights/Risk Gate → Materiality → Required Effect → Carrier-specific Adapter → Evidence/Result → Receiver Return/Reconciliation`

可套用 Gmail、Calendar、Contacts、Forms、chat/message、webhook、API、file drop、sensor/event stream 等；但任何 Carrier 都不因此成為永久入口器官。

## Retired predecessor assumptions
- Gmail = first/mother gate
- `return_to_00 = true`
- fixed `03_board-orchestration/routing-logs` writeback
- fixed `05_XLEN_Reserve_Unenabled/02_Gmail_Bridge` reserve path
- fixed control-plane / consolidation routing
- old intake category names as mandatory ontology

完整 predecessor contract 與當時 routing schema 留在 Git history；若未來重建 Gmail adapter，必須重新驗證 provider API、OAuth/rights、privacy、retention、labels、mutation authority 與 failure return。

Runtime=false | Promotion=false | Closeout=false