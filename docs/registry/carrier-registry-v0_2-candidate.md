# Carrier Registry v0.2 Candidate

Status: Candidate / Carrier Registry / No Runtime / No External Writeback
Use As: index for known and candidate carriers across XuanLing architecture
Do Not Use As: tool authorization, company approval, data access approval, or runtime inventory

## Core

A carrier is a bounded place or surface where a signal, file, model, workflow, or action can be represented. A carrier is not authority by itself.

## Carrier Row

```yaml
Carrier_Row:
  carrier_name:
  carrier_type:
  ecosystem:
  visible: false
  schema_readable: false
  read_verified: false
  write_capable: false
  write_authorized: false
  operational_status: "unknown / candidate / active / parked / red_gate"
  allowed_data_class:
    - "public"
    - "sanitized"
    - "internal_candidate"
  forbidden_data_class:
    - "company_raw"
    - "customer_data"
    - "secrets"
    - "private_relationship_context"
  red_door: []
  next_probe:
  manual_needed:
  return_mode:
```

## Initial Carrier Types

```yaml
Carrier_Types:
  Repo_Carrier:
    examples: ["GitHub repo", "issue", "PR", "release"]
  Drive_Carrier:
    examples: ["Google Drive folder", "Google Doc", "return packet"]
  Signal_Carrier:
    examples: ["Gmail", "Outlook", "calendar event", "daily signal"]
  Identity_Index_Carrier:
    examples: ["Google Contacts", "organization index"]
  Workface_Carrier:
    examples: ["Qinyi_LOR", "Hazumi_LOR", "Aki_LOR", "XuanLing_QHA"]
  Host_Adapter_Carrier:
    examples: ["Revit", "AutoCAD", "Dynamo", "pyRevit", "Rhino", "Grasshopper", "QGIS"]
  Field_App_Carrier:
    examples: ["Xiaoshiguang CUI/GUI", "OCF Cell Registry"]
```

## Red Doors

- Carrier Visible != Carrier Authorized.
- Read Verified != Write Authorized.
- Tool Installed != Tool Approved.
- Personal Carrier != Company Carrier.
- Host Adapter != Production Write.
- Carrier Registry != Access Grant.

## Final Rule

QHA may route only to carriers with visible boundary, data class, authority, gate, and return mode.