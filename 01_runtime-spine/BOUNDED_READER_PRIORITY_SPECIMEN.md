# Bounded Reader Priority Specimen

**Lifecycle:** HISTORICAL_LINEAGE
**Current eligibility:** false

Retained primitives from the retired fixed Window read-order generation:
- establish Identity / Domain / Authority / State before reading deltas;
- do not construct Current from Window-local assumptions or historical paths;
- bounded read first; escalate only when conflict, missing evidence, or re-entry requires it;
- freeze only the affected branch on conflict.

Current reader priority is defined by the Current Surface Manifest and six-dimensional dispatch. Full W01-07 path order remains in Git history.
