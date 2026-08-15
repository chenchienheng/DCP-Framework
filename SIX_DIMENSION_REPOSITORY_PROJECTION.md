# Six-Dimension Repository Projection / 六維倉庫投影

**Status / 狀態:** Architecture Candidate  
**Runtime:** false  
**Promotion:** false  

## 人話 / Human zh-TW

GitHub 倉庫不是 DCP 的 Native Domain，也不是 Authority。它只是「雲」的一種技術投影載體。

對任何 Repository Artifact，先用六個互相獨立的問題判位：

1. **域 Domain** — 原生世界／Owner 在哪裡？
2. **權 Authority** — 誰能讀、判、寫、核准、釋放、ACK？
3. **態 State** — Candidate／Current／Historical／Return／Released／Stale 等哪一態？
4. **圈 Circle** — 本次 Project／Window／Review／Public Release 的作用邊界是什麼？
5. **極 Pole** — Ideas／DCP／GLModel 哪一極或哪些極需要 bounded projection？
6. **雲 Cloud** — GitHub／Drive／DB／SaaS／Local 等哪個 Carrier 承載這次表徵？

預設判位順序為：**域 → 權 → 態 → 圈 → 極 → 雲**。Boundary 可提前停止 affected branch，但 Cloud／Repo 不得先於 Domain／Authority 取得語義主導權。

Dependency、Evidence、Return、Reconciliation、Re-entry、Rebuild 是六維座標之間的 governed relation／transition，不另立第七個資料分類。

## Professional English

This repository is a Cloud/Carrier projection, not a native domain or authority root. Repository artifacts should be interpreted through six orthogonal coordinates: Domain, Authority, State, Circle, Pole and Cloud. The default dispatch order is Domain → Authority → State → Circle → Pole → Cloud. Dependency, evidence, return, reconciliation, re-entry and rebuild are governed relations across coordinates rather than additional storage dimensions.

## Canonical Machine State

```yaml
model: SIX_DIMENSION_DISPATCH
status: ARCHITECTURE_CANDIDATE
dimensions:
  - domain
  - authority
  - state
  - circle
  - pole
  - cloud
default_order:
  - domain
  - authority
  - state
  - circle
  - pole
  - cloud
cloud_binding: GitHub:DCP-Pole-Projection
pole_weight: DCP
repo_is_domain: false
repo_is_authority: false
repo_is_native_source_root: false
relations:
  - dependency
  - evidence
  - return
  - reconciliation
  - reentry
  - rebuild
```

## Repository metabolism

Legacy root families remain visible for lineage/compatibility, but root presence, filename, modification time, searchability, or an old register reference does not re-admit them into Current.

Observed legacy examples include `00_mother-law`, `01_runtime-spine`, `02_translation-layer`, `03_board-orchestration`, `04_adapter-layer`, and `05_topology`. Historical material should be reclaimed only through successor, reader-shield, authority/evidence and re-entry/rebuild gates.

A stale register may still name an artifact that has already been retired or moved into historical lineage. Such a reference is a drift signal, not proof that the artifact should be recreated.

## Cross-repository rule

DCP-Pole-Projection, Ideas-Pole-Projection and GLModel-Pole-Projection are three pole-weighted GitHub projections of one CoreTri architecture. They do not create three truths and they do not grant pole authority. Shared continuity should use bounded pointers, receipts, receiver states and return/rebuild relations rather than copied Native Bodies.
