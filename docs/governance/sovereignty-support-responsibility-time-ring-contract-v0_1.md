# Sovereignty / Support-Authority / Responsibility / Time Ring Contract v0.1

Status: Candidate / Internal Architecture Review / No Runtime / No External Writeback / Not Doctrine
Owner and Final Human Authority: Vitas

## One Core

XuanLing does not organize actors by rank. It organizes them by **who has sovereignty, who may exercise delegated authority, who is responsible for an action, who bears its cost, and where the result must return across time**.

No ring is inherently higher or lower. A ring is valid only when its authority, burden, evidence, and return are visible.

## 1. Five Rings

```yaml
Rings:
  Source_Sovereignty_Ring:
    question: "Who owns the originating intent, private context, and final meaning?"
    default_holder: "Vitas or the native human/domain owner"
    cannot_delegate:
      - final personal meaning
      - private relationship interpretation
      - company approval
      - irreversible public commitment

  Continuity_Time_Sovereignty_Ring:
    question: "What preserves continuity, sequence, expiry, supersession, and return across time?"
    holder: "Time Chain / timestamped carrier lineage"
    functions:
      - active / superseded / archive
      - deadline and expiry
      - temporal context
      - recursive return
      - rebuild order

  Support_Authority_Ring:
    question: "Who may act within a bounded delegated scope?"
    examples:
      - XuanLing_QHA coordination
      - Qinyi framing
      - Hazumi construction candidate
      - Aki audit
      - CoreTri calibration
      - Codex implementation
    rule: "Delegated authority is scoped, revocable, and non-transferable by default."

  Responsibility_Ring:
    question: "Who must produce the work, evidence, correction, maintenance, or return?"
    fields:
      - responsible_actor
      - expected_output
      - completion_evidence
      - return_deadline
      - failure_or_blocked_return

  Cost_Bearing_Ring:
    question: "Who bears the consequence if the action is wrong, late, expensive, unsafe, or abandoned?"
    cost_types:
      - decision_cost
      - execution_cost
      - review_cost
      - maintenance_cost
      - security_and_privacy_cost
      - relationship_cost
      - rollback_cost
      - opportunity_cost
```

## 2. Ring Relationship

```text
Source Sovereignty
-> delegates bounded Support Authority
-> assigns Responsibility
-> exposes Cost Bearer
-> acts under Time Sovereignty
-> produces Evidence / Telemetry
-> returns to Source / Decision / Rebuild
```

Authority without cost exposure is incomplete.
Responsibility without authority is exploitation.
Authority without return is drift.
Time without state transition is only a timestamp.

## 3. Logical Space Cell

```yaml
Sovereignty_Cell:
  cell_id:
  source:
  native_domain:
  source_sovereignty_holder:
  continuity_time:
    created_at:
    valid_until:
    review_at:
    supersedes:
    superseded_by:
  carrier:
  support_authority:
    actor:
    allowed_scope:
    forbidden_scope:
    revocation_condition:
  responsibility:
    expected_output:
    evidence_required:
    return_required:
  cost_bearer:
    actor:
    cost_types: []
  gate:
  action:
  evidence:
  telemetry:
  return_to:
  rebuild_target:
  red_doors: []
```

## 4. Current Ring Mapping

```yaml
Current_Mapping:
  Vitas:
    rings:
      - Source Sovereignty
      - final decision
      - acceptance of irreversible cost

  Time_Chain:
    rings:
      - Continuity / temporal sovereignty
      - active / superseded / archive order

  XuanLing_QHA:
    rings:
      - support authority for classification and routing
      - responsibility for chain visibility and return integration
    not:
      - final authority
      - executor of every task

  Qinyi_Workface:
    rings:
      - support authority for human-readable framing
      - responsibility for semantic and pressure-boundary clarity

  Hazumi_Workface:
    rings:
      - support authority for bounded build candidates
      - responsibility for build packet and construction evidence

  Aki_Workface:
    rings:
      - support authority for claim / permission / public-safe audit
      - responsibility for downgrade and recheck conditions

  CoreTri_Workface:
    rings:
      - support authority for structural calibration
      - responsibility for identifying broken coupling or misplaced sovereignty

  GitHub:
    rings:
      - structural carrier
      - version / reconstructability responsibility
    not:
      - sovereignty holder
      - approval authority

  Google_Drive:
    rings:
      - human review and return carrier
    not:
      - canonical rule authority

  Codex:
    rings:
      - bounded implementation support authority
      - responsibility for diff / tests / implementation return
    not:
      - architecture or merge authority

  Field_Domains:
    examples:
      - Xiaoshiguang
      - Music Personal Decision Model
      - M365 experiment
      - Social / Visual work
    rule: "Native field sovereignty stays in the field; only sanitized patterns may move toward Core."
```

## 5. Time Sovereignty Rules

- Every active item must have a temporal state: Active / Trial / Pending / Superseded / Archive / Expired.
- Old conversations may be archived without deleting lineage.
- A newer document does not supersede an older one unless the relation is explicit.
- A scheduled trigger does not create responsibility unless a receiver and return condition are named.
- A missed return becomes `Missing Return Hook`, not silent completion.
- Temporal context may change a decision without rewriting stable identity.

## 6. Red Doors

- Sovereignty != Control of Everything.
- Support Authority != Subordination.
- Responsibility != Unlimited Burden.
- Capability != Authority.
- Authority != Approval.
- Timestamp != Truth.
- Schedule != Responsibility Assignment.
- Cost Hidden != Cost Removed.
- Field Pattern != Transfer of Field Sovereignty.
- GitHub Canonical != Human Final Decision.
- QHA Coordination != Central Domination.

## 7. Review Questions

Before any action, QHA must answer:

1. Who owns the source and meaning?
2. Who may act, and within what bounded scope?
3. Who is responsible for the return?
4. Who bears the decision, execution, maintenance, and rollback costs?
5. What temporal state is active?
6. Which carrier holds the evidence?
7. What gate prevents authority drift?
8. Where does the result return?

## Final Rule

A XuanLing chain is valid not when many tools are connected, but when sovereignty, delegated authority, responsibility, cost, time, evidence, and return are simultaneously visible.