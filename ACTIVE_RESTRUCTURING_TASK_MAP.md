# Active Restructuring Task Map

> Human-readable map for the current restructuring branch.
>
> Purpose: restore visible task names so the work is understandable from the surface, not only from governance codes such as C-019.

---

## 0. Status

- map_version: v0.3
- status: Active task map / Not closeout
- branch: `audit/lean-dynamic-sync-v0-1-clean`
- related_pr: `#270`
- return_to_00: true

---

## 1. One-Line Reading

This branch is not just tidying documents. It is restructuring XuanLing's internal governance so names, states, tools, humans, cases, valences, runtime claims, security boundaries, temporal records, and return paths stop contaminating each other.

---

## 2. Active Tasks by Human-Readable Name

| Task Name | Internal ID / File | What It Means | Status |
|---|---|---|---|
| 全庫篩選重整 | C-012 / `CLEANUP_QUEUE_REGISTER.md` | classify current files into keep / update / merge / archive / retire | Active |
| Register 對齊 | C-013 | reconcile corpus index, role table, and artifact register | Active |
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
→ dynamic corpus filtering
→ register reconciliation
```

---

## 5. Plain-Language Summary

The branch is currently doing seven practical things:

1. naming things correctly
2. stopping names from stealing each other's roles
3. separating user, Qinyi, XuanLing, tools, cases, and valences
4. turning external ecosystem tools into governed nodes instead of a tool pile
5. protecting instruction, evidence, adapter, credential, and runtime boundaries
6. preventing logs, rules, settings, functions, PRs, and agent actions from collapsing into false same-state records
7. preparing the repo for whole-corpus filtering and machine-readable governance

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
- PR equals closeout

---

## 7. Next Visible Task Names

Recommended next visible work names:

1. `C-019-P0 Cross-Linking` — connect Human Origin Layer back into namespace registry and pollution rules.
2. `C-021 Security Cross-Linking` — connect Security Layer to active task map, adapter specs, and future runtime red gates.
3. `C-022 Temporal Cross-Linking` — connect temporal state sequence to artifact schema, logs, and return packets.
4. `C-012 Whole-Corpus Filter Pass 1` — assign handling decisions to current files.
5. `C-013 Register Reconciliation Pass 1` — align corpus index, role table, and artifact register.
6. `C-017 Ecosystem Roadmap Patch` — safely patch ecosystem onboarding roadmap in small sections.
7. `PR #270 Return Packet` — make the review container readable before merge consideration.

---

## 8. One-Line Correction

```text
Internal governance codes are not enough; every cleanup front needs a human-readable task name.
```
