# Return Packet Template v0.4

Status: Candidate / Return Packet Template / No Runtime / No External Writeback
Use As: common return packet template for QHA / LOR / field / repo returns
Do Not Use As: approved doctrine, legal retention policy, company record policy, automated deletion rule, or merge approval

## Core

Return Packet v0.4 adds temporal retention, essence extraction, pollution control, and pointer fields. A return packet must be readable by Vitas, useful for QHA, and safe for future memory retrieval.

## Vitas-Readable First Layer

```yaml
Vitas_Readable_First_Layer:
  one_line_summary_zh:
  read_from:
  changed_or_found:
  vitas_decision_needed:
  next_reader:
  not_to_claim: []
```

## Temporal Return Header

```yaml
Temporal_Return_Header:
  return_id:
  created_at:
  source_window:
  source_carrier:
  reads_from: []
  continues_from: []
  supersedes: []
  superseded_by:
  status: "Candidate / Return Packet / No Runtime"
  retention_class:
  next_reader:
  write_to:
```

## Chain Fields

```yaml
Chain_Fields:
  facts: []
  inferences: []
  to_verify: []
  candidate_actions: []
  manual_needed: []
  red_doors: []
  not_to_claim: []
```

## Essence Block

```yaml
Essence_Block:
  one_line_core:
  reusable_patterns: []
  field_specific_context: []
  red_doors_added: []
  not_to_claim_added: []
  next_memory_state:
```

## Pollution Check

```yaml
Pollution_Check:
  duplicate_of:
  conflicts_with:
  private_context_risk: false
  runtime_claim_risk: false
  approval_drift_risk: false
  fieldspace_leak_risk: false
  action:
    - "keep_current"
    - "extract_essence"
    - "replace_with_pointer"
    - "park"
    - "cold_archive"
    - "red_gate"
```

## Retention Class

```yaml
Retention_Class:
  class: "Active / Canonicalized / Superseded / Quarantined / Red_Gate"
  active_pointer:
  canonical_pointer:
  archive_pointer:
  decision_queue_pointer:
```

## Filing Block

```yaml
Filing_Block:
  file_title:
  file_name:
  version:
  source_window:
  generated_at:
  save_target:
    drive_candidate:
    github_candidate: []
  full_packet_pointer:
  essence_pointer:
  archive_pointer:
```

## Red Doors

- Return Packet != Closeout.
- Timestamp != Truth.
- Essence Extract != Full Evidence.
- Superseded != Deleted.
- Archive != Approved.
- Retention Rule != Auto Deletion.
- GitHub Candidate File != Approved Doctrine.
- Drive File != Governance Completion.

## Final Rule

Each return packet must carry time, essence, pollution check, retention class, and pointer path. QHA should read the active pointer first, not every full historical packet.