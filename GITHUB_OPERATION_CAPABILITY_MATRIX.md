# GitHub Operation Capability Snapshot

> Lifecycle: `OBSERVED_CAPABILITY_REFERENCE`
> Runtime authority: `none`
> Snapshot truth: time-bounded only

This file records observed connector/tool capabilities for repository work. It is not a durable capability truth, permission grant, execution mandate, or architecture layer. Tool surfaces change over time and must be re-verified when a material operation depends on them.

## Current rules
- `Tool exposes operation != User authorized operation`
- `Capability observed once != Capability guaranteed later`
- `Repository permission != Task authority`
- `Successful API call != Runtime proof`
- `Missing convenience action != Operation impossible`

## Observed classes
Depending on the active connector surface, useful operations may include bounded file read/write, PR/issue interaction, commit comparison, workflow inspection, repository metadata, and tree/content retrieval. Availability must be checked at execution time.

A recursive repository tree census has been observed through the GitHub tree API path in this successor review, so the older claim that whole-tree enumeration was unavailable is retired.

## Mutation boundary
Create/update/delete/merge/label/comment or other mutations require both:
1. an actually available tool operation; and
2. explicit authority for that task and scope.

Where only read access is authorized, mutation capability remains irrelevant.

## Capability drift handling
When a workflow depends on an external tool capability:
- verify the current connector/action and repository identity;
- record relevant failure/availability evidence;
- do not infer availability from an old matrix;
- degrade or HOLD affected work if the required capability is missing;
- preserve a replacement/manual path where material.

## Historical notes
Earlier versions listed a concrete menu of create/update/delete/branch/merge/rename limitations and ended with `return_to_00=true`. Those observations were session-specific and are retained in Git history only.
