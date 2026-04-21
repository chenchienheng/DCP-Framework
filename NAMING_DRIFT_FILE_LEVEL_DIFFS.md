# Naming Drift File-Level Diffs

> File-level comparison for known naming drift families.
> Purpose: move from family-level awareness to actionable file-level resolution.

---

## 0. Core Reading

This document lists observed files under legacy underscore families.
It does not yet finalize which files are:
- unique seed
- duplicate
- contamination

It prepares the next execution step: classification and rebind.

---

## 1. N-001 Runtime Spine Drift

### Legacy: `01_runtime_spine/`

Observed files:
- runtime_spine.md
- chain_flow_map.md
- writeback_protocol.md

### Canonical: `01_runtime-spine/`

Status:
- file-level comparison pending

---

## 2. N-002 Board Orchestration Drift

### Legacy: `03_board_orchestration/`

Observed files:
- board_registry.md
- orchestration_rules.md
- routing_logic.md

### Canonical: `03_board-orchestration/`

Status:
- file-level comparison pending

---

## 3. N-003 Adapter Layer Drift

### Legacy: `04_adapter_layer/`

Observed files:
- adapter_map.md
- source_adapter.md
- writeback_adapter.md

### Canonical: `04_adapter-layer/`

Status:
- file-level comparison pending

---

## 4. Next Execution Step

For each file:

1. classify:
   - seed / duplicate / contamination
2. decide:
   - preserve / rewrite / retire
3. rebind:
   - move into canonical family
4. writeback:
   - record decision in cleanup register

---

## 5. Status

- file_level_diffs_initialized: true
- classification_pending: true
- rebind_pending: true
- return_to_00: true
