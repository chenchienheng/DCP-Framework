# AI Claim Inflation Audit v0.1

Status: Candidate / Aki Audit Card / No Runtime / No External Writeback
Use As: audit card for downgrading inflated AI, agent, workflow, conference, vendor, and pilot claims
Do Not Use As: final rejection, legal review, company policy, public release approval, or closeout

## Core

AI claims often inflate from observation to proof, suggestion to decision, draft to completion, candidate to approval, or PoC to runtime. Aki must downgrade claims unless evidence, telemetry, authority, and return check are visible.

## Inflation Patterns

```yaml
Claim_Inflation_Patterns:
  Observation_To_Verification:
    wrong: "This was observed, therefore verified."
    correction: "Observation is a candidate signal until evidence is reviewed."

  Suggestion_To_Decision:
    wrong: "AI suggested it, therefore it is a decision."
    correction: "AI suggestion requires human authority."

  Draft_To_Completion:
    wrong: "Draft exists, therefore task is complete."
    correction: "Completion requires evidence and return check."

  Feasible_To_Landed:
    wrong: "It seems feasible, therefore it is implemented."
    correction: "Feasibility is not build completion."

  Candidate_To_Approved:
    wrong: "Candidate file exists, therefore approved."
    correction: "Approval requires explicit authority."

  PoC_To_Runtime:
    wrong: "PoC works, therefore runtime is ready."
    correction: "Runtime requires deployment gate, monitoring, ownership, rollback, and approval."
```

## Audit Fields

```yaml
AI_Claim_Audit:
  claim:
  source:
  claim_type: "observation / suggestion / draft / build / evidence / decision / approval / runtime"
  evidence_present: false
  telemetry_present: false
  authority_visible: false
  return_check_present: false
  inflated_terms: []
  corrected_status:
  red_doors: []
  next_reader:
```

## Red Doors

- Observation != Verification.
- Suggestion != Decision.
- Draft != Completed.
- Feasible != Implemented.
- Candidate != Approved.
- PoC != Runtime.
- Human-in-the-loop != Rubber Stamp.
- Evidence Record != Approval.
- Telemetry != Permission.

## Final Rule

If a claim cannot show evidence, telemetry, authority, and return check, downgrade it to Candidate / To Verify / Reference Only.