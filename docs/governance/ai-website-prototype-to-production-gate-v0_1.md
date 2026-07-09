# AI Website Prototype-to-Production Gate v0.1

Status: Candidate / Generic Production Gate / No Runtime / No External Writeback
Use As: generic QHA/Hazumi/Aki gate for evaluating whether an AI-generated website prototype may progress toward controlled deployment
Do Not Use As: proof that any current product can deploy a production website, company deployment approval, security approval, or product specification

## Core

Generating or previewing a website is not the same as operating a production service. Progression requires explicit carrier, identity, data, security, maintenance, evidence, telemetry, rollback, and human ownership.

## Gate Fields

```yaml
AI_Website_Prototype_To_Production_Gate:
  purpose:
  source_evidence:
  prototype_scope:
  deployment_carrier:
  domain_owner:
  hosting_owner:
  authentication:
  authorization_model:
  data_handling:
    data_types: []
    sensitivity:
    storage_location:
    retention:
  security_gate:
    dependency_reviewed: false
    secrets_handling_reviewed: false
    vulnerability_reviewed: false
    logging_defined: false
  maintenance_owner:
  cost_boundary:
  monitoring_and_telemetry:
  backup_and_rollback:
  evidence_record:
  human_reviewer:
  return_check:
  status: "Prototype / Candidate / Conditional Pass / Approved for Controlled Deployment / Rejected / Parked"
```

## Required Distinctions

```yaml
Distinctions:
  prototype: "demonstrates a bounded interface or behavior"
  deployment: "places the build on a reachable carrier"
  operation: "maintains security, availability, cost, ownership, and change control"
  business_ready: "adds legal, privacy, content, support, and organizational responsibility"
```

## Red Doors

- Generated Site != Production Site.
- Preview != Deployment.
- Deployment != Approved Operation.
- Public URL != Security Approval.
- No-Code Interface != No Maintenance.
- Working Demo != Business Readiness.
- Platform Hosting != Ownership Transfer.
- AI Output != Human Acceptance.
- Evidence Missing != Completed.
- Telemetry Missing != Operable.
- Return Check Missing != Closed.

## Final Rule

Keep all unverified product claims outside this gate. The gate is a reusable governance pattern, not evidence that a specific tool currently provides production deployment.