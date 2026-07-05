# Evidence Hygiene Signal Card v0.1

Status: Candidate / Signal Evidence Hygiene / No Runtime / No External Writeback
Use As: minimum evidence boundary for daily signal absorption
Do Not Use As: fact pack, approved brief, investment advice, company strategy, or tool adoption approval

## Core

Every external signal must be separated into facts, inferences, and items to verify before it can return to XuanLing or any domain pack.

## Signal Card

```yaml
Signal_Card:
  signal_id:
  date:
  title:
  source:
  source_type: "official / primary news / secondary report / market quote / user relay / unknown"
  evidence_level: "verified / reported / to_verify / inference"
  fact_summary: []
  inference_summary: []
  to_verify: []
  affected_domains: []
  xuanling_mapping:
    Source:
    Carrier:
    Authority:
    Gate:
    Action:
    Return:
    Rebuild:
  red_doors: []
  candidate_actions: []
  manual_needed: []
  status: "Candidate Signal"
```

## Red Doors

- Reported News != Verified Fact.
- World Signal != Ground Truth.
- Market Signal != Decision.
- Inference != Approved Strategy.
- Candidate Signal != BuildReady Structure.

## Final Rule

A signal cannot become a construction input until its evidence level and return path are visible.
