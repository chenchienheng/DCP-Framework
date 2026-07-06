# Signal Intake Gate v0.1

Status: Candidate / Governance Gate / No Runtime / No External Writeback
Use As: pre-classification gate before signals enter QHA, LOR, repo, Drive, or domain-pack workflows
Do Not Use As: approved doctrine, auto-routing runtime, company policy, merge approval, or external writeback authorization

## Core

Not every useful signal should enter the architecture chain. A signal must first be classified by source, scope, privacy, authority, repeatability, contamination risk, and target layer.

## Intake Categories

```yaml
Signal_Intake_Category:
  Case:
    meaning: "specific personal or work case"
    default_target: "private note / daily return"
  Chat:
    meaning: "conversation-born signal"
    default_target: "MainChat_LOR return candidate"
  Work_Context:
    meaning: "work-role or company-context signal"
    default_target: "private work note unless sanitized"
  Architecture_Build:
    meaning: "candidate construction or template update"
    default_target: "XLQY / DCP candidate docs"
  Governance_Rule:
    meaning: "generalizable red-door or gate rule"
    default_target: "DCP governance candidate"
  Red_Gate:
    meaning: "boundary risk requiring hold"
    default_target: "Decision Queue / Red Door Registry"
  Decision_Item:
    meaning: "requires Vitas decision"
    default_target: "Decision Queue"
  Archive_Only:
    meaning: "historical or superseded material"
    default_target: "archive pointer"
```

## Required Checks

```yaml
Signal_Intake_Check:
  source:
  scope:
  privacy:
  authority:
  repeatability:
  generalizable:
  malicious_risk:
  contamination_risk:
  target_layer:
  retention_class:
  next_reader:
```

## Classification Output

```yaml
Signal_Intake_Result:
  category:
  accepted_as:
  not_accepted_as: []
  target_carrier:
  next_reader:
  manual_needed: []
  red_doors: []
  not_to_claim: []
```

## Red Doors

- Useful Signal != Should Be Stored Everywhere.
- Work Case != Architecture Build.
- Private Work Context != Open Core Material.
- Chat Signal != Approved Rule.
- Signal Intake != Decision.
- Filing Block != Actual Writeback.
- Governance Candidate != Approved Doctrine.

## Final Rule

Classify before storing. Extract essence before promotion. Park or archive before pollution reaches the active chain.
