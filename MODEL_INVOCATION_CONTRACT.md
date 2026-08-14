# Model Operation Contract

> Lifecycle: `PUBLIC_RESEARCH_REFERENCE`
> Runtime: `false`
> Native source root: `false`
> Authority: `none`

This document preserves carrier-neutral primitives for bounded model participation. It does not define a fixed window topology, a required repository writeback target, or a model-owned authority domain.

## 1. Core rule
A model operation is a bounded transformation over authorized sources. It may produce a candidate, analysis, projection, audit, translation, or proposed action, but it does not acquire authority merely by executing successfully.

`Model capability != authority`
`Output != admission`
`Readable source != mutable source`
`Carrier availability != write-back authorization`

## 2. Minimum operation fields
A high-value model operation should be representable with:

- `operation_id`
- `timestamp`
- `receiver_or_owner`
- `model_or_capability`
- `structural_role`
- `source_refs`
- `source_authority`
- `allowed_scope`
- `rights_privacy_boundary`
- `evidence_refs`
- `expected_output_type`
- `claim_ceiling`
- `mismatch_or_gap`
- `contradiction_flag`
- `proposed_action`
- `action_authority`
- `return_target`
- `rebuild_or_reentry_refs`

## 3. Source and scope gate
Before operation:
1. resolve the actual source/carrier;
2. identify who owns meaning and mutation authority;
3. bound what may be read, transformed, retained, or written back;
4. separate facts, inferences, candidates, and unknowns;
5. refuse silent scope expansion.

## 4. Contradiction primitive
Contradiction is signal, not automatic failure. Record it when:
- output conflicts with source evidence;
- output exceeds its assigned role or claim ceiling;
- two bounded operations materially disagree under comparable evidence;
- confidence exceeds evidence quality;
- proposed action conflicts with authority, rights, privacy, or current state.

Recommended handling:
- `compare_sources`
- `recheck_scope`
- `downgrade_confidence`
- `request_authority_decision`
- `preserve_disagreement_as_signal`
- `rebuild_from_last_valid_state`

## 5. Action gate
A model result may propose an action. Execution requires a separate action-authority check. Successful reasoning, generation, or tool availability does not imply permission to mutate a source, carrier, repository, runtime, or external system.

## 6. Return and rebuild
Every material operation should identify where its useful delta returns and what evidence permits later reconstruction. A return packet is not Closeout by itself; it remains subject to receiver reconciliation and any required admission or authority gate.

## 7. Historical compatibility
Earlier versions used fixed `owner_window`, `00` escalation, model-family/window tables, and repository-centric writeback. Those are historical implementation framings, not universal invariants. Historical detail is retained in Git history and `archive/model-operation-generation/README.md`.

## 8. Public-surface ceiling
This file is a public research/reference surface only. Protected semantic-core state, runtime leases, private evidence, and Native Sphere authority remain outside this document.
