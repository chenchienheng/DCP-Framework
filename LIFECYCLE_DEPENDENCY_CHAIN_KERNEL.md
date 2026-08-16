# Lifecycle Dependency Chain Kernel / 生命週期依存鏈核

**Status:** Architecture Candidate  
**Runtime:** false  
**Promotion:** false  
**Repository role:** Public DCP-weighted projection carrier only

## Human zh-TW

這份 Kernel 是目前舊 Master／AXIS／W0／Commander／CloudTop／固定 Tool／固定 Folder Taxonomy 代謝後的最小工作核。它不是新的中央 Truth，也不取代 DCP Native Body。

### 1. Stable Existence before Classification
先問「它是什麼存在」，再問它目前被什麼載體承載；不得以 Folder、Repo、Cloud、Extension 或檔案格式反向定義 ontology。

同一 Stable Existence 可以同時或先後投影為 Markdown、JSON、YAML、PDF、試算表、Database、SQL、CAD、BIM/IFC、3D、Image、Audio、Video、Notebook、Source Code、Binary、Script、Archive、API resource、Issue／PR／Branch、Drive object、SaaS record、Local runtime 或 Model output。

因此固定：

`Carrier ≠ Identity`  
`Extension ≠ Taxonomy`  
`Folder ≠ Ontology`  
`Representation ≠ Truth`  
`Carrier Change ≠ Identity Change`

真正要判斷的是：

`Stable Existence → Function/Capability → Dependency/Constraint → State → Authority → Evidence → Effect/Return → Reconciliation → Rebuild/Metabolism`

### 2. Dispatch Views are optional, not architecture organs
Domain／Authority／State／Circle／Pole／Cloud 只在 material 時作為 bounded dispatch/view axes；不是六層資料夾、六個永久分類，也沒有固定先後順序。

- Domain：原生世界／Owner／Source domain。
- Authority：誰能讀、判、寫、批准、釋放、ACK。
- State：Candidate／Current／Pending／Return／Historical／Quarantine／Released 等生命狀態。
- Circle：本次 Project／Window／Review／Public／Inner-Ring 的作用邊界。
- Pole：Ideas／DCP／GLModel 哪個作用核需要 bounded projection。
- Cloud：Drive／GitHub／DB／SaaS／Local／Model-Agent 等 carrier view。

若一個 axis 對 affected cone 沒有 material effect，就不應為了分類完整性強迫填滿。

### 3. 依存生命鏈
生命來自 governed relations 與 transitions，而不是檔案樹：

`Source → Bind → Dependency → Gate → Action → Evidence → Return → Reconciliation → Metabolism → Re-entry/Rebuild`

其中：
- Boundary before Answer／Action。
- First Real Failure Gate before architecture escalation。
- Local PASS/FAIL 只影響 affected dependency cone。
- Return Written ≠ Receiver Reconciled。
- Historical Searchable ≠ Current Eligible。
- 新 Delta 必須檢查 predecessor 是否失效、已吸收、重複或仍有獨有 evidence。

### 4. Source / Projection / Representation
Native Source 留在合法 Domain。Projection、View、Dashboard、Report、Image、Video、Model Output、Spreadsheet、Database snapshot、CAD/BIM export、Repo artifact 都只是 representation/carrier。

`Projection ≠ Source`  
`Latest ≠ Current`  
`Capability ≠ Authority`

### 5. Action Effect Class
每次作用至少判：

- READ / OBSERVE
- DERIVE / DRAFT
- BOUNDED_MUTATION
- HIGH_RISK_MUTATION
- RELEASE / PUBLISH

Effect class 必須受 Domain、Authority、State、Risk、Reversibility、Evidence、Return Target 約束；工具能力不能自行擴張 effect ceiling。

### 6. Return / Reconciliation
Producer 只負責寫 Return；Receiver 自己決定：

`NO_DELTA | ABSORB | HOLD | TO_VERIFY | REJECT | REBUILD_REQUIRED`

Shared Belt 只承載 Pointer／Receipt／Receiver State／Conflict／Re-entry／Rebuild pointer；不複製 Native Body、不形成第四極。

### 7. Metabolism
代謝鏈固定為：

`Old Body → Primitive Extraction → Successor Coverage → Current Eligibility Removal → Reader/Routing/Navigation/Wake/Rebuild Withdrawal → Lineage Retention → Explicit Re-entry only`

