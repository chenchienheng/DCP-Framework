# Base Field Core v0.1

> Status: Candidate / usable baseline
> Placement: `03_field-governance/`
> Related issues: #135, #167, #185, #196
> Purpose: define the minimum base that lets sources, nodes, dependency
> chains, views, gates, and return paths stand without collapsing into one
> another.

---

## 0. Core

Base Field is not a table, a tool, or a single repository file.

Base Field is the minimum work foundation that keeps source, node,
dependency, view, gate, and return separated but connected.

```text
Base Field
= Source
x Node
x Dependency Chain
x View
x Gate
x Return
```

The first goal is not completeness. The first goal is non-collapse.

A base may be incomplete, but it must be traceable, rebuildable, and able to
return.

---

## 1. Non-Collapse Rule

```text
Incomplete is acceptable.
Untraceable is not.
Editable is acceptable.
Source pollution is not.
Partial is acceptable.
No return path is not.
```

Minimum condition:

```text
Every item must know:
where it came from,
what it depends on,
what it supports,
which view may read it,
which gate controls it,
and where it returns.
```

---

## 2. Six-Layer Base Field

### 2.1 Source

Source is the original input or evidence layer.

It may be a document, official source, chat note, issue, file, tool output,
spreadsheet, report, or human-verified input.

Rule:

```text
Source may generate many views.
View must not overwrite Source.
```

### 2.2 Node

Node is a locatable object inside the field.

Examples:

```yaml
Node:
  - company
  - policy
  - project
  - task
  - document
  - issue
  - pull_request
  - tool
  - adapter
  - public_interface
  - executive_view
```

A node is not valid only because it has a name. It becomes valid when its
source, dependency, view, gate, and return path are traceable.

### 2.3 Dependency Chain

Dependency chain is not a simple line. It is the judgment layer behind
linkage, continuity, dependency, coupling, loop, topology, matrix, overlay,
and cluster.

```text
linkage is not yet a chain
continuity makes the chain observable
dependency makes the chain structurally valid
coupling makes chains become a field
return calibration prevents drift
```

Before assigning category, table, or tool, ask:

```text
What does this node depend on?
What does this node support?
What continuity does it preserve?
What coupling does it create?
What loop does it return through?
Which field-view should represent it without polluting the source?
```

### 2.4 View

View is the role-specific projection of source and node data.

```yaml
View:
  examples:
    - GM_View
    - Consultant_View
    - MotherTree_View
    - Public_Interface_View
    - Task_View
    - QA_View
  rule:
    - views can filter
    - views can summarize
    - views can interpret within boundary
    - views cannot overwrite source
```

### 2.5 Gate

Gate controls whether an item may move, publish, harden, close, reopen, or
return.

```yaml
Gate:
  checks:
    - Source_View_Gate
    - Evidence_Boundary
    - Drift_Gate
    - Permission_Gate
    - Risk_Gate
    - QA_Gate
    - Closure_Gate
    - Reopen_Gate
```

A trigger is not permission. A route is not access. A draft is not a sealed
baseline. A view is not a source.

### 2.6 Return

Return keeps the base alive. An output must be able to return to a register,
issue, file, task, review point, or next-round card.

```yaml
Return:
  possible_targets:
    - MotherTree
    - Registry_Log
    - GitHub_Issue
    - GitHub_PR
    - Drive_Source_File
    - Task_System
    - Next_Round_Card
  required_fields:
    - return_target
    - return_reason
    - changed_state
    - pending_decision
    - next_action
```

---

## 3. Source / View Gate

```text
A source may generate many views.
A view must not overwrite the source.
A view may be corrected when the source is corrected.
A source must not be changed only because a view needs a cleaner story.
```

External reports, executive summaries, public posts, consultant packages, and
task boards are views. They can be useful, but they are not the source itself.

---

## 4. Internal-to-External Language Map

Internal language can stay precise inside MotherTree, Registry, and working
windows. External language must be readable by normal business users.

