# Carrier Connection Intake and Subscription Matrix v0.1

Status: Candidate / Carrier Intake Matrix / GitHub Candidate File / No Runtime / No Subscription Approval / No External Carrier Connection
Use As: decision scaffold for evaluating unconnected carriers, cloud families, subscriptions, and connector lanes
Do Not Use As: procurement approval, subscription purchase instruction, migration approval, company IT policy, or external writeback authorization

## Core

Do not connect or subscribe because a tool is powerful. Connect only when a carrier has a defined node role, data class, permission ring, return path, and retention fate.

```yaml
Connection_Principle:
  not:
    - "connect everything"
    - "subscribe because available"
    - "treat connector as permission"
    - "move private context into public carrier"
  yes:
    - "define node role first"
    - "define data class"
    - "define sovereignty"
    - "define access rings"
    - "define return path"
    - "define retention class"
    - "define red doors"
```

## Intake Gate

```yaml
Carrier_Intake_Gate:
  questions:
    1_node_role: "What unique node role does this carrier serve?"
    2_data_class: "What data belongs here and what must never enter?"
    3_authority: "Who may authorize read/write/share/delete?"
    4_return_path: "Where does its output return?"
    5_retention: "Is this current, canonical, cold archive, or private human-base memory?"
    6_overlap: "Does this duplicate an existing carrier?"
    7_subscription_need: "Is a paid plan necessary for storage, permissions, API, automation, or collaboration?"
    8_exit_plan: "How can the data be exported, archived, or disconnected?"
  output_class:
    - "Do_Not_Connect"
    - "Manual_Use_Only"
    - "Read_Only_Candidate"
    - "Write_Candidate_With_Vitas_Approval"
    - "Subscription_To_Verify"
    - "Red_Gate"
```

## Current Carrier Status

```yaml
Carrier_Status:
  GitHub:
    status: "active candidate canonical chain"
    role: "versioned governance / registries / red doors / hook anchors"
    subscription_status: "already in use by Vitas; no new decision here"
    next: "keep as canonical chain, not raw dump"

  Google_Drive:
    status: "active current working memory"
    role: "human-readable return packets / weekly integration / decision queue"
    subscription_status: "already in use by Vitas; no new decision here"
    next: "add manifest and active pointer index"

  GPT_Schedules:
    status: "active signal and return generation layer"
    role: "trigger / inspection / scheduled return packet"
    subscription_status: "already in use through ChatGPT task system"
    next: "keep core + sidecar separation"

  Gmail:
    status: "sidecar hygiene signal"
    role: "G ecosystem carrier hygiene and signal intake"
    subscription_status: "no subscription decision in this file"
    next: "notify only on drift / risk / broken chain"
```

## Unconnected / Candidate Carriers

