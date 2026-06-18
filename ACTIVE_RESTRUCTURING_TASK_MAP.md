# Active Restructuring Task Map

> Human-readable map for the current restructuring branch.
>
> Purpose: restore visible task names so the work is understandable from the surface, not only from governance codes such as C-019.

---

## 0. Status

- map_version: v0.8
- status: Active task map / Not closeout
- branch: `audit/lean-dynamic-sync-v0-1-clean`
- related_pr: `#270`
- return_to_00: true

---

## 1. One-Line Reading

This branch is not just tidying documents. It is restructuring XuanLing's internal governance so names, states, tools, humans, cases, valences, runtime claims, security boundaries, temporal records, token use, local agent workflows, architecture-window synthesis, eight-gate routing, whole-corpus filtering, and return paths stop contaminating each other.

---

## 2. Active Tasks by Human-Readable Name

| Task Name | Internal ID / File | What It Means | Status |
|---|---|---|---|
| 全庫篩選重整 | C-012 / `WHOLE_CORPUS_FILTER_PASS_1.md`, `C012_WHOLE_CORPUS_FILTER_PASS_1_STATUS.md` | classify current files and PR-added files into keep / update / merge / archive / hold_candidate decisions | Pass 1 added / needs artifact-register update |
| Register 對齊 | C-013 | reconcile corpus index, role table, and artifact register | Pending after C-012 Pass 1 |
| 狀態語校正 | C-014 / `CANONICAL_STATUS_GLOSSARY.md` | prevent Candidate / Approved / Runtime / Closeout drift | Active |
| Runtime 語義降階 | C-015 / `STATUS.md` and related files | keep semantic-runtime distinct from deployed executable runtime | Active |
| 非線性權圈修正 | C-016 / `THREE_COUPLING_RUNTIME_MAP.md`, `WINDOW_12_MASTER_TABLE.md`, `GATE_64_BINDING_NOTE.md` | prevent 1 / 12 / 64 from being read as a linear ladder | Active |
| 全域生態拓撲球對齊 | C-017 / `EXTERNAL_NODE_ONCHAIN_SPEC.md`, `ECOSYSTEM_TOPOLOGY_SPHERE_ALIGNMENT_ADDENDUM.md` | read GitHub, Qinyi, Codex, M365, Drive, Zenodo, tools, and model families as topology-sphere roles, not flat tools | Active |
| Persistent Agent Habitat | C-018 / `MODULE_14_PERSISTENT_AGENT_HABITAT.md` | absorb OpenAI/Ona-style long-running agent habitat into XuanLing runtime landing grammar | Active |
| 命名污染抽離 | C-019 / `NAMESPACE_REGISTRY.md`, `NAMING_POLLUTION_RULES.md` | assign every name a layer, purpose, forbidden misuse, and status | Active |
| Human Origin Layer / Source Anchor | C-019-P0 / `HUMAN_ORIGIN_LAYER.md` | keep User outside XLEN; User is Source Anchor, not node | Added / needs cross-linking |
| Human Origin Naming Rule | C-019-P0 Addendum / `NAMING_POLLUTION_RULES_HUMAN_ORIGIN_ADDENDUM.md` | add hard rule: User ≠ Node | Added / needs parent-rule integration |
| 治理安全與 agent 信任邊界掃描 | C-021 / `SECURITY_THREAT_MODEL.md`, `SECURITY_FINDINGS_REGISTER.md`, `AGENT_INSTRUCTION_INTEGRITY_SPEC.md`, `ADAPTER_SECURITY_BASELINE.md` | protect instruction integrity, adapter red gates, evidence boundaries, credentials, public/private boundary, and runtime activation | Active |
| 時態序列與狀態唯一性 | C-022 / `TEMPORAL_STATE_SEQUENCE_SPEC.md` | bind logs, rules, settings, functions, PRs, and agent actions to time, record, impact, extension, feedback, and review path | Active |
| Token Capital 與私有學習迴圈 | C-023 / `MODULE_15_TOKEN_CAPITAL_PRIVATE_LEARNING_LOOP.md`, `C023_TOKEN_CAPITAL_STATUS.md` | convert AI usage into reusable memory, judgment, workflow, cases, rules, and next-round capability | Added as module + status addendum |
| Codex Presentation Skill Loop | C-024 / `MODULE_16_CODEX_PRESENTATION_SKILL_LOOP.md`, `C024_CODEX_PRESENTATION_SKILL_LOOP_STATUS.md` | turn presentation creation into a bounded local habitat workflow with permission gate, outline-first production, route choice, and skill recycle | Added as module + status addendum |
| 架構窗 v0.9 主線收束 | C-025 / `XUANLING_ARCHITECTURE_WINDOW_v0_9.md`, `C025_ARCHITECTURE_WINDOW_V0_9_STATUS.md` | consolidate C-017 through C-024 into one readable mainline: human direction, model absorption, tool carrying, task return, capability recycling | Added as architecture window + status addendum |
| 八門八轉軸收斂 | C-026 / `EIGHT_GATE_ROTATION_AXIS_CONSOLIDATION.md`, `EIGHT_GATE_ROUTING_PASS_1.md`, `C026_EIGHT_GATE_ROTATION_AXIS_STATUS.md` | route scattered tasks through eight governable gates: source, intake, naming, authority, habitat, production, return, and atlas closeout | Pass 1 added / ready for corpus filtering follow-up |

