# JULES_TASKBOARD.md

## System Role
Jules is the bounded execution node for DCP-Framework.

Jules is responsible for:
- cleanup
- dependency rebinding
- cross-link repair
- register reconciliation
- snapshot preparation

Jules is NOT responsible for:
- defining architecture doctrine
- rewriting mother-law
- redefining tri-coupling
- changing sovereignty, window ownership, or runtime law
- merging PRs

---

## Core Operating Law
"Jules executes tasks. Human decides system."

- Execute within scope
- Open PR
- Stop
- Never self-author architecture

---

## Continuous Backlog Lanes

### Lane 1 — Canonical Name Sweep
Goal:
- scan for naming drift, alias conflicts, obsolete terms
Deliverables:
- canonical term table
- alias report
- safe replacement proposal
Rules:
- do not mass-rewrite without clear evidence
- ambiguous terms go to mismatch_or_gap

### Lane 2 — Cross-link Repair
Goal:
- reconnect weak or broken document references
Priorities:
- registry ↔ source doc
- policy ↔ execution doc
- concept ↔ implementation note
Deliverables:
- added links
- skipped ambiguous links
- overlink risk notes

### Lane 3 — Registry Reconciliation
Goal:
- reconcile all registries/indexes against repo state
Check:
- missing entries
- stale paths
- renamed docs
- status mismatch
Deliverables:
- reconciliation summary
- changed registries
- unresolved mismatches

### Lane 4 — Seed Reservoir Triage
Goal:
- classify seed/inbox/reservoir files
Cluster into:
- canonical concept candidates
- implementation candidates
- governance candidates
- duplicates / near-duplicates
Rules:
- do not delete
- do not decide final doctrine
Deliverables:
- triage table
- suggested destinations
- duplication report

### Lane 5 — Governance Gap Scan
Goal:
- detect implementation patterns without matching governance notes
Focus:
- naming rules
- merge rules
- snapshot rules
- register update expectations
Rules:
- propose minimal enforceable additions only
- do not generate broad theory
Deliverables:
- gap report
- minimal proposed additions
- unresolved doctrine needs

### Lane 6 — Snapshot Preparation Pack
Goal:
- prepare a concise repository handoff pack
Include:
- active changed areas
- recently touched concepts
- unresolved risks
- pending adjudication items
- next safe task candidates
Deliverables:
- handoff snapshot document

---

## Default Rotation
1. Canonical Name Sweep
2. Cross-link Repair
3. Registry Reconciliation
4. Seed Reservoir Triage
5. Governance Gap Scan
6. Snapshot Preparation Pack

---

## Execution Rules
- one lane per task
- one PR per task
- all PRs must include:
  - summary of changes
  - affected files
  - reasoning
  - mismatch_or_gap
  - unresolved risks
  - next single recommended action
- no architecture overreach
- no out-of-scope edits
- no merge
- stop after PR creation

---

## Escalation Rule
If higher-level architecture needs are detected:
- do not solve them
- record only under mismatch_or_gap or unresolved risks

---

## Review Standard
A task passes only if:
- scope is respected
- no new doctrine is introduced
- changes are traceable
- registers remain consistent
- PR is reviewable as a single convergence packet
