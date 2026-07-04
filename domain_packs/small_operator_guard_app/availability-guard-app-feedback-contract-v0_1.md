# Small Operator Availability Guard App｜Sanitized Feedback Contract v0.1

Status: Sanitized Feedback / Internal Architecture Learning / Candidate / No Customer Data / No Runtime / No External Writeback
Source: User-provided sanitized feedback work contract
Use For: XuanLing architecture learning, Qinyi work-contract growth, W2 sanitization, W7 GitHub bridge, W1/Codex/Hazumi handoff, maintenance governance
Do Not Use As: operational data, customer booking data, credentials, API key, external platform authorization, final business decision, public-approved external document
Related PR: #298
Master Gate: #297
Intended Future Carrier: Yiyi_xiao, if created and sanitized

## Core

This feedback pack preserves only the architecture, authority, maintenance, anti-error, and return model of a small lodging availability GUI app. It does not contain customer PII, private conversations, booking details, account passwords, keys, or identifiable operational material.

## Source

Small operators need a low-cost GUI app usable on phone, tablet, or computer. The goal is to reduce availability misreads, incorrect availability promises, double commitments, inconsistent chat replies, lost oral notes, and maintenance black boxes.

## Not Source

This is not a public booking platform, payment system, OTA integration, automatic chat bot, AI auto-commitment system, or final operational decision system.

## Carriers

```yaml
Candidate_Carriers:
  gui_web_app_pwa: "front-end operational surface"
  github_repo: "code and docs carrier"
  hosting: "Vercel / Netlify / Cloudflare Pages candidate"
  database: "Supabase / Firebase candidate"
  official_site_admin: "content source candidate"
  messaging_entry: "LINE OA Rich Menu / LIFF candidate"
```

All tools are carriers, not authority.

## Authority

```yaml
Authority:
  highest_authority: "actual operator / owner"
  daily_operator: "lodging manager or authorized staff"
  maintenance_support: "Vitas / Qinyi / construction window / Codex / Hazumi if authorized"
  rule: "supporters help architecture, maintenance, docs, return, and construction; they do not become data sovereigns or business decision-makers"
```

## Sanitization Boundary

Forbidden in feedback:

- guest name, phone, LINE ID, private message screenshot, booking details, payment record
- password, API key, database URL/key, GitHub token, platform credentials
- unauthorized social content
- unredacted operational screenshot
- personally identifiable behavior record

Allowed in feedback:

- architecture pattern
- GUI Flow
- anti-error gate
- table shape
- permission model
- maintenance boundary
- de-identified error type
- public official content path if authorized

## Core Gates

```yaml
Core_Gates:
  Availability_Gate:
    rule: "Do not produce available-room reply before checking availability."
  Room_Unit_Gate:
    rule: "Do not confirm booking or hold before a specific room/unit is identified."
  Message_Gate:
    rule: "Generated replies are drafts only and require human review and manual send."
  Duplicate_Commitment_Gate:
    rule: "If same room/date is confirmed, held, or blocked, do not report available or create another hold."
  Data_Permission_Gate:
    rule: "Customer data and maintenance data must be separated; maintainer cannot read customer PII by default."
  Material_Truth_Gate:
    rule: "Display material must be official or authorized; generated images must not impersonate real spaces."
  Social_Content_Gate:
    rule: "Social content enters official material library only after account-owner authorization."
```

## BuildReady Candidate Scope

```yaml
BuildReady_Candidate:
  includes:
    - "GUI Web App / PWA prototype"
    - "responsive phone / tablet / desktop UI"
    - "today availability"
    - "availability check"
    - "reply draft"
    - "temporary hold"
    - "confirm booking"
    - "cancel booking"
    - "block date"
    - "error record"
    - "official material source integration"
    - "database schema candidate"
    - "RLS permission draft"
    - "customer data / maintenance data separation"
    - "non-technical operation cards"
    - "go-live checklist"
  not:
    - "runtime"
    - "approved deployment"
    - "customer-data import"
    - "external platform integration approval"
```

## Problem Return Format

```yaml
Problem_Return:
  date: "YYYY-MM-DD"
  reported_by_role: "owner / operator / maintainer"
  screen: "today availability / check availability / reply draft / hold / confirm booking / management"
  issue_without_pii: "what happened, without guest name, phone, LINE ID, or booking detail"
  impact: "whether it affects booking, reply, or data correctness"
  temporary_fix: "how it was handled"
  needed_change: "UI / Gate / Schema / Permission / Template / Training"
  authority_needed: "owner approval / maintainer fix / no approval needed"
  status: "open / fixed / rule_added"
```

## Rebuild Principle

Every error should return to system rebuilding before blaming people:

- was a gate missing?
- did the UI mislead the operator?
- were steps too complex?
- was permission too broad?
- was there no trace?
- did maintenance require access that should remain private?
- was technical pressure transferred to non-technical operators?

## Abstract Pattern

This case abstracts into Small Operator Guard App Pattern:

```yaml
Small_Operator_Guard_App:
  purpose: "reduce misjudgment, preserve authority, avoid black-box maintenance, enable handoff, keep data revocable, convert errors into rules"
  core_rule:
    - "AI drafts only"
    - "maintenance permission != customer data permission"
    - "design support != highest authority"
    - "Candidate != Approved"
    - "BuildReady != Runtime"
```

## Final Rule

The value of this sanitized feedback is to let XuanLing absorb the small-operator anti-error GUI pattern, not private customer data, private operations, or unauthorized materials.
