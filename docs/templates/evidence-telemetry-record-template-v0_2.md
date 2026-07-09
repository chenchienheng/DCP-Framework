# Evidence + Telemetry Record Template v0.2

Status: Candidate / Evidence and Telemetry Template / No Runtime / No External Writeback
Use As: shared record format for result evidence and process trace in small build loops, M365 pilots, GitHub long memory, and field experiments
Do Not Use As: approval, closeout, audit final, company record, or public proof by default

## Core

Evidence shows what was produced. Telemetry shows how the work happened. Both are needed before a work loop can be called traceable.

## Template

```yaml
Evidence_Telemetry_Record:
  task_id:
  source:
  source_version:
  build_card:
  carrier:
  authority_gate:
  action_taken:
  ai_tool_used:
  instruction_summary:
  data_used:
    data_class:
    real_data_used: false
    sanitized_or_mock: true
  output_file_or_location:
  evidence_items:
    - "screenshot"
    - "file path"
    - "list row"
    - "commit sha"
    - "test record"
  telemetry:
    actor:
    tool_chain: []
    model_or_agent_if_any:
    connector_used: []
    runtime_location:
    cost_or_token_note:
    error_or_warning: []
    rollback_possible:
  human_reviewer:
  review_status: "Draft / AI Generated / Human Reviewed / Correction Required / Approved for Internal Use / Approved for External Use / Rejected / Archived"
  correction_needed:
  approval_status:
  date:
  return_note:
  next_reader:
  not_to_claim: []
```

## Evidence vs Telemetry

```yaml
Evidence:
  question: "What exists as proof of result?"
Telemetry:
  question: "What happened during the process, with which tool, data, actor, and gate?"
```

## Red Doors

- Evidence Record != Approval.
- Telemetry != Approval.
- Observability != Permission.
- Log Exists != Governance.
- AI Generated != Human Reviewed.
- Human Reviewed != Approved for External Use.
- Evidence Missing != Completed.
- Telemetry Missing != Traceable.

## Final Rule

A loop with output but no telemetry is not traceable. A loop with telemetry but no evidence is not completed.