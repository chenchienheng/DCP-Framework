# External Mutation Packet — Historical Lineage Specimen

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as active W0 packet contract:** false  
**Executable authority:** none  
**Reclaim disposition:** CANDIDATE_AFTER_POINTER_AND_CALLER_CHECK

舊版固定 `Department / Agent Block / Node ID / Window / Platform Writer / GitHub target` 為 universal writeback packet，並標為 active。此 actor/window/repository topology 已退休。

## Retained primitives
一個 mutation intent 必須保留可重建的最小資訊：
- Stable Life / Source Identity
- Target Carrier / Mutation Kind
- Authority / Rights / Purpose
- Affected Scope
- Expected Revision when mutation is revision-sensitive
- Fidelity / Evidence plan
- Responsibility Owner
- Rollback / Recovery
- Return Target

這些欄位描述 effect 與責任，不建立固定 Department／Agent／Window／Platform Writer ontology。

## Executable successor
- `dcp_kernel/write_intent.py`
- `contracts/write-intent.schema.json`
- `tests/test_write_intent.py`

成功 mutation 後仍須產生 Evidence／Return／Receiver reconciliation；Write success ≠ Absorption。

完整 predecessor packet example 留 Git history；正常 Reader 不需讀本 specimen。
