# Temporal Context and Lineage — retained DCP primitive

**Lifecycle:** RETAINED_PRIMITIVE / REINTERPRETED  
**Current eligibility as sovereign time layer:** false

時間不是獨立 Authority，也不是背景雜訊；它是 State／Lineage／Evidence／Re-entry 判讀的重要 context。

## Invariants
- Event order、revision window、freshness、expiry、retention、return timing 都可能改變 State/Gate 判定。
- Latest ≠ Current；較新時間戳不自動取得 Authority。
- Historical searchable ≠ wake eligible；re-entry 仍需 material need、evidence、authority、successor compatibility。
- 同一 Stable Identity 可跨時間保留 lineage，但不同 revision/state 不得無條件視為同一 Current。
- Tool clock、file modified time、message time、runtime time 都只是 temporal evidence source，需判 provenance/fidelity。

## Successor binding
`Stable Identity → Temporal Context/Revision → State/Freshness → Evidence/Authority Gate → Action/Return → Reconciliation/Re-entry`

舊「時間主權層」語義退休；保留 temporal context primitive。