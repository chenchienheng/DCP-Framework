# Return Check Template v0.1

Status: Candidate / Return Check Template / No Runtime / No External Writeback
Use As: shared closure-check format for small build loops, M365 pilots, GitHub long memory, and field experiments
Do Not Use As: closeout by itself, approval, runtime proof, or audit final

## Core

Return Check verifies whether a loop closed. If closure criteria are missing, the work remains Pending Fix, Reference Only, or Not Closed.

## Template

```yaml
Return_Check:
  check_id:
  task_id:
  build_card:
  evidence_record:
  closure_questions: []
  answered_yes: []
  answered_no: []
  issues_found: []
  red_doors_triggered: []
  human_reviewer:
  result: "Conditional Pass / Pending Fix / Rejected / Parked"
  next_action:
  feedback_loop:
  next_reader:
  write_to:
  not_to_claim: []
```

## Default Closure Questions

- Was the bounded build card completed?
- Does evidence show what was actually created or tested?
- Was only authorized or sanitized data used?
- Is the System of Record or correct carrier visible?
- Is the User Surface clearly not Data Authority?
- Are red doors and remaining gaps listed?
- Is the next action identified?

## Red Doors

- Return Check != Closeout if gaps remain.
- Conditional Pass != Production Approval.
- Pending Fix != Failure.
- Reviewer Note != Final Authority.
- Return Check Missing != Closed.

## Final Rule

A loop closes only when its return check identifies evidence, remaining gaps, and next action.