# BIM / CAD Open Host Bridge v0.1

Status: Candidate / Domain Pack Support / No Runtime / No External Writeback
Use As: public-safe candidate pattern for AI action packet to local host adapter to return packet
Do Not Use As: Revit plugin approval, CAD production automation, company model access, issued drawing workflow, or professional design approval

## Core

The bridge is not one product or one plugin. It is a carrier pattern:

```text
GitHub Release / Action Packet
-> Local Host Adapter
-> Host API / plugin / script
-> Human Gate
-> Return Packet
```

## Possible Hosts

- Revit
- AutoCAD
- Dynamo
- pyRevit
- Rhino
- Grasshopper
- Navisworks
- Excel
- PDF
- QGIS

## Host Adapter Gate

```yaml
Open_Host_Adapter_Gate:
  input:
    - "Action Packet"
    - "sample or sandbox file"
  authority:
    - "human operator"
    - "domain professional"
  allowed_first_phase:
    - "mock data"
    - "sample file"
    - "sandbox model"
    - "read / report"
    - "candidate script"
  forbidden_first_phase:
    - "production model write"
    - "company central model"
    - "issued drawing"
    - "quantity approval"
    - "external writeback"
```

## Return Packet

```yaml
Host_Bridge_Return:
  host:
  action_packet_id:
  file_context: "mock / sample / sandbox"
  actions_attempted: []
  actions_completed: []
  parameters_touched: []
  warnings: []
  manual_review_needed: []
  rollback_notes:
  not_to_claim: []
```

## Red Doors

- Host Adapter Bridge != Production Plugin.
- Sample File != Company Model.
- Action Packet != Authorized Write.
- Script Generated != Design Approval.
- View Created != Sheet Issued.
- Return Packet != Professional Approval.

## Final Rule

Bridge patterns can be public-safe only with mock/sample data and explicit human gate. Real project files remain outside this phase.