# PoC to Runtime Gate Checklist v0.2

Status: Candidate / Runtime Gate Checklist / No Runtime / No External Writeback
Use As: QHA/Aki checklist for preventing proof-of-concept, pilot, or demo work from being misread as runtime readiness
Do Not Use As: production approval, deployment approval, company policy, legal review, or merge approval

## Core

A PoC proves a narrow condition. It does not prove operational readiness. Runtime requires authority, data boundary, telemetry, monitoring, rollback, ownership, security, and return checks.

## Gate Checklist

```yaml
PoC_To_Runtime_Gate:
  scope_defined: false
  production_data_allowed: false
  authority_owner_named: false
  data_boundary_defined: false
  security_review_done: false
  telemetry_defined: false
  evidence_record_complete: false
  return_check_complete: false
  human_reviewer_named: false
  rollback_plan_defined: false
  maintenance_owner_named: false
  failure_mode_reviewed: false
  cost_boundary_defined: false
  external_writeback_reviewed: false
  approval_status: "not_approved / candidate / conditional_pass / approved"
```

## Required Before Runtime Claim

- Approved authority owner.
- Data boundary and sensitivity scope.
- Evidence Record.
- Telemetry plan.
- Return Check.
- Rollback / stop path.
- Maintenance owner.
- Security and permission review.

## Red Doors

- PoC != Runtime.
- Demo != Deployment.
- Human Review != Approval.
- Evidence Missing != Completed.
- Telemetry Missing != Traceable.
- Approved Tool != Approved Data Scope.
- Runtime Claim Requires Explicit Authority.

## Final Rule

Unless all required runtime gates are visible and approved, QHA must keep the work as PoC / Candidate / Conditional Pass, not Runtime.