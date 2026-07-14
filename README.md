# DCP Framework

**A Constraint-Based Framework for Structured Judgment and Layered Interpretation**  
**判定約束框架：一種用於結構化判定與分層詮釋的方法**

---

## Overview / 概述

### EN

The DCP Framework is a conceptual framework for reasoning under constraints.
It provides a structured way to describe how judgments, comparisons, and interpretations are formed when information is incomplete, heterogeneous, or condition-dependent.

Rather than producing answers or decisions, DCP makes explicit the conditions, references, assumptions, and uncertainties involved in any judgment process.

This repository presents DCP as a conceptual and interpretive framework, not as a software system or executable model.

### ZH

DCP（判定約束框架）是一套用於「在條件限制下進行結構化判定」的概念性框架。
它用來描述在資訊不完整、異質或受情境影響時，人們如何形成判定、比較與詮釋。

DCP 並不產生答案，也不替代決策，而是將判定所依賴的條件、參考來源、假設與不確定性加以顯性化，使其可被檢視與重組。

本專案呈現的是一個概念與方法層級的框架，而非軟體、演算法或自動化系統。

---

## Structure of This Repository / 專案結構說明

本倉庫依照概念層級劃分為三個部分，各自獨立但可相互對照閱讀：

### Part 0 — Core (Layer 0)

DCP 核心結構，描述判定的基本構成邏輯，包括：

- 條件（Conditions）
- 參考集合（Reference Sets）
- 約束（Constraints）
- 不確定性（Uncertainty）
- 判定狀態（成立／不成立／未定）

此層為抽象層，定義「什麼是判定」以及「判定如何成立」。

### Part I — Interpretive Layer (Layer 1 / Xuanling System)

在 Layer 0 之上，整理可重複使用的詮釋結構與判定樣式，包括：

- 判定模板
- 條件組合模式
- 可重用的推理結構
- 詮釋流程與語義約束

此層將抽象邏輯轉化為可閱讀、可重組的結構形式，但仍不涉及具體實作或應用。

### Part II — Projection Layer (Layer 2)

本層提供「投影式示例」，用來展示 DCP 如何映射到不同領域中。

這些內容：

- 是示意性的（illustrative）
- 不構成實作或產品
- 不限定特定產業或用途
- 可被視為條件投影或案例原型

其目的在於展示框架的可延展性，而非給出最終應用形式。

---

## Current Repository Role / 目前倉庫角色

Start cleanup-oriented reading with:

1. `README.md`
2. [`docs/alignment/xl00-current-active-index-v0_1.md`](docs/alignment/xl00-current-active-index-v0_1.md)

The current index separates conceptual Foundation material from legacy references, adapter/build candidates, runtime-like content, and open-PR review candidates. It is a review aid only and does not authorize merge, close, migration, deletion, runtime, or publication.

目前索引用來把概念 Foundation、歷史參考、Adapter／施工候選、Runtime-like 內容及 Open PR 分開判位；它不是合併、關閉、搬遷、刪除、Runtime 或公開批准。

---

## How to Read This Repository / 閱讀建議

1. 從 Part 0 開始，理解判定的抽象結構。
2. 閱讀 Part I，理解如何形成可重用的詮釋模式。
3. 將 Part II 視為投影與示例，而非規範或實作。
4. 先讀 Current Repository Role，再展開歷史、Adapter 或施工候選。
5. 各部分可獨立閱讀，也可交叉參照。

---

## Design Principles / 設計原則

### EN

- Constraint-driven rather than rule-driven
- Interpretable rather than opaque
- Modular rather than monolithic
- Open-ended rather than finalized
- Conceptual rather than executable

### ZH

- 以條件為中心，而非規則至上
- 可解釋，而非黑盒
- 模組化，而非單體系統
- 開放演化，而非定稿封閉
- 概念導向，而非可執行程式

---

## Intended Use / 使用方式

This framework may be used as:

- a thinking scaffold
- a reasoning template
- a documentation structure
- a comparative or analytical lens
- a reference for AI-assisted or human reasoning workflows

It does not prescribe actions, decisions, or implementations.

---

## License / 授權說明

This work is licensed under **CC BY-NC-ND 4.0**.

You may:

- read and share the work
- cite it with attribution

You may not:

- use it for commercial purposes
- distribute modified or derivative versions

For commercial or derivative use, separate permission from the author is required.

---

## Citation / 引用方式

Chen, Chien-Heng. *DCP Framework: A Constraint-Based Model for Structured Judgment and Layered Interpretation*. Zenodo, 2026.  
DOI: https://doi.org/10.5281/zenodo.18111818

陳建衡，《DCP 框架：一種結構化判定與分層詮釋的約束模型》，Zenodo，2026。  
DOI：https://doi.org/10.5281/zenodo.18111818

---

## Status

This repository represents an evolving conceptual framework. It is intentionally open-ended and designed to support future reinterpretation and extension.

Public repository visibility does not equal public approval. Open pull requests and cleanup branches remain candidates until explicitly reviewed and merged.