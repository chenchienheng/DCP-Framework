# Semantic / Ground Truth Layer Card v0.1

Status: Candidate / Semantic Grounding Card / No Runtime / No External Writeback
Use As: QHA gate for grounding AI outputs in source evidence, semantic tags, sensitivity, and human review
Do Not Use As: source-of-truth approval, company record, automated classification approval, or public release

## Core

Ground Truth is not AI confidence. A semantic layer must point to source, carrier, evidence, sensitivity, and human review before output can be used.

## Pattern

```text
Manifest -> Semantic Tag -> Sensitivity Gate -> Evidence Record -> Human Review -> Return Check
```

## Fields

```yaml
Semantic_GroundTruth_Record:
  item_id:
  source_file_or_manifest:
  source_location:
  semantic_tag:
  document_type:
  sensitivity:
  proposed_use:
  ai_summary:
  evidence_link:
  human_reviewer:
  review_status:
  return_note:
  not_to_claim: []
```

## Red Doors

- Ground Truth != AI Confidence.
- Semantic Tag != Formal Classification.
- Filelist != Source Review Completed.
- AI Summary != Company Record.
- Human Review Missing != Approved.
- Evidence Missing != Grounded.

## Final Rule

A semantic label can assist navigation, but it cannot become formal truth without source evidence and human review.