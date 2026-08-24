# Repository Status / 倉庫狀態

**Repository class:** Public DCP-weighted CoreTri projection carrier  
**Operational status:** Non-production  
**Runtime evidence:** Not established  
**Promotion / Canon / Authority elevation:** None

## 1｜定位

本倉是 DCP 的公開投影載體，不是 DCP Native Body、Native Source Root、Runtime、Canon 或 Authority Root。

固定：

`Carrier ≠ Identity`  
`Capability ≠ Authority`  
`Recent ≠ Current`  
`Public-safe ≠ Public-approved`  
`BuildReady ≠ Runtime`

正常 Reader：

`README → CURRENT-SURFACE-MANIFEST → LIFECYCLE_DEPENDENCY_CHAIN_KERNEL → PUBLIC-SURFACE-POLICY → STATUS`

舊 Master／MotherTree／W0／AXIS／固定 Agent／Scheduler／Folder topology 只在 conflict、audit、unique evidence/failure 或 explicit re-entry 時 bounded read。

## 2｜單一生命鏈

DCP 現行工作不再按舊資料夾或固定角色組織，而按同一條生命鏈：

`Existence → Relation → Event → Judgment → Capability Binding → Action → Evidence → Return → Receiver Rebuild → New State → Retest`

其中：

- 同一存在跨圖、文、表、程式、3D、API 或其他 Representation 必須能 back-map；否則 `IDENTITY_RESOLUTION_GAP`。
- Relation 不能只剩 A→B；缺 direction/state/time/evidence/effect 或必要的 authority/cost/risk/reversibility/return path 時，標 `STATIC_RELATION_ONLY`。
- Event 先判 materiality；Non-material 不喚醒全體。
- Judgment 先於工具；模型、Agent、人、平台只依 Need 綁定能力。
- Action 只在合法 Scope／Authority／Risk／Reversibility／Evidence 內形成 Candidate effect；Gate PASS 不授權執行。
- Return 只有在 Receiver Actual Read → Native Disposition → Reconcile → Rebuild → Behavior/World Delta → Retest 後，才有成熟度證據。

## 3｜主要 Gate

### Reception Gateway

外部 Request 先做 Source／Scope／Rights／Materiality／Affected Receiver 判斷。一般 bounded request 可直接 route；只有 irreversible、sensitive、authority change 或真正 Owner Decision 才 escalation。

`Owner ≠ Default API Gateway`

### Cross-pole Feedback

其他極只讀 affected slice。真反例必須修 affected assumption；Representation drift 必須 HOLD；理解不搬走 Authority；單次 PASS 不算成熟。

### Public Encounter

第一次外部相遇只允許 lawful、bounded、revocable projection：

`Native Capability → Lawful Projection → External Encounter → External Evidence → Receiver Return → Native Rebuild`

`Capability Demo ≠ Architecture Validation`  
`External Adoption ≠ Authority Transfer`  
`PUBLIC_PROJECTION_CANDIDATE ≠ PUBLIC_APPROVED`

### Living Loop

`dcp_kernel/living_loop.py` 只組合既有 Gateway／Relation／Public Encounter／Operable Birth gates，不建立第二 control plane。第一個 material break 必須被暴露，不能靠後段成功遮掉前段缺口。

## 4｜代謝與 Withdrawal

Legacy metabolism：

`Primitive/Evidence/Failure Extraction → Successor Binding → Current Eligibility Removal → Reader/Routing/Wake/Rebuild Withdrawal → Minimal Lineage → Pooled Reclaim Review`

Archive、Rename、Move、Historical label、Issue closure 或 search=0 都不等於 withdrawal complete。

每退掉一個 legacy capability，同時問 successor 是否真的接得住原 Need／Event；接不住就標 `OPERABILITY_GAP`，不能把「清乾淨」冒充「已出生」。

目前 01_runtime-spine／03_field-governance／04_adapter-layer 的 successor body review 已完成，但 caller/rebuild/wake withdrawal 仍有 debt；pooled reclaim 尚未授權。

## 5｜Operable Birth

最低出生證據不是文件、Render、PR 或測試存在，而是完整觀察到：

`Existence → Relation → Material Event → Judgment → Capability → Gated Action → Evidence → Receiver Rebuild → New State → Retest`

若 Return 已寫但 Receiver 未重建：`RETURN_NOT_REBUILT`。

若工作反而增加中央化、Carrier 依賴、第二真實或 Owner 人工轉送負荷：`BIRTH_REGRESSION`。

只有完整生命鏈真的讓下一輪狀態不同，才記 `OPERABLE_BIRTH_DELTA`。

目前 GUI-LU Owner-exit pilot 仍缺 Receiver Actual Read／Native Disposition／Behavior Delta／Retest，因此：

`Operable Birth = NOT_PROVEN`  
`Autonomy = NOT_PROVEN`

## 6｜Current Evidence / Open Debt

已存在 Candidate-level executable pieces：

- meaning / judgment / coexistence / composition
- Current / affected cone / capability / carrier resolution
- action gate / write intent / transition / consequence
- Return state machine / re-entry / rebuild
- relation semantics / reception gateway / public encounter / living loop
- feedback synthesis / legacy caller census / withdrawal guards

但最新 branch 尚未觀察到 PR-triggered GitHub Actions run，因此：

`CI = TO_VERIFY`  
`latest test PASS = NOT_CLAIMED`

仍需證明：

- full caller/rebuild/wake withdrawal；
- non-text / physical wake absence；
- Receiver-owned Native rebuild；
- observable Behavior／World State Delta；
- independent Retest；
- Runtime environment evidence（若未來要宣稱 Runtime）。

本 Status 是 Current projection，不是 Promotion、Runtime Receipt、Release Authorization、Canon Admission、Receiver ACK 或 Authority Grant。
