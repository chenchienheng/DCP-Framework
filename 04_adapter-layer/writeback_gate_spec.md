# External Mutation Gate — Historical Lineage Specimen

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as W0/ChatGPT/GitHub write gate:** false  
**Executable authority:** none  
**Reclaim disposition:** CANDIDATE_AFTER_POINTER_AND_CALLER_CHECK

舊版將 W0、ChatGPT 與 GitHub 固定成 external writeback control path；該 actor/carrier topology 已退休。

## Retained primitives
- External mutation requires Stable Identity、Source、Target、Authority、Rights、Purpose、Affected Scope、Revision/Fidelity、Evidence、Responsibility、Recovery 與 Return。
- Carrier／Agent／platform name 不產生 write authority。
- Revision-sensitive mutation 必須綁 expected revision；target existence 不得猜測。
- Gate PASS 只表示 bounded mutation candidate，可否實際執行仍由合法 execution surface 與 authority 決定。
- Successful write ≠ Native absorption／Current／Approval／Release。
- Gate failure 應保持 read-only/HOLD，不得 silent reroute。

## Executable successor
- `dcp_kernel/write_intent.py`
- `contracts/write-intent.schema.json`
- `tests/test_write_intent.py`

完整 W0／ChatGPT／GitHub predecessor 保留於 Git history；正常 Reader 不需讀本 specimen。
