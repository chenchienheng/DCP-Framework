# Metabolized Primitives / 代謝後可重用原語

**Status:** Architecture Candidate  
**Runtime:** false  
**Promotion:** false

這份文件不是把舊架構換名字保存，而是只留下跨世代仍有行為價值的 Primitive。舊 W0/Wx、AXIS、Legion、固定 Agent 名稱、merge-to-main=Active、舊 Master/Registry 自我宣告均不繼承。

## Human zh-TW

### 1. Lifecycle Primitive
一個 Artifact 的生命週期必須可描述為：來源／候選／驗證／有效狀態／回流／調和／歷史／隔離／重入／重建。任何單一事件（例如 merge、搬檔、改名、被搜尋到）都不能自行建立 Current。

### 2. Stable Identity + Lineage
Artifact 必須能在 Window、Repo、Carrier、名稱、表徵改變後仍追溯同一 Stable Identity。Carrier path 是定位資訊，不是 Identity。

### 3. Hardening Gate
跨 Window／Tool／Carrier 移交時，至少驗證：語義完整性、必要欄位、Authority、Evidence、Return Route、Claim Ceiling。Gate 只凍結 affected branch，不默認停整個世界。

### 4. Receiver-Owned Return
Return Written 不等於 Receiver Absorbed。Receiver 自己判 Material Delta／NO_DELTA／HOLD／TO_VERIFY，Producer 不代填 ACK。

### 5. Carrier-Neutral Role Binding
Capture、classify、translate、verify、writeback、reconcile 等功能可由不同 Tool／Model／Window／SaaS 承擔；工具名稱不是架構不變核。先判 Domain → Authority → State → Circle → Pole → Cloud，再綁定當下可用 Carrier。

### 6. Metabolism over Relocation
代謝不是把舊物搬去 archive、加 Historical 前綴或建立更多 index。有效代謝必須完成：抽取可重用 Primitive → 建立 Successor → 移除舊 Current eligibility → 壓縮 Reader exposure → 保留必要 lineage → 定義 re-entry gate。

### 7. Localized Failure
錯誤與失效只應傳播到 affected dependency cone。Local FAIL ≠ Whole-world FAIL；Local PASS ≠ Global Closure。

### 8. Public / Release Separation
Public placement ≠ Public-approved。公開 Carrier 仍必須遵守 Rights／Privacy／Purpose／Evidence／Retention／Release Authority。

## Professional English

Reusable primitives are retained only where they remain behaviorally valid across architecture generations: lifecycle typing, stable identity and lineage, bounded hardening gates, receiver-owned return, carrier-neutral role binding, metabolism with successor/re-entry, affected-scope failure localization, and explicit release control. Legacy window, axis, agent, runtime and master-label ontologies are not inherited.

## Canonical Machine State

```yaml
artifact: METABOLIZED_PRIMITIVES
status: ARCHITECTURE_CANDIDATE
runtime: false
promotion: false
retained:
  - lifecycle_typing
  - stable_identity_lineage
  - bounded_hardening_gate
  - receiver_owned_return
  - carrier_neutral_role_binding
  - successor_based_metabolism
  - affected_scope_failure_localization
  - explicit_release_control
retired:
  - merge_to_main_equals_current
  - fixed_W0_Wx_ontology
  - fixed_AXIS_authority
  - fixed_agent_identity
  - legion_as_current_architecture
  - old_master_label_as_authority
  - old_register_as_current_truth
```

## Successor relations

- Current repository interpretation → `CURRENT-SURFACE-MANIFEST.json`
- Six-dimensional projection → `SIX_DIMENSION_REPOSITORY_PROJECTION.md`
- Historical disposition → `LEGACY-DESIGN-DISPOSITION.json`
- Historical discovery only → `REPOSITORY_CORPUS_INDEX.md`
