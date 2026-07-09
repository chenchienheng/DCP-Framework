# Evidence Ledger Template v0.1

Status: Candidate / Source Evidence Ledger / No Runtime / No External Writeback / Not Approved
Use As: evidence-library intake template for official documents, event notes, screenshots, social posts, and internal observations
Do Not Use As: source approval, legal verification, company record, or final truth

## Core

Every external signal must show what the source supports, what it does not support, its evidence level, and what remains to verify. A source may support a narrow observation without supporting product availability, company approval, runtime readiness, or strategy.

## Template

```yaml
Evidence_Ledger_Record:
  evidence_id:
  source_title:
  source_type: "official_doc / official_announcement / event_note / screenshot / social_post / internal_observation / secondary_report"
  publisher_or_origin:
  source_date:
  captured_at:
  file_or_url:
  carrier:
  exact_quote_or_extract:
  page_section_or_timestamp:
  what_it_supports: []
  what_it_does_not_support: []
  evidence_level: "A_primary / B_direct / C_secondary / D_observation / E_unverified"
  authority_level:
  sensitivity:
  verification_status: "verified / partially_verified / pending / disputed"
  to_verify: []
  related_gate:
  related_build_card:
  next_reader:
  not_to_claim: []
```

## Evidence Levels

```yaml
Evidence_Levels:
  A_primary: "official primary source or first-party technical record"
  B_direct: "direct screenshot, transcript, or event material with limited scope"
  C_secondary: "reputable report or interpretation of a primary source"
  D_observation: "user or window observation without complete source record"
  E_unverified: "social claim, incomplete screenshot, or unsupported product assertion"
```

## Source-Type Boundaries

```yaml
Boundaries:
  official_doc:
    can_support: "documented capability, published policy, stated architecture"
    cannot_support: "company internal approval or local deployment"
  event_note:
    can_support: "what was presented or observed at the event"
    cannot_support: "stable product specification unless backed by official docs"
  screenshot:
    can_support: "visible interface state at capture time"
    cannot_support: "general availability, permanence, or organization approval"
  social_post:
    can_support: "community narrative, claimed experience, or wording risk"
    cannot_support: "official feature fact or company adoption basis"
  internal_observation:
    can_support: "local experiment state"
    cannot_support: "general product claim or public proof"
```

## Red Doors

- Source Exists != Claim Verified.
- Screenshot != Stable Specification.
- Event Statement != General Availability.
- Official Announcement != Internal Approval.
- Social Post != Product Documentation.
- Evidence Level != Authority Grant.
- Extract != Full Context.

## Final Rule

No external signal may be promoted beyond Candidate until its Evidence Ledger record shows source type, support scope, non-support scope, verification status, and next verification step.