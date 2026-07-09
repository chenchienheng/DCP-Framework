# A2A / MCP Red Door Card v0.1

Status: Candidate / Red Door Card / No Runtime / No External Writeback
Use As: QHA/Aki red-door card for agent-to-agent and model-context/tool connectivity claims
Do Not Use As: protocol approval, connector approval, security approval, runtime integration, or company policy

## Core

Interoperability is not authorization. A2A-style coordination and MCP-style tool/data connection do not automatically grant authority, data permission, or company approval.

## Red Door Statements

```yaml
A2A_MCP_Red_Doors:
  A2A: "agent coordination protocol does not imply authority sharing"
  MCP: "tool or data connection does not imply data permission"
  AP2_or_payment_agent: "payment-capable agent does not imply transaction authorization"
  agent_hub: "agent marketplace or hub does not imply internal approval"
```

## Gate Questions

```yaml
Gate_Questions:
  identity: "which agent or tool is acting?"
  authority: "who authorized the action?"
  data_scope: "what data can it read?"
  write_scope: "what can it write or change?"
  audit: "what evidence and telemetry are logged?"
  rollback: "can the action be reversed?"
  responsibility: "who is accountable?"
```

## Red Doors

- A2A != Authority Sharing.
- MCP != Data Permission.
- Tool Connection != Approved Carrier.
- Payment Agent != Unlimited Payment Authorization.
- Agent Hub != Runtime Approval.
- Interoperability != Governance.

## Final Rule

Treat interoperability as a carrier possibility, not an authority grant. Route through Zero Trust and AI Action Authorization Matrix before action.