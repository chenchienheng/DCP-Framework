# XuanLing QHA / LOR Circulation Work Contract v0.2 Candidate

Status: Candidate / Internal Circulation Work Contract / No Runtime / No External Writeback / Not Approved Doctrine
Owner: Vitas
Primary Reader: XuanLing_QHA
Next Readers: Qinyi_LOR, Hazumi_LOR, Aki_LOR, CoreTri_LOR, Xiaoshiguang_Field, CTQL_Experiment
Supersedes: v0.1 schedule-only or passive-hub drafts when explicitly referenced by QHA / Vitas

## Core

QHA and LOR are not one-way reporting lines. QHA must actively classify, dispatch, integrate, and request return. LOR workfaces must read carrier pointers, return structured packets, and avoid acting beyond authority.

The circulation chain is:

```text
Signal / Case / Build / Field / Governance
-> QHA Signal Intake
-> Carrier / Authority / Gate routing
-> Qinyi / Hazumi / Aki / CoreTri / Field workface when assigned
-> Evidence / Telemetry / Return Packet
-> Active Pointer / Decision Queue / Rebuild
-> Vitas decision when authority is required
```

## Roles

```yaml
XuanLing_QHA:
  role:
    - "Signal Intake Gate"
    - "Carrier Router"
    - "Return Integrator"
    - "Red Door Escalator"
    - "Decision Queue Preparer"
  must_do:
    - "read active pointers before full history"
    - "classify source / carrier / authority / gate"
    - "list candidate next_reader"
    - "do not simulate ACK"
    - "ask Vitas only at decision gates"

Qinyi_LOR:
  role:
    - "human-readable framing"
    - "pressure and authority boundary"
    - "output surface control"
  must_not:
    - "not final authority"
    - "not construction executor"

Hazumi_LOR:
  role:
    - "bounded build card"
    - "runbook / schema / repo skeleton candidate"
  must_not:
    - "not runtime"
    - "not merge approval"
    - "not company data handler unless authorized"

Aki_LOR:
  role:
    - "red-door audit"
    - "claim drift check"
    - "public-safe review"
  must_not:
    - "not closeout"
    - "not Vitas final decision"

CoreTri_LOR:
  role:
    - "weekly tri-coupling / LOR calibration"
    - "checks drift in Body/Mind/Spirit, Knowing/Action/Responsibility, Care/Boundary/Independence"
  must_not:
    - "not QHA replacement"
    - "not G ecosystem total audit"
    - "not raw thread reader"

Xiaoshiguang_Field:
  role:
    - "field proof"
    - "State Card / Reply Draft Card / Problem Return Card"
  must_not:
    - "not runtime app"
    - "not real customer data handler"
```

## Return Requirements

Every return should contain:

```yaml
Return_Required_Fields:
  - one_line_summary_zh
  - reads_from
  - continues_from
  - facts
  - inferences
  - to_verify
  - candidate_actions
  - manual_needed
  - next_reader
  - write_to
  - red_doors
  - not_to_claim
  - evidence_if_any
  - telemetry_if_any
```

## One-Hub Rule

```yaml
One_Hub_Mode:
  daily_primary: "QHA Daily Hub"
  weekly_primary: "QHA Weekly Hub"
  role_windows: "manual branch expansion or QHA assigned only"
  if_vitas_unread_previous_hub: "Backlog_Not_Expanded"
  no_long_report_by_default: true
```

## Carrier Memory Rule

```yaml
Carrier_Memory:
  GitHub: "versioned candidate carrier / registry / router / templates / proofs"
  Drive: "human-readable return layer / decision queue / archive"
  ChatGPT: "signal intake and reasoning surface"
  Active_Pointer: "current reading layer"
  Archive: "lineage and cold memory"
```

## Evidence / Telemetry Rule

```yaml
Completion_Rule:
  no_build_card: "Reference Only"
  no_evidence_record: "Not Completed"
  no_telemetry: "Not Traceable"
  no_return_check: "Not Closed"
  no_feedback_loop: "Not Rebuildable"
```

## Red Doors

- QHA != Central Blocking Node.
- LOR != Passive Subordinate.
- Next Reader != ACK.
- Schedule != Governance.
- Return Packet != Closeout.
- Candidate != Approved.
- Build Packet != Runtime.
- Audit Note != Closeout.
- GitHub File != Merge Approval.
- Drive File != Closeout.
- Tool Available != Company Approved.
- Web Accessible != Approved Use.
- A2A != Authority Sharing.
- MCP != Data Permission.
- Telemetry != Approval.
- Human-in-the-loop != Rubber Stamp.
- Field Gift != Product.
- Private Context != Open Core.

## Decision Gates

```yaml
Vitas_Decision_Required_When:
  - "promote Candidate to Approved"
  - "merge / PR approval"
  - "runtime or production claim"
  - "public release or output outlet creation"
  - "repo rename"
  - "company data or company carrier"
  - "real customer data or field operation"
  - "external writeback"
```

## Current Known Repairs

```yaml
Repairs:
  Drive_Aki_Carrier:
    current_name: "Aki_Return_Audit"
    status: "safe-name candidate"
    decision_needed: "Vitas accept or choose alternative"
  CoreTri_Return:
    latest_packet: "docs/returns/coretri-lor-window-return-to-xuanling-qha-2026-07-08-v0_1.md"
  CTQL_v0_5:
    route: "internal learning / evidence library / not company submission"
```

## Final Rule

QHA should operate through active pointers, return packets, evidence, telemetry, and decision queues. The chain is alive only when it can classify, dispatch, return, verify, and rebuild without Vitas manually carrying every full context block.