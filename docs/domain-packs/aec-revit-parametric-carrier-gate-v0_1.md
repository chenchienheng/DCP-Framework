# AEC Revit Parametric Carrier Gate v0.1

Status: Candidate / Domain Pack Support / No Runtime / No External Writeback
Use As: candidate boundary for AI-assisted Revit parameter / drawing / BIM workflow integration
Do Not Use As: BIM source of truth, construction document, Revit production automation, company workflow approval, or professional design approval

## Core

AI coding tools can increasingly help generate scripts, add-ins, API wrappers, and parameter-aware workflows. For Revit, the important carrier is not a screenshot. The important carrier is parameterized BIM data, API actions, families, schedules, views, and model state.

This domain pack positions Revit as a Parametric BIM Carrier under XuanLing governance.

```text
Design Intent -> Parameter Schema -> Revit API / Add-in / Script -> Model Element / Family / View / Schedule -> Review -> Return Packet -> Rebuild
```

## Carrier Types

```yaml
Revit_Carriers:
  Parameter_Carrier:
    role: "type / instance parameters, shared parameters, schedules"
  Geometry_Carrier:
    role: "walls, floors, families, spaces, MEP elements"
  View_Carrier:
    role: "plans, sections, sheets, tags, annotations"
  Automation_Carrier:
    role: "C# add-in, Dynamo, pyRevit, Design Automation, scripts"
  Review_Carrier:
    role: "diff, report, issue, return packet"
```

## Gate Model

```yaml
Revit_AI_Gate:
  Source:
    - "design intent"
    - "project standard"
    - "parameter requirement"
  Carrier:
    - "Revit model"
    - "family"
    - "schedule"
    - "API script"
  Authority:
    - "project BIM lead"
    - "designer / engineer of record"
    - "company standard owner"
  Gate:
    - "sandbox model first"
    - "parameter mapping verified"
    - "no production model write without approval"
    - "review report required"
  Action:
    - "generate candidate script"
    - "create sandbox element"
    - "export report"
  Return:
    - "what changed"
    - "parameters touched"
    - "views / schedules affected"
    - "warnings"
  Rebuild:
    - "rollback"
    - "patch parameter map"
    - "human review"
```

## Red Doors

- Revit API Script != Design Approval.
- Parameter Read != Authorized Write.
- Sandbox Model != Production Model.
- Generated Family != Company Standard Family.
- View Created != Sheet Issued.
- Schedule Output != Quantity Approval.
- Beautiful Model != Constructability.
- AI-assisted BIM Change != Engineer of Record Approval.
- Tool Capability != BIM Authority.

## Relation to XuanLing

This domain pack extends carrier taxonomy from text / repo / drive / app cells into parametric BIM carriers. Revit data can become a field-specific carrier only when authority, gate, action, return, and rebuild are explicit.

## Next Candidate Files

- `docs/domain-packs/revit-parameter-carrier-schema-v0_1.md`
- `docs/templates/revit-ai-change-return-packet-v0_1.md`
- `docs/domain-packs/aec-bim-sandbox-to-production-gate-v0_1.md`
