# Active Pointer Rows 2026-07-07 v0.1

Status: Candidate / Active Pointer Seed / No Runtime / No External Writeback
Use As: first pointer seed for QHA chain experiment and output engineering candidates
Do Not Use As: approved truth, release approval, merge approval, or closeout

## Core

QHA should read active pointer rows before reading full historical packets. These rows seed the current experiment queue.

## Rows

```yaml
Active_Pointer_Rows:
  - pointer_id: "CR-001"
    title: "Carrier Registry v0.2 Candidate"
    current_status: "Active"
    canonical_repo_pointer: "DCP/docs/registry/carrier-registry-v0_2-candidate.md"
    next_reader: ["Qinyi_LOR", "Aki_LOR"]
    red_doors: ["Carrier Visible != Carrier Authorized", "Read Verified != Write Authorized"]

  - pointer_id: "PR-001"
    title: "Production Router v0.1 Candidate"
    current_status: "Active"
    canonical_repo_pointer: "DCP/docs/router/production-router-v0_1-candidate.md"
    next_reader: ["Qinyi_LOR", "XuanLing_QHA"]
    red_doors: ["Router Assignment != Execution Approval"]

  - pointer_id: "OM-001"
    title: "Output Repo Skeleton v0.1 Candidate"
    current_status: "Active"
    canonical_repo_pointer: "DCP/docs/output/output-repo-skeleton-v0_1-candidate.md"
    next_reader: ["Hazumi_LOR", "Aki_LOR"]
    red_doors: ["Output Repo Skeleton != Repo Created", "Public-safe != Public-approved"]

  - pointer_id: "BIM-001"
    title: "BIM / CAD Open Host Bridge v0.1 Candidate"
    current_status: "Active"
    canonical_repo_pointer: "DCP/docs/domain-packs/bim-cad-open-host-bridge-v0_1.md"
    next_reader: ["Hazumi_LOR", "Aki_LOR", "Ecosystem_Architecture_Experiment"]
    red_doors: ["Host Adapter Bridge != Production Plugin", "Sample File != Company Model"]

  - pointer_id: "ORG-001"
    title: "Origin Context Boundary"
    current_status: "Internal Only"
    canonical_repo_pointer: "No public detail pointer"
    next_reader: ["Qinyi_LOR", "Aki_LOR"]
    red_doors: ["Internal Context != Public Proof", "Private Field Context != Output Repo"]

  - pointer_id: "SW-001"
    title: "Software / Skills Carrier Registry v0.2 Candidate"
    current_status: "Active"
    canonical_repo_pointer: "DCP/docs/registry/software-skills-carrier-registry-v0_2-candidate.md"
    next_reader: ["Qinyi_LOR", "Aki_LOR", "Ecosystem_Architecture_Experiment"]
    red_doors: ["Skill Visible != Skill Authorized", "Connector Available != Approved Carrier"]
```

## Final Rule

Active pointer rows guide reading. They do not approve action, release, merge, runtime, or publication.