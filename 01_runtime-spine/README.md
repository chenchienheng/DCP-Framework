# 01 Runtime-Spine — Legacy Discovery Alias

**Lifecycle:** LEGACY_PATH_ALIAS  
**Current runtime role:** none  
**Normal reader:** no

此路徑保存早期 log/version/freeze/writeback generation 的 lineage，不是現行 Runtime Spine，也不是固定 schema layer。

## Retained primitives
- change/revision/evidence/return 需要可追溯；
- writeback 必須有 Authority、target、effect ceiling 與 reconciliation；
- freeze／version 是 State/Policy，不是永久器官；
- log 是 evidence carrier，不是 Truth 或 Current。

現行 successor：`Stable Existence → Dependency/State → Authority/Gate → Action/Evidence → Return/Reconciliation → Rebuild/Metabolism`。

`Log ≠ Truth | Version ≠ Current | Freeze ≠ Authority | Writeback ≠ Reconciled`

本路徑只供 bounded lineage/audit/re-entry；後續 body 逐一做 unique evidence/caller/rebuild census，再進 unified reclaim review。
