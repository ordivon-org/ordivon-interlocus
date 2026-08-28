#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "authority" / "CURRENT.json"
OWNER = "research-owner:network"
AUTHORITY = "authority:ordivon:research-owner:network"


def fail(message: str) -> None:
    raise SystemExit(f"authority contract: {message}")


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain one object")
    return value


def relative_file(value: object, label: str) -> Path:
    if not isinstance(value, str) or not value or value != value.strip():
        fail(f"{label} must be a non-empty relative path")
    pure = PurePosixPath(value)
    if pure.is_absolute() or ".." in pure.parts:
        fail(f"{label} escapes the owner root: {value}")
    path = ROOT.joinpath(*pure.parts)
    if not path.is_file():
        fail(f"{label} is not recoverable from current owner root: {value}")
    return path


def git_lineage(revision: object) -> None:
    if not (ROOT / ".git").exists():
        return
    if not isinstance(revision, str) or len(revision) != 40:
        fail("publication source.sourceRevision must be a 40-character Git revision")
    check = subprocess.run(
        ["git", "merge-base", "--is-ancestor", revision, "HEAD"],
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if check.returncode != 0:
        fail(f"publication source revision is not an ancestor of HEAD: {revision}")


def main() -> int:
    current = load_json(CURRENT)
    if current.get("schemaVersion") != 1 or current.get("kind") != "ordivon.research-owner-current":
        fail("CURRENT kind/schemaVersion differs")
    if current.get("ownerResearchRef") != OWNER or current.get("authorityRef") != AUTHORITY:
        fail("CURRENT owner/authority identity differs")

    publication_path = relative_file(current.get("publication"), "CURRENT.publication")
    raw = publication_path.read_bytes()
    observed_ref = "sha256:" + hashlib.sha256(raw).hexdigest()
    if current.get("currentAuthorityVersionRef") != observed_ref:
        fail("CURRENT authority version does not equal publication bytes")
    if publication_path.stem != observed_ref.removeprefix("sha256:"):
        fail("publication filename does not equal publication digest")

    publication = load_json(publication_path)
    if publication.get("schemaVersion") != 1 or publication.get("kind") != "ordivon.research-owner-publication":
        fail("publication kind/schemaVersion differs")
    if publication.get("ownerResearchRef") != OWNER or publication.get("authorityRef") != AUTHORITY:
        fail("publication owner/authority identity differs")

    source = publication.get("source")
    if not isinstance(source, dict) or source.get("kind") != "git":
        fail("publication source must be Git")
    git_lineage(source.get("sourceRevision"))

    recovery = publication.get("currentRecovery")
    if not isinstance(recovery, dict) or recovery.get("targetRole") != "OWNER_RESEARCH_CORPUS":
        fail("publication currentRecovery differs")
    relative_file(recovery.get("locator"), "publication.currentRecovery.locator")

    closeouts = publication.get("closeouts")
    if not isinstance(closeouts, list) or not closeouts:
        fail("publication closeouts are missing")
    provenance_count = 0
    for index, closeout in enumerate(closeouts):
        if not isinstance(closeout, dict):
            fail(f"closeouts[{index}] must be an object")
        provenance = closeout.get("provenance")
        if not isinstance(provenance, list) or not provenance:
            fail(f"closeouts[{index}].provenance is missing")
        for offset, locator in enumerate(provenance):
            relative_file(locator, f"closeouts[{index}].provenance[{offset}]")
            provenance_count += 1

    print(
        "authority contract: valid "
        f"owner={OWNER} authorityVersion={observed_ref} "
        f"closeouts={len(closeouts)} provenancePaths={provenance_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
