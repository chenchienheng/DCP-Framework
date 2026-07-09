# Outsider-Readable Small Loop Gate v0.1

Status: Candidate / Productization Gate / No Runtime / No Public Release / No External Writeback
Use As: gate for turning deep XuanLing/CTQL architecture into one external-readable, tryable, verifiable small loop
Do Not Use As: product launch, pricing approval, public offer, commercial validation, or runtime claim

## Core

The next challenge is not to prove the whole architecture. The next challenge is to produce one small loop that an outsider can understand, try, verify, and evaluate without needing to understand XuanLing.

## Loop Requirements

```yaml
Outsider_Readable_Loop:
  problem_statement:
    required: true
    rule: "must be understandable without internal terminology"
  input:
    required: true
    rule: "must be sanitized or mock data"
  action:
    required: true
    rule: "bounded, reversible, and human-gated"
  evidence:
    required: true
    rule: "show what was actually created or tested"
  return_check:
    required: true
    rule: "show pass / pending fix / rejected criteria"
  user_value:
    required: true
    rule: "must be useful without explaining the full architecture"
  boundary:
    required: true
    rule: "state what it does not do"
```

## Candidate Loops

```yaml
Candidate_Loops:
  M365_Manifest_Loop:
    input: "filelist manifest"
    output: "classification table + evidence + return check"
  Xiaoshiguang_Three_Cards:
    input: "mock inquiry / state"
    output: "State Card + Reply Draft Card + Problem Return Card"
  GitHub_Long_Memory_Loop:
    input: "issue / markdown / label / return packet"
    output: "active pointer + summary + rebuild note"
```

## Evaluation Questions

```yaml
Evaluation:
  can_understand_without_xuanling: false
  can_try_with_mock_data: false
  evidence_visible: false
  return_check_visible: false
  red_doors_visible: false
  next_iteration_visible: false
```

## Red Doors

- External-readable != Public-approved.
- Tryable Loop != Product Launch.
- Payable Candidate != Revenue Validation.
- Mock Data != Real Operation.
- Evidence Visible != Final Approval.
- Small Loop != Small Vision.

## Final Rule

Do not ask outsiders to understand the full system first. Give them one bounded loop with input, action, evidence, return check, and next iteration.