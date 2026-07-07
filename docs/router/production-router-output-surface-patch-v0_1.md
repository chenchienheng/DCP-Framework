# Production Router Output Surface Patch v0.1

Status: Candidate / Router Patch / No Runtime / No External Writeback
Use As: output-surface rule for Qinyi / QHA / public-safe module planning
Do Not Use As: approved communication policy, public release approval, or merge approval

## Core

Not every internal reasoning step should become visible output. The production router should decide the output surface before routing work to Qinyi, Hazumi, Aki, or output modules.

## Output Surface Levels

```yaml
Output_Surface_Level:
  L0_Internal_Reasoning:
    visible: false
    rule: "do not expose by default"
  L1_Vitas_Readable:
    visible: true
    fields: ["conclusion", "basis", "risk", "next_step", "not_to_claim"]
  L2_Return_Packet:
    visible: "internal carrier"
    fields: ["facts", "inferences", "to_verify", "red_doors", "next_reader", "write_to"]
  L3_Public_Safe_Draft:
    visible: "review only"
    requires: "Aki public-safe check"
  L4_Public_Approved:
    visible: "external"
    requires: "Vitas approval"
```

## Routing Patch

```yaml
Production_Router_Output_Patch:
  before_dispatch:
    - "choose output surface"
    - "choose carrier"
    - "choose LOR"
    - "choose return mode"
  qinyi_default:
    output_surface: "L1_Vitas_Readable"
  hazumi_default:
    output_surface: "L2_Return_Packet / Build Packet"
  aki_default:
    output_surface: "L2_Return_Packet / Audit Note"
  output_repo_default:
    output_surface: "L3_Public_Safe_Draft unless Vitas approves L4"
```

## Red Doors

- Visible Output != Full Reasoning.
- Public-safe Draft != Public-approved.
- Return Packet != Displayed Reasoning.
- Qinyi Translation != Final Decision.
- Output Surface != Authority.

## Final Rule

The router should decide what level of visibility a response deserves. Most internal reasoning stays internal; visible output should be concise, bounded, and decision-aware.