---

## 3. Why This May Feel Hard to Read

The previous cleanup language exposed task names such as:

- naming cleanup
- repo cleanup
- artifact register
- Qinyi support pack
- XuanLing topology

The current branch uses internal governance codes such as:

- C-012
- C-017
- C-019
- C-019-P0
- C-021
- C-022
- C-023
- C-024
- C-025
- C-026

Those codes are useful for repo governance but poor for human readability.

Therefore this file restores the visible task layer.

---

## 4. Current Main Workstream

```text
Surface vocabulary cleanup
→ namespace registry
→ pollution rules
→ human origin boundary
→ ecosystem topology sphere
→ persistent agent habitat
→ governance security spine
→ temporal state sequence
→ token capital learning loop
→ Codex local skill loop
→ architecture window v0.9
→ eight-gate rotation-axis consolidation
→ whole-corpus filter pass 1
→ register reconciliation
```

---

## 5. Plain-Language Summary

The branch is currently doing twelve practical things:

1. naming things correctly
2. stopping names from stealing each other's roles
3. separating user, Qinyi, XuanLing, tools, cases, and valences
4. turning external ecosystem tools into governed nodes instead of a tool pile
5. protecting instruction, evidence, adapter, credential, and runtime boundaries
6. preventing logs, rules, settings, functions, PRs, and agent actions from collapsing into false same-state records
7. converting AI usage into reusable memory, judgment, workflow, cases, rules, and next-round capability
8. turning local Codex artifact production into a bounded, reviewable, recyclable skill loop
9. consolidating scattered modules into one readable architecture window
10. routing scattered tasks through eight governable gates
11. classifying corpus files into keep / update / merge / archive / hold_candidate decisions
12. preparing the repo for artifact-register update and register reconciliation

---

## 6. Boundaries

This branch does not mean:

- full architecture is checked out
- main branch is updated
- runtime is deployed
- external tools are authorized
- the user is an XLEN node
- Qinyi is autonomous
- adapter writeback is active
- temporal sequence spec is a deployed event store
- token usage automatically equals token capital
- Codex has universal superiority over ChatGPT / Qinyi
- a single successful workflow is an approved permanent skill
- architecture window v0.9 is approved doctrine
- eight-gate routing is approval
- Pass 1 decision is final deletion or archive action
- PR equals closeout

---

## 7. Next Visible Task Names

Recommended next visible work names:

1. `C012-A Artifact Register Update` — update `UNIFIED_ARTIFACT_REGISTER.md` with Pass 1 handling decisions.
2. `C012-B Inventory Refresh` — add PR #270 new files into a refreshed corpus inventory.
3. `C013-A Register Reconciliation` — align `REPOSITORY_CORPUS_INDEX.md` and `ROLE_CLASSIFICATION_TABLE.md` after C-012 Pass 1.
4. `C-025 Mainline Cross-Linking` — connect architecture window v0.9 to active modules, return packet, and review map.
5. `C-019-P0 Cross-Linking` — connect Human Origin Layer back into namespace registry and pollution rules.
6. `C-021 Security Cross-Linking` — connect Security Layer to active task map, adapter specs, and future runtime red gates.
7. `C-022 Temporal Cross-Linking` — connect temporal state sequence to artifact schema, logs, and return packets.
8. `C-023 Token Capital Cross-Linking` — connect private learning loop to XLA, LOA, cost governance, and model routing notes.
9. `C-024 Codex Skill Loop Cross-Linking` — connect local habitat workflow to LOA, Skill Recycle, and artifact-production safety rules.
10. `PR #270 Return Packet` — make the review container readable before merge consideration.

---

## 8. One-Line Correction

```text
Internal governance codes are not enough; every cleanup front needs a human-readable task name.
```
