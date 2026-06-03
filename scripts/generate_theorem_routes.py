#!/usr/bin/env python3
"""Generate theorem/proof route artifacts for a leaf LRA volume."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable

try:
    import yaml
except Exception:  # pragma: no cover - PyYAML is available in the local toolchain.
    yaml = None


PROOF_BEARING_ENVS = {"theorem", "proposition", "lemma", "corollary"}
TYPE_PREFIX = {"theorem": "thm", "proposition": "prop", "lemma": "lem", "corollary": "cor"}
BEGIN_ENV_RE = re.compile(
    r"\\begin\{(?P<env>theorem|proposition|lemma|corollary|definition|axiom)\}(?:\[(?P<title>[^\]]*)\])?",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
PROOF_FOR_RE = re.compile(r"\\LRAProofFor\{([^{}]+)\}")
HYPERREF_RE = re.compile(r"\\hyperref\[([^\]]+)\]")
PROOF_VAULT_RE = re.compile(r"\\ProofVaultURL\{([^{}]*)\}")
STRUCTURAL_RE = {
    "volume": re.compile(r"\\LRAVolume\{([^{}]+)\}"),
    "chapter": re.compile(r"\\LRAChapter\{([^{}]+)\}"),
    "section": re.compile(r"\\LRASection\{([^{}]+)\}"),
    "subsection": re.compile(r"\\LRASubsection\{([^{}]+)\}"),
}
METADATA_RE = re.compile(r"\\LRA(?:TheoremId|ProofPath|Tags|Metadata)\b")
ROUTE_VERSION = "leaf-theorem-routes-v1"
SCHEMA = "lra.theorem_routes"
SCHEMA_VERSION = 1
ESSENTIAL_ROUTE_FIELDS = {"theorem_id", "title", "type", "theorem_tex", "proof_tex", "proof_label", "vault_path"}
OPTIONAL_ROUTE_FIELDS = {
    "volume",
    "chapter",
    "section",
    "subsection",
    "tags",
    "dependencies",
    "source_commit",
    "route_version",
}
ALL_ROUTE_FIELDS = ESSENTIAL_ROUTE_FIELDS | OPTIONAL_ROUTE_FIELDS | {"source_repo"}
THEOREM_ID_RE = re.compile(r"^(thm|prop|lem|cor):[a-z0-9][a-z0-9_.-]*$")
PROOF_LABEL_RE = re.compile(r"^prf:[a-z0-9][a-z0-9_.-]*$")


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    path: str = ""
    line: int = 1
    severity: str = "error"


@dataclass
class TheoremNode:
    theorem_id: str
    title: str
    env: str
    path: Path
    line: int
    volume: str
    chapter: str
    section: str
    subsection: str
    dependencies: list[str]


@dataclass
class ProofFile:
    path: Path
    proof_labels: list[str]
    proof_for: list[str]
    return_refs: list[str]
    vault_urls: list[str]
    has_professional_body: bool
    has_detailed_body: bool
    dependencies: list[str]


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def is_archived(path: Path, root: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    return "archive" in parts or "legacy-orphan-proofs" in parts


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        out: list[str] = []
        escaped = False
        for ch in line:
            if ch == "\\":
                escaped = not escaped
                out.append(ch)
                continue
            if ch == "%" and not escaped:
                break
            escaped = False
            out.append(ch)
        lines.append("".join(out))
    return "\n".join(lines)


def line_number(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def iter_tex_files(root: Path, required_part: str) -> Iterable[Path]:
    for path in sorted(root.rglob("*.tex")):
        if any(part.startswith(".") for part in path.parts):
            continue
        if is_archived(path, root):
            continue
        if required_part in path.parts:
            yield path


def find_matching_end(text: str, env: str, start: int) -> int:
    begin_pat = re.compile(rf"\\begin\{{{re.escape(env)}\}}")
    end_pat = re.compile(rf"\\end\{{{re.escape(env)}\}}")
    depth = 1
    pos = start
    while depth > 0:
        nb = begin_pat.search(text, pos)
        ne = end_pat.search(text, pos)
        if ne is None:
            return len(text)
        if nb is not None and nb.start() < ne.start():
            depth += 1
            pos = nb.end()
        else:
            depth -= 1
            pos = ne.end()
    return pos


def slug(value: str) -> str:
    value = value.lower().replace(":", "-")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "unknown"


def title_from_label(label: str) -> str:
    root = label.split(":", 1)[-1]
    return " ".join(part.capitalize() for part in re.split(r"[-_]+", root) if part)


def git_commit(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def load_chapter_metadata(root: Path) -> dict[Path, dict]:
    metadata: dict[Path, dict] = {}
    for path in sorted(root.rglob("chapter.yaml")):
        if is_archived(path, root):
            continue
        data: dict = {}
        if yaml is not None:
            try:
                loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
                if isinstance(loaded, dict):
                    data = loaded
            except Exception:
                data = {}
        if not data:
            text = path.read_text(encoding="utf-8", errors="replace")
            for key in ("subject", "volume", "path"):
                match = re.search(rf"^{key}:\s*(.+)$", text, re.MULTILINE)
                if match:
                    data[key] = match.group(1).strip().strip("'\"")
        chapter_root = path.parent
        metadata[chapter_root] = data
    return metadata


def owning_chapter(path: Path, chapter_metadata: dict[Path, dict]) -> tuple[Path | None, dict]:
    best: tuple[Path | None, dict] = (None, {})
    for chapter_root, data in chapter_metadata.items():
        try:
            path.relative_to(chapter_root)
        except ValueError:
            continue
        if best[0] is None or len(chapter_root.parts) > len(best[0].parts):
            best = (chapter_root, data)
    return best


def structural_location(path: Path, text: str, root: Path, chapter_metadata: dict[Path, dict]) -> tuple[dict[str, str], list[Finding]]:
    warnings: list[Finding] = []
    structure = {key: "unknown" for key in ("volume", "chapter", "section", "subsection")}
    for key, pattern in STRUCTURAL_RE.items():
        match = pattern.search(text)
        if match:
            structure[key] = slug(match.group(1))

    chapter_root, data = owning_chapter(path, chapter_metadata)
    if structure["volume"] == "unknown":
        structure["volume"] = str(data.get("volume") or "volume-iii")
    if structure["chapter"] == "unknown":
        structure["chapter"] = slug(str(data.get("subject") or (chapter_root.name if chapter_root else "unknown")))

    try:
        parts = path.relative_to(chapter_root if chapter_root else root).parts
    except ValueError:
        parts = path.parts
    if "notes" in parts:
        notes_index = parts.index("notes")
        if structure["section"] == "unknown" and len(parts) > notes_index + 1:
            structure["section"] = slug(parts[notes_index + 1])
        if structure["subsection"] == "unknown" and len(parts) > notes_index + 2:
            structure["subsection"] = slug(Path(parts[notes_index + 2]).stem)
    if structure["section"] == "unknown":
        structure["section"] = structure["chapter"]

    if not all(pattern.search(text) for pattern in STRUCTURAL_RE.values()):
        warnings.append(Finding("missing_structural_macro", "Structural macros absent; route used metadata/path derivation.", rel(path, root), severity="warning"))
    return structure, warnings


def extract_dependencies(text: str, owner_target: str | None = None) -> list[str]:
    refs = []
    for ref in HYPERREF_RE.findall(text):
        if ref.startswith("prf:"):
            continue
        if owner_target and ref == owner_target:
            continue
        if ref.startswith(("def:", "ax:", "thm:", "lem:", "prop:", "cor:")) and ref not in refs:
            refs.append(ref)
    return refs


def discover_theorems(root: Path, chapter_metadata: dict[Path, dict]) -> tuple[list[TheoremNode], list[Finding]]:
    nodes: list[TheoremNode] = []
    findings: list[Finding] = []
    for path in iter_tex_files(root, "notes"):
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        structure, structural_warnings = structural_location(path, text, root, chapter_metadata)
        findings.extend(structural_warnings)
        for match in BEGIN_ENV_RE.finditer(text):
            env = match.group("env")
            end = find_matching_end(text, env, match.end())
            body = text[match.end():end]
            labels = LABEL_RE.findall(body)
            line = line_number(text, match.start())
            if env not in PROOF_BEARING_ENVS:
                continue
            if not labels:
                findings.append(Finding("missing_theorem_label", f"Proof-bearing {env} has no label.", rel(path, root), line))
                continue
            label = labels[0]
            title = (match.group("title") or "").strip() or title_from_label(label)
            deps = extract_dependencies(body)
            nodes.append(
                TheoremNode(
                    theorem_id=label,
                    title=title,
                    env=env,
                    path=path,
                    line=line,
                    volume=structure["volume"],
                    chapter=structure["chapter"],
                    section=structure["section"],
                    subsection=structure["subsection"],
                    dependencies=deps,
                )
            )
    return nodes, findings


def discover_proofs(root: Path) -> tuple[list[ProofFile], list[Finding]]:
    proofs: list[ProofFile] = []
    findings: list[Finding] = []
    for path in iter_tex_files(root, "proofs"):
        if path.name == "index.tex" or "exercises" in path.parts:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        proof_labels = [label for label in LABEL_RE.findall(text) if label.startswith("prf:")]
        proof_for = PROOF_FOR_RE.findall(text)
        if not proof_labels and not proof_for and not path.stem.startswith("prf-"):
            continue
        if len(set(proof_for)) > 1:
            findings.append(Finding("conflicting_lra_proof_for", f"Proof file has conflicting \\LRAProofFor targets: {', '.join(sorted(set(proof_for)))}.", rel(path, root)))
        lower = text.lower()
        target = proof_for[0] if len(set(proof_for)) == 1 else None
        proofs.append(
            ProofFile(
                path=path,
                proof_labels=proof_labels,
                proof_for=proof_for,
                return_refs=[ref for ref in HYPERREF_RE.findall(text) if ref.startswith(("thm:", "prop:", "lem:", "cor:"))],
                vault_urls=PROOF_VAULT_RE.findall(text),
                has_professional_body=bool(re.search(r"professional\s+(standard\s+)?proof", lower)),
                has_detailed_body=bool(re.search(r"detailed\s+(learning\s+)?proof", lower)),
                dependencies=extract_dependencies(text, target),
            )
        )
    return proofs, findings


def proof_label_root(proof: ProofFile) -> str:
    if proof.proof_labels:
        return proof.proof_labels[0].split(":", 1)[-1]
    if proof.path.stem.startswith("prf-"):
        return proof.path.stem[4:]
    return proof.path.stem


def associate_proofs(proofs: list[ProofFile], theorem_ids: set[str]) -> tuple[dict[str, tuple[ProofFile, str]], dict[str, int], list[Finding]]:
    associations: dict[str, tuple[ProofFile, str]] = {}
    counts = {"lra_proof_for": 0, "metadata": 0, "return_link": 0, "label_root": 0, "legacy_heuristic": 0}
    findings: list[Finding] = []
    root_map = {label.split(":", 1)[-1]: label for label in theorem_ids}

    for proof in proofs:
        target = None
        method = ""
        unique_proof_for = sorted(set(proof.proof_for))
        if len(unique_proof_for) == 1:
            target = unique_proof_for[0]
            method = "lra_proof_for"
        elif METADATA_RE.search(proof.path.read_text(encoding="utf-8", errors="replace")):
            method = "metadata"
        if target is None and proof.return_refs:
            candidates = [ref for ref in proof.return_refs if ref in theorem_ids]
            if len(set(candidates)) == 1:
                target = candidates[0]
                method = "return_link"
        if target is None:
            root = proof_label_root(proof)
            if root in root_map:
                target = root_map[root]
                method = "label_root"
        if target is None and proof.path.stem.startswith("prf-"):
            root = proof.path.stem[4:]
            if root in root_map:
                target = root_map[root]
                method = "legacy_heuristic"

        if target is None:
            findings.append(Finding("unresolved_proof_association", "Proof file cannot be associated to a theorem route.", proof.path.as_posix()))
            continue
        if target not in theorem_ids:
            findings.append(Finding("invalid_proof_target", f"Proof file points to nonexistent theorem_id {target}.", proof.path.as_posix()))
            continue
        if target in associations:
            other = associations[target][0]
            findings.append(Finding("duplicate_proof_target", f"Multiple proof files claim theorem_id {target}: {other.path.as_posix()} and {proof.path.as_posix()}.", proof.path.as_posix()))
            continue
        associations[target] = (proof, method)
        counts[method] += 1
    return associations, counts, findings


def make_route(node: TheoremNode, proof: ProofFile, method: str, root: Path, source_repo: str, source_commit: str) -> dict:
    proof_label = proof.proof_labels[0] if proof.proof_labels else ""
    dependencies = sorted(set(node.dependencies + proof.dependencies))
    vault_path = f"{node.volume}/{node.chapter}/{slug(node.theorem_id)}"
    return {
        "theorem_id": node.theorem_id,
        "title": node.title,
        "type": node.env,
        "volume": node.volume,
        "chapter": node.chapter,
        "section": node.section,
        "subsection": node.subsection,
        "theorem_tex": rel(node.path, root),
        "proof_tex": rel(proof.path, root),
        "proof_label": proof_label,
        "vault_path": vault_path,
        "tags": [],
        "dependencies": dependencies,
        "source_repo": source_repo,
        "source_commit": source_commit,
        "route_version": ROUTE_VERSION,
        "association_method": method,
        "proof_vault_url": proof.vault_urls[0] if proof.vault_urls else "",
        "has_professional_body": proof.has_professional_body,
        "has_detailed_learning_body": proof.has_detailed_body,
    }


def validate_routes(routes: list[dict], expected_nodes: list[TheoremNode], associations: dict[str, tuple[ProofFile, str]], root: Path) -> tuple[list[Finding], list[Finding]]:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    ids: dict[str, list[dict]] = {}
    vaults: dict[str, list[dict]] = {}
    route_keys: dict[tuple[str, str], list[dict]] = {}
    for route in routes:
        theorem_id = route.get("theorem_id", "")
        proof_tex = route.get("proof_tex", "")
        theorem_tex = route.get("theorem_tex", "")
        proof_label = route.get("proof_label", "")
        vault_path = route.get("vault_path", "")
        ids.setdefault(theorem_id, []).append(route)
        vaults.setdefault(vault_path, []).append(route)
        route_keys.setdefault((theorem_id, proof_tex), []).append(route)
        for key in sorted(ESSENTIAL_ROUTE_FIELDS):
            if not route.get(key):
                errors.append(Finding("missing_essential_field", f"Route {theorem_id or '<unknown>'} is missing essential field {key}.", theorem_tex))
        for key in sorted(OPTIONAL_ROUTE_FIELDS):
            if key not in route:
                warnings.append(Finding("missing_optional_field", f"Route {theorem_id or '<unknown>'} is missing optional field {key}.", theorem_tex, severity="warning"))
        if theorem_id and not THEOREM_ID_RE.match(theorem_id):
            errors.append(Finding("malformed_theorem_id", f"Malformed theorem_id {theorem_id}.", theorem_tex))
        if proof_label and not PROOF_LABEL_RE.match(proof_label):
            errors.append(Finding("malformed_proof_label", f"Malformed proof_label {proof_label}.", proof_tex))
        for field_name, route_path in (("theorem_tex", theorem_tex), ("proof_tex", proof_tex)):
            if route_path:
                full_path = root / route_path
                if not full_path.exists():
                    errors.append(Finding("route_path_missing", f"{field_name} path does not exist: {route_path}.", route_path))
                elif is_archived(full_path, root):
                    errors.append(Finding("route_points_to_archive", f"{field_name} points into archived legacy material: {route_path}.", route_path))
        if "source_repo" not in route:
            warnings.append(Finding("missing_optional_field", f"Route {theorem_id or '<unknown>'} is missing optional field source_repo.", theorem_tex, severity="warning"))
        if "tags" in route and not route.get("tags"):
            warnings.append(Finding("missing_tags", "Optional tags are absent.", theorem_tex, severity="warning"))
        if "dependencies" in route and not route.get("dependencies"):
            warnings.append(Finding("missing_dependency_data", "Optional dependency data is absent.", proof_tex, severity="warning"))
        if not route.get("source_commit"):
            warnings.append(Finding("missing_source_commit", "source_commit is unavailable.", theorem_tex, severity="warning"))
        if "proofs" in Path(proof_tex).parts and "notes" in Path(proof_tex).parts:
            warnings.append(Finding("proof_path_convention", "proof_tex still uses proofs/notes; future convention should mirror notes subfolders under proofs/.", proof_tex, severity="warning"))
        if not route.get("proof_vault_url"):
            warnings.append(Finding("missing_vault_backlink", "Optional proof-vault backlink is absent.", proof_tex, severity="warning"))

    for theorem_id, grouped in ids.items():
        if len(grouped) > 1:
            errors.append(Finding("duplicate_theorem_id", f"Duplicate theorem_id {theorem_id}."))
    for vault_path, grouped in vaults.items():
        if len(grouped) > 1:
            errors.append(Finding("vault_path_collision", f"vault_path {vault_path} is used by multiple routes."))
    for key, grouped in route_keys.items():
        if len(grouped) > 1:
            errors.append(Finding("route_collision", f"Route collision for theorem/proof pair {key}."))
    for node in expected_nodes:
        if node.theorem_id not in associations:
            errors.append(Finding("missing_proof_stub", f"Theorem {node.theorem_id} has no associated proof stub.", rel(node.path, root), node.line))
    return errors, warnings


def validate_artifact_schema(artifact: dict, root: Path) -> tuple[list[Finding], list[Finding]]:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    top_level_required = ["schema", "schema_version", "generated_at", "source_repo", "source_commit", "route_version", "route_count", "routes"]
    for key in top_level_required:
        if key not in artifact:
            errors.append(Finding("missing_schema_field", f"Route artifact is missing top-level field {key}."))
    if artifact.get("schema") != SCHEMA:
        errors.append(Finding("invalid_schema", f"Expected schema {SCHEMA}, found {artifact.get('schema')!r}."))
    if artifact.get("schema_version") != SCHEMA_VERSION:
        errors.append(Finding("invalid_schema_version", f"Expected schema_version {SCHEMA_VERSION}, found {artifact.get('schema_version')!r}."))
    routes = artifact.get("routes", [])
    if not isinstance(routes, list):
        errors.append(Finding("invalid_routes_type", "Top-level routes field must be a list."))
        return errors, warnings
    if artifact.get("route_count") != len(routes):
        errors.append(Finding("route_count_mismatch", f"route_count is {artifact.get('route_count')}, but routes contains {len(routes)} records."))

    for route in routes:
        for key in sorted(ESSENTIAL_ROUTE_FIELDS):
            if not route.get(key):
                errors.append(Finding("missing_essential_field", f"Route {route.get('theorem_id', '<unknown>')} is missing essential field {key}.", route.get("theorem_tex", "")))
        for key in sorted(OPTIONAL_ROUTE_FIELDS):
            if key not in route:
                warnings.append(Finding("missing_optional_field", f"Route {route.get('theorem_id', '<unknown>')} is missing optional field {key}.", route.get("theorem_tex", ""), severity="warning"))
        theorem_id = route.get("theorem_id", "")
        proof_label = route.get("proof_label", "")
        if theorem_id and not THEOREM_ID_RE.match(theorem_id):
            errors.append(Finding("malformed_theorem_id", f"Malformed theorem_id {theorem_id}.", route.get("theorem_tex", "")))
        if proof_label and not PROOF_LABEL_RE.match(proof_label):
            errors.append(Finding("malformed_proof_label", f"Malformed proof_label {proof_label}.", route.get("proof_tex", "")))
        for field_name in ("theorem_tex", "proof_tex"):
            route_path = route.get(field_name, "")
            if route_path:
                full_path = root / route_path
                if not full_path.exists():
                    errors.append(Finding("route_path_missing", f"{field_name} path does not exist: {route_path}.", route_path))
                elif is_archived(full_path, root):
                    errors.append(Finding("route_points_to_archive", f"{field_name} points into archived legacy material: {route_path}.", route_path))
    return errors, warnings


def route_diff(previous: dict | None, current: dict, errors: list[Finding]) -> dict | None:
    if previous is None:
        return None
    before = {route["theorem_id"]: route for route in previous.get("routes", []) if "theorem_id" in route}
    after = {route["theorem_id"]: route for route in current.get("routes", []) if "theorem_id" in route}
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    common = sorted(set(before) & set(after))
    return {
        "theorem_ids_before": len(before),
        "theorem_ids_after": len(after),
        "added_ids": added,
        "removed_ids": removed,
        "duplicate_ids": [finding.message for finding in errors if finding.code == "duplicate_theorem_id"],
        "moved_theorem_tex": [
            {"theorem_id": tid, "before": before[tid]["theorem_tex"], "after": after[tid]["theorem_tex"]}
            for tid in common
            if before[tid].get("theorem_tex") != after[tid].get("theorem_tex")
        ],
        "moved_proof_tex": [
            {"theorem_id": tid, "before": before[tid]["proof_tex"], "after": after[tid]["proof_tex"]}
            for tid in common
            if before[tid].get("proof_tex") != after[tid].get("proof_tex")
        ],
        "changed_vault_path": [
            {"theorem_id": tid, "before": before[tid]["vault_path"], "after": after[tid]["vault_path"]}
            for tid in common
            if before[tid].get("vault_path") != after[tid].get("vault_path")
        ],
        "route_collisions": [finding.message for finding in errors if finding.code == "route_collision"],
        "vault_path_collisions": [finding.message for finding in errors if finding.code == "vault_path_collision"],
    }


def write_diff_markdown(path: Path, diff: dict | None) -> None:
    if diff is None:
        return
    lines = ["# Theorem Route Diff", ""]
    for key in ("theorem_ids_before", "theorem_ids_after"):
        lines.append(f"- `{key}`: {diff[key]}")
    for key in ("added_ids", "removed_ids", "duplicate_ids", "moved_theorem_tex", "moved_proof_tex", "changed_vault_path", "route_collisions", "vault_path_collisions"):
        value = diff[key]
        lines.append(f"- `{key}`: {len(value)}")
        for item in value[:25]:
            lines.append(f"  - `{item}`")
        if len(value) > 25:
            lines.append(f"  - ... {len(value) - 25} more")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate(root: Path) -> tuple[dict, list[Finding], list[Finding], dict[str, int], dict | None]:
    source_repo = root.name
    source_commit = git_commit(root)
    output_dir = root / "build" / "knowledge"
    previous_path = output_dir / "theorem-routes.json"
    previous = None
    if previous_path.exists():
        try:
            previous = json.loads(previous_path.read_text(encoding="utf-8-sig"))
        except Exception:
            previous = None

    chapter_metadata = load_chapter_metadata(root)
    nodes, theorem_findings = discover_theorems(root, chapter_metadata)
    proofs, proof_findings = discover_proofs(root)
    theorem_ids = {node.theorem_id for node in nodes}
    associations, counts, association_findings = associate_proofs(proofs, theorem_ids)

    routes = []
    for node in sorted(nodes, key=lambda item: item.theorem_id):
        associated = associations.get(node.theorem_id)
        if associated is None:
            continue
        proof, method = associated
        routes.append(make_route(node, proof, method, root, source_repo, source_commit))

    validation_errors, validation_warnings = validate_routes(routes, nodes, associations, root)
    errors = [f for f in theorem_findings + proof_findings + association_findings + validation_errors if f.severity == "error"]
    warnings = [f for f in theorem_findings + proof_findings + association_findings + validation_warnings if f.severity == "warning"]

    artifact = {
        "schema": SCHEMA,
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "source_repo": source_repo,
        "source_commit": source_commit,
        "route_version": ROUTE_VERSION,
        "route_count": len(routes),
        "proof_bearing_theorem_count": len(nodes),
        "association_method_counts": counts,
        "routes": routes,
        "validation": {
            "errors": [asdict(error) for error in errors],
            "warnings": [asdict(warning) for warning in warnings],
            "status": "PASS" if not errors else "FAIL",
        },
    }
    schema_errors, schema_warnings = validate_artifact_schema(artifact, root)
    errors.extend(schema_errors)
    warnings.extend(schema_warnings)
    artifact["validation"] = {
        "errors": [asdict(error) for error in errors],
        "warnings": [asdict(warning) for warning in warnings],
        "status": "PASS" if not errors else "FAIL",
        "summary": {
            "missing_essential_field_count": sum(1 for finding in errors if finding.code == "missing_essential_field"),
            "missing_optional_field_count": sum(1 for finding in warnings if finding.code == "missing_optional_field"),
            "malformed_theorem_id_count": sum(1 for finding in errors if finding.code == "malformed_theorem_id"),
            "malformed_proof_label_count": sum(1 for finding in errors if finding.code == "malformed_proof_label"),
            "vault_path_collision_count": sum(1 for finding in errors if finding.code == "vault_path_collision"),
            "route_path_missing_count": sum(1 for finding in errors if finding.code == "route_path_missing"),
            "archive_route_count": sum(1 for finding in errors if finding.code == "route_points_to_archive"),
        },
    }
    return artifact, errors, warnings, counts, route_diff(previous, artifact, errors)


def write_outputs(root: Path, artifact: dict, diff: dict | None) -> None:
    output_dir = root / "build" / "knowledge"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "theorem-routes.json").write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    if yaml is not None:
        (output_dir / "theorem-routes.yaml").write_text(yaml.safe_dump(artifact, sort_keys=False, allow_unicode=False), encoding="utf-8")
    else:
        (output_dir / "theorem-routes.yaml").write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    if diff is not None:
        (output_dir / "route-diff.json").write_text(json.dumps(diff, indent=2) + "\n", encoding="utf-8")
        write_diff_markdown(output_dir / "route-diff.md", diff)


def print_text(artifact: dict, diff: dict | None) -> None:
    validation = artifact["validation"]
    print("Theorem route generation summary")
    for key in ("schema", "schema_version", "source_repo", "source_commit", "route_version", "proof_bearing_theorem_count", "route_count"):
        print(f"{key}: {artifact[key]}")
    print("association_method_counts:")
    for key, value in artifact["association_method_counts"].items():
        print(f"  {key}: {value}")
    print(f"warning_count: {len(validation['warnings'])}")
    print(f"error_count: {len(validation['errors'])}")
    for key, value in validation.get("summary", {}).items():
        print(f"{key}: {value}")
    print(f"status: {validation['status']}")
    if diff is None:
        print("route_diff: no previous snapshot")
    else:
        print("route_diff: generated")
        print(f"  added_ids: {len(diff['added_ids'])}")
        print(f"  removed_ids: {len(diff['removed_ids'])}")
        print(f"  moved_theorem_tex: {len(diff['moved_theorem_tex'])}")
        print(f"  moved_proof_tex: {len(diff['moved_proof_tex'])}")
        print(f"  changed_vault_path: {len(diff['changed_vault_path'])}")
    for finding in validation["errors"][:50]:
        print(f"ERROR {finding['code']} {finding['path']}:{finding['line']} - {finding['message']}")
    if len(validation["errors"]) > 50:
        print(f"... {len(validation['errors']) - 50} more errors")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate theorem route artifacts for a leaf LRA volume.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--validate-only", action="store_true", help="Generate and validate in memory without writing route artifacts.")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    artifact, errors, _warnings, _counts, diff = generate(root)
    if not args.validate_only:
        write_outputs(root, artifact, diff)
    if args.format == "json":
        print(json.dumps({"artifact": artifact, "route_diff": diff}, indent=2))
    else:
        print_text(artifact, diff)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
