# OCF as Dependency Cell Substrate v0.1 Candidate

Status: Candidate / Core Support / Not Doctrine / No Runtime

## Core

OCF means Open Cell Feedback. It is a candidate substrate for representing data as living dependency cells rather than static rows.

## Cell vs Row

A row stores fields. A cell carries source, local context, sovereignty, state, gates, actions, return hooks, and next cells.

```yaml
OCF_Cell_Minimum:
  source:
  local:
  sovereignty:
  current_state:
  visible_rings: []
  editable_rings: []
  dependencies: []
  blockers: []
  allowed_actions: []
  forbidden_actions: []
  generated_outputs: []
  return_hooks: []
  next_cells: []
  audit_trail:
```

## Relation to Open Core

```yaml
Open_Core_Map:
  Source: "cell.source"
  Carrier: "cell.local / current carrier"
  Authority: "cell.sovereignty"
  Gate: "blockers / allowed_actions / forbidden_actions"
  Action: "generated_outputs"
  Return: "return_hooks"
  Rebuild: "next_cells / audit_trail"
```

## Red Doors

- OCF Cell != SQL Row.
- Generated Output != Sent Action.
- Candidate Cell != Runtime State.
- Field Cell Pattern != Root Doctrine.
- Private Field Context != Core Content.
