# Cross-Repo Dedup Matrix v0.1

Status: Candidate / Dedup Matrix / No Runtime

## Core

Repeated concepts become hook anchors only after ownership, local use, and return path are defined.

## Matrix

| Concept | Canonical Owner | DCP Use | XLQY Use | Yiyi Use | Disposition |
|---|---|---|---|---|---|
| Invariant Chain | DCP | canonical | pointer | pointer | keep canonical |
| Red Doors | DCP | canonical | local role-flow projection | app-gate projection | localize projection |
| Return Packet | DCP | canonical pattern | flow return template | problem return | localize projection |
| CoreTri | XLQY | context pointer | canonical | care-context pointer | keep canonical |
| Qinyi Task Flow | XLQY | pointer | canonical | operator-flow support | keep canonical |
| App Guard Pattern | Yiyi | abstract reference | task example reference | canonical | keep canonical |
| Human-Base Boundary | Yiyi | private-boundary reference | method reference | canonical | keep canonical |

## Disposition Types

```yaml
Disposition:
  keep_canonical: "keep as source in owner repo"
  replace_with_pointer: "remove full duplicate and keep pointer"
  localize_projection: "keep local use only"
  park: "historical or inactive"
```

## Red Doors

- Repeated text is not a hook anchor by itself.
- Hook anchor requires owner, local use, and return path.
- Private app projection cannot become public core by accident.
