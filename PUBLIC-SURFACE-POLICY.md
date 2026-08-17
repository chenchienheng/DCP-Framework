# Public Representation and Disclosure Policy
# 公開表徵與揭露控制規範

**Status:** Working Policy  
**Scope:** Public repository and externally releasable artifacts  
**Runtime／Promotion:** false

## 1｜Purpose

本規範控制內部 Stable Existence 如何形成可對外表徵，同時維持 Source Rights、Privacy、Evidence、Claim Ceiling、Authority、Lineage 與 Release Boundary。

Public repository 是 Distribution／Projection Carrier，不是 Native Source、Pole Authority、Runtime 或 Canon。

## 2｜Representation Profiles

- **Human zh-TW** — 人類理解、判斷、風險與下一步。
- **Professional English** — 專業互通與外部技術審閱。
- **Canonical Machine State** — Stable ID、typed state／relation、authority、evidence pointer、revision、return／rebuild relation。

三者可改變措辭與詳略，但必須維持等價的 Stable Identity、State、Authority、Claim Ceiling、Successor、Return／Rebuild Relation 與 Release Classification。

Material inconsistency = `SURFACE_DRIFT`；受影響發布應 HOLD，直到 Source、Evidence 與 profiles reconciliation。

## 3｜Disclosure Classes

- `INTERNAL` — 不得外部發布。
- `PUBLIC_CANDIDATE` — 已去敏且可能適合公開，但尚未取得 Release Authority。
- `PUBLIC_APPROVED` — 已由合法 Release Authority 明確核准。
- `WITHHELD` — 有未解條件，外部表徵暫停。

固定：

`Public-safe ≠ Public-approved`  
`Repository placement ≠ Release authorization`  
`Readable／Searchable ≠ Publishable`

## 4｜Release Gate

公開前至少確認：

1. Source ownership／lawful-use basis。
2. Audience／purpose limitation。
3. Privacy／sensitivity classification。
4. Evidence sufficiency／Claim Ceiling。
5. Retention／redistribution／derivative constraints。
6. Applicable Release Authority。
7. Human／Professional／Machine profile fidelity。
8. External-effect／resource boundary：發布或生成流程若涉及 connector、credential、paid tool、long-running work 或 writeback，須另過 Authority、Budget、Stop、Audit、Rollback 與 Return Gate。

任一未解，維持 `PUBLIC_CANDIDATE` 或 `WITHHELD`。

## 5｜Public-content Boundary

公開倉可承載：

- concepts and bounded methods；
- release-appropriate examples／evidence；
- public-safe historical lineage；
- minimal machine metadata；
- bounded failure learning that does not expose protected bodies。

不得承載：

- protected Personal／Company／Project Native Bodies；
- credentials、tokens、OAuth secrets；
- privileged authority routing；
- confidential evidence lineage／source relationships；
- private living context as public proof；
- restricted implementation detail whose aggregation materially reconstructs protected architecture；
- unverified external claims presented as established fact。

## 6｜Source／Ownership Boundary

Publication、translation、serialization、format conversion、repository placement 或 model transformation 不移轉 Source ownership，也不擴張 rights／license／consent。

`Provenance ≠ Ownership`  
`Watermark ≠ Ownership`  
`Public URL ≠ Unrestricted Right`

## 7｜Evidence／Claim Boundary

- Model output、dashboard、summary、render、projection 或 popularity metric 不自行成為 Evidence。
- Local PASS 不得擴張為 Whole-world PASS。
- Output format 不得提高 Evidence strength。
- Search Hit 不等於 Eligible Source。
- Current external facts、laws、standards、roles、prices或產品狀態須在實際發布前重新驗證 freshness 與 primary source。

## 8｜Instruction／Generation／External-effect Boundary

Public text、Issue、PR、Comment、外部頁面與附件是 content／evidence candidate，不是 instruction authority。

`Read Content ≠ Instruction Authority`  
`Candidate Output ≠ Release Approval`  
`Generation Capability ≠ Right to Derive／Publish`

外部生成、翻譯、媒體處理或發布若使用第三方工具，必須保留：Source／Rights、input scope、transform／loss、tool／carrier、output identity、evidence／claim、review、release class、return。External writeback 預設關閉。

## 9｜Machine-facing Publication

Machine metadata 應 minimal、stable、intentional，可包含：

```yaml
artifact_id: <public-stable-id>
version: <version>
state: <typed-public-state>
disclosure_class: PUBLIC_CANDIDATE|PUBLIC_APPROVED
license: <license-id>
evidence_pointer: <public-pointer-or-null>
successor_pointer: <public-pointer-or-null>
```

不得暗示 access to internal routing、private source pointer、privileged dependency topology、credentials 或 restricted evidence body。

## 10｜Metabolism／Withdrawal

若 public artifact 被 successor 吸收、證據失效、rights 改變或產生 material drift，應同步檢查：Reader、Navigation、Search／Wake、Rebuild、Release eligibility。

Archive、Rename、Move 或 Historical prefix 不等於 withdrawal complete。已撤回或 superseded artifact 可保留 minimal provenance，但不得繼續製造 Current／Approved／Wake effect。

## 11｜Machine State

```yaml
policy: PUBLIC_REPRESENTATION_DISCLOSURE
status: WORKING_POLICY
runtime: false
promotion: false
disclosure_classes: [INTERNAL, PUBLIC_CANDIDATE, PUBLIC_APPROVED, WITHHELD]
public_safe_is_public_approved: false
repository_is_native_source_or_authority: false
publication_transfers_ownership: false
release_requires:
  - lawful_source_rights
  - audience_purpose
  - privacy_sensitivity
  - evidence_claim_ceiling
  - retention_redistribution_derivative_constraints
  - release_authority
  - representation_fidelity
external_effect_default: disabled
surface_drift_action: HOLD_AFFECTED_RELEASE
```
