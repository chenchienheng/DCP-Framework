# Action Classification Lineage — predecessor three-action taxonomy

**Lifecycle:** HISTORICAL_ACTION_SPECIMEN  
**Current action taxonomy:** false  
**Runtime / Authority:** false

舊版要求所有 repository execution 都映射到 `structural_cleanup / dependency_link / state_register_update` 三類。這是早期 repo-centric work taxonomy，不足以表達現行 Need／Judgment／Capability／Action Effect／Responsibility／Return。

## Retained primitives
- Action 必須有 bounded scope、Authority、Evidence／verification、Expected Effect、Stop/Failure condition 與 Return。
- 執行工作不得因 convenience 靜默改寫 Meaning／Identity／Authority。
- 高階 conflict 應保持 Conflict/HOLD 並回到合法 Receiver，而不是由 executor 自行裁定。
- Structural cleanup、dependency repair、state reconciliation 仍可作 descriptive action labels，但不具有 exhaustive taxonomy 地位。

## Current action model
`Need → Judgment → permitted effect ceiling → Minimum Necessary Action → Work Contract when action is needed → Consequence/Responsibility → Evidence → Return/Rebuild`

`NO_ACTION`、`OBSERVE`、`PREPARE`、bounded mutation 等可依實際 Need 成立；不存在「每個任務一定要塞進三種 repo action」的規則。

Machine successors：`dcp_kernel/action_gate.py`、`dcp_kernel/decision_chain.py`、`dcp_kernel/platform.py`、`dcp_kernel/consequence.py`。

完整 predecessor taxonomy 留 Git history。
