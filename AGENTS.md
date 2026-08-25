# AGENTS.md｜Repository Agent Rules

## Repository Role

This repository is a public DCP-oriented CoreTri projection carrier. It preserves repository revisions and bounded public evidence; it is not the DCP Native Source Root, Native Current, Canon, or Architecture Authority.

For repository work, use `CURRENT-SURFACE-MANIFEST.json` for repository-local reader routing and open only the affected surface. This file governs repository operations only; it does not grant semantic, Native, release, or promotion authority.

Agents working in this repository are bounded review, cleanup, test, and minimal-patch carriers only.

## Allowed Work

Agents may:
- inspect pull request diffs;
- list changed files;
- identify mergeability blockers;
- identify out-of-scope file changes;
- preserve already-merged content from `main`;
- keep pull requests within the requested scope;
- propose minimal safe patches;
- apply minimal edits only when explicitly requested;
- run safe local checks when available.

## Not Allowed

Agents must not:
- redefine core architecture;
- create new architecture axes;
- rewrite core doctrine;
- modify identity-core documents unless explicitly requested;
- convert documentation into runtime behavior;
- introduce API, database, background execution, or automation semantics unless explicitly requested;
- merge pull requests automatically;
- remove architecture content without explicit instruction;
- promote pending concepts into finalized doctrine.

## Governance Roles

- Task-selected models and agents are replaceable, scope-bounded carriers; their names do not establish fixed roles or Authority.
- Repository maintenance executors may inspect, patch, test, and return evidence only within the granted task scope.
- GitHub is the repository revision/evidence carrier and pull-request gate; it is not the Native Source Root or Architecture Authority.
- Final approval and merge authority remain with the user or another explicitly named human authority.

## Review Gates

Before editing, check:
1. What pull request or branch is the target?
2. What files are in scope?
3. What files are outside scope?
4. What already-merged content must be preserved?
5. What is the minimum safe patch?

## Scope Rules

If a pull request includes files outside scope:
- report diff pollution;
- propose removing the file from the pull request diff;
- do not rewrite the file unless explicitly instructed.

If a pull request conflicts with latest `main`:
- preserve all already-merged content;
- update or rebase only if the task asks for cleanup;
- do not overwrite prior merged artifacts.

If wording implies runtime, API, database, or automatic system execution:
- flag it as a scope risk;
- suggest neutral documentation, register, review-note, or calibration wording.

## Default Output Format

Always respond with:

- Status: PASS / HOLD / BLOCK
- Changed files:
- Out-of-scope files:
- Risks:
- Minimal patch:
- Needs human decision: YES / NO

## Final Rule

Do not merge automatically. Final approval remains with the user.
