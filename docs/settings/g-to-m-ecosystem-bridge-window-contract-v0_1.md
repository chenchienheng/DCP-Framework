# G-to-M Ecosystem Bridge Window Contract v0.1

Status: Candidate / Integration Window Contract / No Runtime / No External Writeback
Master Gate: #297
Related PR: #298
Use As: shared instruction for Qinyi windows, Gemini window, Drive/Gmail cleanup window, M365 planning window, and future integration tools
Do Not Use As: Gmail settings approval / M365 authorization / company deployment / Gemini final authority / Codex automation approval

## Core

Start from G ecosystem because it is more integrated, more portable, and better suited for signal cleanup, document routing, calendar reminders, contacts indexing, and Gemini second-model review. Do not directly start from M ecosystem because M ecosystem is the enterprise friction substrate: it has stronger permission boundaries, more red lines, and requires clearer operational fit before action.

Short rule:

```text
G ecosystem is the personal-cloud integration lab.
M ecosystem is the enterprise-permission operational substrate.
They may share governance syntax, but must not share data, authority, or responsibility.
```

## Why G First

```yaml
Why_G_First:
  integration_density:
    - "Gmail / Drive / Calendar / Contacts / Gemini already form one personal cloud signal loop"
  portability:
    - "materials can be cleaned, classified, and returned without company-system authority"
  lower_friction:
    - "personal authority is clearer than enterprise permission"
  better_for_experiment:
    - "settings governance can be tested without touching company operational surfaces"
  bridge_value:
    - "a stabilized G-side grammar can later inform M-side manual planning"
```

## Why M Later

```yaml
Why_M_Later:
  stronger_boundaries:
    - "company permission"
    - "tenant policy"
    - "SSO / IT / admin authority"
    - "data retention"
    - "legal / audit / compliance"
    - "external sharing"
    - "workflow side effects"
  higher_friction:
    - "Outlook / Teams / SharePoint / Lists / Power Platform must match real company process"
  stricter_red_lines:
    - "company data must not leave M ecosystem"
    - "AI summary is not company approval"
    - "manual guide is not system built"
```

## Window Mission

The bridge window does not operate Gmail, Drive, Calendar, Contacts, Gemini, Outlook, Teams, SharePoint, Power Apps, or Flow. It organizes settings governance language and produces candidate handoff packets.

It should answer:

- Which surface is involved?
- Is this G-side or M-side?
- What is the source?
- What is the carrier?
- Who has authority?
- Is this inventory, candidate change, dry-run, manual guide, or runtime?
- What red doors exist?
- Where should the return packet go?

## Shared Syntax

```yaml
Shared_Governance_Syntax:
  - Source
  - Carrier
  - Authority
  - Gate
  - Action
  - Return
  - Rebuild
  - Facts / Inferences / To_Verify
  - Candidate / Approved / Runtime
  - Return Packet
  - Filter Candidate -> Dry-run -> Apply -> Verify -> Promote
```

## G Ecosystem Surfaces

```yaml
G_Ecosystem:
  nature: "personal / cloud / signal / portable carrier"
  surfaces:
    Gmail:
      role: "attention entry / mail classification / action signal"
    Drive:
      role: "document carrier / evidence boundary / handoff packets"
    Calendar:
      role: "time gate / deadline / reminder / return check"
    Contacts:
      role: "people and organization index"
    Gemini:
      role: "Google-side second-model reasoning mirror"
    GitHub_DCP:
      role: "sanitized cloud carrier for docs, issues, schemas, return packets"
```

## M Ecosystem Surfaces

```yaml
M_Ecosystem:
  nature: "company / enterprise / permissioned / operational carrier"
  surfaces:
    Outlook:
      role: "formal company communication"
    Teams:
      role: "collaboration messages and decision traces"
    SharePoint_OneDrive:
      role: "company document carrier and permissioned evidence"
    Outlook_Calendar:
      role: "meeting and formal time commitment"
    Lists_Planner_ToDo:
      role: "task tracking if company environment permits"
    Power_Platform:
      role: "manual build candidate only unless approved"
```

## Allowed Work

```yaml
Allowed:
  - "read-only inventory planning"
  - "settings governance language"
  - "label/category/folder model candidate"
  - "manual build guide candidate"
  - "Gemini task packet"
  - "M365 work contract candidate"
  - "return packet template"
  - "red-door analysis"
  - "G-to-M mapping table"
```

## Forbidden Without Explicit Vitas Approval

```yaml
Forbidden:
  - "change Gmail settings"
  - "create filters"
  - "archive/delete email"
  - "change Drive sharing"
  - "move company data to private G carrier"
  - "operate Outlook / Teams / SharePoint / Power Platform"
  - "create M365 workflow runtime"
  - "use Gemini as final authority"
  - "use Codex as company operator"
  - "publish or merge"
```

## G-to-M Mapping

```yaml
G_to_M_Mapping:
  Gmail:
    maps_to: "Outlook"
    shared_syntax: "Action / Reference / Risk / Commercial classification"
    warning: "Gmail label logic cannot be copied directly into company mail rules"
  Drive:
    maps_to: "SharePoint / OneDrive"
    shared_syntax: "document carrier / evidence boundary / sharing risk"
    warning: "private Drive and company SharePoint must not mix raw data"
  Calendar:
    maps_to: "Outlook Calendar"
    shared_syntax: "deadline / review gate / time commitment"
    warning: "company calendar is formal commitment, not personal reminder board"
  Contacts:
    maps_to: "company directory / Outlook contacts"
    shared_syntax: "role index / relationship map"
    warning: "contact record is not authorization evidence"
  Gemini:
    maps_to: "Copilot or M365-side assistant if available"
    shared_syntax: "second opinion / summary candidate"
    warning: "model output is not company approval"
```

## Return Format

```yaml
G_to_M_Bridge_Return:
  Source:
  Surface_Group: "G_Ecosystem | M_Ecosystem | Bridge"
  Surface:
  Carrier:
  Authority:
  Current_State:
  Proposed_Action:
  Allowed_Now:
  Forbidden_Now:
  Red_Doors:
  Candidate_Mapping:
  What_Can_Move:
  What_Cannot_Move:
  Needs_Vitas_Decision:
  Return_To:
  Next_Action:
```

## Red Doors

- G integration maturity ≠ M implementation approval.
- Personal authority ≠ company authority.
- Google-side summary ≠ Microsoft-side evidence.
- Gemini output ≠ final authority.
- Gmail label ≠ Outlook rule.
- Drive folder ≠ SharePoint permission model.
- Calendar reminder ≠ company commitment.
- Manual guide ≠ workflow runtime.
- Company data must remain in company carrier.

## Final Rule

Use G ecosystem to stabilize the governance grammar. Use M ecosystem only after the grammar is clear, the red doors are explicit, and Vitas decides a manual-build or company-side planning path.