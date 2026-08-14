# DCP Framework / 翾靈 Foundation

**Repository class / 倉庫分類：** Public research and reference corpus  
**Operational status / 運作狀態：** Non-production  
**Authority model / 權限模型：** No implicit runtime or decision authority

## Overview / 概述

DCP is a structural framework for representing dependency, state, authority, evidence, change, and return across distributed systems and workflows.

DCP 是一套用於描述分散式系統與工作流中 Dependency、State、Authority、Evidence、Change 與 Return 的結構化框架。

This repository contains the public research and reference surface of that framework. It publishes concepts, validation patterns, bounded examples, historical research artifacts, and citation material suitable for external review. It does not serve as a native data root or expose protected internal implementation detail.

本倉庫承載該框架的公開研究與參考表面，包含適合外部審閱的概念、驗證模式、有限範例、歷史研究成果與引用資料；它不是 Native Data Root，也不承載受保護的內部實作細節。

## Representation architecture / 表徵架構

Public documentation follows three aligned representation profiles:

公開文件採三個互相對準的表徵層級：

- **Human Profile / 人類閱讀層** — Traditional Chinese for direct comprehension and review.
- **External Profile / 外部交換層** — English for publication, interoperability, and external technical review.
- **Canonical Machine Profile / 機器規範層** — minimal stable identifiers, typed states, versions, and public evidence references.

The profiles share one governed meaning. Differences in presentation are allowed; differences in state, authority, claim ceiling, or release classification are not.

三個表徵層共用同一受治理語義。呈現方式可以不同，但 State、Authority、Claim Ceiling 與 Release Classification 不得互相漂移。

## Public scope / 公開範圍

The repository may contain:

本倉可承載：

- public research primitives and terminology / 公開研究 primitive 與術語
- validation and failure patterns / 驗證與失敗模式
- bounded examples and reference artifacts / 有限範例與參考成果
- release-appropriate historical lineage / 適合公開的歷史脈絡
- published citations and evidence references / 已發布引用與證據指標

Protected internal dependency topology, privileged authority routing, private evidence lineage, sensitive source relationships, and implementation-specific machine contracts remain outside the public corpus.

受保護的內部 dependency topology、privileged authority routing、private evidence lineage、敏感來源關係與實作特定 machine contract 不屬於公開語料範圍。

## Interpretation / 判讀原則

Repository location, filename, issue state, or modification time does not establish architectural truth or operational maturity. Readers should resolve the declared artifact role, lifecycle state, evidence scope, and release classification before relying on a document.

Repository 位置、檔名、Issue 狀態或修改時間都不能單獨建立 Architecture Truth 或 Operational Maturity。使用文件前，應先解析其 Artifact Role、Lifecycle State、Evidence Scope 與 Release Classification。

## Machine metadata / 機器中繼資料

```yaml
repository_class: public_research_corpus
runtime: false
native_source_root: false
representation_profiles:
  human: zh-TW
  external: en
  machine: canonical-minimal
release_control: explicit
```

## License / 授權

**Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International (CC BY-NC-ND 4.0).**

可閱讀、分享及標示來源引用；商業或衍生使用需另取得作者許可。  
You may read, share, and cite with attribution. Commercial or derivative use requires separate permission.

## Citation / 引用

Chen, Chien-Heng. *DCP Framework: A Constraint-Based Model for Structured Judgment and Layered Interpretation*. Zenodo, 2026. DOI: https://doi.org/10.5281/zenodo.18111818

陳建衡，《DCP 框架：一種結構化判定與分層詮釋的約束模型》，Zenodo，2026。

For disclosure and representation controls, see `PUBLIC-SURFACE-POLICY.md`.

揭露與表徵控制請參閱 `PUBLIC-SURFACE-POLICY.md`。
