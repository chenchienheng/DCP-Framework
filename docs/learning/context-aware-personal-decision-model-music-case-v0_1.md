# Context-Aware Personal Decision Model｜Music Case v0.1

Status: Candidate / Internal Learning / No Runtime / No External Writeback / Not Approved Doctrine
Source Case: Apple Music driving and family-soothing playlist reconstruction
Use As: QHA learning material for context-aware personal judgment, rejection reasoning, scoped preference, and cross-domain transfer
Do Not Use As: global user personality doctrine, permanent preference lock, automated recommendation approval, or Apple Music runtime spec

## Core

A personal assistant should not merely remember which items a user likes. It should learn which criteria the user applies in different contexts, why an item was accepted or rejected, how confident that judgment is, and whether the rule is local or general.

## Main Learning

```yaml
Personalization:
  not_only:
    - "click history"
    - "play count"
    - "favorites"
    - "skip behavior"
  must_include:
    - "rejection reason"
    - "context scope"
    - "retention logic"
    - "confidence"
    - "evidence"
    - "update and return"
```

## Failure Modes

```yaml
Failure_Modes:
  classification_complete_but_use_incomplete:
    rule: "Classification correctness does not imply context usability."

  risk_reduction_becomes_lifeless:
    rule: "Clean does not mean obscure, old-fashioned, or emotionally flat."

  tool_match_becomes_semantic_match:
    rule: "Tool Match != Semantic Match != User-Approved Match."

  batch_completion_becomes_usable_delivery:
    rule: "Batch Completion != Usable Delivery."
```

## Six-Layer Model

```yaml
Personal_Decision_Model:
  Stable_Identity_Preferences:
    examples:
      - "not vulgar"
      - "not cheap"
      - "not excessively noisy"
      - "contemporary but not trend-blind"

  Context_Preferences:
    examples:
      solo_driving: "more rhythm and exploration allowed"
      family_driving: "low embarrassment, low stimulation"
      home_soothing: "low semantic load, ambient, low dynamic variation"
      formal_work: "clear, grounded, verifiable"

  Negative_Preference_Ledger:
    fields:
      - item
      - rejected_from
      - reason
      - allowed_context
      - global_ban

  Positive_Retention_Logic:
    fields:
      - retained_item
      - retained_because
      - reusable_features

  Confidence_And_Evidence:
    fields:
      - criterion
      - confidence
      - evidence
      - scope
      - not_applied_to

  Update_And_Return:
    chain:
      - Source
      - User Feedback
      - Reason Extraction
      - Scope Judgment
      - Preference Patch
      - Candidate Rebuild
      - Tool Verification
      - User Trial
      - Return
      - Active Model Update
```

## Cross-Domain Transfer

```yaml
Transfer:
  procurement: "hot-selling / price / rating are signals, not final choice"
  work_documents: "format preference must be explained by evidence, precision, and audience need"
  travel: "hotel choice depends on context, companions, fatigue, and value threshold"
  interpersonal_communication: "tone depends on relationship, power distance, emotion, and ethical boundary"
  schedules: "artifact generation is not delivery or adoption"
```

## Red Doors

- Item Rejected != Global Ban.
- One Reaction != Permanent Personality Rule.
- Popularity Signal != Personal Approval.
- Tool Match != Suitable Choice.
- Front-end Simplicity != Back-end Governance Loss.
- Artifact Generated != Artifact Delivered != Artifact Adopted.

## Final Rule

QHA should learn the user's reasons, scope, and confidence—not only their choices. Preference must remain contextual, evidence-based, revisable, and returnable.