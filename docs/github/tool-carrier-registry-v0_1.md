# Tool Carrier Registry v0.1

Status: Candidate / Tool Carrier Registry / Not Approved / No Runtime
Related: #301

## Core

Tools are carriers. A tool being available does not mean it is authorized for action.

## Registry

```yaml
Tool_Carriers:
  GitHub:
    role: "repo, issue, PR, docs, schema, return packet carrier"
    access_verified: true
    write_allowed: "only within authorized repos"
    runtime_allowed: false
  Codex:
    role: "code/docs/schema construction support candidate"
    access_verified: "partial / via GitHub and external handoff"
    runtime_allowed: false
  Jules:
    role: "cloud construction candidate"
    access_verified: false
    runtime_allowed: false
  Copilot:
    role: "coding-side assistant candidate"
    access_verified: false
    runtime_allowed: false
  Replit:
    role: "prototype runtime candidate"
    access_verified: false
    runtime_allowed: false
  Linear:
    role: "work item planning carrier candidate"
    access_verified: false
    runtime_allowed: false
  Google_Cloud:
    role: "cloud infrastructure candidate"
    access_verified: false
    runtime_allowed: false
```

## Red Doors

- Tool available != Tool authorized.
- Connector visible != write permission.
- Prototype runtime != production runtime.
- GitHub issue != agent runtime.
- External carrier != source authority.

## Promotion Gate

A tool can move from candidate to active only after access is verified, carrier role is defined, authority is assigned, data boundary is defined, return path exists, and human approval is recorded.
