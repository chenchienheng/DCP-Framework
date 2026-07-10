# Context-Aware Personal Decision Model Card v0.1

Status: Candidate / Personal Decision Governance Card / No Runtime / No External Writeback / Not Approved Doctrine
Use As: QHA model for scoped preference learning across music, procurement, documents, travel, schedules, and interpersonal communication
Do Not Use As: psychological diagnosis, permanent personality profile, autonomous recommendation authority, or identity lock

## Core

Personalization should model decision criteria under context, not merely remember liked or disliked items.

## Record Structure

```yaml
Personal_Decision_Record:
  user_id:
  domain:
  context:
  item_or_option:
  signal_source:
  decision: "retain / reject / reclassify / trial / park"
  reason:
  criterion_type: "stable / contextual / negative / positive / version / usability"
  scope:
  allowed_elsewhere:
  confidence: "low / medium / high"
  evidence:
  external_popularity_signal:
  tool_match_status:
  semantic_match_status:
  user_approved_status:
  version_gate:
  return_signal:
  next_review:
```

## Decision Layers

```yaml
Decision_Layers:
  Stable_Criteria:
    rule: "change slowly and require repeated evidence"
  Context_Criteria:
    rule: "apply only to named situations"
  Rejection_Ledger:
    rule: "record why, where, and whether rejection is global"
  Retention_Logic:
    rule: "record why retained and what value it delivered"
  Confidence:
    rule: "separate confirmed preference from inference"
  Update_Return:
    rule: "trial feedback updates the model through review, not automatic overwrite"
```

## Front-End / Back-End Rule

```yaml
Interface_Rule:
  backend:
    may_hold:
      - "version"
      - "source"
      - "confidence"
      - "evidence"
      - "scope"
      - "superseded status"
  frontend:
    should_show:
      - "short recognizable name"
      - "current status"
      - "next useful action"
```

## Red Doors

- Preference != Identity.
- Rejection != Global Ban.
- Popularity != Suitability.
- Tool Match != Semantic Match.
- Semantic Match != User Approval.
- One Trial != Permanent Rule.
- Personalization != Manipulation.
- Recommendation != Authority.
- Front-end Simplicity != Missing Governance.

## Final Rule

The assistant may propose a preference patch, but only the user can confirm, reject, narrow, or retire it.