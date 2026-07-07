# Repo Internal Alignment Protocol v0.1

Status: Candidate / Repo Alignment Protocol / No Runtime / No External Writeback
Use As: minimum rule for making each repository internally aligned before cross-repo circulation
Do Not Use As: approved doctrine, merge approval, runtime automation, public release, or deletion instruction

## Core

A chain is not real if repository contents only accumulate. Each repository must have an internal alignment layer that separates current active files, superseded files, domain files, templates, red doors, return packets, and output candidates.

## Alignment Questions

Every repository must answer:

```yaml
Repo_Alignment_Check:
  repo_role:
  canonical_current_files: []
  active_pointers: []
  superseded_or_reference_files: []
  domain_or_fieldspace_files: []
  templates: []
  red_doors: []
  return_paths: []
  output_candidates: []
  not_to_claim: []
```

## Internal Layers

```yaml
Internal_Layers:
  00_Index:
    purpose: "current map and active pointers"
  Core_or_Root:
    purpose: "repo-specific root rules"
  Governance:
    purpose: "red doors, gates, containment"
  Templates:
    purpose: "reusable return / schema / manifest templates"
  Returns:
    purpose: "bounded return packets and summaries"
  Archive_or_Superseded:
    purpose: "old or replaced material, not current truth"
```

## Red Doors

- Repo File != Current Truth.
- Candidate File != Approved Doctrine.
- Internal Alignment != Merge Approval.
- Superseded != Deleted.
- Archive != Approved.
- Output Candidate != Public Release.
- Fieldspace File != Open Core.

## Final Rule

Before QHA routes a repository as a carrier, it must know what is active, what is superseded, what is internal-only, what is field-specific, and what can be used as an output candidate.