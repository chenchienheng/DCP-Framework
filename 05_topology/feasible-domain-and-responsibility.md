# Feasible Domain and Responsibility — retained DCP primitive

**Lifecycle:** RETAINED_PRIMITIVE / CURRENT_RELEVANT  
**Runtime:** false

可行域不是單純限制，而是由現行條件、Dependency、Evidence、Authority、Risk、Carrier capability 與 Return capacity 共同界定的合法作用範圍。

## Invariants
- 超出可行域者只能 Candidate/HOLD/TO_VERIFY，不得冒充已成立。
- Responsibility 不是固定角色名，而是對 action、evidence、return、rebuild consequence 的可追溯承接。
- Capability 不自動擴大 Authority；Authority 也不能消除 evidence requirement。
- Feasible Domain 可因 material delta 擴張、縮小或換 representation，但 Stable Identity 不必改變。
- 無合法 receiver/return path 的 mutation 不形成閉環。

## Successor chain
`Stable Existence → Dependency/Constraint → Evidence/Authority → Feasible Domain → Action → Consequence → Receiver Return → Reconciliation/Rebuild`

此 primitive 保留為 DCP 核心養分；不建立新的固定 layer 或 role topology。