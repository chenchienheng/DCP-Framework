# External Signal Entry Chain Specification

Department: Adapter Layer / Core
Node Type: External Signal Entry Node
Version: v0.1

## Core Purpose
Define a tool-agnostic external signal entry chain for all inbound external
triggers. This specification treats messaging platforms, web inputs,
webhook/API inputs, crawler inputs, telecom signals, and IoT sensor signals
as interchangeable entry nodes rather than unique or isolated integrations.

## Axis Mapping
- **Primary Axis:** AXIS-01 (World Chain) - Universal entry point.
- **Secondary Axis:** AXIS-05 (Review Chain) - Universal fallback/failure gate.

## Common Fields Definition
Every external entry node must declare the following parameters to be
considered compliant with the runtime:

- `entry_type`: The category of the inbound signal (messaging, webhook, sensor).
- `platform_or_protocol`: The specific service or standard (LINE, HTTP, SMS).
- `signal_format`: The structural format of the inbound data (JSON, Plaintext).
- `authentication_boundary`: How the signal proves its origin or authorization.
- `cost_or_quota_constraint`: Strict bounds on execution cost and rate limits.
- `primary_axis`: Must be AXIS-01.
- `secondary_axis`: AXIS-05 or specific internal routing chain.
- `review_path`: The mandatory gateway for signal verification before action.
- `return_path`: The destination for logs, output, or writeback archiving.
- `return_failed`: Must route to AXIS-05 for human/manual recovery.
- `replaceability_rule`: The exact mechanism by which this entry node can be
  swapped for an equivalent node without causing runtime collapse.

## Example Mapping Table

| Node | Entry Type | Format | Replaceability |
|---|---|---|---|
| LINE | Messaging | JSON | Swappable with WhatsApp/Telegram |
| Webhook | API Trigger | JSON | Bound to API contract |
| IoT Sensor | Sensor Data | MQTT | Standardized numeric mapping |
| Email Inbox | Comm. | MIME | IMAP protocol standardization |

## Analysis

### Mismatch or Gap
- The current runtime heavily couples platform-specific details (e.g. tokens)
  too early in the flow. A generic abstraction layer must exist between the
  raw inbound payload and the internal logic queue.
- Authentication boundaries for webhooks often require immediate responses
  (e.g., HTTP 200 OK) which conflicts with asynchronous review cycles.

### Unresolved Risks
- **Signal Flooding:** Without a standardized rate-limiter at the edge of
  the chain, the system is vulnerable to cascading failure from rapid external
  signals (e.g., bot floods, sensor malfunctions).
- **Format Drift:** External APIs or signal structures may change without
  warning, breaking the entry chain if schema validation is not strictly
  enforced at the boundary.

### Boundary Rate Limiting Requirement (Candidate)
External signals entering the chain must pass through an edge limiter before being accepted into downstream routing. **Note: Until implemented, this remains a candidate security requirement and not runtime protection.**

The expected control semantics for the edge limiter are:
- **Per-source Rate Limit:** A strict cap on the number of signals per source (e.g., per IP, API key, or origin identifier) within a defined time window.
- **Burst Threshold:** An allowable burst capacity that slightly exceeds the standard limit for brief intervals before triggering limits.
- **Cooldown / Backoff:** An enforced waiting period or exponential backoff applied to sources exceeding their threshold.
- **Queue or Drop Behavior:** A defined policy determining whether excess signals are placed in a holding queue (for asynchronous retry) or immediately dropped.
- **Priority Override:** Trusted sources or manual operator interventions may bypass standard limits under controlled conditions.
- **Logging / Audit Trail:** Every rate-limit trigger must generate an auditable log entry for monitoring bot floods or sensor malfunctions.
- **Failure Mode:** If the rate limiter itself fails, it should default to a "fail-closed" or highly restricted state to prevent cascading failure of the primary chain.
- **Return Path:** Blocked or flooded signals should return an explicit "rate-limited" status to the origin and route a failure notification to AXIS-05 for human review.

### Schema Validation Requirement (Candidate)
External signals entering the chain must be strictly validated against a defined schema template at the boundary before processing. **Note: Until implemented, this remains a candidate security requirement and not runtime protection.**

The expected control semantics for the schema validation are:
- **Strict Typing and Structure:** All inbound payloads must match an explicit structure (e.g., required headers, body fields, and metadata). Unknown fields must be rejected or stripped.
- **Boundary Rejection/Hold:** Payloads failing schema validation must be immediately rejected at the entry node or held in a dead-letter queue. They must not propagate to the primary AXIS-01 track.
- **Error Handling & Return Path:** A standardized error response must be returned to the origin when possible, and failure notifications routed to AXIS-05 for human review.
- **Evidence Logging:** Every schema rejection must generate a sanitized log entry (without recording potentially malicious payload bodies) to detect format drift or targeted fuzzing.
- **Schema Versioning:** The validation template must enforce versioning to allow controlled transitions when external APIs update their formats, mitigating unexpected breakage.

**Minimal Example Validation Template:**
```json
{
  "entry_node_id": "REQ-String",
  "payload_version": "REQ-String(v1.0)",
  "timestamp": "REQ-ISO8601",
  "data": "REQ-Object(StrictSchema)",
  "metadata": "OPT-Object"
}
```
*Note: Any payload missing required fields or containing invalid types must be dropped and logged. This is an architectural spec; no CVE or dependency advisory applies here.*

### Next Single Recommended Action
- Create a lightweight schema validation template for inbound payloads that
  can be applied universally to all entry nodes before they are allowed onto
  the primary AXIS-01 track.
- Define a standard rate-limiter and cost-bounding template at the edge of
  the chain to mitigate signal flooding and cascading failures.
