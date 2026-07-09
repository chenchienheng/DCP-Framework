# Live Intake Source Routing Gate v0.1

Status: Candidate / Source Routing Gate / No Runtime / No External Writeback / Not Doctrine
Use As: QHA gate for routing Vitas_LiveIntake material into the correct workface, carrier, decision queue, or archive
Do Not Use As: scheduled return proof, Qinyi_LOR identity, runtime automation, GitHub/Drive writeback proof, or Vitas decision replacement

## Core

Live intake is source material. It can become a candidate packet, red-door patch, build fragment, schedule correction, field reframing, or decision item only after QHA classification.

## Gate

```yaml
Live_Intake_Source_Gate:
  source_window: "Vitas_LiveIntake"
  source_type:
    - "raw thought"
    - "manual correction"
    - "rejection /退件"
    - "candidate handoff"
    - "field reframing"
    - "schedule patch draft"
    - "red-door patch"
    - "buildable fragment"
  source_packaged: false
  authority: "Vitas retains sovereignty"
  carrier_candidate:
    - "XLQY return / intake file"
    - "DCP governance patch"
    - "Yiyi field packet"
    - "Drive return packet"
    - "Decision Queue"
  required_gate:
    - "Signal Intake"
    - "Authority Ring"
    - "Output Surface"
  return_required:
    - "QHA return note"
    - "next_reader assignment"
    - "manual_needed if decision gate exists"
```

## Classification Matrix

```yaml
Classification:
  Chat_Context:
    action: "keep context / no dispatch"
  Human_Readable_Need:
    route_to: "Qinyi_LOR"
  Buildable_Fragment:
    route_to: "Hazumi_LOR after QHA gate"
  Red_Door_or_Drift:
    route_to: "Aki_LOR"
  Core_Structure_Drift:
    route_to: "CoreTri_LOR"
  Field_Reframing:
    route_to: "Xiaoshiguang_Field"
  Approval_or_Writeback:
    route_to: "Vitas Decision Queue"
```

## Required Return Additions

```yaml
Required_Return_Additions:
  live_intake_source:
    source_window:
    intake_type:
    packaged:
    requires_qinyi_lor_read:
    requires_hazumi_build:
    requires_aki_audit:
    requires_coretri_check:
    requires_vitas_decision:
```

## Red Doors

- Source Intake != Scheduled Return.
- Raw Thought != Candidate Action.
- Manual Correction != Doctrine.
- Conversation Output != Carrier Writeback.
- Vitas Live Signal != Approval Unless Explicit.
- Dispatch Candidate != ACK.
- Live Intake != Closeout.

## Final Rule

QHA should not ignore Vitas_LiveIntake and should not over-promote it. Classify, route, and record only what is packaged or decision-relevant.