# Carrier Registry Ecosystem Sovereignty Patch v0.1

Status: Candidate / Carrier Registry Patch / No Runtime / No External Writeback
Use As: field patch for Carrier Registry v0.2 to record ecosystem sovereignty and cross-ecosystem routing conditions
Do Not Use As: connector approval, access grant, company authorization, runtime inventory, or public release

## Core

Carrier Registry should not only say whether a carrier is visible, readable, or writable. It must also record the carrier's native ecosystem, native sovereignty, cross-ecosystem allowance, authority requirement, gate requirement, and return requirement.

## Add Fields

```yaml
Carrier_Registry_Ecosystem_Patch:
  source_ecosystem:
  native_sovereignty:
  native_carrier:
  cross_ecosystem_allowed: false
  authority_required:
  gate_required: []
  return_required:
  small_build_loop_required: false
  output_surface:
  red_door: []
```

## Meaning

```yaml
Field_Meaning:
  source_ecosystem: "where the signal or carrier originates"
  native_sovereignty: "who or what governs the carrier in its own ecosystem"
  cross_ecosystem_allowed: "whether the signal may move across ecosystems"
  authority_required: "who must decide before action"
  gate_required: "which gates must be passed"
  return_required: "what proof or return is required"
  small_build_loop_required: "whether Build Card / Evidence / Return Check is required"
```

## Examples

```yaml
Examples:
  Gmail:
    source_ecosystem: "G"
    native_carrier: "email / labels / inbox"
    cross_ecosystem_allowed: true
    gate_required: ["Signal Intake", "Privacy Boundary"]
  M365_Workflow_Surface:
    source_ecosystem: "M"
    native_carrier: "Lists / SharePoint / Teams"
    cross_ecosystem_allowed: "sanitized only"
    gate_required: ["Company Ring", "Evidence", "Return Check"]
  Apple_iCloud:
    source_ecosystem: "Private_Local"
    native_carrier: "device-side human-base"
    cross_ecosystem_allowed: "manual export only"
    gate_required: ["Private Local Sovereignty"]
```

## Red Doors

- Carrier Visible != Carrier Authorized.
- Native Carrier != Portable Data.
- Cross-Ecosystem Allowed != Writeback Approval.
- Personal Carrier != Company Carrier.
- Sanitized Pattern != Company Record.

## Final Rule

QHA must understand the ecosystem sovereignty of a carrier before routing any signal across ecosystems.