# Transition Gate Lineage — 64-gate predecessor specimen

**Lifecycle:** METABOLIZED_HISTORICAL_SPECIMEN  
**Current eligibility as 64-gate runtime structure:** false  
**Runtime / Authority:** false

舊版以 64 Gate × 12 Window × 三耦面預留「runtime structural binding space」，並設定 `return_to_00=true`。這是早期 transition representation，不是現行固定拓撲；不得因歷史數量、Window 對位或檔案存在而重建 64-gate organ。

## Retained primitive

Gate 只需要描述一個有界 transition 是否可以合法發生。最小判斷可包含：
- Stable Identity / state before
- Need / trigger / material delta
- dependency / affected scope
- authority / rights / evidence
- entry condition
- permitted effect ceiling
- action / transform
- consequence / responsibility
- exit state / evidence
- return target / reconciliation / rebuild requirement

## Current interpretation

- Gate count 不固定；一個 Need 可以沒有 mutation gate，也可以需要多個 domain-specific gate。
- 12 Window、Bone/Event/Writeback 三面、Gate 01–64 range 都只是 historical representation。
- Gate PASS ≠ execution authority。
- Gate presence ≠ Runtime。
- Gate failure 只 HOLD affected action/relation，不自動導向 00／AXIS／中央 review hub。
- 新 Gate 只有在既有 primitive 無法表達 material constraint 時才可形成 Candidate，不因編號空位而補齊。

## Successor binding

`Need / Event → Identity/State → Dependency/Affected Cone → Judgment/Authority/Evidence → Action Gate → Consequence → Receiver Return → Reconciliation/Rebuild`

Machine successors：`dcp_kernel/action_gate.py`、`dcp_kernel/transition.py`、`dcp_kernel/judgment.py`、`dcp_kernel/consequence.py`、`dcp_kernel/return_state.py`。

完整 64-gate / 12-window predecessor mapping 留 Git history；正常 Reader 不需讀本 specimen。
