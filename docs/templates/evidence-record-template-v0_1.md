# Evidence Record Template v0.1

Status: Candidate / Evidence Template / No Runtime / No External Writeback
Use As: shared evidence record format for small build loops, M365 pilots, GitHub long memory, and field experiments
Do Not Use As: approval, closeout, audit final, company record, or public proof by default

## Core

Evidence Record converts "AI said it was done" into a verifiable record of what was actually created, tested, reviewed, and still missing.

## Template

```yaml
Evidence_Record:
  task_id:
  source:
  source_version:
  build_card:
  carrier:
  action_taken:
  ai_tool_used:
  instruction_summary:
  output_file_or_location:
  evidence_items:
    - "screenshot"
    - "file path"
    - "list row"
    - "commit sha"
    - "test record"
  human_reviewer:
  review_status: "Draft / AI Generated / Human Reviewed / Correction Required / Approved for Internal Use / Approved for External Use / Rejected / Archived"
  correction_needed:
  approval_status:
  date:
  return_note:
  next_reader:
  not_to_claim: []
```

## Minimum Evidence Requirements

- What was built or changed.
- Where it exists.
- Who reviewed it or who must review it.
- Whether real data was used.
- Whether external writeback occurred.
- What remains incomplete.

## Red Doors

- Evidence Record != Approval.
- Screenshot != Governance Completion.
- Commit SHA != Merge Approval.
- AI Generated != Human Reviewed.
- Human Reviewed != Approved for External Use.
- Evidence Missing != Completed.

## Final Rule

No Evidence Record means the work remains Not Completed or Reference Only.