# Carrier Manifest Schema v0.1

Status: Candidate / Manifest Schema / No Runtime / No External Writeback
Use As: schema candidate for describing carrier capabilities and limits
Do Not Use As: authorization, runtime connector spec, company approval, or access grant

## Core

A carrier manifest describes what a carrier can see, read, write, return, and what gates apply.

## Schema

```yaml
Carrier_Manifest:
  carrier_id:
  carrier_name:
  carrier_type:
  ecosystem:
  description:
  visibility:
    visible_to_qha: false
    visible_to_lor: []
  read:
    read_capable: false
    read_verified: false
    readable_objects: []
  write:
    write_capable: false
    write_authorized: false
    writable_objects: []
  data_boundary:
    allowed_data_classes: []
    forbidden_data_classes: []
  authority:
    owner:
    approver:
    manual_gate_required: true
  return:
    return_mode:
    return_packet_required: true
    default_write_to:
  red_doors: []
  status: "unknown / candidate / active / parked / red_gate"
```

## Red Doors

- Manifest != Authorization.
- Read Capable != Read Approved.
- Write Capable != Write Authorized.
- Carrier Owner != Vitas Decision by default.
- Tool Access != Data Boundary Clearance.

## Final Rule

Do not route work to a carrier until its manifest exposes data boundary, authority, gate, and return mode.