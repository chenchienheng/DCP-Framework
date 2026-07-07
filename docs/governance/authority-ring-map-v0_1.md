# Authority Ring Map v0.1

Status: Candidate / Authority Boundary Map / No Runtime / No External Writeback
Use As: authority-ring map for QHA routing, repo cleanup, output boundary, and private/work/public separation
Do Not Use As: legal policy, company policy, approved doctrine, or runtime permission model

## Core

Every signal, document, repo file, carrier, and action must be mapped to an authority ring before QHA routes or stores it.

## Rings

```yaml
Authority_Rings:
  R0_Private_Local_Sovereignty:
    examples:
      - "private relationship context"
      - "family / medical / personal device layer"
      - "Apple / iCloud human-base"
    default_storage: "not public repo; internal pointer or human-base only"

  R1_Internal_Work_Ring:
    examples:
      - "ChatGPT / QHA / LOR"
      - "Google Drive return packets"
      - "GitHub three working repos"
      - "candidate docs"
    default_storage: "Drive or internal GitHub candidate"

  R2_Fieldspace_Ring:
    examples:
      - "Xiaoshiguang field proof"
      - "sanitized OCF card specs"
      - "small-operator guard app candidates"
    default_storage: "Yiyi repo / sanitized field files"

  R3_Output_Module_Ring:
    examples:
      - "Return Packet Template"
      - "Carrier Manifest"
      - "Open Host Adapter Bridge sample"
    default_storage: "future output repo candidate only after Vitas approval"

  R4_Company_Ring:
    examples:
      - "company data"
      - "Company_M365"
      - "formal BIM / CAD model"
      - "work role context"
    default_storage: "not QHA public chain; private work note or company-authorized carrier only"

  R5_Red_Gate_Ring:
    examples:
      - "secrets"
      - "credentials"
      - "customer data"
      - "payment records"
      - "external writeback"
      - "runtime deployment"
    default_storage: "hold / decision queue / no write by default"
```

## Routing Rule

```yaml
Ring_Routing:
  if_private: "do not put into public repo"
  if_internal_candidate: "may enter DCP / XLQY / Yiyi according to role"
  if_fieldspace: "Yiyi only, sanitized"
  if_output_module: "future output repo only after public-safe and Vitas approval"
  if_company: "do not route into personal cloud chain except sanitized abstraction"
  if_red_gate: "manual Vitas decision required"
```

## Red Doors

- Private Ring != Public Proof.
- Internal Candidate != Public Release.
- Fieldspace != Open Core.
- Company Context != Architecture Build.
- Output Candidate != Output Approval.
- Red Gate != Auto-Rejection.

## Final Rule

QHA must classify authority ring before carrier routing. If the ring is unclear, route to Decision Queue or park.