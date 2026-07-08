# Small Build Loop Gate v0.1

Status: Candidate / Build Evidence Return Gate / No Runtime / No External Writeback
Use As: QHA gate for turning complex architecture into a small verifiable loop
Do Not Use As: company policy, build approval, production approval, runtime spec, or closeout

## Core

Large architecture should land through the smallest verifiable loop. A loop is not closed until it has a Build Card, Evidence Record, Return Check, and Feedback Loop.

## Loop

```yaml
Small_Build_Loop:
  Build_Card:
    meaning: "one bounded action or test"
  Evidence_Record:
    meaning: "what was actually created, tested, or observed"
  Return_Check:
    meaning: "whether the closure criteria were met"
  Feedback_Loop:
    meaning: "what must change in the next iteration"
```

## Closure Rules

```yaml
Closure_Rules:
  - "No Build Card = Reference Only"
  - "No Evidence Record = Not Completed"
  - "No Return Check = Not Closed"
  - "Feedback Missing = Not Rebuildable"
```

## Applies To

```yaml
Applies_To:
  - "M365 internal workflow model"
  - "Gmail living signal gate"
  - "Drive canonical root probe"
  - "GitHub content conformance"
  - "Xiaoshiguang field cards"
  - "future output module samples"
```

## Red Doors

- Blueprint != Build.
- Build != Adoption.
- Evidence Missing != Completed.
- Return Check Missing != Closed.
- User Surface != Data Authority.
- Reminder != Approval.
- Build Card Accepted != Build Completed.

## Final Rule

QHA should prefer a small verified loop over expanded blueprint writing.