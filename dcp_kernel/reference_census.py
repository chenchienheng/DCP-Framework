from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import PurePosixPath


class ReferenceClass(str, Enum):
    LIVE_CALLER = "LIVE_CALLER"
    LINEAGE_POINTER = "LINEAGE_POINTER"
    SELF_REFERENCE = "SELF_REFERENCE"
    UNKNOWN_HOLD = "UNKNOWN_HOLD"


CURRENT_SURFACES = {
    "README.md",
    "CURRENT-SURFACE-MANIFEST.json",
    "LIFECYCLE_DEPENDENCY_CHAIN_KERNEL.md",
    "PUBLIC-SURFACE-POLICY.md",
    "STATUS.md",
}

EXECUTABLE_PREFIXES = (
    "dcp_kernel/",
    "contracts/",
    "tests/",
    "tools/",
    ".github/",
)

LINEAGE_BASENAMES = {
    "REPOSITORY_CORPUS_INDEX.md",
    "NAMING_DRIFT_FILE_LEVEL_DIFFS.md",
    "NAMING_DRIFT_NORMALIZATION_PROPOSAL.md",
    "UNIFIED_ARTIFACT_REGISTER.md",
}

LEGACY_PREFIXES = (
    "00_meta/",
    "00_mother-law/",
    "01_native-board/",
    "01_runtime-spine/",
    "02_runtime-ops/",
    "02_translation-layer/",
    "03_board-orchestration/",
    "03_field-governance/",
    "04_adapter-layer/",
    "04_interface-layer/",
    "05_XLEN_Reserve_Unenabled/",
    "05_topology/",
    "archive/",
)


@dataclass(frozen=True)
class ReferenceObservation:
    caller_path: str
    target_family: str
    classification: ReferenceClass
    excerpt: str


def classify_reference(caller_path: str, target_family: str) -> ReferenceClass:
    """Classify a reference without equating search visibility with live dependency."""
    normalized = PurePosixPath(caller_path).as_posix().lstrip("./")
    target = target_family.rstrip("/") + "/"

    if normalized.startswith(target):
        return ReferenceClass.SELF_REFERENCE
    if normalized in CURRENT_SURFACES or normalized.startswith(EXECUTABLE_PREFIXES):
        return ReferenceClass.LIVE_CALLER
    if PurePosixPath(normalized).name in LINEAGE_BASENAMES:
        return ReferenceClass.LINEAGE_POINTER
    if normalized.startswith(LEGACY_PREFIXES):
        return ReferenceClass.LINEAGE_POINTER
    return ReferenceClass.UNKNOWN_HOLD


def scan_text_map(files: dict[str, str], families: tuple[str, ...]) -> tuple[ReferenceObservation, ...]:
    observations: list[ReferenceObservation] = []
    for caller_path, text in files.items():
        for family in families:
            needle = family.rstrip("/") + "/"
            if needle not in text:
                continue
            excerpt = next((line.strip() for line in text.splitlines() if needle in line), needle)
            observations.append(
                ReferenceObservation(
                    caller_path=caller_path,
                    target_family=family,
                    classification=classify_reference(caller_path, family),
                    excerpt=excerpt[:240],
                )
            )
    return tuple(observations)


def has_proven_live_caller(observations: tuple[ReferenceObservation, ...], family: str) -> bool:
    return any(
        item.target_family == family and item.classification is ReferenceClass.LIVE_CALLER
        for item in observations
    )


def has_unknown_hold(observations: tuple[ReferenceObservation, ...], family: str) -> bool:
    return any(
        item.target_family == family and item.classification is ReferenceClass.UNKNOWN_HOLD
        for item in observations
    )
