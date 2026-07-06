# Node Registry v0.1

Status: Candidate / Node Registry / GitHub Candidate File / No Runtime / No External Carrier Connection
Use As: first active node registry for the chain ecology across GPT, Google Drive, GitHub, and sidecar cloud families
Do Not Use As: approved system inventory, production integration map, subscription approval, company IT policy, or external writeback authorization

## Core

A node is not a tool. A node is a carrier-position with role, permission, memory fate, return path, and red doors.

```yaml
Node_Definition:
  required:
    - node_id
    - carrier_family
    - node_role
    - status
    - data_class
    - allowed_inputs
    - forbidden_inputs
    - outputs
    - next_reader
    - return_path
    - retention_class
    - red_doors
```

## Active Nodes

```yaml
Active_Node_Groups:
  GPT_Schedule_Core:
    nodes:
      - QHA_Daily_Dispatch
      - Qinyi_LOR
      - Hazumi_Build_Pass
      - Aki_Audit_Pass
      - XSG_Field_Return
      - CoreTri_LOR_Weekly
    role: scheduled return, dispatch, construction, audit, field return, weekly calibration
    retention_class: Active
  Google_Drive_Return_Packets:
    role: current working memory and human-readable return packets
    retention_class: Active
  GitHub_Canonical_Chain:
    role: versioned governance, repo-safe candidate files, registries, red doors, hook anchors
    retention_class: Canonicalized
  Sidecar_Signals:
    nodes:
      - Morning_Signal
      - Gmail_Hygiene_Watch
    role: external signal and G ecosystem hygiene intake
    retention_class: Essence Extract
```

## Candidate Nodes

```yaml
Candidate_Nodes:
  Box_or_Dropbox_Cold_Archive:
    role: cold archive, heavy artifact quarantine, historical deposits
    status: candidate only
    activation_gate:
      - archive volume justifies new carrier
      - retrieval path is defined
      - subscription need is verified
  OneDrive_or_iCloud_Private_Human_Base:
    role: private human-base and device-side continuity
    status: candidate only
    activation_gate:
      - private data boundary is explicit
      - not for Open Core
  M365_Company_Work_Carrier:
    role: company collaboration and process segment carrier
    status: candidate only / permission gated
    activation_gate:
      - company authorization
      - data boundary
      - defined workflow lane
  SQL_Runtime_Data_Carrier:
    role: structured query and app persistence carrier
    status: future candidate
    activation_gate:
      - OCF Cell Registry stabilized
      - field proof needs runtime persistence
  Ledger_Audit_Carrier:
    role: narrow audit proof candidate
    status: future candidate
    activation_gate:
      - strict audit requirement
      - pollution freezing risk controlled
```

## Red Doors

- Node Registry != Approved System Inventory.
- Tool != Node.
- Connector != Permission.
- Subscription != Integration.
- GitHub File != Approved Doctrine.
- Drive File != Closeout.
- Private Human Base != Open Core.
- Company Carrier != Personal Carrier.
- SQL Row != OCF Cell.
- Ledger Proof != Governance Truth.

## Registry Rule

```yaml
Registry_Rule:
  new_node_requires:
    - Carrier_Intake_Gate
    - node_role
    - data_class
    - authority
    - next_reader
    - retention_class
    - red_doors
  no_node_without_return_path: true
```
