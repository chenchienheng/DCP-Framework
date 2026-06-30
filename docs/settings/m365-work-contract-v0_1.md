# M365 Work Contract v0.1

Status: Candidate / Company Operational Carrier Contract / Manual Build Only / No Runtime
Master Gate: #297
Related Plan: docs/settings/g-m-gemini-settings-governance-plan-v0_1.md

## Core

M ecosystem is the company/enterprise operational carrier. It is not the same as the personal G ecosystem. It should be governed by company permission, manual build, and return review.

## Surfaces

```yaml
M365_Settings_Surface:
  Outlook:
    role: "company mail and formal communication"
  Teams:
    role: "collaboration messages and decision traces"
  SharePoint_OneDrive:
    role: "company document carrier / permissioned evidence"
  Outlook_Calendar:
    role: "meeting and formal time commitments"
  Lists_Planner_ToDo:
    role: "task tracking if company environment permits"
```

## Outlook Category Model

```yaml
M_Outlook_Categories:
  00_Action: "needs reply, confirmation, deadline, review, payment, contract"
  10_Project: "project, client, vendor, consultant, engineering issue"
  20_Commercial: "quotation, billing, contract, procurement, payment"
  30_Risk_Access: "permission, account, compliance, EHS, risk"
  90_Reference: "announcement, FYI, closed record"
```

Rules:

- Do not auto-delete company mail.
- Do not auto-archive unread company action mail.
- Client, supervisor, contract, and payment mail always require a human gate.
- Any automatic rule should start with a dry-run period.

## Teams Contract

Teams is a conversation carrier, not final archive.

Can: search recent discussion, summarize action items, track whether a decision formed, convert important discussion into a return packet candidate.

Cannot: treat chat as formal approval, send unauthorized replies, change company task state automatically, move private or company chat into personal space.

## SharePoint / OneDrive Contract

SharePoint is the company evidence carrier.

Can: store formal documents, preserve versions, support search/reference, carry review material.

Cannot: mix into personal Drive, publicly share unreviewed material, replace company file library with personal GitHub.

## Calendar Contract

Company calendar is commitment, not personal note storage.

- Meeting = commitment.
- Review deadline = gate.
- Client schedule = risk signal.
- Personal reminder should not be mixed into company calendar.
- AI may suggest reminders but must not accept or decline meetings on behalf of Vitas without approval.

## Boundary

```yaml
M365_Boundary:
  no_raw_company_material_to_private_carrier: true
  no_personal_github_as_company_runtime: true
  no_local_endpoint_inspection: true
  no_automatic_writeback_without_vitas: true
```

## Output Candidates

- M365 category model.
- SharePoint folder model.
- Teams return packet model.
- Calendar gate model.
- Manual build guide.

## Final Rule

M ecosystem may share governance syntax with G ecosystem, but not data, authority, or responsibility.