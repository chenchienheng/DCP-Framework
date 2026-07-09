# AI Action Authorization Matrix v0.1

Status: Candidate / Authorization Matrix / No Runtime / No External Writeback
Use As: shared gate for AI-assisted actions across M365, GitHub, documents, field experiments, and agent simulations
Do Not Use As: company policy, legal approval, runtime permission model, or automatic execution rule

## Core

AI ability does not equal AI authority. Each action must be classified by reversibility, impact, audience, data sensitivity, and approval need before any execution.

## Matrix

```yaml
AI_Action_Authorization_Matrix:
  Low_Risk:
    conditions:
      - "internal only"
      - "reversible"
      - "low impact"
      - "sanitized or test data"
    allowed_ai_role:
      - "organize"
      - "draft"
      - "classify"
      - "suggest"
    human_gate: "light review"
    examples:
      - "draft internal index"
      - "classify file manifest"
      - "summarize sanitized notes"

  Medium_Risk:
    conditions:
      - "internal high impact"
      - "external-facing draft but reversible"
      - "permission or workflow implication"
    allowed_ai_role:
      - "assist"
      - "prepare candidate"
      - "flag risk"
    human_gate: "required review before use"
    examples:
      - "technical brief draft"
      - "workflow list design"
      - "GitHub candidate doc"

  High_Risk:
    conditions:
      - "external commitment"
      - "irreversible"
      - "financial / legal / security / credential / customer data"
      - "company system writeback"
    allowed_ai_role:
      - "read-only analysis if authorized"
      - "red-door warning"
      - "prepare question for human authority"
    human_gate: "explicit approval required"
    examples:
      - "send external message"
      - "merge production change"
      - "touch company data"
      - "payment / contract / credential action"
```

## Shared Red Doors

- AI 能做 != AI 有權做.
- Agent 可執行 != 可進 Runtime.
- AI 輸出 != 人工核准.
- Human-in-the-loop != 形式審查.
- Build Card Accepted != Build Completed.
- Evidence Missing != Completed.
- Return Check Missing != Closed.

## Required Return

```yaml
AI_Action_Return:
  task_id:
  risk_level:
  action_type:
  data_class:
  human_reviewer:
  evidence_required: true
  return_check_required: true
  not_to_claim: []
```

## Final Rule

When in doubt, downgrade the action level. AI may assist, but authority must remain visible.