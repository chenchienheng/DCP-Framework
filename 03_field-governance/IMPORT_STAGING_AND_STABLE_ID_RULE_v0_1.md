# Import Eligibility / Stable Identity Binding — Lineage Specimen

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as fixed staging schema:** false

## Retained primitives
- Imported／user-collected／tool-generated material first enters eligibility/lifecycle review; ingestion success does not support Current claims or governed action by itself.
- Proposed ID ≠ Stable Identity.
- Stable Identity requires lineage, match/create rule, authority/evidence and duplicate/conflict handling.
- Intake metadata should preserve Source Origin、Submitter/Authority、Time/Revision、Evidence State、Rights/Privacy、Representation/Carrier、Return Path。
- Candidate／HOLD／Reject／Historical need lifecycle state; do not silently delete or promote.
- Format conversion, upload, sync or parsing does not constitute absorption.

舊 Import_Staging table、固定 ID families、QIN/BASE fields 與 QA_Gate/Change_Log schema 已退休。

## Successor binding
`External/Internal Material → Source Eligibility → Stable Identity Match/Create → Rights/Evidence/State → Materiality → Receiver Disposition → Return/Reconciliation/Rebuild`

Carrier-specific staging tables may be generated as projections when needed; they do not become Core ontology.

完整 predecessor 留 Git history。