| Internal term | External wording | Plain meaning |
|---|---|---|
| XuanLing | cross-platform work governance architecture | method for connecting data, tasks, documents, and tools |
| spherical topology | layered work map / ecosystem map | where tools and tasks sit in the overall work map |
| invariant core | core principle / core decision rule | what cannot drift when the context changes |
| multi-chain field | multi-source and multi-task work environment | many sources, tools, documents, and tasks handled together |
| return calibration | feedback and correction mechanism | work returns for review, correction, and update |
| dependency chain | task dependency path / relationship path | how one item depends on or supports another |
| coupling | integration / connection | two systems or tasks start working together |
| loop | feedback loop | work can be checked and corrected after output |
| MotherTree | master governance register | main record of rules, versions, and decisions |
| return-chain | writeback to master record | important changes return to the main register or issue |
| Source | data source | where the original information comes from |
| View | user-facing view | version shown to a specific role or audience |
| Gate | review checkpoint | condition checked before moving forward |
| Return | feedback path | where an output returns for update or calibration |
| Source / View Gate | source-view separation rule | reports must not overwrite the original source |
| CloudTop | company knowledge base / operating data base | company capability, source, task, and knowledge base |
| Base Field | work foundation layer | base structure for sources, tasks, tools, views, and return paths |
| Qinyi Interface | public-facing AI interface / branded external interface | public-facing communication and demonstration layer |
| Closure | baseline confirmation | version can be referenced, but not necessarily frozen forever |
| Reopen | review again | reopen when new data, risk, or error appears |
| drift | deviation from target | meaning, role, evidence, or task has moved off target |

External output rule:

```text
Do not expose internal architecture terms directly in business, public,
consultant, or company-facing outputs unless the audience has already been
onboarded.
```

Use ordinary work language:

```text
work architecture
data foundation
governance process
decision view
feedback mechanism
review checkpoint
source separation
```

---

## 5. Base Routing Examples

### 5.1 Government Source

```yaml
Input: national policy or statistics source
Layer: Source
View:
  - market_background
  - policy_context
Gate:
  - cannot become company intent
  - cannot become project opportunity without hardening
Return:
  - source_ledger
  - strategy_matrix
```

### 5.2 Company Capability

```yaml
Input: company capability, office, project record, or support signal
Layer: Node / Source
View:
  - GM_View
  - Consultant_View
Gate:
  - capability is not cooperation willingness
  - support signal is not confirmed resource
Return:
  - CloudTop
  - evidence_matrix
```

### 5.3 GitHub Registry Note

```yaml
Input: issue comment, PR, rule candidate, registry log
Layer: Return / Gate
View:
  - MotherTree_View
  - Window_Operating_View
Gate:
  - not company data
  - not public-facing output by default
Return:
  - MotherTree
  - Registry_Log
```

### 5.4 Public Interface Output

```yaml
Input: internal architecture or method
Layer: View
View:
  - Public_Interface_View
Gate:
  - translate internal language
  - remove private material
  - avoid exposing full dependency chain
Return:
  - public_content_review
  - MotherTree_if_structural_change_appears
```

---

## 6. Build Order

Do not build a large table first. Build the base in this order:

```yaml
Build_Order:
  1: Base_Field_Core
  2: Source_View_Gate
  3: Dependency_Chain_Reading_Rule
  4: Internal_External_Language_Map
  5: View_Layer_Map
  6: Return_Path_Schema
  7: Minimal_Router_Launcher
```

Each step must remain small enough to be reviewed and rebuilt.

---

## 7. Keep / Split / Do Not Do

```yaml
Keep:
  - source_node_view_gate_return_separation
  - dependency_chain_reading
  - external_language_translation
  - return_path_requirement
  - rebuildable_baseline

Split_Out:
  - company_sensitive_source_data
  - full_market_point_cloud_data
  - public_facing_copywriting
  - detailed_private_identity_rules
  - tool_specific_implementation_steps

Do_Not:
  - do not rewrite DCP
  - do not seal this as final doctrine
  - do not mix company data with registry governance
  - do not treat GitHub as system ontology
  - do not treat Drive as MotherTree
  - do not treat Qinyi as the full architecture
  - do not turn Pending into Fact
  - do not turn capability into cooperation willingness
  - do not turn investment into project opportunity
```

---

## 8. Current Decision

```yaml
Decision: Conditional_Go
Reason:
  - Base Field Core is usable as a minimum foundation.
  - It is intentionally incomplete but structurally rebuildable.
  - It avoids direct closure and avoids company/private data.
  - It provides a stable path for later Source, View, Gate, and Return files.
Next_Action:
  - register this file in repository index
  - decide whether Source_View_Gate should split into a separate file
  - decide whether Dependency_Chain_Reading_Rule becomes registry log or file
Return_Path: Issue #196 -> PR -> MotherTree review -> Registry / hardening map
```
