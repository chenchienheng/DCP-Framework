from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from dcp_kernel.reference_census import scan_text_map


TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".toml", ".ini", ".cfg", ".sh",
}
FAMILIES = ("01_runtime-spine", "03_field-governance", "04_adapter-layer")
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def collect_text_files(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        try:
            result[rel] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
    return result


def build_payload(root: Path) -> dict[str, object]:
    observations = scan_text_map(collect_text_files(root), FAMILIES)
    by_family: dict[str, Counter[str]] = defaultdict(Counter)
    rows = []
    for item in observations:
        classification = item.classification.value
        by_family[item.target_family][classification] += 1
        rows.append(
            {
                "caller_path": item.caller_path,
                "target_family": item.target_family,
                "classification": classification,
                "excerpt": item.excerpt,
            }
        )

    summary = {}
    for family in FAMILIES:
        counts = by_family[family]
        summary[family] = {
            "live_caller_count": counts.get("LIVE_CALLER", 0),
            "lineage_pointer_count": counts.get("LINEAGE_POINTER", 0),
            "self_reference_count": counts.get("SELF_REFERENCE", 0),
            "unknown_hold_count": counts.get("UNKNOWN_HOLD", 0),
            "caller_absence_proven": counts.get("LIVE_CALLER", 0) == 0 and counts.get("UNKNOWN_HOLD", 0) == 0,
        }

    return {
        "artifact_role": "BOUNDED_REFERENCE_CENSUS_EVIDENCE",
        "runtime": False,
        "promotion": False,
        "destructive_action_authorized": False,
        "families": list(FAMILIES),
        "summary": summary,
        "observations": rows,
        "claim_boundary": [
            "SEARCH_HIT_IS_NOT_CURRENT",
            "UNKNOWN_REFERENCE_IS_HOLD",
            "CALLER_ABSENCE_ONLY_COVERS_SCANNED_TEXT_SURFACE",
            "CALLER_ABSENCE_DOES_NOT_PROVE_REBUILD_DEPENDENCY_ABSENCE",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    payload = build_payload(root)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(args.output.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
