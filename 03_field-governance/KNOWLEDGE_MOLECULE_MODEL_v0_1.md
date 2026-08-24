# Evidence-Bounded Recomposable Unit — Primitive Specimen

**Lifecycle:** RETAINED_PRIMITIVE / SUCCESSOR_COMPILATION_CANDIDATE  
**Current eligibility as fixed Molecule schema:** false

舊 `Knowledge Molecule` 的價值不在 Molecule_ID 或固定 table，而在：知識／證據可被拆成可追溯、可限制、可重新組合的最小有效單元，而不必把整份文件或資料集搬進同一庫。

## Retained primitive
一個可重組單元至少應能回答：
- Stable Existence / Entity binding
- Source / revision / provenance
- Claim or capability supported
- Cannot-support / limitation boundary
- Evidence role / confidence / claim ceiling
- Rights / privacy / disclosure boundary
- Dependency / context / affected scope
- Representation / carrier location
- Receiver / return / reconciliation state

單元可以由文字段落、資料列、DB record、CAD/BIM object、圖像區域、影音片段、code symbol、API response、issue/PR event、model output 等 Carrier 表徵，但 Carrier 不建立 Identity。

## Recomposition invariant
`Task/Question + Boundary/Authority + Context/Dependency → eligible units → compatibility/fidelity check → bounded composition → traceable output/return`

Recomposition by constraints, not retrieval volume. Weak／Pending／conflicting units 可 HOLD 或降階，不因可搜尋而升格。

## Successor binding
`Stable Existence → Source/Evidence → Claim Ceiling → Dependency/Context → Materiality → Representation/Composition → Receiver Return/Reconciliation/Rebuild`

舊 Molecule_ID／Vector_ID／Role_ID／Weight_Profile 固定 schema 留 Git history；需要某種 DB/vector implementation 時再由 Carrier adapter 生成 projection，不回寫成 ontology。
