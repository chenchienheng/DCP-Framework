# Repo Split Carrier Map v0.1

Status: Candidate / Repo Split Planning / Not Approved / No Runtime
Source: User-provided repo split direction and GitHub repository checks
Use As: carrier routing map for DCP-XLEN_XAFD_XLQY, XLQY_Qinyi_Flow_CoreTri, and future Yiyi_xiao
Do Not Use As: repo creation proof, merge approval, public doctrine, or runtime authorization
Related PR: #298
Master Gate: #297
Issue Anchor: #299

## Actual Repository Check

```yaml
Checked:
  DCP_Framework:
    result: "redirects to DCP-XLEN_XAFD_XLQY"
  DCP_XLEN_XAFD_XLQY:
    result: "active repository / current PR #298 carrier"
  XLQY_Qinyi_Flow_CoreTri:
    result: "repository exists, but write attempt returned 403 Resource not accessible by integration"
  Yiyi_xiao:
    result: "not found by current connector check"
```

## Carrier Map

```yaml
DCP_XLEN_XAFD_XLQY:
  layer: "root lineage / Open Core / repo cleanup"
  role:
    - "DCP / XLEN / XAFD / XLQY lineage"
    - "Open Core first build set"
    - "PR #298 cleanup"
    - "Issue #299 dependency anchor"
    - "red doors / templates / schemas"
  not:
    - "private family archive"
    - "small-operator production app"
    - "company runtime"

XLQY_Qinyi_Flow_CoreTri:
  layer: "Qinyi flow / CoreTri carrier"
  intended_role:
    - "Qinyi working mode"
    - "CoreTri alignment"
    - "multi-carrier task assistant mode"
    - "GUI Flow and Return Packet patterns"
  current_gate: "write access not available to this connector"

Yiyi_xiao:
  layer: "small-operator guard app carrier"
  intended_role:
    - "sanitized availability guard app pattern"
    - "GUI flow"
    - "permission and maintenance boundaries"
    - "anti-error rules"
  current_gate: "repo not found; should be private or strictly sanitized before public use"
```

## Split Rule

- Root protocol and Open Core stay in DCP-XLEN_XAFD_XLQY.
- Qinyi Flow and CoreTri patterns should move to XLQY_Qinyi_Flow_CoreTri when write access is available.
- Small operator app patterns should move to Yiyi_xiao only after repo creation and sanitation decision.
- Private, customer, credential, and identifiable operational data must not enter public repos.

## Red Doors

- Repo exists != write permission.
- Repo split != doctrine approval.
- Public repo != public-approved content.
- Sanitized app pattern != production app.
- Maintainer access != customer data access.
- Pattern can move; private data cannot.
