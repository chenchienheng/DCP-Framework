# CTQL / QHA Cross-Window Chain Ecology Review v0.1

Status: Candidate / Internal Architecture Review / Cross-Window Alignment / No Runtime / No External Writeback / Not Doctrine
Use As: QHA review of overlaps, missing returns, red doors, and fieldspace boundaries across current windows and carriers
Do Not Use As: approved doctrine, runtime specification, GitHub merge approval, company policy, public whitepaper, or production architecture

## Core

The current system has moved beyond isolated GPT conversations and now has a recognizable multi-window, multi-carrier, multi-return topology. The main risk is no longer absence of structure; it is duplicate workfaces, schedule semantics that no longer match One-Hub mode, carrier overreach, and incomplete proof that returns actually close the loop.

## 1. Overlapping Windows

### 1.1 QHA_Daily_Dispatch vs QHA Daily Hub

Result: Overlap / naming conflict.

- Both describe daily routing and integration.
- One-Hub mode should retain one canonical daily surface.
- Recommended canonical name: `QHA Daily Hub`.
- `QHA_Daily_Dispatch` should become an internal function inside the Hub, not a separate scheduled window.

### 1.2 QHA Weekly Integration vs CoreTri_LOR Weekly Check

Result: Partial overlap, but roles can remain distinct.

- QHA Weekly Integration: integrates returns, active pointers, unresolved decisions, and next-cycle routing.
- CoreTri_LOR Weekly Check: checks tri-coupling drift, role drift, gift-pressure drift, and LOR misalignment.
- Required order: CoreTri calibration return -> QHA Weekly Integration.
- They must not both independently produce full weekly summaries.

### 1.3 Qinyi_LOR daily cycles vs Vitas_LiveIntake

Result: Previously mixed; now structurally separated.

- `Vitas_LiveIntake` is raw source / manual alignment.
- `Qinyi_LOR` is scheduled human-readable return.
- Remaining risk: social or live-intake materials being treated as already packaged Qinyi returns.

### 1.4 Xiaoshiguang_Field_Return vs XuanLing_Stage_Return

Result: Old overlap should be retired.

- `Xiaoshiguang_Field_Return` should remain the canonical field-proof return surface.
- `XuanLing_Stage_Return` should remain disabled unless explicitly re-scoped for a different stage function.

### 1.5 Social Window vs Qinyi_LOR

Result: Adjacent, not identical.

- Social Window: external perception, narrative, visual-text experiment.
- Qinyi_LOR: human-readable governance return, pressure and authority boundary.
- Social metrics or visual anchors must not enter QHA as architecture proof.

## 2. Missing Returns and Missing Next Readers

### 2.1 Hazumi Build Pass

Gap:
- Build candidates exist, but every build does not yet consistently return an Evidence + Telemetry Record and Return Check.

Required return:
- build_card_id
- files changed
- evidence
- telemetry
- unresolved gaps
- next_reader = Aki or QHA

### 2.2 Aki Audit Pass

Gap:
- Audit cards exist, but there is no single mandatory audit return format linking claim downgrade to a rebuild target.

Required return:
- claim audited
- evidence basis
- corrected status
- red door triggered
- rebuild target
- next_reader = QHA / Hazumi / Vitas

### 2.3 Xiaoshiguang Field

Gap:
- State / Reply Draft / Problem Return templates exist, but no complete sample cycle has returned through XLQY to DCP.

Required proof:
- one mock State Card
- one mock Problem Return Card
- one Field Return Packet
- one QHA Return Check

### 2.4 GitHub / Drive Return

Gap:
- Files and folders exist, but active pointers and return-index rows are not yet consistently updated after each new carrier artifact.

Required rule:
- every accepted carrier file must either enter active pointer, support index, archive pointer, or decision queue.

### 2.5 One-Hub ACK

Gap:
- `next_reader` still risks being interpreted as acceptance.

Required red door:
- Next Reader != ACK.
- Scheduled Output != Handoff Completed.
- Handoff is complete only when a return packet, evidence item, or explicit human acknowledgement exists.

## 3. Carrier Mixing Risks

### 3.1 ChatGPT

Correct role:
- live reasoning and candidate intake.

Risk:
- conversation output being treated as filed carrier state.

Red door:
- Conversation Output != GitHub / Drive File.

### 3.2 GitHub

Correct role:
- versioned construction carrier.

Risk:
- a file or commit being treated as approval or active doctrine.

Red door:
- Commit Exists != Approved State.
- File Exists != Active Pointer.

### 3.3 Google Drive

