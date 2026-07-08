# Production Router Cross-Ecosystem Patch v0.1

Status: Candidate / Production Router Patch / No Runtime / No External Writeback
Use As: router patch for cross-ecosystem work before dispatching Qinyi / Hazumi / Aki / QHA / field windows
Do Not Use As: execution approval, connector approval, company workflow, runtime router, or merge approval

## Core

Before dispatch, Production Router must determine whether the task stays in its native ecosystem or crosses into another ecosystem. Cross-ecosystem routing requires explicit source, carrier, authority, gate, output surface, and return mode.

## Before Dispatch

```yaml
Production_Router_Cross_Ecosystem_Check:
  identify_source_ecosystem:
  identify_native_carrier:
  identify_target_carrier:
  check_authority:
  check_gate: []
  choose_output_surface:
  choose_return_mode:
  decide_small_build_loop:
  decide_next_reader:
```

## Signal Types

```yaml
Signal_Types:
  Native_Signal:
    meaning: "stays inside original ecosystem; no cross routing needed"
  Cross_Ecosystem_Signal:
    meaning: "must be translated, carried, and returned across ecosystem boundary"
  Red_Door_Signal:
    meaning: "security, company, private, financial, or authority risk"
  Nutrient_Signal:
    meaning: "useful vocabulary or pattern; no action by default"
```

## Routing Defaults

```yaml
Routing_Defaults:
  human_language_or_pressure:
    next_reader: "Qinyi_LOR"
    output_surface: "Vitas_Readable"
  build_card_needed:
    next_reader: "Hazumi_LOR"
    condition: "Vitas or QHA gate assigns bounded build"
  drift_or_public_safe_needed:
    next_reader: "Aki_LOR"
    condition: "risk, claim drift, private leakage, or public-facing output"
  cross_carrier_integration:
    next_reader: "XuanLing_QHA"
  field_loop:
    next_reader: "Xiaoshiguang_Field only when field source exists"
```

## Red Doors

- Router Assignment != Execution Approval.
- Cross-Ecosystem Signal != Authorized Data Transfer.
- Native Tool Boundary != QHA Boundary.
- Output Surface != Authority.
- Build Card Needed != Build Approved.

## Final Rule

Router must identify ecosystem crossing before selecting tools or LORs.