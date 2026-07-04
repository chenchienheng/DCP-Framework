# Cell Substrate v0.1

Status: Candidate / Core Support / No Runtime

## Core

A unit has source, carrier, authority, state, gate, return path, and rebuild rule.

## Shape

```yaml
Cell:
  source:
  carrier:
  authority:
  state:
  gates: []
  allowed: []
  blocked: []
  return_path:
  rebuild_rule:
```

## Red Doors

- Cell is not row.
- Storage is not authority.
- Candidate is not approved.
- Return is not closeout.
