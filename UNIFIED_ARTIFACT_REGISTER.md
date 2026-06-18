# Unified Artifact Register

> Unified register for the current durable architecture corpus.
>
> Purpose: keep active artifacts, historical support, candidate modules, and cleanup decisions readable under the eight-gate routing structure.

---

## 0. Status

- register_version: v0.2
- status: Active register / Needs reconciliation after Pass 1
- source_inventory: `current_files.txt`
- filter_source: `WHOLE_CORPUS_FILTER_PASS_1.md`
- gate_source: `EIGHT_GATE_ROUTING_PASS_1.md`
- related_pr: `#270`
- closeout: false
- return_to_00: true

---

## 1. Register Reading

The corpus is no longer a flat document list.

Each artifact should be read through:

```yaml
Artifact_Record:
  path:
  family_or_group:
  primary_gate:
  secondary_gate:
  handling_decision:
  current_status:
  next_action:
```

Handling decisions are not final removal actions.
They are review states for corpus governance.

---

## 2. Gate Legend

| Gate | Name | Short Role |
|---|---|---|
| G1 | Source Anchor Gate | human origin, direction, review |
| G2 | Intake & Source Gate | source, evidence, temporal intake |
| G3 | Naming & Boundary Gate | namespace, layer, exposure, status |
| G4 | Authority & Dispatch Gate | permission, XAFD, review, red gate |
| G5 | Habitat & Carrier Gate | local/cloud/repo/tool/runtime carrier |
| G6 | Production & Route Gate | artifact route, output path, use case |
| G7 | Return & Recycle Gate | LOR, token capital, skill recycle |
| G8 | Atlas & Closeout Gate | XLA, register, archive, closeout boundary |

---

## 3. Reconciled Register Groups

### Group A — Source Anchor / Mother-Law / Continuity

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `00_meta/user_identity_anchor.md` | G1 | keep | source-anchor bone |
| `HUMAN_ORIGIN_LAYER.md` | G1 | keep | active source-anchor layer |
| `NAMING_POLLUTION_RULES_HUMAN_ORIGIN_ADDENDUM.md` | G1 | keep | hard rule: User is not node |
| `00_mother-law/README.md` | G8 | keep | mother-law index |
| `00_mother-law/existence-consistency-rule.md` | G8 | keep | core consistency rule |
| `00_mother-law/mother-architecture-registry-v0-1.md` | G8 | update | align with architecture window v0.9 |

### Group B — Status / Naming / Boundary Controls

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `CANONICAL_STATUS_GLOSSARY.md` | G3 | keep | active status glossary |
| `NAMESPACE_REGISTRY.md` | G3 | keep | active namespace registry |
| `NAMING_POLLUTION_RULES.md` | G3 | keep | active naming pollution rules |
| `C019_NAMESPACE_POLLUTION_STATUS.md` | G3 | keep | C-019 status note |
| `CONTAMINATION_AND_PRIORITY_POLICY.md` | G3 | keep | active anti-pollution policy |
| `LEGACY_SEED_NAMING_NORMALIZATION_PLAN.md` | G3 | keep | useful naming normalization plan |
| `NAMING_DRIFT_RESOLUTION_REGISTER.md` | G3 | keep | active naming resolution register |
| `NAMING_DRIFT_FILE_LEVEL_DIFFS.md` | G3 | merge | support material for naming register |
| `ROLE_CLASSIFICATION_TABLE.md` | G3 | update | update with eight-gate fields |

### Group C — Source / Temporal / Evidence / Replay

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `TEMPORAL_STATE_SEQUENCE_SPEC.md` | G2 | keep | active temporal-state sequence spec |
| `DISCONTINUITY_REGISTER.md` | G2 | update | add temporal-state fields |
| `MODEL_CONTRADICTION_REGISTER.md` | G2 | update | source/evidence/status separation needed |
| `REPLAY_READINESS_REPORT.md` | G2 | update | align with temporal and evidence fields |
| `SCHEDULING_EFFECTIVENESS_GAP_NOTE.md` | G2 | update | connect to effect proof |
| `SCHEDULING_EFFECT_REGISTER.md` | G2 | keep | useful effect register |
| `04_adapter-layer/source_map.md` | G2 | update | source/view/evidence separation needed |
| `03_board-orchestration/window_delta_mapping_template.md` | G2 | update | align with temporal event schema |
| `01_native-board/pulse_rollup.md` | G2 | update | temporal pulse alignment |
| `01_runtime-spine/github_delta_driven_pulse_rule.md` | G2 | update | pulse rule alignment |
| `SNAPSHOT_MECHANISM_PROPOSAL.md` | G2 | hold_candidate | candidate for snapshot / restore layer |

