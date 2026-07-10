# Carrier-Reconstructed Thread Protocol v0.1

Status: Candidate / Continuity Experiment / No Runtime / No Hidden Chat Access / No External Writeback
Owner: Vitas
Primary Reader: XuanLing_QHA

## One Core

A contract card cannot give a model platform-level access to hidden or archived ChatGPT conversations. It can, however, turn an accessible carrier set into a **reconstructable work thread** that can be opened, read, continued, and returned by Chat, Work, Codex, or another authorized tool.

## 1. Thread Definition

A work thread is not a conversation transcript.

```yaml
Carrier_Work_Thread:
  thread_id:
  title:
  source_anchor:
  sovereignty_holder:
  support_authority:
  responsible_actor:
  cost_bearer:
  time_state:
  active_pointer:
  source_refs: []
  current_claim:
  evidence_refs: []
  telemetry_refs: []
  blocked_items: []
  next_reader:
  expected_output:
  return_to:
  not_to_claim: []
```

## 2. Open Thread Protocol

```text
1. Verify carrier access.
2. Read public DCP root and bootstrap.
3. Read Active Work Thread Index.
4. Open only the listed source refs.
5. Confirm sovereignty / responsibility / cost / time state.
6. Continue one bounded action.
7. Write evidence and a return pointer.
8. Update the thread state; do not rewrite the whole history.
```

## 3. Read Thread Protocol

A reader must return:

```yaml
Thread_Read_Proof:
  thread_id:
  files_or_issue_read: []
  reconstructed_state:
  known_facts: []
  unresolved_items: []
  active_decision:
  next_reader:
  trigger:
  expected_output:
  confidence:
  missing_context: []
```

If required context is absent, mark `Missing Context` rather than asking Vitas to repost the full history by default.

## 4. Continue Thread Protocol

A continuation may do only one of:

- classify
- draft
- build candidate
- audit
- verify evidence
- update pointer
- request human decision
- archive / supersede candidate

Every continuation must produce:

```yaml
Thread_Return:
  changed:
  evidence:
  telemetry:
  reason:
  affected_refs: []
  next_state:
  next_reader:
  return_check:
```

## 5. GitHub Thread Surfaces

```yaml
GitHub_Thread_Surfaces:
  Branch:
    role: "bounded candidate workspace"
  Markdown_File:
    role: "contract, state, evidence, or pointer"
  Issue:
    role: "durable discussion / decision / work-thread surface"
  Pull_Request:
    role: "bounded change proposal and review thread"
  Commit:
    role: "versioned evidence of file change"
```

No surface is final authority by itself.

## 6. Chat / Work / Codex Mapping

```yaml
Modes:
  Chat:
    role: "live intake, semantic correction, human alignment"
  Work:
    role: "long-running thread orchestration across accessible carriers"
  Codex:
    role: "bounded implementation, repo diff, test, and code return"
```

The same thread may be continued across modes only through shared carrier pointers.

## 7. Archive Rule

Old ChatGPT conversations may be moved to a project or archive as historical source material.

They are not required for normal continuation when all active state has been compressed into:

- bootstrap
- active pointer
- source refs
- evidence / telemetry
- decision queue
- return check

Archive does not equal deletion, and history does not remain active merely because it exists.

## 8. Red Doors

- Contract Card != Hidden Thread Access.
- Thread Reconstruction != Transcript Recovery.
- Issue Opened != Work Accepted.
- Reader Named != ACK.
- Commit Exists != Review Passed.
- PR Opened != Merge Approval.
- Active Pointer != Full Evidence.
- Archive != Forgetting.
- Continuation != Authority Transfer.

## 9. Success Criteria

The experiment passes when a new authorized session can:

1. read the bootstrap and active index;
2. reconstruct the current work state without old chat transcripts;
3. identify sovereignty, responsibility, cost, and next return;
4. perform one bounded action;
5. leave a return that another session can read.

## Final Rule

The goal is not to imitate Codex by pretending to read inaccessible conversations. The goal is to make work continuity independent of any single conversation through carrier-reconstructed threads.