# Temporal Return Packet Retention Rule v0.1

Status: Candidate / Return Retention Rule / No Runtime / No External Writeback
Use As: timestamp, distillation, pollution control, and new-old transition rule for return packets
Do Not Use As: legal retention policy, company record policy, approved doctrine, or automated deletion rule

## Core

Every return packet should have a time lock and a retention fate. A packet without time, source, essence, contamination check, and next state becomes future pollution.

## Required Temporal Fields

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

## Essence Extraction

```yaml
Essence_Block:
  one_line_core:
  facts: []
  inferences: []
  to_verify: []
  reusable_patterns: []
  field_specific_context: []
  red_doors: []
  not_to_claim: []
```

## Pollution Control

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

## Retention Classes

```yaml
Retention_Class:
  Active:
    meaning: "current working packet"
    carrier: "Google Drive / current folder"
  Canonicalized:
    meaning: "essence has been promoted to repo-safe candidate"
    carrier: "GitHub"
  Superseded:
    meaning: "replaced by newer packet, keep pointer only"
    carrier: "Archive or cold storage"
  Quarantined:
    meaning: "contains contamination risk or private context"
    carrier: "cold archive / human-base only"
  Red_Gate:
    meaning: "must not be used until Vitas decision"
    carrier: "Decision Queue / Red Door Registry"
```

## New-Old Transition Rule

When a new packet arrives:

1. compare with existing latest packet
2. extract essence
3. update canonical pointer if needed
4. mark old packet as superseded or active reference
5. move inactive full text to archive if appropriate
6. keep only short pointer in current working layer

## Red Doors

- Newer != Better.
- Older != Invalid.
- Superseded != Deleted.
- Archive != Approved.
- Essence Extract != Full Evidence.
- Timestamp != Truth.
- Retention Rule != Auto Deletion.

## Final Rule

Return packets should behave like memory: keep the main thread active, suppress secondary noise, preserve history for special retrieval, and prevent old pollution from returning as current truth.