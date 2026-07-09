# Shadow Agent Risk Audit Card v0.1

Status: Candidate / Aki Audit Card / No Runtime / No External Writeback
Use As: audit card for detecting unapproved agentic workflows, unsanctioned web tools, and hidden writeback risk
Do Not Use As: disciplinary policy, security final, company policy, or automated enforcement

## Core

A shadow agent risk appears when a tool or workflow can act across data, tools, or systems without visible authority, telemetry, human review, and return check.

## Audit Questions

```yaml
Shadow_Agent_Audit:
  tool_or_agent:
  who_started_it:
  account_or_tenant:
  data_accessed:
  tools_called:
  background_runtime: false
  external_writeback_possible: false
  human_review_visible: false
  evidence_visible: false
  telemetry_visible: false
  rollback_possible: false
  authority_owner:
  risk_level: "low / medium / high / red_gate"
```

## Common Risks

- Web tool used with company data outside approved tenant.
- Agent running in background without clear owner.
- File upload used as data transfer without review.
- Mobile confirmation mistaken for full approval chain.
- Community claim treated as company permission.
- Tool integration used before data boundary is known.

## Red Doors

- Can Run != Authorized Runtime.
- Tool Available != Company Approved.
- Background Task != Governed Workflow.
- Upload Feature != Data Permission.
- Human Click != Human Accountability.
- Telemetry Missing != Safe.

## Final Rule

If authority, data scope, telemetry, and return are not visible, classify as Shadow Agent Risk and route to Aki / Vitas decision.