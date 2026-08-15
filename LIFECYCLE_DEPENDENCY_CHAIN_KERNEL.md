# Lifecycle Dependency Chain Kernel / 生命週期依存鏈核

**Status:** Architecture Candidate  
**Runtime:** false  
**Promotion:** false  
**Repository role:** Public DCP-weighted projection carrier only

## Human zh-TW

這份 Kernel 是目前舊 Master／AXIS／W0／Commander／CloudTop／固定 Tool 架構代謝後的最小工作核。它不是新的中央 Truth，也不取代 DCP Native Body。

### 1. 六維定位
任何存在先以六個正交座標判位：

**域 Domain → 權 Authority → 態 State → 圈 Circle → 極 Pole → 雲 Cloud**

- 域：原生世界／Owner 在哪裡。
- 權：誰能讀、判、寫、批准、釋放、ACK。
- 態：Candidate／Current／Pending／Return／Historical／Quarantine／Released 等生命狀態。
- 圈：本次 Project／Window／Review／Public／Inner-Ring 的作用邊界。
- 極：Ideas／DCP／GLModel 哪個作用核需要 bounded projection。
- 雲：Drive／GitHub／DB／SaaS／Local／Model-Agent 等 Carrier。

Carrier、Repo、Folder、Window、Tool、Agent 不因位置或名稱取得 Identity／Authority。

### 2. 依存生命鏈
座標本身不等於生命。生命來自 governed relations 與 transitions：

`Source → Bind → Dependency → Gate → Action → Evidence → Return → Reconciliation → Metabolism → Re-entry/Rebuild`

其中：
- Boundary before Answer／Action。
- First Real Failure Gate before architecture escalation。
- Local PASS/FAIL 只影響 affected dependency cone。
- Return Written ≠ Receiver Reconciled。
- Historical Searchable ≠ Current Eligible。

### 3. Source / Projection / Representation
Native Source 留在合法 Domain。Projection、View、Dashboard、Report、Image、Video、Repo、Whitepaper、Model Output 都只是 representation/carrier。

`Projection ≠ Source`  
`Representation ≠ Truth`  
`Latest ≠ Current`  
`Capability ≠ Authority`

### 4. Action Effect Class
每次作用至少判：

- READ / OBSERVE
- DERIVE / DRAFT
- BOUNDED_MUTATION
- HIGH_RISK_MUTATION
- RELEASE / PUBLISH

Effect class 必須受 Domain、Authority、State、Risk、Reversibility、Evidence、Return Target 約束；工具能力不能自行擴張 effect ceiling。

### 5. Return / Reconciliation
Producer 只負責寫 Return；Receiver 自己決定：

`NO_DELTA | ABSORB | HOLD | TO_VERIFY | REJECT | REBUILD_REQUIRED`

Shared Belt 只承載 Pointer／Receipt／Receiver State／Conflict／Re-entry／Rebuild pointer；不複製 Native Body、不形成第四極。

### 6. Metabolism
代謝鏈固定為：

`Old Body → Primitive Extraction → Successor Coverage → Current Eligibility Removal → Reader Exposure Reduction → Lineage Retention → Explicit Re-entry only`

搬到 Archive、改檔名、加 Historical 前綴都不算代謝完成。

### 7. Error Containment
錯誤依 WORLD／MODEL／REPRESENTATION／CARRIER／AUTHORITY／EVIDENCE／READER 類型定位，只 invalidate affected scope。錯誤可發現、可界定、可局部失效、可回流修正、可重建；不宣稱零錯誤或零幻覺。

## Professional English

The kernel describes a carrier-neutral lifecycle dependency system using six orthogonal coordinates—Domain, Authority, State, Circle, Pole, and Cloud—plus governed relations for source binding, dependency, gating, action effects, evidence, return, reconciliation, metabolism, re-entry and rebuild. It replaces fixed axis/window/tool hierarchies with bounded, receiver-owned, affected-scope semantics. Repository presence, recency and platform capability do not establish identity, authority or current eligibility.

## Canonical Machine State

```yaml
kernel: LIFECYCLE_DEPENDENCY_CHAIN
status: ARCHITECTURE_CANDIDATE
runtime: false
promotion: false
coordinates:
  order: [domain, authority, state, circle, pole, cloud]
relations:
  - source_bind
  - dependency
  - gate
  - action_effect
  - evidence
  - return
  - reconciliation
  - metabolism
  - reentry
  - rebuild
effect_classes:
  - READ_OBSERVE
  - DERIVE_DRAFT
  - BOUNDED_MUTATION
  - HIGH_RISK_MUTATION
  - RELEASE_PUBLISH
receiver_states:
  - NO_DELTA
  - ABSORB
  - HOLD
  - TO_VERIFY
  - REJECT
  - REBUILD_REQUIRED
invariants:
  projection_is_not_source: true
  representation_is_not_truth: true
  capability_is_not_authority: true
  latest_is_not_current: true
  return_written_is_not_reconciled: true
  historical_searchable_is_not_current: true
  local_pass_is_not_global_pass: true
  local_fail_is_not_whole_world_fail: true
  repo_is_not_native_authority: true
```

## Successor surface

Normal readers should start from:
1. `README.md`
2. `CURRENT-SURFACE-MANIFEST.json`
3. `LIFECYCLE_DEPENDENCY_CHAIN_KERNEL.md`
4. `SIX_DIMENSION_REPOSITORY_PROJECTION.md`
5. `PUBLIC-SURFACE-POLICY.md`

Legacy files are lineage/failure/re-entry surfaces only.
