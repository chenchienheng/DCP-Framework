# Discontinuity / Dependency-Debt Lineage — predecessor register

**Lifecycle:** METABOLIZED_HISTORICAL_SPECIMEN  
**Current eligibility as Register / task authority:** false  
**Runtime / Authority:** false

舊版用 Register 集中列出 repository gaps，並將 `12-window master / 64-gate / three-coupling runtime map / external-node onchain / return_to_00` 當作待補架構。這些固定 topology 與 register-driven next action 已退休，不得因歷史 gap 再被重建。

## Retained primitives

系統確實需要區分不同型態的 discontinuity，但它們應回到 dependency/state/evidence，而不是形成中央 Register authority：

- **Expected Incompleteness**：施工中合理缺口，不自動視為 failure。
- **Material Dependency Debt**：會阻斷合法 action／return／rebuild 的缺口。
- **Evidence Gap / Unknown**：尚無足夠證據，不得猜測補完。
- **Lineage Gap**：無法確認 predecessor／successor／source revision。
- **Receiver Debt**：Return 已產生但 read／disposition／reconciliation／rebuild 未閉合。
- **Carrier/Binding Debt**：所需 capability 存在但目前 Carrier／rights／authority／fidelity 不足。

## Current rule

Gap 的存在只產生 `HOLD / PENDING / AFFECTED_DEPENDENCY_DEBT`，不自動產生新文件、新 Window、新 Axis、新 Registry 或新 runtime organ。

每個 material debt 應至少可回答：
- Stable Life / Need 是什麼？
- 哪條 dependency 被阻斷？
- Evidence/Unknown 到哪裡？
- 哪個 Authority／Receiver 有權處理？
- 最小必要 action 是什麼？
- Return／Rebuild 如何閉合？

## Retired predecessor instructions

以下舊「下一步」不得因本 lineage specimen 自動復活：
- 建立 `WINDOW_12_MASTER_TABLE.md`
- 建立 `GATE_64_BINDING_NOTE.md`
- 建立 `THREE_COUPLING_RUNTIME_MAP.md`
- 建立 `EXTERNAL_NODE_ONCHAIN_SPEC.md`
- `return_to_00 = true`
- 缺一個 Master Map / Register 就視為 harmful discontinuity

## Successor binding

`Need / Stable Identity → Affected Dependency Cone → Gap Type / Evidence → Authority/Gate → Minimum Necessary Action → Return → Reconciliation/Rebuild`

Machine successors：`dcp_kernel/resolution.py`、`dcp_kernel/judgment.py`、`dcp_kernel/return_state.py`、`dcp_kernel/family_metabolism.py`。

完整 predecessor gap table 與 early-repository construction context 留 Git history；正常 Reader 不需讀本 specimen。
