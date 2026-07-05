# Signal Level Model v0.1

Status: Candidate / Signal Governance / No Runtime

## Core

Signal level describes how much attention and governance response a signal deserves. It is not approval and not action authorization.

## Levels

```yaml
Signal_Levels:
  L0_Noise:
    meaning: "low relevance or transient noise"
    action: "ignore or archive"
  L1_Watch:
    meaning: "worth watching, not yet structural"
    action: "track lightly"
  L2_Governance:
    meaning: "affects boundary, tool, cost, data, authority, or process"
    action: "create red-door or contract candidate"
  L3_Strategic:
    meaning: "affects market, infrastructure, family enterprise, or long-term positioning"
    action: "return to Vitas judgment matrix"
  L4_Red_Door:
    meaning: "potential immediate boundary or authority risk"
    action: "manual review required"
```

## Red Doors

- Signal Level != Decision.
- L3 Strategic != Investment Approval.
- L4 Red Door != Automatic Rejection.
- Watch Signal != Build Input.

## Return Rule

Each signal level must return to the correct carrier: archive, watchlist, red-door registry, Vitas decision queue, or domain pack candidate.