### Group D — Authority / Dispatch / Security

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `SECURITY_THREAT_MODEL.md` | G4 | keep | active governance security model |
| `SECURITY_FINDINGS_REGISTER.md` | G4 | keep | active security findings register |
| `AGENT_INSTRUCTION_INTEGRITY_SPEC.md` | G4 | keep | active instruction integrity spec |
| `01_runtime-spine/legacy_writeback_block_rule.md` | G4 | keep | red-gate predecessor |
| `04_adapter-layer/writeback_gate_spec.md` | G4 | keep | important writeback gate spec |
| `04_adapter-layer/activation_order.md` | G4 | update | clarify approval boundary |
| `04_adapter-layer/writeback_packet_contract.md` | G4 | update | align with adapter baseline and temporal records |
| `EXTERNAL_API_VERSION_GOVERNANCE_NOTE.md` | G4 | update | avoid API / XAFD pollution |
| `MODEL_INVOCATION_CONTRACT.md` | G4 | update | align with authority and token routing |
| `MODEL_TO_WINDOW_OWNERSHIP_MAP.md` | G4 | update | routing is not approval |
| `05_topology/feasible-domain-and-responsibility.md` | G4 | keep | responsibility boundary |

### Group E — Habitat / Carrier / Ecosystem Nodes

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `MODULE_14_PERSISTENT_AGENT_HABITAT.md` | G5 | keep | active habitat module |
| `ADAPTER_SECURITY_BASELINE.md` | G5 | keep | active adapter safety baseline |
| `EXTERNAL_NODE_ONCHAIN_SPEC.md` | G5 | keep | active external node spec |
| `ECOSYSTEM_TOPOLOGY_SPHERE_ALIGNMENT_ADDENDUM.md` | G5 | keep | active topology sphere addendum |
| `ECOSYSTEM_FAMILY_ONBOARDING_ROADMAP.md` | G5 | update | absorb topology sphere / habitat routing |
| `MODEL_FAMILY_ONCHAIN_SPEC.md` | G5 | update | align with ecosystem topology sphere |
| `NETWORK_STRUCTURE_HIERARCHY_NOTE.md` | G5 | update | align with topology sphere |
| `GITHUB_OPERATION_CAPABILITY_MATRIX.md` | G5 | update | distinguish capability from authorization |
| `AGENT_READINESS_CHECKLIST.md` | G5 | update | connect to habitat and adapter safety |
| `THIRD_RUNTIME_ENVIRONMENT_NOTE.md` | G5 | hold_candidate | runtime boundary still candidate |
| `04_adapter-layer/gamma_entry_spec.md` | G5 | hold_candidate | external tool entry candidate |
| `04_adapter-layer/replit_relay_spec.md` | G5 | hold_candidate | external relay candidate |

### Group F — Production / Route / Skill Loop

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `MODULE_16_CODEX_PRESENTATION_SKILL_LOOP.md` | G6 | keep | active Codex local skill loop module |
| `C024_CODEX_PRESENTATION_SKILL_LOOP_STATUS.md` | G6 | keep | C-024 status note |
| `JULES_TASKBOARD.md` | G6 | update | hold broad daily cleanup until routing stable |
| `CHATGPT_GITHUB_BOOTSTRAP.md` | G6 | archive | historical bootstrap |

### Group G — Return / Recycle / Token Capital

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `MODULE_15_TOKEN_CAPITAL_PRIVATE_LEARNING_LOOP.md` | G7 | keep | active token capital module |
| `C023_TOKEN_CAPITAL_STATUS.md` | G7 | keep | C-023 status note |

### Group H — Atlas / Register / Architecture / Cleanup

