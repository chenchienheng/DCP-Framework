# Issue Routing v0.1

Status: Candidate / Issue Routing / No Runtime

## Core

Issues are nodes. Route them by repo role and state.

## Row

```yaml
Issue_Row:
  issue_number:
  title:
  owner_repo:
  node_type:
  state:
  relation:
  return_to:
  next_action:
```

## Repo Targets

- DCP_Xuan-Ling_CoreTri: root, open core, red doors, repo network, issue chain.
- XLQY_Qinyi-Flow_CoreTri: Qinyi flow, CoreTri, role map, GUI flow, return pattern.
- Yiyi_Xiao-shi-guang_CUI_App: app gate, operator flow, problem return, app role.

## States

- Keep
- Supersede
- Park
- Red_Gate
- Needs_Human_Decision

## Red Doors

- Routing is not closing.
- Supersede is not deletion.
- Park is not rejection.
- Target repo is not approval.
