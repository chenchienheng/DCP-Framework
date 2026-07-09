# Tri-Repo Cycle Proof Check v0.1

Status: Candidate / Cycle Proof Check / No Runtime / No External Writeback
Use As: QHA check for proving whether Core -> Flow -> Field -> Flow -> Core actually circulates
Do Not Use As: runtime proof, merge approval, public release, or closeout

## Core

A tri-repo ecology is only proven when a rule can move from Core to Flow, become a bounded field proof, return through Flow, and re-enter Core only as a sanitized generalized pattern.

## Cycle

```yaml
Tri_Repo_Cycle:
  Step_1_Core_Gate:
    source: "DCP governance / router / small build loop gate"
    output: "bounded instruction or gate"

  Step_2_Flow_Dispatch:
    source: "XLQY dispatch / build packet / audit request"
    output: "field proof card request"

  Step_3_Field_Proof:
    source: "Yiyi state / reply / problem card"
    output: "sanitized evidence or problem return"

  Step_4_Flow_Return:
    source: "XLQY field return packet"
    output: "audit note / generalized pattern candidate"

  Step_5_Core_Rebuild:
    source: "DCP red door / registry / router patch"
    output: "updated rule or active pointer"
```

## Proof Fields

```yaml
Cycle_Proof_Row:
  cycle_id:
  core_source:
  flow_dispatch:
  field_card:
  field_return:
  flow_audit:
  core_rebuild_target:
  evidence_present: false
  return_check_present: false
  private_context_removed: false
  red_doors: []
  result: "Not Started / Partial / Conditional Pass / Returned / Parked"
```

## First Candidate Cycle

```yaml
First_Candidate_Cycle:
  cycle_id: "TRI-CYCLE-001"
  core_source: "DCP/docs/governance/small-build-loop-gate-v0_1.md"
  flow_dispatch: "XLQY/docs/returns/field-return-packet-template-v0_1.md"
  field_card: "Yiyi/docs/ui/state-card-template-v0_1.md"
  field_return: "Yiyi/docs/ui/problem-return-card-template-v0_1.md"
  core_rebuild_target: "DCP/docs/alignment/tri-repo-linkage-index-v0_1.md"
```

## Red Doors

- Link Exists != Cycle Completed.
- Field Card Exists != Field Proof Completed.
- Return Packet Exists != Return Check Passed.
- Generalized Pattern != Root Doctrine.
- Cycle Proof != Runtime.

## Final Rule

QHA should call the tri-repo cycle real only after evidence and return check exist for at least one complete Core -> Flow -> Field -> Flow -> Core loop.