# Full-Lifecycle Asset Matrix

> **Lifecycle:** HISTORICAL_SPECIMEN
> **Current authority:** false
> **Runtime:** false
> **Reader shield:** The S1–S5 / W0-Wx / Jules-Codex / merge-to-main model below is a historical lifecycle specimen. It must not be used as the current DCP lifecycle or authority model.
> **Successor interpretation:** use `CURRENT-SURFACE-MANIFEST.json`, `SIX_DIMENSION_REPOSITORY_PROJECTION.md`, and current receiver-owned return/reconciliation rules.
> **Retained value:** asset lifecycle tracking, handoff hardening, stable IDs, return path, and archival lineage remain reusable primitives after bounded re-interpretation.

> Purpose: Preserve a historical lifecycle/schema specimen for
> artifacts within the former DCP-Framework corpus generation.

---

## 1. Asset Definition

An **Asset** is any durable artifact registered within the repository,
including markdown specifications, log entries, and bridge contracts. All assets
must be tracked through their full lifecycle from scouting to archival.

---

## 2. Historical Lifecycle Stages

| Stage | Name | Description |
| :--- | :--- | :--- |
| **S1** | **Scout** | Raw discovery or external signal (unhardened). |
| **S2** | **Draft** | Initial structural formulation (internal war-room). |
| **S3** | **Review** | Formal evaluation against Mother-Law and Bone rules. |
| **S4** | **Active** | Historical rule: merged into `main` and registered in the corpus index. **This is no longer a Current admission rule.** |
| **S5** | **Archived** | Superseded or preserved as execution trace only. |

---

## 3. Historical Schema Alignment Rules

To ensure cross-window consistency, every asset declared:

- **Asset_ID:** `[FAMILY]-[TYPE]-[SEQUENCE]` (e.g., META-SPEC-001).
- **Location_Link:** Canonical path within the repository.
- **Return_Path:** Target path for future updates or corrections.
- **State_Layer:** `ACTIVE`, `STRUCTURE_ESTABLISHED`, or `SUPERSEDED`.

These fields remain useful as lineage primitives, but repository location or merge status no longer establishes Current, Authority, or receiver absorption.

---

## 4. Historical Cross-Window Handoff Contract

When an asset moved between windows (e.g., from a scout window to the bone
window), it passed through a **Hardening Gate**:

- **Rule 1:** Verify semantic integrity (no unauthorized fact promotion).
- **Rule 2:** Ensure all required fields for the destination window are present.
- **Rule 3:** Update `Legion_Log` with the handoff trace.

Current interpretation replaces fixed window/agent roles with bounded Domain → Authority → State → Circle → Pole → Cloud dispatch and receiver-owned return/reconciliation.

---

## 5. Historical Matrix View

| Asset Type | Primary Window | Review Node | Registry |
| :--- | :--- | :--- | :--- |
| **Bone (Core)** | W0 (Bone) | Mother-Law | REPOSITORY_CORPUS_INDEX |
| **Event (Pulse)** | W0 (Pulse) | Jules | GITHUB_CHAIN_MASTER_MAP |
| **Draft (War-room)** | Wx (Temporary) | ChatGPT | CLEANUP_QUEUE_REGISTER |
| **Adapter (Bridge)** | Wx (Adapter) | Codex | UNIFIED_ARTIFACT_REGISTER |

The table above is retained only as historical lineage and failure-learning material.

---

## 6. Status

- **ID:** META-SPEC-002
- **Historical Status:** STRUCTURE_ESTABLISHED_IN_PREVIOUS_GENERATION
- **Current Eligibility:** false
- **Last_Reconciled:** 2026-04-21
- **Re-entry:** explicit bounded successor/admission decision required
