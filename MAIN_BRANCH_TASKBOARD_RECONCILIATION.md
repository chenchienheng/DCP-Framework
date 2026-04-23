# Main Branch Taskboard Reconciliation

## Purpose

Re-align internal taskboard and execution context with the current `main`
branch state using state layering, preserving chain continuity and replay
traces instead of blindly closing issues.

## Scope

- scan current `main`
- classify open issues (ACTIVE, STRUCTURE_ESTABLISHED, SUPERSEDED)
- map execution issues to Coretri master axes
- preserve execution trace
- reconcile internal task list against actual repository state

## 1. Valid Master Axis Layers on Main

Based on structural scanning of the `main` branch, the following Master Layers
are currently valid and actively present:

- **AXIS-02 Existence:** `00_mother-law/existence-chain-master-layer.md`
- **AXIS-03 Time:** `TIME_CHAIN_MASTER_LAYER.md`
- **AXIS-04 Space:** `SPACE_CHAIN_MASTER_LAYER.md`
- **AXIS-05 Review:** `REVIEW_CHAIN_MASTER_LAYER.md`
- **Other Core Rules:** `GITHUB_CHAIN_MASTER_MAP.md`, `WINDOW_12_MASTER_TABLE.md`

*(Note: AXIS-01 World (`WORLD_CHAIN_MASTER_AXIS.md`) was reverted in PR #27
and is currently inactive on `main`)*

## 2. Issue State Classification & Axis Mapping

Open issues are classified to preserve their execution trace rather than
immediately closing them.

### ACTIVE

Currently active work streams that have not been superseded or established.

- **#9 - [Jules] First standardized task packet run (Registry + Snapshot readiness)**
  - `execution_only: true`
  - `mapped_axis: AXIS-05` (Review / Validation)
  - Status: Remains open, waiting on registry sweep execution.

- **#6 - [Jules] Scheduler Topology Reconciliation to Platform Map**
  - `execution_only: true`
  - `mapped_axis: AXIS-03` (Time / Scheduling)
  - Status: Remains open, waiting on reconciliation execution.

### STRUCTURE_ESTABLISHED

Issues where the core structural layer has been merged, but the issue trace
remains open to preserve continuity or handle subsequent execution phases.

- **#20 - [Coretri Axis] Review Chain Master Layer**
  - `mapped_axis: AXIS-05`
  - Status: Layer established (PR #21 merged). Remains open as continuity anchor.

- **#18 - [Coretri Axis] Time Chain Master Layer**
  - `mapped_axis: AXIS-03`
  - Status: Layer established (PR #26 merged). Remains open as continuity anchor.

- **#17 - [Coretri Axis] Existence Chain Master Layer**
  - `mapped_axis: AXIS-02`
  - Status: Layer established (PR #22 merged). Remains open as continuity anchor.

- **#16 - [Coretri Axis] World Chain Master Layer**
  - `mapped_axis: AXIS-01`
  - Status: Layer reverted (PR #27). Remains open as the architecture trace
    for AXIS-01 is currently unresolved.

- **#15 - [Jules] Governance Proposal Consolidation
  (Snapshot + Merge Law + Replay Readiness)**
  - `execution_only: true`
  - `mapped_axis: AXIS-05` (Review / Proposal Consolidation)
  - Status: Structure established via PR #23. Open to preserve replay trace.

### SUPERSEDED

Issues that are fully superseded with no dependency trace remaining. These
are safe to close.

- **#2 - Extract xuanling-seed-v0-1 into controlled corpus map**
  - `execution_only: true`
  - `mapped_axis: AXIS-04` (Space / Corpus positioning)
  - Status: Fully superseded by PR #13. Safe to close.

- **#1 - Re-index existing repository corpus into a durable chain map**
  - `execution_only: true`
  - `mapped_axis: AXIS-04` (Space / Chain Mapping)
  - Status: Fully superseded by PR #12. Safe to close.

## 3. Recommended Cleaned Taskboard

Based on the `main` state and state layering, the taskboard should prioritize
cleanup while preserving execution traces:

1. **State Clean: Close Fully Superseded Issues**
   - Close ONLY #1 and #2.
2. **Registry Clean: Next Execution Packet**
   - Use the ACTIVE issues (#6, #9) to perform a registry sweep ensuring
     `REPOSITORY_CORPUS_INDEX.md` and related registers align with the established
     master layers.
3. **Branch Topology Clean**
   - Re-evaluate branch cleanup order now that Master Layers are anchored
     on `main`.

## 4. Mismatch or Gap

- **Trace Preservation Gap**: Previous cleanup logic assumed merging a PR meant
  the issue should close. State layering requires issues to remain open as
  `STRUCTURE_ESTABLISHED` until the full execution chain is validated.
- **AXIS-01 Gap**: The World Chain axis is currently un-established on `main`
  after the revert, leaving a gap in the Coretri axis foundation.

## 5. Next Recommended Action

- Close fully superseded issues (#1, #2) and retain the others in their
  classified state layers to preserve chain continuity.
