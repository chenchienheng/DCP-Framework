# Context-Aware Personal Decision Model Gate v0.1

Status: Candidate / Personalization Governance Gate / No Runtime / No External Writeback
Use As: QHA gate for converting user feedback into scoped, reversible, evidence-based preference updates
Do Not Use As: psychological diagnosis, permanent identity profile, autonomous recommendation authority, or universal personality rule

## Core

Personalization should model decision criteria by context, not merely remember liked or disliked items. Rejections and retentions must be scoped, evidenced, confidence-rated, and reversible.

## Gate Fields

```yaml
Personal_Decision_Gate:
  domain:
  context:
  source_feedback:
  decision_type: "retain / reject / reclassify / defer"
  extracted_reason: []
  scope:
    applies_to: []
    does_not_apply_to: []
  confidence: "explicit / high-inference / candidate / pending-trial"
  evidence: []
  external_signals_used: []
  authority:
    candidate_by:
    final_by:
  active_state: "candidate / active / superseded / archived"
  return_required: true
  next_trial:
  not_to_claim: []
```

## Required Distinctions

- Item preference vs context preference.
- Stable criterion vs temporary mood.
- Negative reason vs global ban.
- Popularity signal vs personal approval.
- Platform retrieval vs correct version.
- Back-end governance richness vs front-end cognitive load.

## Cross-Domain Use

```yaml
Domains:
  music: "tone, social safety, fatigue, popularity, version"
  procurement: "quality, maintenance, identity fit, gift or home use"
  reports: "specificity, evidence, legal basis, calculation, reader layer"
  travel: "location, quality, fatigue, family vs solo context"
  communication: "relationship, power distance, emotional load, ethical boundary"
  scheduling: "notification burden, active state, handoff, adoption"
```

## Red Doors

- Preference Record != Permanent Identity.
- One Reaction != Global Rule.
- External Popularity != User Approval.
- Tool Retrieval != Correct Object.
- Correct Object != Suitable Choice.
- Suitable Choice != User Approved.
- Generated List != Usable Delivery.
- Active Version Missing != Safe Continuity.

## Final Rule

QHA may propose a preference patch, but Vitas remains final authority. Every patch must have scope, confidence, evidence, trial, return, and supersession path.