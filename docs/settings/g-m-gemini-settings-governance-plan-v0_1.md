# G Ecosystem → M Ecosystem → Gemini Settings Governance Plan v0.1

Status: Candidate / Settings Governance Plan / No Runtime / No External Writeback
Owner: Vitas
Qinyi Role: settings-domain inventory, semantic cleanup, layering, handoff packet, return review
Hazumi / Codex Role: UI, repo, or document construction only after explicit approval
Master Gate: #297
Related PR: #298

## Core

This plan upgrades Gmail cleanup into ecosystem-level settings governance.

Gmail is the entry point, but the actual target is a portable governance syntax for personal Google-side surfaces, enterprise Microsoft-side surfaces, and Gemini as a second-model reasoning mirror.

```text
G ecosystem = personal / cloud / signal / portable carrier
M ecosystem = company / enterprise / permissioned / operational carrier
Gemini = Google-side reasoning mirror / second-model reviewer / not authority
Qinyi = bridge / cleanup / contract / return review
Codex = bounded executor after approval
Vitas = final authority
```

Shared governance syntax:

```text
Source -> Carrier -> Authority -> Gate -> Action -> Return -> Rebuild
```

## Part A｜G Ecosystem

G ecosystem is not Gmail alone. It is a personal cloud carrier set.

```yaml
G_Settings_Surface:
  Gmail:
    function: "attention entry / task signal / billing and security reminders"
  Drive:
    function: "document carrier / evidence storage / public-safe and private separation"
  Calendar:
    function: "time commitment / deadline / reminder / review gate"
  Contacts:
    function: "people and organization index"
  Gemini:
    function: "second-model reasoning / Google-side mirror / external signal digestion"
```

### Gmail

Current main labels:

```yaml
Gmail_Main_Labels:
  00_待處理: "needs confirmation, reply, deadline, pickup, payment, contract, quote, meeting, review"
  10_工作: "company, client, vendor, engineering, smart building, GitHub/work-chain"
  20_帳務: "invoice, receipt, card, payment, billing"
  30_帳號安全: "login, verification, password, security alert"
  90_封存低優先: "newsletter, promotion, social, reading, sales follow-up"
```

Next Gmail work is not random moving. It is review of true action candidates, low-risk native filters, and UI work only after approval.

### Drive

Drive is the main G-side document carrier.

Target structure candidate:

```yaml
Drive_Target_State:
  00_Inbox_待整理: "unclassified incoming material"
  10_XuanLing_Candidate: "candidate XuanLing work material"
  20_PublicSafe: "public-safe material"
  30_PrivateAnchor: "private anchor material"
  40_Work_Handoff: "handoff and return packets"
  90_Archive: "historical material"
```

Drive should be inventoried before permission or sharing changes.

### Calendar

Calendar is a time gate, not a note dump.

Use for deadlines, payment/subscription checks, pickup, meetings, review gates, and return checks. Do not convert every signal into an event.

### Contacts

Contacts is an authority and relationship index, not only an address book.

Candidate groups: Company, Clients/Vendors, Family, XuanLing, Services.

Contacts help locate roles; they are not authorization evidence.

## Part B｜Gemini Work Contract

Gemini is not another Qinyi and not final authority.

```yaml
Gemini_Work_Contract:
  Role: "Google-side reasoning mirror / second opinion / long-context digestion"
  Can_Do:
    - "digest Google-side document context"
    - "second-model check of Qinyi candidate outputs"
    - "external signal absorption"
    - "comparison tables"
    - "public-safe rewrite candidate"
  Cannot_Do:
    - "final approval"
    - "company policy decision"
    - "GitHub merge"
    - "company-side writeback"
    - "identity or world-model final lock"
    - "treat Drive documents as approved source by default"
```

Gemini output must return to Qinyi as Facts / Inferences / To Verify / Risk / Suggested Action.

## Part C｜M Ecosystem

M ecosystem is the company/enterprise operational carrier. It must not inherit private G-side data or authority.

```yaml
M365_Settings_Surface:
  Outlook: "company mail and formal communication"
  Teams: "collaboration messages and decision traces"
  SharePoint_OneDrive: "company document carrier / permissioned evidence"
  Outlook_Calendar: "meeting and formal time commitments"
  Lists_Planner_ToDo: "task tracking if company environment permits"
```

M365 work is contract-first and manual-build-first. AI may draft category models, folder models, review models, and manual guides. It must not treat M365 output as final authority.

## Part D｜G vs M Boundary

```yaml
G_vs_M_Boundary:
  G_Ecosystem:
    nature: "personal / cloud / portable / candidate / signal"
  M_Ecosystem:
    nature: "company / enterprise / permissioned / operational"
```

Reusable across both sides:

- five-classification model
- Source -> Carrier -> Authority -> Gate -> Action -> Return -> Rebuild
- Candidate / Approved / Runtime
- Facts / Inferences / To Verify
- Return Packet
- Filter Candidate -> Dry-run -> Apply -> Verify -> Promote

Not transferable:

- raw company material
- private mail contents
- company permissions
- account authorization material
- unreviewed private identity material
- internal decision evidence

## Part E｜Phases

```yaml
Phase_1_G_Inventory:
  Gmail: "continue #295 return review"
  Drive: "inventory XuanLing / Gmail cleanup / handoff / Qinyi / Hazumi files"
  Calendar: "inventory recent deadline / renewal / pickup / review reminders"
  Contacts: "candidate key people / vendor / family / service grouping"
  Gemini: "establish Gemini work contract v0.1"

Phase_2_G_Cleanup:
  Gmail: "00_待處理 review, low-risk filters after approval"
  Drive: "handoff area, Candidate/PublicSafe/PrivateAnchor split, sharing risk awareness"

Phase_3_Gemini:
  output: "Gemini task packet and return format"

Phase_4_M365:
  output: "M365 work contract v0.1"

Phase_5_Codex:
  output: "bounded UI/repo/manual-guide tasks only after approval"
```

## Part F｜Acceptance Criteria

```yaml
G_Ecosystem_Acceptance:
  Gmail:
    - "00_待處理 only real action candidates"
    - "low priority not in inbox"
    - "security not archived"
  Drive:
    - "handoff files findable"
    - "candidate/public/private separated"
    - "sharing risks known"
  Calendar:
    - "deadlines visible"
  Gemini:
    - "outputs always return to Qinyi"
    - "no final authority claims"

M_Ecosystem_Acceptance:
  Outlook:
    - "company action mail visible"
  Teams:
    - "important decisions converted to return packet candidate"
  SharePoint:
    - "company files remain in company carrier"
  Governance:
    - "no private/company authority mixing"
```

## Final Judgment

The task is not Gmail cleanup anymore. The task is ecosystem settings governance.

G ecosystem organizes personal cloud and external signals. M ecosystem carries company permissions and formal workflows. Gemini provides second-model mirroring. They may share governance syntax, but must not share data, authority, or responsibility.