```yaml
Unconnected_Carriers:
  Box:
    candidate_role: "cold archive / enterprise file quarantine / long-retention historical deposit"
    connect_when:
      - "Google Drive current memory becomes too crowded"
      - "large historical bundles need cold archive"
      - "access-control separation is required"
    do_not_connect_when:
      - "only because storage exists"
      - "only for duplicate backup without retrieval plan"
    subscription_to_verify: true
    decision_default: "Do not subscribe yet"

  Dropbox:
    candidate_role: "cold archive / sync-friendly artifact deposit / external collaboration archive candidate"
    connect_when:
      - "large file exchange or cold archive becomes a repeated need"
      - "Box is not suitable or already unavailable"
    do_not_connect_when:
      - "same role already satisfied by Drive/GitHub"
    subscription_to_verify: true
    decision_default: "Do not subscribe yet"

  OneDrive:
    candidate_role: "M ecosystem bridge / private or company-adjacent working memory / Office file carrier"
    connect_when:
      - "M365 work chain becomes a stable, authorized lane"
      - "company documents require M ecosystem-native handling"
      - "SharePoint / Teams / Outlook dependencies become explicit"
    red_gate:
      - "Personal M != Company M365"
      - "company data requires permission"
    subscription_to_verify: true
    decision_default: "Do not subscribe or connect until lane is separated"

  iCloud:
    candidate_role: "private human-base / device-side continuity / personal memory"
    connect_when:
      - "private notes, device continuity, or human-base capture needs a carrier"
      - "not intended for Open Core"
    red_gate:
      - "private context must not enter GitHub"
    subscription_to_verify: true
    decision_default: "Use manually first; no integration yet"

  SharePoint_Teams_M365:
    candidate_role: "company collaboration and process segment carrier"
    connect_when:
      - "company permission and data boundary are explicit"
      - "workflow requires M ecosystem native loops"
    red_gate:
      - "Tool capability != company authorization"
      - "personal architecture != company policy"
    subscription_to_verify: true
    decision_default: "Read/advise only until authorized"

  Apple_Notes_Files_Reminders_Shortcuts:
    candidate_role: "private capture / device-adjacent signal / personal routine carrier"
    connect_when:
      - "human-base capture needs low-friction personal input"
    do_not_connect_when:
      - "the data should be canonical or shared"
    subscription_to_verify: false
    decision_default: "manual/private only"

  SQL_or_Relational_DB:
    candidate_role: "structured local storage / query / app persistence"
    connect_when:
      - "OCF Cell fields need stable query and app runtime"
      - "a field proof becomes product-grade"
    red_gate:
      - "SQL row != OCF Cell"
      - "database schema != governance architecture"
    subscription_to_verify: true
    decision_default: "not before OCF Cell Registry stabilizes"

  Blockchain_or_Ledger:
    candidate_role: "immutability / audit proof / trust ledger candidate"
    connect_when:
      - "a narrow proof-of-history or audit requirement exists"
    do_not_connect_when:
      - "used as ideology or replacement for governance"
    red_gate:
      - "ledger proof != truth"
      - "immutability can freeze pollution"
    subscription_to_verify: true
    decision_default: "not needed now"
```

## Subscription Gate

```yaml
Subscription_Gate:
  allow_only_if:
    - "carrier role is unique"
    - "data class is defined"
    - "read/write boundary is defined"
    - "there is a repeated need, not one-off curiosity"
    - "existing carriers cannot safely handle the role"
    - "exit/export plan exists"
  reject_if:
    - "cool tool"
    - "temporary inspiration"
    - "duplicate storage"
    - "unclear permission"
    - "unclear retention"
    - "private context leakage risk"
```

## Connection Order Candidate

```yaml
Connection_Order_Candidate:
  Phase_0_Current:
    active:
      - "GPT schedules"
      - "Google Drive"
      - "GitHub"
    task:
      - "Return Packet Template v0.4"
      - "active / superseded / archive pointer index"
      - "Node Registry"

  Phase_1_Manual_M_Ecosystem_Map:
    active: false
    task:
      - "separate Personal M from Company M365"
      - "define OneDrive / SharePoint / Teams roles"
      - "no writeback without authorization"

  Phase_2_Private_Human_Base:
    active: false
    candidates:
      - "iCloud"
      - "OneDrive personal"
    task:
      - "define private note boundaries"
      - "prevent Open Core leakage"

  Phase_3_Cold_Archive:
    active: false
    candidates:
      - "Box"
      - "Dropbox"
    task:
      - "verify need for cold archive"
      - "compare storage, retrieval, sharing, export, cost"

  Phase_4_Runtime_Data:
    active: false
    candidates:
      - "SQL"
      - "app database"
      - "ledger only if narrow audit need exists"
    task:
      - "only after OCF Cell Registry and field proof stabilize"
```

## Red Doors

- Subscription != Integration.
- Connector Available != Permission.
- Paid Plan != System Maturity.
- Company M365 != Personal M ecosystem.
- Private Human Base != Open Core.
- Cold Archive != Trash Can.
- SQL Row != OCF Cell.
- Blockchain Proof != Governance Truth.
- Tool Capability != Authority.
- Connection Candidate != Active Carrier.

## Next Step

```yaml
Next_Step:
  build:
    - "Node Registry v0.1"
    - "Carrier Capability Matrix v0.1"
    - "Return Packet Template v0.4 patch"
  verify_later:
    - "Box / Dropbox current plan and API needs"
    - "OneDrive / SharePoint / Teams permission boundary"
    - "iCloud manual/private capture role"
    - "SQL / runtime DB need after field proof"
```

## Final Rule

No new subscription, connector, or cloud family should be activated until it has passed the Carrier_Intake_Gate and has a defined node role in the chain ecology.
