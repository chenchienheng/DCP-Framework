# Carrier Connection Intake Matrix v0.1

Status: Candidate / Carrier Intake Matrix / No Runtime / No Subscription Decision / No External Writeback
Use As: evaluation matrix for unconnected or optional cloud/library/tool carriers before connecting, subscribing, or assigning chain roles
Do Not Use As: subscription approval, OAuth authorization, procurement decision, enterprise policy, production integration, or data migration approval

## Core

A carrier should not be connected because it exists or because the tool is powerful. A carrier is connected only if it has a clear node role, boundary, return path, authority gate, privacy class, and retention fate.

```yaml
Connection_Principle:
  question: "What chain role does this carrier serve?"
  not: "What tool can it do?"
  required_before_connection:
    - node_role
    - data_class
    - authority_gate
    - read_write_scope
    - return_path
    - retention_class
    - pollution_risk
    - subscription_need
```

## Intake Fields

```yaml
Carrier_Intake_Record:
  carrier_name:
  ecosystem_family:
  current_status:
    - "not_connected"
    - "connected_read_only"
    - "connected_candidate"
    - "active_core"
    - "sidecar"
    - "cold_archive_candidate"
    - "private_human_base_candidate"
  proposed_node_role:
  use_for: []
  do_not_use_as: []
  data_class:
    - "public_signal"
    - "personal_private"
    - "company_sensitive"
    - "client_data"
    - "field_context"
    - "repo_safe_candidate"
    - "archive_only"
  permission_scope:
    read:
    write:
    share:
    delete:
  authority_gate:
    required_approver: "Vitas"
    escalation_conditions: []
  return_path:
    next_reader:
    write_to_candidate:
    filing_block_required: true
  retention_class:
  pollution_check:
    private_context_risk:
    runtime_claim_risk:
    approval_drift_risk:
    fieldspace_leak_risk:
    duplicate_storage_risk:
  subscription_decision:
    needed_now: false
    reason:
    alternatives:
    decision_status: "Candidate / Not Approved"
```

## Current Carrier Family Map

```yaml
Carrier_Family_Map:
  GitHub:
    current_status: "active_core"
    node_role: "canonical version memory / governance chain / hook anchor"
    subscription_note: "already used; subscription decision outside this file"
    must_not: "store private field context or treat file existence as approval"

  Google_Drive:
    current_status: "active_working_memory"
    node_role: "human-readable current returns / daily-weekly circulation / decision queue"
    subscription_note: "already used; avoid dump behavior"
    must_not: "be treated as closeout"

  GPT_Schedules:
    current_status: "active_signal_return_layer"
    node_role: "trigger / inspection / return-packet generator"
    subscription_note: "already used through ChatGPT plan; not evaluated here"
    must_not: "be treated as autonomous runtime"

  Gmail:
    current_status: "sidecar"
    node_role: "G ecosystem signal and hygiene watch"
    subscription_note: "no new subscription implied"
    must_not: "bulk modify without explicit permission"

  Google_Calendar:
    current_status: "possible sidecar"
    node_role: "time-routing / schedule exception / future activation node"
    subscription_need: "not yet"
    must_not: "auto-create events without explicit instruction"

  Box:
    current_status: "cold_archive_candidate"
    node_role: "cold archive / heavy artifact quarantine / historical deposit"
    subscription_need: "to evaluate only when archive volume or compliance need appears"
    must_not: "connect merely because archive concept exists"

  Dropbox:
    current_status: "cold_archive_candidate"
    node_role: "cold archive / cross-device shared archive candidate"
    subscription_need: "to evaluate against Box, Google Drive storage, and iCloud"
    must_not: "duplicate Drive without retention rule"

  OneDrive:
    current_status: "private_or_company_human_base_candidate"
    node_role: "M ecosystem bridge / private or company work memory depending account boundary"
    subscription_need: "only if M ecosystem work lane becomes active"
    must_not: "mix personal and company M365 data"

  iCloud:
    current_status: "private_human_base_candidate"
    node_role: "device-adjacent private continuity / personal field notes"
    subscription_need: "only if private human-base memory needs structured retention"
    must_not: "leak private notes into Open Core"

  Notion:
    current_status: "optional_workspace_candidate"
    node_role: "human-readable knowledge workspace candidate"
    subscription_need: "defer; may duplicate Drive/GitHub"
    must_not: "become another unsorted memory dump"

  Slack_Teams:
    current_status: "communication_carrier_candidate"
    node_role: "message return / team coordination / conversation evidence"
    subscription_need: "only when team or company lane is explicit"
    must_not: "treat chat as approval"

  SQL_or_App_DB:
    current_status: "future_structural_storage_candidate"
    node_role: "structured cell field storage / query layer"
    subscription_need: "not a subscription question; requires product/runtime design"
    must_not: "confuse database row with OCF Cell"

  Blockchain_or_Ledger:
    current_status: "future_audit_ledger_candidate"
    node_role: "immutable audit proof / external trust anchor"
    subscription_need: "not needed now"
    must_not: "treat proof as governance truth"
```

## Subscription Gate

```yaml
Subscription_Gate:
  approve_only_if:
    - "carrier has unique node role not covered by active carriers"
    - "data class is clear"
    - "read/write authority is clear"
    - "retention fate is clear"
    - "expected use recurs enough to justify cost"
    - "Vitas explicitly approves"
  reject_or_defer_if:
    - "duplicate of existing Drive/GitHub/GPT lane"
    - "only curiosity-driven"
    - "unclear privacy boundary"
    - "no return path"
    - "no immediate use case"
```

## Connection Decision States

```yaml
Connection_Decision_State:
  Not_Needed:
    meaning: "no current role"
  Watch:
    meaning: "possible future role, no connection"
  Candidate:
    meaning: "role exists but no permission or subscription decision"
  Read_Only_Test:
    meaning: "limited non-destructive read evaluation"
  Active_Sidecar:
    meaning: "can feed QHA but is not core"
  Active_Core:
    meaning: "part of primary chain ecology"
  Red_Gate:
    meaning: "blocked due to privacy, authority, or pollution risk"
```

## Red Doors

- Subscription != Integration.
- Connector Available != Authorized Carrier.
- Connected Tool != Active Node.
- Read Permission != Write Permission.
- Company Carrier != Personal Carrier.
- Archive Carrier != Approved Memory.
- Sidecar != Core.
- Duplicate Storage != Resilience.
- Cost Paid != Value Proven.
- OAuth Grant != Governance Approval.

## Immediate Use

Use this matrix before connecting or subscribing to Box, Dropbox, OneDrive, iCloud expansion, Notion, Slack/Teams lanes, database storage, blockchain/audit ledgers, or any future cloud family.

Final rule: place first, subscribe later. A carrier without a node role is not a system component; it is only a tool option.