| Artifact | Primary Gate | Handling | Note |
|---|---|---|---|
| `ACTIVE_RESTRUCTURING_TASK_MAP.md` | G8 | keep | current human-readable task map |
| `CLEANUP_QUEUE_REGISTER.md` | G8 | keep | active cleanup queue |
| `EIGHT_GATE_ROTATION_AXIS_CONSOLIDATION.md` | G8 | keep | active P0 consolidation spec |
| `EIGHT_GATE_ROUTING_PASS_1.md` | G8 | keep | active first routing table |
| `C026_EIGHT_GATE_ROTATION_AXIS_STATUS.md` | G8 | keep | C-026 status note |
| `XUANLING_ARCHITECTURE_WINDOW_v0_9.md` | G8 | keep | active architecture window |
| `C025_ARCHITECTURE_WINDOW_V0_9_STATUS.md` | G8 | keep | C-025 status note |
| `WHOLE_CORPUS_FILTER_PASS_1.md` | G8 | keep | active C-012 pass |
| `C012_WHOLE_CORPUS_FILTER_PASS_1_STATUS.md` | G8 | keep | C-012 status note |
| `REPOSITORY_CORPUS_INDEX.md` | G8 | update | reconcile after this register |
| `UNIFIED_ARTIFACT_REGISTER.md` | G8 | update | current file; now v0.2 |
| `BRANCH_TOPOLOGY_AND_CLEANUP_REGISTER.md` | G8 | merge | absorb into cleanup queue / architecture map |
| `CLUSTER_COVERAGE_MATRIX.md` | G8 | update | link coverage to eight gates |
| `CLUSTER_COVERAGE_NOTE.md` | G8 | merge | absorb into matrix or register |
| `DYNAMIC_CORPUS_DATABASE_NOTE.md` | G8 | keep | active dynamic corpus direction |
| `GITHUB_CHAIN_MASTER_MAP.md` | G8 | update | avoid GitHub-as-center reading |
| `GITHUB_NORMALIZATION_PHASE_PLAN.md` | G8 | merge | absorb into cleanup phase plan |
| `LEGACY_SEED_BRANCH_INVENTORY_SNAPSHOT.md` | G8 | archive | historical snapshot |
| `LEGACY_SEED_CONTAMINATION_TRIAGE.md` | G3 | keep | useful contamination reference |
| `LEGACY_SEED_MERGE_CANDIDATE_SHORTLIST.md` | G8 | update | route by eight gates |
| `MERGE_LAW_PROPOSAL.md` | G8 | hold_candidate | proposal remains candidate |
| `PRIMARY_BONE_STABILITY_SCORECARD.md` | G8 | keep | useful stability scorecard |
| `README.md` | G8 | update | reflect v0.9 later without overclaiming |
| `SEED_SHADOW_POINTER.md` | G8 | archive | historical pointer |
| `SEMANTIC_COMPRESSION_REPORT.md` | G8 | archive | historical report |
| `STAGE_SYNC_SNAPSHOT_2026-04-21.md` | G8 | archive | dated snapshot |
| `STATUS.md` | G8 | update | reflect latest candidate boundaries |
| `THREE_COUPLING_RUNTIME_MAP.md` | G8 | keep | central topology map |
| `WINDOW_12_MASTER_TABLE.md` | G8 | keep | central window table |
| `XUANLING_WORLD_READINESS_MILESTONES.md` | G8 | hold_candidate | avoid maturity inflation |

---

## 4. Register Gaps

The following are known gaps after v0.2:

1. `current_files.txt` does not yet include PR #270 added files.
2. `REPOSITORY_CORPUS_INDEX.md` and `ROLE_CLASSIFICATION_TABLE.md` still need reconciliation.
3. Some historical files listed in v0.1 are not present in `current_files.txt`; they should be checked before removal from long-term references.
4. Keep/update/merge/archive decisions are Pass 1 review states, not final actions.

---

## 5. Next Actions

```yaml
Next_Actions:
  C012_B:
    action: refresh current_files inventory to include PR #270 artifacts
  C013_A:
    action: reconcile REPOSITORY_CORPUS_INDEX against this register
  C013_B:
    action: reconcile ROLE_CLASSIFICATION_TABLE against this register
  C014_A:
    action: propagate canonical status terms into updated artifacts
```

---

## 6. Non-Promotion Rules

Do not promote:

| From | To |
|---|---|
| register entry | approved doctrine |
| handling decision | final action |
| archive candidate | useless artifact |
| merge candidate | erased value |
| keep | permanent immunity |
| update | defect |
| hold_candidate | active runtime |

---

## 7. Status

- register_synchronized: partial
- pass_1_decisions_loaded: true
- eight_gate_fields_added: true
- needs_inventory_refresh: true
- needs_repository_index_reconciliation: true
- needs_role_table_reconciliation: true
- closeout: false
