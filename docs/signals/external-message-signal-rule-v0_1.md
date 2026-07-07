# External Message Signal Rule v0.1

Status: Candidate / Signal Intake Rule / No Runtime / No External Writeback
Use As: rule for digesting external promotional messages as low-trust signal material
Do Not Use As: vendor approval, reply instruction, procurement signal, subscription approval, or trust rating

## Core

An external promotional message is not automatically useful and not automatically trustworthy. It may still contain market vocabulary, risk framing, or boundary lessons.

## Classification

```yaml
External_Message:
  source_type: "low-trust external signal"
  commercial_intent: true
  adoption_required: false
  reply_required: false
  useful_signal_possible: true
  default_intake_category: "External_Signal / Archive_Only unless material"
```

## Digest Rule

```yaml
Digest_Rule:
  - "Commercial intent does not invalidate signal value."
  - "Absorption is not adoption."
  - "Useful signal is not source trust."
  - "Reading is not engagement."
```

## Extract

```yaml
Extract:
  - "assumed pain point"
  - "problem vocabulary"
  - "requested disclosure"
  - "red door suggested"
  - "carrier registry rule affected"
```

## Red Doors

- External Message != Trusted Source.
- Reading != Engagement.
- Commercial Signal != Adoption.
- Source Claim != Verified Fact.
- Useful Vocabulary != Source Trust.
- External Message != QHA Mainline Task.

## Final Rule

QHA can absorb external messages into signal nutrients and red doors, but must not route them to action, reply, adoption, or procurement without Vitas decision.