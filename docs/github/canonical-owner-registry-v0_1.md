# Canonical Owner Registry v0.1

Status: Candidate / Registry / No Runtime

## Core

Each shared concept has one canonical owner. Other repositories keep pointers or local projections.

## Registry

```yaml
Canonical_Owners:
  invariant_chain:
    owner: "DCP_Xuan-Ling_CoreTri"
    local_projection:
      XLQY_Qinyi_Flow_CoreTri: "task-flow method"
      Yiyi_Xiao-shi-guang_CUI_App: "app-flow pattern"
  red_doors:
    owner: "DCP_Xuan-Ling_CoreTri"
    local_projection:
      XLQY_Qinyi_Flow_CoreTri: "role and flow boundaries"
      Yiyi_Xiao-shi-guang_CUI_App: "app safety gates"
  coretri:
    owner: "XLQY_Qinyi-Flow_CoreTri"
    local_projection:
      DCP_Xuan-Ling_CoreTri: "context reference"
      Yiyi_Xiao-shi-guang_CUI_App: "care-centered app context"
  qinyi_task_flow:
    owner: "XLQY_Qinyi-Flow_CoreTri"
    local_projection:
      DCP_Xuan-Ling_CoreTri: "domain-pack pointer"
      Yiyi_Xiao-shi-guang_CUI_App: "operator-flow support"
  app_guard_pattern:
    owner: "Yiyi_Xiao-shi-guang_CUI_App"
    local_projection:
      DCP_Xuan-Ling_CoreTri: "abstract domain reference"
      XLQY_Qinyi-Flow_CoreTri: "task assistant example"
```

## Rules

- One canonical owner per concept.
- Other repositories use pointers or local projections.
- Local projection is not the canonical source.
- Change requests return to the canonical owner.

## Red Doors

- Duplicate copy is not canonical ownership.
- Local projection is not doctrine.
- Reference is not migration completion.
