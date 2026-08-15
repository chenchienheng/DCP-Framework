# Import Staging and Stable ID Rule v0.1 — Metabolized Primitive Stub

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as fixed BASE schema:** false

## 保留 Primitive
- Imported／user-collected／tool-generated material enters an eligibility/review state before it can support Current claims or governed action.
- Proposed ID ≠ Confirmed Stable Identity.
- Stable Identity requires lineage, matching/creation rule, authority/evidence and duplicate/conflict handling.
- Intake metadata must preserve Source Origin、Submitter/Authority、Time/Revision、Evidence State、Rights/Privacy、Return Path。
- Staging／Candidate may be retained without being Current; rejected/held items need lifecycle state rather than silent deletion.

舊 Import_Staging table、固定 ID families、QIN/BASE output fields 與 QA_Gate/Change_Log schema 已退休。

現行 successor：Source Eligibility + Stable Identity Binding + Lifecycle State + Historical/Re-entry + six-dimensional dispatch。

完整舊 schema 保留於 Git history。
