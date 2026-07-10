# Personal Decision Model & Cross-Domain Assistant Learning Report v0.1

Status: Candidate / Internal Learning / No Runtime / No External Writeback / Not Approved Doctrine
Source Case: Apple Music driving and family ambient playlist reconstruction
Use As: QHA learning material for context-aware personal decision modeling across music, procurement, documents, travel, communication, scheduling, and field systems
Do Not Use As: permanent personality profile, global preference doctrine, autonomous recommendation authority, or user identity claim

## Core

A dedicated assistant should not merely remember which items a user likes. It should learn which criteria the user applies, in which context, with what confidence, and why an item was retained, rejected, or reclassified.

## Main Insight

```yaml
Context_Aware_Personal_Decision_Model:
  learns:
    - "why an item was rejected"
    - "why the same item is acceptable in one context but not another"
    - "how popularity, quality, ethics, shared-listening comfort, and operational convenience interact"
    - "how criteria update through feedback rather than becoming permanently fixed"
```

## Failure Patterns

```yaml
Failure_Patterns:
  Classification_Without_Function:
    red_door: "Correct classification != correct user experience"
  Cleanliness_Overcorrected:
    red_door: "Lowering risk != removing vitality"
  Tool_Match_Inflation:
    red_door: "Tool Match != Semantic Match != User-Approved Match"
  Batch_Completion_Inflation:
    red_door: "Batch Completion != Usable Delivery"
```

## Preference Model Layers

```yaml
Preference_Model_Layers:
  Stable_Identity_Preferences:
    examples:
      - "not vulgar"
      - "not cheap"
      - "not excessively noisy"
      - "values quality and completeness"
      - "does not lower standards merely to fill a list"
      - "likes mainstream relevance without blindly following trends"

  Context_Preferences:
    examples:
      solo_driving: "more rhythm and exploration allowed"
      family_shared_listening: "low embarrassment, low stimulation, safe to share"
      family_ambient: "instrumental or low-semantic-load environment sound"
      night_drive: "mid-tempo, continuous, low fatigue"
      formal_work: "clear, verifiable, low emotional overstatement"

  Negative_Preference_Ledger:
    rule: "store rejection reason and scope, not only rejected item"

  Positive_Retention_Logic:
    rule: "infer why an item stays, not merely what resembles it"

  Confidence_and_Evidence:
    rule: "each criterion requires confidence, evidence, scope, and exclusions"

  Update_and_Return:
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

## Cross-Domain Rules

```yaml
Rules:
  1: "Build criteria before generating options"
  2: "Rejection reason is more valuable than rejected item"
  3: "Every preference must have context scope"
  4: "Popularity enters Candidate Pool only"
  5: "Tool results require version and semantic validation"
  6: "Front-end names must respect cognitive load"
  7: "Build one reviewable minimum unit at a time"
  8: "Superseded versions must be explicitly marked"
  9: "User trial is model calibration, not failure"
  10: "The assistant must distinguish confirmed, high-confidence inference, candidate criterion, and unverified"
```

## Cross-Domain Applications

- Procurement: sales rank and reviews are signals, not final fit.
- Documents: style preference is secondary to evidence, legal basis, calculation, and reader entry layer.
- Travel: hotel preference changes by companions, fatigue, location, and willingness to pay.
- Communication: tone depends on relationship, power distance, emotional state, and ethical boundary.
- Scheduling: artifact generation is not delivery or adoption.

## Shared Red Doors

- Tool Match != Semantic Match.
- Semantic Match != User-Approved Match.
- Popular != Suitable.
- Stable Preference != Global Ban.
- One Rejection != Permanent Personality Rule.
- Front-end Simplicity != Back-end Governance Simplicity.
- Artifact Generated != Artifact Delivered != Artifact Adopted.

## Final Rule

QHA should treat user acceptance, rejection, reclassification, and context shifts as bounded preference evidence. The model must remain scoped, confidence-rated, reversible, and returnable.