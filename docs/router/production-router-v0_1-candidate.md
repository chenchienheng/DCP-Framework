# Production Router v0.1 Candidate

Status: Candidate / Routing Index / No Runtime / No External Writeback
Use As: task routing table from signal or request to carrier, LOR, gate, and return mode
Do Not Use As: execution approval, production routing runtime, company workflow, or merge approval

## Core

The production router determines where a task should go before any build or action starts. It separates signal, build, audit, field, and decision routes.

## Router Row

```yaml
Production_Router_Row:
  task_type:
  source:
  intake_category: "Case / Chat / Work_Context / Architecture_Build / Governance_Rule / Red_Gate / Decision_Item / Archive_Only"
  carrier:
  assigned_LOR:
  gate_required:
  output_format:
  return_mode:
  red_door: []
  manual_needed:
  next_reader:
```

## Default Routing

```yaml
Default_Routing:
  human_wording_or_pressure:
    assigned_LOR: "Qinyi_LOR"
    output_format: "human-readable return"
  bounded_build_fragment:
    assigned_LOR: "Hazumi_LOR"
    output_format: "build packet"
  drift_or_claim_audit:
    assigned_LOR: "Aki_LOR"
    output_format: "audit note"
  cross_carrier_integration:
    assigned_LOR: "XuanLing_QHA"
    output_format: "dispatch / integration return"
  private_work_case:
    assigned_LOR: "Qinyi_LOR"
    output_format: "private note / no Open Core"
  output_module_candidate:
    assigned_LOR: "Hazumi_LOR + Aki_LOR"
    output_format: "module skeleton + public-safe audit"
```

## Red Doors

- Router Assignment != Execution Approval.
- Assigned LOR != Final Authority.
- Output Format != Runtime.
- Production Router != Production System.
- Red Gate Item != Auto-Rejection.

## Final Rule

QHA routes tasks by source, carrier, authority, gate, return mode, and red-door risk before dispatching any LOR.