Archive、Rename、Move、Historical prefix 都只是 containment，不等於 metabolism complete。

#### Work-item lifecycle
PR／Issue／Branch／Return／Candidate／Pending／ACK／TO_VERIFY 都只是不同 work-item carrier/state，不是永久治理器官。

- OPEN/ACTIVE 必須仍有 Domain／Authority／Affected Scope／Evidence／Next Gate／Return Target。
- MERGED/CLOSED 只代表 carrier event；`Merged ≠ Current ≠ Absorbed ≠ Approved`。
- CLOSED_UNMERGED 預設不具 Current eligibility；有獨有 primitive/evidence 才保留 re-entry value。
- SUPERSEDED 後，舊 merge order、READY/HOLD、review verdict、tool/agent assumptions 失去 Current effect。
- provenance 優先留在原生 carrier history；不另建立活文件複製歷史。

### 8. Classification Metabolism Rule
當分類本身開始大於內容，或同一 existence 因不同副檔名被拆成多個永久家族，視為 `TAXONOMY_OVERGROWTH`。

處理順序：

`Existence Rebind → Alias Merge → Function/State/Authority Re-evaluation → Carrier Metadata Demotion → Reader Surface Compaction → Historical Label Retention only if useful`

不因 `.md/.json/.yml/.pdf/.xlsx/.dxf/.dwg/.ifc/.glb/...` 不同而建立平行真值；也不因同一檔案可被多工具讀取而複製出多份 Current Body。

### 9. Error Containment
錯誤依 WORLD／MODEL／REPRESENTATION／CARRIER／AUTHORITY／EVIDENCE／READER 類型定位，只 invalidate affected scope。錯誤可發現、可界定、可局部失效、可回流修正、可重建；不宣稱零錯誤或零幻覺。

## Professional English

The kernel is existence-first and carrier-neutral. Stable identity, function/capability, dependency/constraints, lifecycle state, authority, evidence, effects/returns, reconciliation and rebuild/metabolism are primary. File extensions, folders, repositories, clouds and representations are secondary carrier metadata. Domain/Authority/State/Circle/Pole/Cloud are optional dispatch views used only when material; they are not mandatory ontology layers. The same stable existence may be represented across documents, databases, spreadsheets, CAD/BIM/3D, media, code, binaries, APIs, issues/PRs/branches or model outputs without creating parallel truths.

## Canonical Machine State

```yaml
kernel: LIFECYCLE_DEPENDENCY_CHAIN
status: ARCHITECTURE_CANDIDATE
runtime: false
promotion: false
primary_semantics:
  - stable_existence
  - function_capability
  - dependency_constraint
  - lifecycle_state
  - authority
  - evidence
  - effect_return
  - reconciliation
  - rebuild_metabolism
carrier_semantics:
  extension_is_taxonomy: false
  folder_is_ontology: false
  repository_is_authority: false
  carrier_change_changes_identity: false
  same_existence_multi_carrier: true
dispatch_views:
  axes: [domain, authority, state, circle, pole, cloud]
  mandatory: false
  fixed_order: false
  use_only_when_material: true
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
metabolism:
  withdraw_surfaces: [reader, routing, navigation, wake, rebuild]
  archive_or_rename_only_is_complete: false
  taxonomy_overgrowth_state: TAXONOMY_OVERGROWTH
invariants:
  projection_is_not_source: true
  representation_is_not_truth: true
  capability_is_not_authority: true
  latest_is_not_current: true
  return_written_is_not_reconciled: true
  historical_searchable_is_not_current: true
  local_pass_is_not_global_pass: true
  local_fail_is_not_whole_world_fail: true
  extension_is_not_taxonomy: true
  folder_is_not_ontology: true
  carrier_is_not_identity: true
```

## Successor surface

Normal readers should start from:
1. `README.md`
2. `CURRENT-SURFACE-MANIFEST.json`
3. `LIFECYCLE_DEPENDENCY_CHAIN_KERNEL.md`
4. `PUBLIC-SURFACE-POLICY.md`
5. `STATUS.md`

Legacy files are lineage/failure/re-entry surfaces only. Additional formats or carrier types may join the library without creating new ontology families solely because their file type differs.
