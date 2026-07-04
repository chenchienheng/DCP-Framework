# Xiaoshiguang App｜Codex / Hazumi Handoff v0.1

Status: Candidate / BuildReady Handoff / Public-safe / No Runtime / No Customer Data

## 0｜一句核心

This handoff prepares Codex / Hazumi construction without exposing customer data or granting production authority.

## 1｜Construction Scope

Allowed construction targets:

- GUI Web App / PWA prototype
- role-based UI modes
- Supabase schema candidate
- RLS tests
- availability checking logic
- message draft templates
- staging deployment config without secrets
- documentation

Forbidden construction targets:

- production deployment without owner approval
- real customer database
- LINE auto-send
- payment processing
- OTA integration
- service key commits
- `.env` commits

## 2｜Source Package

Use sanitized candidate artifacts only:

- v0.6 Backend Authority-Safe artifact
- v0.7 Authority Lock Contract
- Official source list without private data
- Photo import rules
- Privacy boundary rules

Do not use:

- customer screenshots
- real bookings
- private LINE messages
- payment details
- unapproved social media imports

## 3｜Implementation Priority

1. Keep GUI simple.
2. Implement Mom_Mode / Yiyi_Mode / Maintainer_Mode.
3. Connect Supabase only in staging.
4. Verify maintainer cannot read customer PII.
5. Keep LINE reply as draft-only.
6. Build tests for double-booking prevention.
7. Prepare owner approval checklist.

## 4｜Testing Gate

Required tests:

- no-check no-available-reply
- no-room no-confirm
- existing booking blocks available reply
- hold blocks second hold
- block date blocks booking
- expired hold requires human review
- cancellation requires reason
- maintainer cannot select guests
- maintainer cannot export bookings
- unauthenticated cannot access app

## 5｜Return Packet

Return_Packet:
  version: "v0.1"
  completed:
    - files_changed
    - tests_added
    - gates_implemented
  pending:
    - owner_decisions
    - pricing_table
    - real_room_mapping
  risks:
    - pii_access
    - line_entry_visibility
    - public_repo_leakage
  evidence:
    - test_output
    - diff_summary
    - screenshots_without_pii
  next_action:
    - owner_review
    - staging_deploy
    - rls_test

## 6｜No Authority Override

Codex / Hazumi may construct; they do not approve runtime.  
Vitas / Qinyi may review; they do not override Yiyi.  
GitHub may store code; it does not own the business data.
