# Agent Identity / Zero Trust Gate Card v0.1

Status: Candidate / Identity and Zero Trust Gate / No Runtime / No External Writeback
Use As: QHA gate for agent identity, task authority, data scope, tool access, and human responsibility
Do Not Use As: zero trust deployment, company policy, security approval, runtime permission model, or legal conclusion

## Core

Do not trust an agent, tool, workflow, or internal system by default. Each action needs identity, authority, data scope, tool scope, evidence, telemetry, and return.

## Gate Fields

```yaml
Agent_Identity_ZeroTrust_Gate:
  agent_or_tool_name:
  human_requester:
  authority_owner:
  identity_context:
    account_or_tenant:
    role:
    environment:
  data_scope:
    allowed_data:
    forbidden_data:
    sensitivity:
  tool_scope:
    allowed_tools: []
    forbidden_tools: []
  action_scope:
    allowed_action:
    forbidden_action:
    reversible: false
  evidence_required: true
  telemetry_required: true
  human_review_required: true
  return_check_required: true
```

## Zero Trust Rules

- Internal does not mean automatically trusted.
- Familiar tool does not mean authorized action.
- Approved platform does not mean all data is allowed.
- Agent identity must be visible before action.
- Every tool call must have data boundary and return path.

## Red Doors

- Agent Can Act != Agent May Act.
- Identity Visible != Authority Granted.
- Enterprise Tool != All-Data Access.
- Human-in-the-loop != Rubber Stamp.
- Zero Trust Reference != Zero Trust Deployment.
- Telemetry != Approval.

## Final Rule

If agent identity, data scope, authority, or return path is unclear, route to Red Gate or Vitas Decision Queue.