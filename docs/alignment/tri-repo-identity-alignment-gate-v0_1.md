# Tri-Repo Identity Alignment Gate v0.1

Status: Candidate / Repo Identity Alignment / No Runtime / No Rename Executed / No External Writeback
Use As: gate for aligning the actual GitHub three-repo identity before README, description, or future output outlet decisions
Do Not Use As: rename approval, public release, output repo creation, merge approval, or doctrine

## Core

The current GitHub structure is three repositories: Core, Flow, and Field. Output is not a fourth core repository. Output is only a future release outlet for public-safe modules, pending Vitas decision.

```yaml
Actual_Tri_Repo:
  Core:
    repo: "chenchienheng/DCP_Xuan-Ling_CoreTri"
    identity: "DCP / XuanLing CoreTri governance framework"
  Flow:
    repo: "chenchienheng/XLQY_Qinyi-Flow_CoreTri"
    identity: "Qinyi Flow / QHA-LOR return layer"
  Field:
    repo: "chenchienheng/Yiyi_Xiao-shi-guang-CUI-App"
    identity: "Private Xiaoshiguang CUI Guard Field"

Future_Output_Outlet:
  status: "Future / Not part of tri-repo body"
  candidate_name: "XuanLing_Output_Modules"
  role: "public-safe schema / template / sample release outlet"
```

## Correction

```yaml
Correction:
  previous_problem:
    - "internal tri-repo and future output outlet were mixed"
    - "rename ideas appeared before identity alignment"
    - "output repo could be mistaken as a fourth core repo"
  corrected_position:
    - "three repos are Core / Flow / Field"
    - "Output is a release outlet, not tri-repo body"
    - "rename is last step, not first step"
```

## Alignment Gate

```yaml
Repo_Identity_Alignment_Gate:
  check_dimensions:
    - "repo name still usable"
    - "GitHub description aligned with current role"
    - "README first screen states Status / Role / Do Not Use As"
    - "internal docs reflect QHA / One-Hub / Production Router / Output Surface changes"
    - "old content marked stale / reference / superseded"
    - "public-private boundary risk identified"
  priority:
    1: "content conformance"
    2: "README first screen"
    3: "repo description"
    4: "cross-repo links"
    5: "rename decision"
```

## Draft Descriptions

```yaml
Descriptions:
  Core: "DCP / XuanLing CoreTri governance framework for structured judgment, carrier routing, authority gates, return loops, and rebuildable interpretation layers."
  Flow: "Qinyi Flow and QHA/LOR return layer for role-separated handoffs, log cells, build candidates, and audit feedback."
  Field: "Private sanitized CUI guard field for availability, permission, maintenance, anti-error rules, and field-proof interaction patterns."
```

## Red Doors

- Output Repo != Fourth Core Repo.
- Repo Exists != Identity Aligned.
- README Exists != Current.
- File Exists != Content Conforms.
- Rename Should Be Last Step.
- Field Private Name != Public-Safe Name.

## Final Rule

Keep current repo names for now. Align content and descriptions first. Treat output only as a future public-safe release outlet.