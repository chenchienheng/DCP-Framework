from __future__ import annotations

import json
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


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    observations = scan_text_map(collect_text_files(root), FAMILIES)
    payload = [
        {
            "caller_path": item.caller_path,
            "target_family": item.target_family,
            "classification": item.classification.value,
            "excerpt": item.excerpt,
        }
        for item in observations
    ]
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
