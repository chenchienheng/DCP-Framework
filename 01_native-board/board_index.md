# Native Board Index

Department: Native Board
Agent Block: Board Index
Node ID: NBD-001
Window: W0
Platform Writer: ChatGPT
Version: v0.1
Status: active
Coupling Face: Event

## Core
This is the primary entry board for runtime routing, blockers, follow-up, and logs.

## Sections
1. runtime_status
2. blockers
3. task_follow_up
4. latest_logs
5. adapter_status

## Routing
- task_follow_up -> 02_runtime_ops/task_follow_up.md
- blockers -> 01_native-board/blockers.md
- adapter_layer -> 04_adapter-layer/

## Runtime Status
- mode: GitHub-native-first
- board_state: seed
- writeback_gate: enabled
- external_layers: staged

## Notes
- This board is the primary read entry for Gamma.
- Replit may use this board as the first interaction relay entry.
