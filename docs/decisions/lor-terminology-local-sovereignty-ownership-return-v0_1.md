# LOR Terminology Decision Note v0.1

Status: Candidate / Terminology Decision Note / Needs Vitas Decision / No Runtime / No External Writeback
Purpose: prevent silent semantic overwrite between Local / Sovereignty / Return and Local / Ownership / Return

## Core

Aki proposes that LOR be standardized as Local / Ownership / Return, with sovereignty, authority, and accountability placed inside Ownership. Existing XuanLing usage has often used Local / Sovereignty / Return. This difference must not be silently overwritten.

## Current Meanings

```yaml
Option_A:
  name: "Local / Sovereignty / Return"
  strengths:
    - "preserves the original language of local field, sovereignty, and return"
    - "emphasizes that data and action remain under the rightful field or human authority"
  risk:
    - "sovereignty may not explicitly include operational ownership and accountability"

Option_B:
  name: "Local / Ownership / Return"
  strengths:
    - "Ownership can contain sovereignty, authority, accountability, and maintenance responsibility"
    - "more operationally legible in enterprise and implementation contexts"
  risk:
    - "may narrow or alter the original sovereignty meaning if treated as replacement"

Option_C:
  name: "Local / Ownership-Sovereignty / Return"
  strengths:
    - "preserves both original sovereignty and operational ownership"
    - "can distinguish philosophical core from implementation language"
  risk:
    - "heavier terminology"
```

## Recommended Interim Rule

```yaml
Interim:
  canonical_core_semantics: "Local / Sovereignty / Return"
  operational_translation: "Local / Ownership / Return"
  ownership_includes:
    - "sovereignty"
    - "authority"
    - "accountability"
    - "maintenance responsibility"
  status: "Candidate dual-language mapping until Vitas decides"
```

## Red Doors

- Translation != Semantic Replacement.
- Enterprise Language != Core Doctrine.
- Ownership != Possession of People or Private Context.
- Sovereignty != Unlimited Authority.
- Terminology Patch != Approved Doctrine.

## Vitas Decision Needed

Choose one:

1. Keep LOR = Local / Sovereignty / Return everywhere.
2. Change LOR = Local / Ownership / Return everywhere.
3. Use dual mapping: core = Sovereignty; operational/enterprise = Ownership.

## Final Rule

Until Vitas decides, QHA must preserve the existing sovereignty meaning and may use Ownership only as an operational translation, not as a silent replacement.