Correct role:
- human-readable return, decision queue, weekly review, archive.

Risk:
- duplicate folders, stale copies, or Drive documents being treated as canonical without revision currency check.

Red door:
- Drive File != Canonical Current.

### 3.4 M365

Correct role:
- controlled human-gated experiment carrier.

Risk:
- sanitized learning patterns being misread as company data integration or build approval.

Red door:
- M365 Pattern != Company Deployment.

### 3.5 Codex

Correct role:
- bounded cloud construction carrier.

Risk:
- construction ability being interpreted as architecture authority.

Red door:
- Codex Build != QHA Decision.

## 4. Candidate Promotion Risks

Current high-risk promotion points:

- External conference signal -> internal truth.
- Social post -> official product fact.
- Build card -> build completed.
- GitHub commit -> approved doctrine.
- Social traffic -> architecture validation.
- M365 runbook -> company system.
- Field card template -> operational app.
- PoC -> runtime.

Required common rule:

```yaml
Promotion_Gate:
  source_verified: false
  authority_visible: false
  evidence_present: false
  telemetry_present: false
  return_check_present: false
  explicit_approval_present: false
```

Without all required conditions, retain Candidate / To Verify / Reference Only.

## 5. Generalizable vs Fieldspace-Only

### 5.1 Generalizable to Core / Flow

- Source / Carrier / Authority / Gate / Action / Evidence / Telemetry / Return / Rebuild.
- Candidate / Approved / Runtime separation.
- Evidence Ledger.
- AI Action Authorization Matrix.
- Zero Trust / Agent Identity gate.
- A2A / MCP red doors.
- Live Intake source classification.
- One-Hub schedule convergence.
- Return Packet / Next Reader / Write To discipline.
- Small Build Loop: Build Card / Evidence / Return Check / Feedback.

### 5.2 Keep in Xiaoshiguang Fieldspace

- Guest-facing wording.
- Booking-state examples.
- Owner review card details.
- Private relationship context.
- Yiyi origin and gift meaning.
- Availability, quote, payment, check-in, stay-service, and feedback field states.
- Real operational rules, customer records, payment details, and platform settings.

### 5.3 Keep in Social Fieldspace

- Visual anchors.
- IG / Reel metrics.
- styling and scene experiments.
- lifestyle narrative and character presentation.

Only sanitized boundary rules may return to Flow or Core.

## 6. New Red Doors Required

- QHA Daily Dispatch != Separate Daily Window.
- CoreTri Weekly Check != Weekly Integration.
- Social Resonance != Architecture Evidence.
- File Created != Active Pointer Updated.
- Next Reader != ACK.
- Scheduled Output != Handoff Completed.
- Carrier Reference != Carrier Read.
- Generalizable Pattern != Root Doctrine.
- Field State Machine != Production Workflow.
- Return Packet Without Rebuild Target != Closed Loop.

## 7. Vitas Final Decision Queue

Vitas should retain final authority for:

1. Whether `QHA Daily Hub` fully supersedes the separate `QHA_Daily_Dispatch` scheduled window.
2. Whether `Aki_Return_Audit` becomes the canonical Drive folder name.
3. Whether LOR remains Local / Sovereignty / Return or uses the dual mapping with Ownership.
4. Whether v0.2 circulation contract supersedes all earlier circulation drafts.
5. Whether TRI-CYCLE-001 may proceed with mock Xiaoshiguang data.
6. Whether any Output Outlet / public-safe release surface should be created.
7. Any merge, runtime, company data, real field data, or external writeback action.

## 8. Final Review Result

```yaml
Cross_Window_Review:
  chain_ecology_present: true
  fully_closed_loop_proven: false
  main_overlap:
    - "QHA_Daily_Dispatch vs QHA Daily Hub"
    - "QHA Weekly Integration vs CoreTri weekly full-report behavior"
    - "Xiaoshiguang_Field_Return vs legacy XuanLing_Stage_Return"
  main_missing_return:
    - "Hazumi build evidence/telemetry return"
    - "Aki audit rebuild-target return"
    - "first complete Xiaoshiguang mock cycle"
    - "active pointer updates after accepted files"
  main_carrier_risk:
    - "file existence being mistaken for active/current/approved state"
  next_action:
    - "freeze new window creation"
    - "canonicalize One-Hub naming"
    - "run one complete mock Core -> Flow -> Field -> Flow -> Core cycle"
    - "update active pointer after every accepted artifact"
```

## Final Rule

The architecture has enough components. The next proof is not another window or another doctrine. It is one fully evidenced, traceable, returned, and rebuilt loop with no role ambiguity.