# Open XuanLing Core｜GitHub Construction Canonical Gate v0.3

Status: Candidate / Canonical Construction Gate / Not Approved / No Runtime / No External Writeback
Sources: Construction analysis v0.1, Review Qinyi gate, Contract Qinyi return, Chat Qinyi v0.2, Cloud-first #297 context
Use As: Builder Qinyi / Review Qinyi / Contract Qinyi / Hazumi-Codex / Vitas alignment source
Do Not Use As: Approved doctrine / GitHub merge approval / runtime authorization / public launch / platform commitment

## Core

Open XuanLing Core should stop expanding as a whitepaper and become a small, stable, boring, brand-neutral governance core that can be built, reviewed, tested, and returned inside GitHub.

The minimum usable unit is not an agent, CLI, adapter, or runtime. The minimum usable unit is Gate Decision:

```text
Given a task or proposal, decide Go / Conditional Go / Park / Stop / Needs Human Approval, then produce a Return Packet.
```

## Canonical Gate Decision

```yaml
Canonical_Gate_Decision:
  decision: "Conditional Pass"
  approved_final: false
  runtime: false
  external_writeback: false
  public_release: false
  can_forward_to_builder_qinyi: true
  can_forward_to_reviewer_qinyi: true
  can_forward_to_contract_qinyi: true
  can_forward_to_hazumi_codex: "Only after Builder draft + Reviewer gate + Vitas decision"
```

## Core / Domain Packs Separation

Core includes only brand-neutral governance grammar:

- Source / Carrier / Authority / Gate / Action / Return / Rebuild
- State Model
- Red Doors
- Semantic Firewall
- Source Card
- Gate Review
- Return Packet
- Gate Decision Schema

Domain Packs are optional and not core requirements:

- Qinyi Path Bridge Pack
- Hazumi Codex Workcell Pack
- Company M365 Manual Build Pack
- Education AI Twin Gate Pack
- Family Decision Boundary Pack
- Relationship Message Boundary Pack

Qinyi / Hazumi / W-system can be early domain packs, but they must not be required for Open XuanLing Core.

## First Build Set

Stage the first build set under `open-core/` inside this repository until Vitas decides whether to split a dedicated repository.

Required candidate files:

- open-core/README.md
- open-core/SPEC.md
- open-core/STATE_MODEL.md
- open-core/RED_DOORS.md
- open-core/SEMANTIC_FIREWALL.md
- open-core/SOURCE_CARD.md
- open-core/GATE_REVIEW.md
- open-core/RETURN_PACKET.md
- open-core/schemas/source_card.schema.json
- open-core/schemas/gate_decision.schema.json
- open-core/schemas/return_packet.schema.json
- open-core/examples/ai_tool_request.yaml
- open-core/examples/company_workflow_candidate.yaml
- .github/ISSUE_TEMPLATE/gate_review.yml
- .github/pull_request_template.md

## Forbidden First Build

No CLI. No runtime. No adapters. No domain packs. No full whitepaper. No public launch. No company raw data. No private origin material. No Qinyi / Hazumi as core-required personas.

## Review Order

Builder Qinyi drafts candidate files. Review Qinyi checks repo usability, external readability, core/domain separation, schema testability, semantic firewall, and redgate risks. Vitas decides. Hazumi / Codex builds only after that decision.

## External Wording

Use external wording:

```text
This project may feel broad because it connects governance, AI assistance, documents, platforms, and human responsibility. The core is intentionally small: a gate-review protocol for action, authority, and return.
```

## Not To Claim

- Open XuanLing Core is Approved.
- The repo is runtime-ready.
- ADK / Codex / M365 are connected.
- Qinyi / Hazumi are core-required personas.
- This is a complete whitepaper.
- This is company policy.
- This is an AI agent framework or chatbot.
- This replaces human review.
- This contains company raw data.

## Can Claim

- This is a Candidate governance core.
- It defines Source / Carrier / Authority / Gate / Action / Return / Rebuild.
- Phase 1 focuses on spec, schema, examples, and templates.
- It does not provide runtime.
- It does not perform external writeback.
- It does not connect to any platform.