# Image Generation Validation — Historical Failure Lineage

> Lifecycle: `HISTORICAL_REFERENCE`
> Current eligibility as node/runtime contract: `false`
> Runtime: `false`
> Authority: `none`

This document preserves useful failure observations from an earlier ChatGPT_Image_2 node experiment. The fixed AXIS-01/AXIS-05 routing, master asset-node return, repository register requirement, and automatic regeneration loop are retired.

## Retained findings
- image generation may satisfy style instructions while drifting from the intended subject identity;
- identity-sensitive work needs explicit lawful reference evidence rather than assumed intrinsic model memory;
- successful generation does not prove artifact quality, identity fidelity, publication approval or durable writeback;
- repeated regeneration without changed constraints/evidence can reproduce the same failure;
- output verification should examine the actual requested effect and task-specific defects before downstream use.

## Current handling
For a material image task:
1. resolve the subject/reference authority and allowed reference set;
2. bind requested transformation and variation tolerance;
3. generate/edit through the available authorized carrier;
4. compare the output against material identity/geometry/text/style constraints;
5. record mismatch evidence and decide whether to revise, regenerate, HOLD, reject or return;
6. treat any storage/publication/writeback as a separate authorized action.

`Image generated != Identity matched`
`Identity matched != Asset approved`
`Asset approved != Public approved`
`Carrier capability != Publication/writeback authority`

Use `VISUAL_IDENTITY_ANCHOR_SPEC.md` only as an evidence-bounded continuity reference. Full predecessor validation details remain in Git history.
