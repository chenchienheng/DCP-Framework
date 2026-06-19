# Codex Activity Rollup / Token Window Feedback v0.1 Candidate

> Candidate observability feedback for the Qinyi-Codex Collaboration Window. This is not a Codex task request, not a settings update, not billing proof, not proof of a fixed official reset rule, and not Native Loop evidence.

---

## 0. Status

```yaml
Document_Status: Candidate
Use_As:
  - Codex workspace-agent observability feedback
  - Cost Gate support material
  - Qinyi-Codex collaboration window guardrail note
Runtime_State: No_Runtime
External_Writeback_State: No_External_Writeback
Settings_Update: No
Billing_Proof: No
Native_Loop_Proof: No
Closeout_State: Not_Closeout
Evidence_Level:
  - User_Observed_Activity_Card
  - Needs_Official_or_Runtime_Verification_Before_Reset_Timing_Claim
```

---

## 1. One-Line Reading

Codex activity stats appear to roll up in a windowed pattern that may correlate with short-cycle reset behavior while coexisting with longer reset limits. This suggests token observability may follow quota-window aggregation rather than simple daily real-time counting.

---

## 2. Observed Stats

Latest observed activity card:

```yaml
Latest_Observed:
  Cumulative_Tokens: "約 1.7 億"
  Peak_Day: "約 6991.6 萬"
  Current_Streak: "3 days"
  Longest_Streak: "14 days"
```

Previous observed activity card:

```yaml
Previous_Observed:
  Cumulative_Tokens: "約 1.2 億"
  Peak_Day: "約 4249.3 萬"
  Current_Streak: "3 days"
  Longest_Streak: "14 days"
```

Observed delta:

```yaml
Observed_Delta:
  Cumulative_Increase: "約 5000 萬 tokens"
  Peak_Day_Increase: "約 2742.3 萬 tokens"
  Interpretation: "delayed rollup / window aggregation, not pure real-time display"
```

---

## 3. Hypothesis

Candidate interpretation:

```yaml
Activity_Rollup_Hypothesis:
  Possible_Drivers:
    - short-cycle quota / reset window
    - daily heatmap rollup
    - weekly usage reset / quota state
    - delayed dashboard refresh
  Status: Plausible_Observation
  Evidence_Level: User_Observed_Activity_Card
```

Boundary:

- Do not claim Codex officially refreshes activity stats every fixed short cycle.
- Do not treat the activity card as a real-time token meter.
- Do not treat the activity card as billing proof.
- Do not assume weekly reset and token heatmap use the same backend counter.

---

## 4. Why This Matters For Codex Work

If token stats follow reset-window aggregation, high-density work can appear to jump after a window closes.

This means Codex collaboration should not rely on visible activity cards as immediate stop signals.

Required controls must be internal to each work round:

- Per-task Cost Gate
- Retry limit
- Stop condition
- Human review before escalation
- No unbounded background loop
- No multi-branch expansion without LOR
- Return Packet required

Activity dashboard is useful as observability, but not sufficient as governance.

---

## 5. Guardrail Update

Candidate rules:

```text
Activity Dashboard ≠ Cost Gate
Visible Token Count ≠ Real-time Meter
Reset Window ≠ Permission Window
Weekly Reset ≠ Safe-to-Run Signal
Quota Available ≠ Task Approved
```

Meaning:

Even if quota appears to reset, Codex still needs LOR / Gate / Cost Gate before action.

---

## 6. Token Risk Level

Latest observed peak:

```yaml
Peak_Day: "約 6991.6 萬 tokens"
```

Agent-like multiplication estimate:

```yaml
If_2x: "約 1.4 億 tokens/day"
If_3x: "約 2.1 億 tokens/day"
If_10x: "約 7 億 tokens/day"
```

This supports the prior warning:

```text
Human-controlled high-density use = virtual lab.
Unbounded agent mode = token chain reaction.
```

---

## 7. Recommended Codex Window Handling

For future Codex rounds:

- Do not wait for dashboard update to stop.
- Set Cost Gate before task begins.
- Set Retry Limit before task begins.
- Set Stop Condition before task begins.
- Require Return Packet after task ends.
- If stats jump after rollup, record it as Observability Signal only.

Minimum Cost Gate:

```yaml
Cost_Gate:
  Mode: Required
  Per_Task_Budget:
  Retry_Limit:
  Tool_Allowlist:
  Background_Run: "No by default"
  Multi_Branch: "No without explicit LOR"
  Stop_Condition:
  Human_Review_Before_Escalation: true
```

---

## 8. Final Judgment

```yaml
Codex_Activity_Rollup_Observation: Candidate_Go
Short_Reset_Correlation: Plausible_Observation_Not_Official_Proof
Weekly_Reset_Coexistence: Plausible_Observation_Needs_Confirmation
Billing_Proof: No-Go
Real_Time_Token_Meter: No-Go
Cost_Gate_Required: Go
Agent_Mode_Watch: Yellow
Unbounded_Agent_Mode: No-Go
```

---

## 9. Final Sentence

Codex activity stats may be following a reset-window rollup pattern, which could explain why token totals jump in blocks rather than update smoothly. Quota reset is not governance: Codex still needs Cost Gate, Stop Condition, Retry Limit, Human Review, and Return Packet before high-density or agent-like work.
