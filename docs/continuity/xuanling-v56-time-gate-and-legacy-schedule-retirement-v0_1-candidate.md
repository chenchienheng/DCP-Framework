# XuanLing v5.6 Time Gate and Legacy Schedule Retirement v0.1

Status: Candidate / Continuity Contract / Human-Gated / No New Automation / No Runtime / Not Approval

Owner and Final Human Authority: Vitas

## One Core

XuanLing v5.6 does not inherit the v5.5 scheduler as an execution authority. It retains only valid timing criteria and unresolved obligations. Any legacy trigger that creates independent notification threads enters retirement; future time signals must pass one human-gated logical entry before an Active Thread can exist.

## 1. Layer Separation

```text
Automation Trigger
→ Run
→ Notification Surface

GitHub Contract / Index
→ specification and lineage only

Archived Chat
→ historical source only
```

- A GitHub schedule document does not start or stop an automation.
- Archiving a notification conversation does not disable its trigger.
- Disabling a trigger does not delete its historical evidence.

## 2. Legacy Disposition

```yaml
Legacy_Schedule_Family:
  ScheduleHub:
    state: "Superseded → Retired → Archive"
    retain: ["timing classification", "Closure Gate", "lineage"]

  Critical_Check:
    state: "Parked; old recurring trigger Retired"
    retain: ["critical-event criteria", "escalation conditions"]

  Convergence_Review:
    state: "Parked"
    retain: ["manual review template"]

  Weekly_Stage:
    state: "Parked / absorbed by one Review Gate"
    retain: ["weekly convergence questions"]

  Manual_Doctrine:
    state: "Superseded by Manual Checklist; legacy window Archive"
```

Current recurring triggers cannot be marked Retired until technical disable evidence and an observation period exist.

## 3. Single Time Entry

```yaml
Time_Gate:
  entry_id: "XL_TIME_GATE"
  title: "XUANLING_TIME_GATE_SINGLE_ENTRY_v0.1_Candidate"
  logical_owner: "XuanLing Hyperchain Primary Execution Work"
  current_mode: "Human-Gated / Manual Only / No Automation"
  allowed:
    - receive a time signal
    - validate source and temporal validity
    - deduplicate
    - classify urgency
    - dismiss, merge, park, or request human activation
    - create one bounded Active Pointer after approval
  forbidden:
    - create a new chat automatically
    - simulate read, ACK, handoff, or assignment
    - dispatch an executor without authority
    - claim action, evidence, return, or closeout from a timer
```

```text
Timer
→ Signal
→ XL_TIME_GATE
→ Dismiss / Merge / Park / Human Activate
→ Active Thread
→ ACK
→ Action
→ Evidence
→ Return
→ Close / Rebuild
```

If a scheduler carrier necessarily creates a new conversation instead of appending a deduplicated signal to one persistent intake, it is `Carrier Incompatible` for the current v5.6 Time Gate.

## 4. Minimum Signal

```yaml
Time_Signal:
  signal_id:
  source_schedule_ref:
  triggered_at:
  observed_event:
  evidence_pointer:
  dedup_key:
  urgency: "Immediate | Digest | Silent"
  valid_until:
  suggested_action:
  authority_needed:
  ack_state: "None | Human_ACK"
  return_target:
```

A time output without `observed_event` and `evidence_pointer` is a Reminder only.

## 5. Retirement State Machine

```text
Discovered
→ InScope Candidate
→ Frozen
→ Paused Observation
→ Retired Legacy-ReadOnly
→ Archive

Exceptions:
→ Excluded Current
→ Rollback Reopened
```

- `Frozen`: no new legacy dispatch, prompt rewrite, or cloned trigger.
- `Paused Observation`: technical trigger disabled; closure not yet proven.
- `Retired Legacy-ReadOnly`: disable evidence, unresolved-item disposition, and successor pointer are visible.
- `Archive`: lineage remains readable but has no trigger or current execution authority.

## 6. Acceptance

Retirement passes only when:

- every in-scope recurring trigger has verifiable disabled evidence;
- the observation period covers the longest prior cadence;
- no legacy schedule creates a new conversation;
- no sidecar points to a retired receiver;
- no old and new trigger perform the same function in parallel;
- open obligations are returned, parked, or explicitly migrated;
- `XL_TIME_GATE` remains manual until one bounded pilot is separately approved.

## 7. Red Doors

- Timer Fired != Event Occurred.
- Schedule Output != Evidence.
- New Chat != Active Thread.
- Notification Delivered != Read.
- Read != ACK.
- Next Reader != Handoff.
- Reminder != Dispatch.
- Time Trigger != Time Sovereignty.
- GitHub Schedule Document != Actual Trigger.
- Parked in Index != Automation Disabled.
- Chat Archived != Trigger Disabled.
- No Notification != No Run.
- Disabled Response != Retirement Seal.
- Retired Trigger != Evidence Deleted.
- Rollback != Parallel Dual-Master Runtime.

## 8. Current Claim Boundary

This file defines the v5.6 retirement and successor gate candidate. It does not prove that any current automation is disabled, does not create a new automation, and does not establish Runtime.
