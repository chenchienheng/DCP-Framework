# XL00 Current Active Index v0.1 Candidate

**Repository:** `XuanLing-00-Foundation-DCP`  
**Visibility:** Public  
**State:** Candidate / Repository-role repair / No merge approval / No runtime  
**Human title:** 翾靈 00｜DCP 公開基礎與概念框架

## 一句核心

本倉的 Current Role 是公開的 DCP／XuanLing 概念基礎；Workbench、Adapter、Sync、施工包與 Runtime-like 內容不得因已存在於分支或 Pull Request，就自動成為 Foundation 或 Current Canonical。

## Repository Role

```yaml
Repo_Role:
  use_as:
    - DCP conceptual foundation
    - constraint and judgment framework
    - public explanatory material
    - reusable conceptual patterns
  do_not_use_as:
    - current control home
    - private workspace
    - adapter implementation home
    - build executor workspace
    - runtime or deployment source
    - company-data carrier
```

## Current Safe Reading Layer

1. `README.md`
2. 本文件 `CURRENT_ACTIVE_INDEX.md`
3. 經逐項複審後，被明確標記為 Foundation-compatible 的概念文件

`main` 內其他歷史資料與 Open PR 應先分類，不因存在而自動視為 Active Current。

## Content Classification Candidate

```yaml
Classification:
  FOUNDATION:
    meaning: conceptual DCP / XuanLing patterns compatible with README
  LEGACY_REFERENCE:
    meaning: preserves historical lineage but is not current
  ADAPTER_CANDIDATE:
    meaning: connector, bridge or tool integration requiring another carrier decision
  BUILD_CANDIDATE:
    meaning: bounded construction or workbench material, not Foundation
  RUNTIME_LIKE:
    meaning: executable, scheduled, sync or deployment-oriented material
  MOVE_CANDIDATE:
    meaning: useful but located in the wrong repository role
  PARK:
    meaning: preserved with no current commission
  SUPERSEDED_CANDIDATE:
    meaning: replaced in current role, lineage retained
```

## Open Pull Request Disposition Candidate

| PR | Topic | Candidate disposition | Reason |
|---|---|---|---|
| #228 | Object-Centric Base Pattern | KEEP_REVIEWING | Closest to conceptual Foundation; still Candidate |
| #298 | Cloud Workbench v0.8 | NEEDS_VITAS | Large workbench candidate; may create a second control home |
| #296 | W1 preflight | MOVE_CANDIDATE | Bounded build／return material, not Foundation |
| #274 | Contacts identity adapter | MOVE_CANDIDATE | Adapter／identity implementation layer |
| #275 | Sheet bridge optimization | PARK | Runtime-like optimization outside current priorities |
| #273 | LINE placeholder fix | PARK | Depends on a legacy adapter layer |
| #270 | Lean Dynamic Sync | SUPERSEDED_CANDIDATE | Conflicts with the current single-control／pointer approach |
| #264 | CloudTop／Registry split | SUPERSEDED_CANDIDATE | Historical boundary source retained; current tri-carrier model is broader |
| #254 | Scheduled hygiene scan | SUPERSEDED_CANDIDATE | Historical automation pattern; not the current warehouse loop |

These classifications are review candidates only. They do not close, merge, move, delete, or approve any Pull Request.

## Public Boundary

- Public repository content is not automatically Public-approved doctrine.
- Private conversations, relationship details, company originals, credentials, customer data and unredacted field evidence must not enter this repository.
- A concept may be reusable without its original private Source being published.

## Next Bounded Action

1. Independent review of this role map and PR classification.
2. Identify file-level Foundation／Legacy／Adapter／Runtime-like groups.
3. Prepare a reversible batch plan before any move, close, merge or deletion.

## Red Doors

- Repository Exists != Current Canonical
- Open PR != Active Work
- Draft PR != Safe To Delete
- Public Repo != Public-approved
- Foundation != Runtime
- Classification != Migration
- Candidate != Approved
- Merge != Closeout
