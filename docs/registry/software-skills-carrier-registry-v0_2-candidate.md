# Software / Skills Carrier Registry v0.2 Candidate

Status: Candidate / Carrier Registry Support / No Runtime / No External Writeback
Use As: classification index for available, visible, candidate, and red-door software or skill carriers
Do Not Use As: tool authorization, connector approval, company integration, runtime inventory, or access grant

## Core

Software and skills are carriers or capability surfaces. They are not authority. Each tool must be classified before QHA routes a task to it.

## Class Model

```yaml
Skill_Class:
  S0_Verified_Core:
    meaning: "already used as core carrier or template support"
    rule: "may be referenced as candidate source with return path"
  S1_Next_Probe:
    meaning: "visible or likely available, needs capability check"
    rule: "probe only with non-sensitive task"
  S2_Task_Only:
    meaning: "use only when a specific task requires it"
    rule: "no standing role"
  S3_Output_Skill:
    meaning: "can produce public-safe artifact or module"
    rule: "requires Aki public-safe check"
  S4_Meeting_Return:
    meaning: "transcription / meeting / audio return carrier"
    rule: "no private or company data unless authorized"
  S5_Red_Door:
    meaning: "high-risk or permission-sensitive capability"
    rule: "manual gate required"
  S6_Local_Sovereignty:
    meaning: "device-side or personal continuity layer"
    rule: "does not enter public core by default"
```

## Registry Row

```yaml
Software_Skill_Row:
  tool_name:
  ecosystem:
  skill_class:
  visible: false
  capability_surface: []
  read_capable: false
  write_capable: false
  write_authorized: false
  data_boundary:
  cost_boundary:
  red_doors: []
  next_probe:
  assigned_LOR:
  return_mode:
```

## Red Doors

- Skill Visible != Skill Authorized.
- Connector Available != Approved Carrier.
- Tool Capability != Permission.
- Local Skill != Company Authorization.
- Output Skill != Public Approval.
- Meeting Transcript != Consent.
- Cost Paid != Data Clearance.

## Final Rule

QHA routes only to skills with visible class, boundary, gate, and return mode.