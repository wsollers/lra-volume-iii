#!/usr/bin/env python3
"""Generate and locally validate semantic artifact packages from TeX blocks.

By default this driver does not call an external reviewer or external LLM.
It wraps the local governance tools that validate structured semantic ASTs:

* validate_semantic_logic.py
* compare_semantic_ast_extractors.py

For TeX environments without an artifact package, this driver creates a draft
local package under the output directory, populates shallow ASTs from the
standard quantified and predicate-reading blocks, then validates those ASTs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


SUPPORTED_KINDS = ("definition", "theorem", "lemma", "proposition", "corollary")
KIND_PREFIX = {
    "definition": "def:",
    "theorem": "thm:",
    "lemma": "lem:",
    "proposition": "prop:",
    "corollary": "cor:",
}
INPUT_RE = re.compile(r"\\input\{(?P<path>[^{}]+)\}")
DISPLAY_RE = re.compile(r"\\\[(?P<body>.*?)\\\]", re.S)
OPERATOR_RE = re.compile(r"\\operatorname\{(?P<name>[A-Za-z][A-Za-z0-9]*)\}\s*(?:\((?P<args>[^()]*)\))?")
DEPENDENCY_RE = re.compile(r"\\hyperref\[(?P<label>[^\]]+)\]")


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def governance_root() -> Path:
    candidates: list[Path] = []
    env = os.environ.get("LRA_GOVERNANCE_ROOT")
    if env:
        candidates.append(Path(env))
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidates.append(parent.parent / "lra-governance")
    candidates.append(Path("F:/repos/lra-governance"))
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if (resolved / "tools" / "governance" / "validate_semantic_logic.py").exists():
            return resolved
    fail("lra-governance was not found; set LRA_GOVERNANCE_ROOT or use --governance-root")


def load_semantic_chapter_sweep(governance: Path) -> Any:
    tool = governance / "tools" / "governance" / "semantic_chapter_sweep.py"
    if not tool.exists():
        fail(f"semantic_chapter_sweep.py not found at {tool}")
    sys.path.insert(0, str(tool.parent))
    spec = importlib.util.spec_from_file_location("lra_semantic_chapter_sweep", tool)
    if spec is None or spec.loader is None:
        fail(f"could not import {tool}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_kinds(raw: str) -> set[str]:
    values = {item.strip().lower() for item in raw.split(",") if item.strip()}
    unknown = values - set(SUPPORTED_KINDS)
    if unknown:
        fail(f"unknown kind(s): {', '.join(sorted(unknown))}")
    return values


def label_slug(label: str) -> str:
    return label.replace(":", "-", 1)


def read_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path}: YAML root is not a mapping")
    return data


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def file_sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def file_sha256_bare(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if completed.returncode != 0:
        return "0" * 40
    return completed.stdout.strip()


def kebab(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "-", value)
    return value.strip("-").lower()


def raw_latex(latex: str) -> dict[str, str]:
    return {"kind": "raw_latex", "latex": latex.strip()}


def first_display(text: str) -> str:
    match = DISPLAY_RE.search(text)
    if match:
        return match.group("body").strip()
    return text.strip()


def all_displays(text: str) -> list[str]:
    found = [match.group("body").strip() for match in DISPLAY_RE.finditer(text)]
    return found or ([text.strip()] if text.strip() else [])


def split_top_level_args(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def predicate_registry(governance: Path) -> dict[str, str]:
    path = governance / "predicates.yaml"
    if not path.exists():
        return {}
    data = read_yaml(path)
    mapping: dict[str, str] = {}
    for item in data.get("predicates", []) or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "")
        pred_id = str(item.get("id") or "")
        if name and pred_id:
            mapping[name] = pred_id
            mapping[kebab(name)] = pred_id
    return mapping


def predicate_ast_from_latex(latex: str, registry: dict[str, str]) -> dict[str, Any] | None:
    predicates: list[dict[str, Any]] = []
    for match in OPERATOR_RE.finditer(latex):
        name = match.group("name")
        if not name or not name[:1].isupper():
            continue
        pred_id = registry.get(name) or registry.get(kebab(name)) or f"pred:{kebab(name)}"
        predicates.append(
            {
                "kind": "predicate",
                "predicate_id": pred_id,
                "arguments": [raw_latex(arg) for arg in split_top_level_args(match.group("args"))],
            }
        )
    if not predicates:
        return None
    node = predicates[0]
    for predicate in predicates[1:]:
        node = {"kind": "and", "left": node, "right": predicate}
    return node


def predicate_ids_from_latex(latex: str, registry: dict[str, str]) -> list[str]:
    ids: list[str] = []
    for match in OPERATOR_RE.finditer(latex):
        name = match.group("name")
        if name and name[:1].isupper():
            ids.append(registry.get(name) or registry.get(kebab(name)) or f"pred:{kebab(name)}")
    return sorted(set(ids))


def quantified_variables(latex: str, quantifier: str) -> list[str]:
    variables: list[str] = []
    pattern = re.compile(
        rf"\\{quantifier}\s*(?P<body>.*?)(?=(?:\\forall|\\exists|\\Rightarrow|\\Longrightarrow|\\implies|\\land|\\lor|\.|,?\s*\)|,?\s*\]|\Z))",
        re.S,
    )
    for match in pattern.finditer(latex):
        body = match.group("body")
        body = re.split(r"\\in|\\subseteq|\\subset|:", body, maxsplit=1)[0]
        body = re.split(r"\\;|;|\\quad|\\text", body, maxsplit=1)[0]
        names = [item.strip() for item in body.split(",") if item.strip()]
        for name in names or [f"{quantifier}_{len(variables) + 1}"]:
            cleaned = re.sub(r"[^A-Za-z\\]+", "", name).strip() or f"{quantifier}_{len(variables) + 1}"
            variables.append(cleaned)
    return variables


def quantifier_ast_from_latex(latex: str) -> dict[str, Any]:
    body: dict[str, Any] = raw_latex(latex)
    binders: list[tuple[str, str]] = []
    for variable in quantified_variables(latex, "exists"):
        binders.append(("exists", variable))
    for variable in quantified_variables(latex, "forall"):
        binders.append(("forall", variable))
    for kind, variable in reversed(binders):
        binder_id = f"binder-{kebab(variable) or kind}"
        body = {
            "kind": kind,
            "binder": {"binder_id": binder_id, "symbol": variable, "domain": None},
            "restriction": None,
            "body": body,
        }
    return body


def ast_from_latex(latex: str, registry: dict[str, str]) -> dict[str, Any]:
    predicate = predicate_ast_from_latex(latex, registry)
    base = predicate or raw_latex(latex)
    if r"\Longleftrightarrow" in latex or r"\iff" in latex:
        parts = re.split(r"\\Longleftrightarrow|\\iff", latex, maxsplit=1)
        return {"kind": "iff", "left": ast_from_latex(parts[0], registry), "right": ast_from_latex(parts[1], registry)}
    if r"\Rightarrow" in latex or r"\implies" in latex:
        parts = re.split(r"\\Rightarrow|\\implies", latex, maxsplit=1)
        return {"kind": "implies", "left": ast_from_latex(parts[0], registry), "right": ast_from_latex(parts[1], registry)}
    if r"\forall" in latex or r"\exists" in latex:
        quantified = quantifier_ast_from_latex(latex)
        if predicate:
            return {"kind": "and", "left": quantified, "right": base}
        return quantified
    if r"\neg" in latex or r"\not" in latex:
        return {"kind": "not", "operand": base}
    return base


def remark_map(sweep: Any, block: Any) -> dict[str, list[str]]:
    return sweep.remark_bodies(block.text)


def remark_display(remarks: dict[str, list[str]], needle: str) -> str:
    for title, bodies in remarks.items():
        if needle in title:
            for body in bodies:
                display = first_display(body)
                if display:
                    return display
    return ""


def path_context(repo_relative_path: str) -> tuple[str, str, str]:
    parts = repo_relative_path.replace("\\", "/").split("/")
    book = parts[1] if len(parts) > 1 else "unknown-book"
    chapter = parts[2] if len(parts) > 2 else "unknown-chapter"
    topic = "unknown-topic"
    if "notes" in parts:
        index = parts.index("notes")
        if index + 1 < len(parts):
            topic = parts[index + 1]
    return book, chapter, topic


def resolve_input_target(raw: str, *, current_file: Path, repo_root: Path) -> Path:
    normalized = raw.replace("/", os.sep)
    candidates: list[Path] = []
    path = Path(normalized)
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append(repo_root / path)
        candidates.append(current_file.parent / path)
    with_suffix: list[Path] = []
    for candidate in candidates:
        with_suffix.append(candidate)
        if candidate.suffix != ".tex":
            with_suffix.append(candidate.with_suffix(".tex"))
    for candidate in with_suffix:
        if candidate.exists():
            return candidate.resolve()
    return with_suffix[0].resolve()


def router_closure(start: Path, repo_root: Path, seen: set[Path] | None = None) -> list[Path]:
    seen = seen or set()
    path = start.resolve()
    if path in seen or not path.exists() or path.suffix != ".tex":
        return []
    seen.add(path)
    result = [path]
    text = path.read_text(encoding="utf-8", errors="ignore")
    for match in INPUT_RE.finditer(text):
        child = resolve_input_target(match.group("path"), current_file=path, repo_root=repo_root)
        result.extend(router_closure(child, repo_root, seen))
    return result


def ordered_tex_targets(target: Path, repo_root: Path) -> list[Path]:
    if target.is_file():
        return router_closure(target, repo_root)
    index = target / "index.tex"
    if index.exists():
        return router_closure(index, repo_root)
    return sorted(path.resolve() for path in target.rglob("*.tex"))


def inventory_source_blocks(sweep: Any, target: Path, repo_root: Path, kinds: set[str]) -> dict[str, Any]:
    blocks: dict[str, Any] = {}
    for tex in ordered_tex_targets(target, repo_root):
        for block in sweep.formal_blocks(tex, repo_root):
            if block.env not in kinds:
                continue
            expected = KIND_PREFIX.get(block.env)
            if expected and not block.label.startswith(expected):
                continue
            blocks.setdefault(block.label, block)
    return blocks


def find_artifact_packages(target: Path, repo_root: Path, kinds: set[str], labels: set[str]) -> list[dict[str, Any]]:
    search_root = target if target.is_dir() else repo_root
    packages: list[dict[str, Any]] = []
    for artifact in sorted(search_root.rglob("artifact.yaml")):
        package_dir = artifact.parent
        corrected = package_dir / "corrected.tex"
        if not corrected.exists():
            continue
        data = read_yaml(artifact)
        identity = data.get("identity") or {}
        label = str(identity.get("label") or "")
        kind = str(identity.get("kind") or "")
        if kind not in kinds:
            continue
        if labels and label not in labels:
            continue
        packages.append(
            {
                "label": label,
                "kind": kind,
                "artifact": artifact,
                "corrected_tex": corrected,
                "package_dir": package_dir,
                "source_file": str((data.get("location") or {}).get("source_file") or ""),
            }
        )
    return packages


def generated_artifact(
    *,
    sweep: Any,
    block: Any,
    repo_root: Path,
    governance: Path,
    registry: dict[str, str],
) -> dict[str, Any]:
    remarks = remark_map(sweep, block)
    standard_latex = remark_display(remarks, "standard quantified") or first_display(block.text)
    predicate_latex = remark_display(remarks, "predicate reading")
    negation_latex = remark_display(remarks, "negated quantified")
    contrapositive_latex = remark_display(remarks, "contrapositive")
    statement_latex = standard_latex or first_display(block.text)
    statement_ast = ast_from_latex(statement_latex, registry)
    predicate_ast = predicate_ast_from_latex(predicate_latex, registry) if predicate_latex else None
    negation_ast = ast_from_latex(negation_latex, registry) if negation_latex else None
    book, chapter, topic = path_context(block.repo_relative_path)
    title = block.title or block.label
    source_file = repo_root / block.repo_relative_path
    dependency_edges = [
        {"kind": "dependency", "target": label, "display": None, "notes": "Extracted from source dependency block."}
        for label in sorted(set(DEPENDENCY_RE.findall(block.text)))
    ]
    return {
        "schema_version": "lra.semantic-artifact/1.0",
        "identity": {
            "label": block.label,
            "kind": block.env,
            "title": title,
            "canonical_name": title,
            "status": "draft",
            "atomicity": {
                "status": "atomic",
                "concepts_detected": [title],
                "owning_concept": title,
                "split_reason": None,
            },
        },
        "location": {
            "repository": f"wsollers/{repo_root.name}",
            "commit": run_git(repo_root, "rev-parse", "HEAD"),
            "volume": "iii",
            "book": book,
            "chapter": chapter,
            "topic": topic,
            "source_file": block.repo_relative_path,
            "source_line_start": block.line_start,
            "source_line_end": block.line_end,
            "source_hash": file_sha256(source_file),
        },
        "classification": {
            "mathematical_domain": chapter,
            "artifact_form": "generated_local_parse",
            "logical_shape": "parsed_from_tex",
            "logical_framework": "mathematical_vernacular",
            "language_level": "object_language",
        },
        "context": [],
        "parameters": [],
        "assumptions": [],
        "statement": {
            "canonical_prose": title,
            "canonical_latex": statement_latex,
            "semantic_ast": statement_ast,
        },
        "logical_forms": {
            "standard_quantified": {
                "latex": standard_latex,
                "ast": ast_from_latex(standard_latex, registry) if standard_latex else raw_latex(""),
            },
            "predicate_reading": {
                "latex": predicate_latex,
                "ast": predicate_ast or raw_latex(predicate_latex),
                "registry_predicates": predicate_ids_from_latex(predicate_latex, registry),
                "registry_structures": [],
            }
            if predicate_latex
            else None,
            "negation": {
                "mechanical": {"latex": negation_latex, "ast": negation_ast} if negation_latex else None,
                "approved_normal_form": None,
                "normalization_requires": [],
            },
            "contrapositive": {
                "latex": contrapositive_latex,
                "ast": ast_from_latex(contrapositive_latex, registry),
            }
            if contrapositive_latex
            else None,
            "equivalent_forms": [],
        },
        "semantics": {
            "witness_dependencies": [],
            "vacuity_behavior": [],
            "definedness": {"mode": "unknown", "conditions": [], "obligations": []},
            "uniqueness_conditions": [],
            "equality_cases": [],
            "edge_cases": [],
        },
        "failure_analysis": {
            "applicability_failures": [],
            "statement_failures": [],
            "counterexample_shape": None,
        },
        "relationships": {
            "dependency_edges": dependency_edges,
            "ontology_edges": [],
            "provenance_edges": [],
            "proof_edges": [],
        },
        "notation": {"introduced": [], "used": [], "local_conventions": []},
        "exposition": {
            "interpretation": "",
            "exposition": [],
            "examples": [],
            "non_examples": [],
            "common_confusions": [],
        },
        "verification": {
            "canonical_proof": None,
            "formalizations": [],
            "external_library_crosswalks": [],
            "proof_vault_records": [],
        },
        "provenance": {
            "origin": {
                "kind": "normalized_source_statement",
                "source_status": "single_primary_statement",
                "primary_source_statement": {
                    "role": "primary_statement",
                    "source_id": None,
                    "label": block.label,
                    "citation": None,
                    "page_range": None,
                    "evidence": "Generated locally from the source TeX block and support remarks.",
                    "notes": "Draft parser output; not reviewed semantic content.",
                },
                "component_sources": [],
                "derivation_rule": "local_tex_ast_parser",
                "requires_review": True,
            },
            "explicit_from_source": ["source TeX block"],
            "normalized_from_source": ["standard quantified statement", "predicate reading", "negation blocks"],
            "inferred_from_registry": [],
            "generated_by_analysis": ["tools/governance/drive_semantic_artifact_reviews.py"],
            "unresolved": [],
        },
        "governance": {
            "governance_repository": "wsollers/lra-governance",
            "governance_commit": run_git(governance, "rev-parse", "HEAD"),
            "registry_commit": run_git(governance, "rev-parse", "HEAD"),
            "schema_commit": run_git(governance, "rev-parse", "HEAD"),
            "renderer_contract": "governed-tex-v1",
        },
    }


def write_draft_support_files(
    *,
    package_dir: Path,
    block: Any,
    artifact: Path,
    corrected: Path,
    data: dict[str, Any],
) -> None:
    """Write local-draft support files that mirror the semantic package family.

    These files are intentionally local deterministic artifacts for the
    no-external-review mode.  They do not claim external semantic review and
    therefore do not include a governed `external-review-receipt.yaml`.
    """

    source_lines = block.text.rstrip().splitlines(keepends=True)
    corrected_lines = corrected.read_text(encoding="utf-8").rstrip().splitlines(keepends=True)
    patch = "".join(
        difflib.unified_diff(
            source_lines,
            corrected_lines,
            fromfile=f"a/{block.repo_relative_path}",
            tofile=f"b/{block.repo_relative_path}",
            lineterm="",
        )
    )
    source_patch = package_dir / "source.patch"
    source_patch.write_text(patch + ("\n" if patch and not patch.endswith("\n") else ""), encoding="utf-8")

    label = block.label
    unresolved = (data.get("provenance") or {}).get("unresolved") or []
    validation = {
        "schema_version": "lra.semantic-artifact-validation/1.0",
        "artifact_label": label,
        "result": "pass_with_warnings",
        "checks": {
            "generated_artifact_written": "pass",
            "corrected_tex_written": "pass",
            "local_logic_validation": "skipped",
            "independent_ast_extractor_comparison": "skipped",
            "external_semantic_review": "skipped",
        },
        "diagnostics": [
            {
                "code": "LOCAL_DRAFT_NOT_EXTERNAL_REVIEWED",
                "severity": "warning",
                "field": None,
                "message": "Generated by the local Python AST driver; no external semantic-review receipt is present.",
                "autofixable": False,
            }
        ],
    }
    write_yaml(package_dir / "validation.yaml", validation)

    source_map = {
        "schema_version": "lra.semantic-artifact-source-map/1.0",
        "artifact_label": label,
        "mappings": [
            {
                "field": "statement",
                "source_file": block.repo_relative_path,
                "line_start": block.line_start,
                "line_end": block.line_end,
                "origin": "analysis",
                "confidence": "medium",
                "notes": "Derived from the source environment and nearby semantic remark blocks by the local driver.",
            },
            {
                "field": "logical_forms",
                "source_file": block.repo_relative_path,
                "line_start": block.line_start,
                "line_end": block.line_end,
                "origin": "analysis",
                "confidence": "medium",
                "notes": "Parsed from prose/TeX forms with deterministic local heuristics.",
            },
        ],
    }
    write_yaml(package_dir / "source-map.yaml", source_map)

    registry_needs = {
        "schema_version": "lra.semantic-artifact-registry-needs/1.0",
        "artifact_label": label,
        "missing_predicates": [],
        "missing_structures": [],
        "missing_relations": [],
        "missing_notation": [],
        "alias_candidates": [],
        "ambiguities": unresolved,
    }
    write_yaml(package_dir / "registry-needs.yaml", registry_needs)

    resolver_note = {
        "status": "skipped",
        "message": "Local AST sweep did not query external formalization/proof-vault indexes.",
    }
    write_yaml(
        package_dir / "formalization-links.yaml",
        {
            "schema_version": "lra.semantic-artifact-formalization-links/1.0",
            "artifact_label": label,
            "resolved": [resolver_note],
        },
    )
    write_yaml(
        package_dir / "proof-vault-links.yaml",
        {
            "schema_version": "lra.semantic-artifact-proof-vault-links/1.0",
            "artifact_label": label,
            "resolved": [resolver_note],
        },
    )

    package_note = {
        "schema_version": "lra.local-semantic-artifact-draft-package/1.0",
        "artifact_label": label,
        "created_at": dt.datetime.now(dt.UTC).isoformat().replace("+00:00", "Z"),
        "status": "local_draft_not_external_reviewed",
        "source": {
            "repository": "wsollers/lra-volume-iii",
            "file": block.repo_relative_path,
            "line_start": block.line_start,
            "line_end": block.line_end,
        },
        "files": {
            "artifact": {"path": "artifact.yaml", "sha256": file_sha256_bare(artifact)},
            "corrected_tex": {"path": "corrected.tex", "sha256": file_sha256_bare(corrected)},
            "source_patch": {"path": "source.patch", "sha256": file_sha256_bare(source_patch)},
            "validation": {"path": "validation.yaml", "sha256": file_sha256_bare(package_dir / "validation.yaml")},
            "source_map": {"path": "source-map.yaml", "sha256": file_sha256_bare(package_dir / "source-map.yaml")},
            "registry_needs": {
                "path": "registry-needs.yaml",
                "sha256": file_sha256_bare(package_dir / "registry-needs.yaml"),
            },
            "formalization_links": {
                "path": "formalization-links.yaml",
                "sha256": file_sha256_bare(package_dir / "formalization-links.yaml"),
            },
            "proof_vault_links": {
                "path": "proof-vault-links.yaml",
                "sha256": file_sha256_bare(package_dir / "proof-vault-links.yaml"),
            },
        },
        "not_emitted": {
            "package_yaml": "Not emitted for this local no-external-review run; the governed package schema requires real external-review evidence.",
            "external_review_receipt_yaml": "Not emitted for this local no-external-review run.",
            "audit_validation_yaml": "Not emitted for this local no-external-review run; audit validation is produced only after governed review/application/reversion.",
        },
    }
    write_yaml(package_dir / "local-draft-package.yaml", package_note)

    readme = """# Local semantic artifact draft

This directory mirrors the deterministic support-file family used by governed
semantic artifact packages, but it is not a reviewed governance package.

This run used the local no-external-review mode.  Consequently it did not create
`external-review-receipt.yaml`, and it did not create the schema-governed
`package.yaml`, because that schema requires live external review evidence.

If a future run is explicitly invoked through the governed external-review/LLM
path, this limitation does not apply: that mode must create real reviewer
evidence and may emit the governed package manifest.

Run outputs added after generation:

- `logic-validation.json`
- `ast-extractor-comparison.json`

Use this draft for fast mechanical triage.  Promote it to a governed package
only through the documented semantic artifact review workflow.
"""
    (package_dir / "README.md").write_text(readme, encoding="utf-8")


def expected_governed_files() -> list[str]:
    return [
        "package.yaml",
        "artifact.yaml",
        "corrected.tex",
        "source.patch",
        "validation.yaml",
        "source-map.yaml",
        "registry-needs.yaml",
        "formalization-links.yaml",
        "proof-vault-links.yaml",
        "external-review-receipt.yaml",
        "audit-validation.yaml",
    ]


def expected_ast_sources() -> list[dict[str, Any]]:
    return [
        {
            "id": "local_naive_driver",
            "producer": "tools/governance/drive_semantic_artifact_reviews.py",
            "required": True,
            "role": "baseline deterministic AST from governed TeX and semantic remark blocks",
        },
        {
            "id": "llm_semantic_reviewer",
            "producer": "governed external-review/LLM mode",
            "required": True,
            "role": "independently generated semantic AST from prose, quantified forms, predicate readings, negations, and TeX",
        },
        {
            "id": "surface_regex",
            "producer": "tools/governance/compare_semantic_ast_extractors.py",
            "required": True,
            "role": "shallow source cues: labels, environment kind, quantifiers, implication/equivalence, negation, predicates, dependencies",
        },
        {
            "id": "pylatexenc",
            "producer": "pylatexenc latex walker when installed",
            "required": False,
            "role": "LaTeX node walk over source/corrected TeX",
        },
        {
            "id": "tree_sitter_latex",
            "producer": "tree_sitter_language_pack when installed",
            "required": False,
            "role": "independent LaTeX parse tree over source/corrected TeX",
        },
        {
            "id": "nltk_prose",
            "producer": "NLTK when installed/configured",
            "required": False,
            "role": "prose tokenization and cue extraction for quantifier/predicate candidates; not authoritative alone",
        },
        {
            "id": "sympy",
            "producer": "SymPy parser/symbolic transforms where the formula fragment is in scope",
            "required": False,
            "role": "symbolic expression AST and algebraic/symbol pushing checks for supported fragments",
        },
        {
            "id": "latex2sympy",
            "producer": "latex2sympy/latex2sympy2 style parser when installed",
            "required": False,
            "role": "LaTeX-to-SymPy AST for supported displayed math fragments",
        },
        {
            "id": "sage_parser",
            "producer": "SageMath sage.misc.parser.Parser when a Sage-capable runtime is available",
            "required": False,
            "role": "symbolic expression, equation, inequality, variable, function-call, and implicit-multiplication AST witness for supported algebraic fragments",
        },
        {
            "id": "python_ast",
            "producer": "stdlib ast over generated Python-side symbolic/predicate expressions",
            "required": False,
            "role": "sanity check for generated symbolic expression encodings, not raw TeX",
        },
        {
            "id": "lean_ast_export",
            "producer": "Lean/mathlib or user Lean export when a corresponding theorem is known",
            "required": False,
            "role": "formal reference AST/crosswalk for proven artifacts",
        },
        {
            "id": "microsoft_quantifier",
            "producer": "configured Microsoft quantifier/parser tool if available",
            "required": False,
            "role": "additional quantified-form extraction and comparison source",
        },
    ]


def ast_comparison_dimensions() -> list[dict[str, Any]]:
    return [
        {
            "id": "quantifier_order",
            "required": True,
            "description": "Compare quantifier nesting/order across AST candidates.",
        },
        {
            "id": "quantifier_variable_count",
            "required": True,
            "description": "Compare quantifier macro count and bound-variable count, including grouped binders such as a,b,c in a single quantified list.",
        },
        {
            "id": "binders_and_domains",
            "required": True,
            "description": "Compare binders, explicit domains, implicit ambient domains, restrictions, and binder scope.",
        },
        {
            "id": "let_assumptions_and_initial_conditions",
            "required": True,
            "description": "Account for every Let/Suppose/Assume/Given/Where clause and include the full initial-condition context of the theorem or definition.",
        },
        {
            "id": "implication_equivalence_shape",
            "required": True,
            "description": "Compare implication, converse, inverse, contrapositive, biconditional, and n-way equivalence structure.",
        },
        {
            "id": "predicate_identities",
            "required": True,
            "description": "Compare predicate identities, aliases, arities, argument order, type order, and construction sites.",
        },
        {
            "id": "structure_identities",
            "required": True,
            "description": "Compare structures as first-class semantic objects, including structure aliases, arities, carrier/ambient types, and construction dependencies.",
        },
        {
            "id": "variable_ambient_type_flow",
            "required": True,
            "description": "Track variables and ambient types across function calls, predicate applications, structure constructions, coercions, and inherited contexts.",
        },
        {
            "id": "negation_placement",
            "required": True,
            "description": "Compare exact negation placement and De Morgan/quantifier-dual transformations used by mechanical negation.",
        },
        {
            "id": "witness_dependencies",
            "required": True,
            "description": "Compare existential witnesses, dependencies on prior binders/assumptions, and independence claims.",
        },
        {
            "id": "mechanically_derived_statements",
            "required": True,
            "description": "Use the normalized AST/logic to mechanically derive and verify companion statements such as negation, contrapositive, converse, inverse, and supported equivalent forms.",
        },
        {
            "id": "indexed_source_alignment",
            "required": True,
            "description": "Search indexed sources for theorem/definition candidates, cite and annotate matches, and record whether the artifact is source-derived, loosely aligned, or author-created.",
        },
    ]


def write_llm_plan_manifest(
    *,
    output_root: Path,
    target: Path,
    repo_root: Path,
    governance: Path,
    selected_blocks: list[Any],
    existing_packages: dict[str, dict[str, Any]],
) -> Path:
    """Write a Codex-side orchestration plan for governed LLM review mode.

    The local Python process cannot put Codex into Plan mode or create Codex
    threads.  This manifest is the deterministic handoff: Codex should consume
    it, create one plan with section-scoped child tasks/threads as appropriate,
    and update completion status only from real package and validation evidence.
    """

    sections: dict[str, dict[str, Any]] = {}
    for ordinal, block in enumerate(selected_blocks, start=1):
        book, chapter, topic = path_context(block.repo_relative_path)
        section_key = f"{book}/{chapter}/{topic}"
        section = sections.setdefault(
            section_key,
            {
                "section_key": section_key,
                "book": book,
                "chapter": chapter,
                "topic": topic,
                "status": "pending",
                "codex_thread": None,
                "items": [],
            },
        )
        package_dir = existing_packages.get(block.label, {}).get("package_dir")
        if package_dir is None:
            package_dir = output_root / label_slug(block.label)
        section["items"].append(
            {
                "ordinal": ordinal,
                "label": block.label,
                "kind": block.env,
                "source_file": block.repo_relative_path,
                "source_line_start": block.line_start,
                "source_line_end": block.line_end,
                "package_dir": str(package_dir),
                "status": "pending",
                "status_reason": "queued_for_governed_llm_review",
                "expected_files": expected_governed_files(),
                "expected_ast_sources": expected_ast_sources(),
                "ast_comparison_dimensions": ast_comparison_dimensions(),
                "completion_evidence": {
                    "external_review_receipt": None,
                    "package_manifest": None,
                    "ast_ensemble": None,
                    "ast_confidence_report": None,
                    "source_alignment_report": None,
                    "mechanical_derivation_report": None,
                    "audit_validation": None,
                    "logic_validation": None,
                    "ast_extractor_comparison": None,
                    "volume_validation": None,
                    "build": None,
                },
            }
        )

    manifest = {
        "schema_version": "lra.semantic-artifact-llm-plan/1.0",
        "mode": "codex_plan_governed_llm_review",
        "created_at": dt.datetime.now(dt.UTC).isoformat().replace("+00:00", "Z"),
        "target": str(target),
        "repo_root": str(repo_root),
        "governance_root": str(governance),
        "output_root": str(output_root),
        "orchestration": {
            "codex_plan_mode_required": True,
            "recommended_thread_granularity": "section",
            "per_item_external_review_required": True,
            "local_python_validation_required": True,
            "multi_ast_comparison_required": True,
            "normalization_required": True,
            "symbolic_transform_checks": [
                "mechanical_negation",
                "contrapositive",
                "converse",
                "inverse",
                "predicate_detection",
                "structure_detection",
                "arity_and_type_order",
                "quantifier_scope",
                "quantifier_variable_count",
                "binder_dependencies",
                "let_assumptions",
                "initial_conditions",
                "ambient_type_flow",
            ],
            "source_alignment": {
                "indexed_source_lookup_required": True,
                "exact_match_not_required": True,
                "unmatched_items_status": "candidate_author_created_or_unindexed",
                "report_unmatched_items_for_user_classification": True,
            },
            "status_rule": "Mark an item complete only after required package files exist, external evidence is real/live-verifiable, local AST gates are recorded, the LLM AST is compared against the naive/local/parser/formal AST ensemble, structural dimensions and mechanical derivations are recorded, indexed source alignment is cited/annotated or marked unmatched for user classification, confidence is recorded, and audit-validation.yaml records the final result.",
            "allowed_terminal_item_statuses": [
                "complete",
                "blocked_mathematical_review",
                "blocked_infrastructure",
                "failed_validation",
                "pending_user_source_classification",
            ],
        },
        "sections": list(sections.values()),
    }
    path = output_root / "llm-review-plan.json"
    write_json(path, manifest)
    return path


def generate_package(
    *,
    sweep: Any,
    block: Any,
    repo_root: Path,
    governance: Path,
    output_root: Path,
    registry: dict[str, str],
) -> dict[str, Any]:
    package_dir = output_root / label_slug(block.label)
    artifact = package_dir / "artifact.yaml"
    corrected = package_dir / "corrected.tex"
    data = generated_artifact(sweep=sweep, block=block, repo_root=repo_root, governance=governance, registry=registry)
    write_yaml(artifact, data)
    corrected.write_text(block.text.rstrip() + "\n", encoding="utf-8")
    write_draft_support_files(package_dir=package_dir, block=block, artifact=artifact, corrected=corrected, data=data)
    return {
        "label": block.label,
        "kind": block.env,
        "artifact": artifact,
        "corrected_tex": corrected,
        "package_dir": package_dir,
        "source_file": block.repo_relative_path,
        "generated": True,
    }


def run_json(command: list[str]) -> tuple[int, dict[str, Any] | None, str, str]:
    completed = subprocess.run(command, capture_output=True, text=True)
    payload = None
    if completed.stdout.strip():
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError:
            payload = None
    return completed.returncode, payload, completed.stdout, completed.stderr


def severity_rank(payload: dict[str, Any] | None) -> int:
    if not payload:
        return 1000
    result = str(payload.get("result") or "")
    base = {
        "blocked": 400,
        "fail": 300,
        "pass_with_warnings": 100,
        "pass": 0,
    }.get(result, 200)
    findings = payload.get("findings") or []
    weights = {"blocking": 80, "error": 40, "warning": 10, "info": 1}
    return base + sum(weights.get(str(item.get("severity") or ""), 0) for item in findings if isinstance(item, dict))


def run_package(
    *,
    package: dict[str, Any],
    governance: Path,
    repo_root: Path,
    output_root: Path,
) -> dict[str, Any]:
    label = package["label"]
    out_dir = output_root / label_slug(label)
    logic_output = out_dir / "logic-validation.json"
    compare_output = out_dir / "ast-extractor-comparison.json"
    ensemble_output = out_dir / "ast-ensemble.json"

    logic_cmd = [
        sys.executable,
        str(governance / "tools" / "governance" / "validate_semantic_logic.py"),
        "--artifact",
        str(package["artifact"]),
        "--corrected-tex",
        str(package["corrected_tex"]),
        "--format",
        "json",
    ]
    logic_code, logic_payload, logic_stdout, logic_stderr = run_json(logic_cmd)
    if logic_payload is not None:
        write_json(logic_output, logic_payload)
    else:
        write_json(logic_output, {"result": "tool_error", "stdout": logic_stdout, "stderr": logic_stderr})

    compare_payload: dict[str, Any] | None = None
    compare_code: int | None = None
    source_file = str(package.get("source_file") or "")
    source_path = repo_root / source_file if source_file else None
    if source_path is not None and source_path.exists():
        compare_cmd = [
            sys.executable,
            str(governance / "tools" / "governance" / "compare_semantic_ast_extractors.py"),
            "--source-tex",
            str(source_path),
            "--artifact",
            str(package["artifact"]),
            "--target-label",
            label,
            "--format",
            "json",
        ]
        compare_code, compare_payload, compare_stdout, compare_stderr = run_json(compare_cmd)
        if compare_payload is not None:
            write_json(compare_output, compare_payload)
        else:
            write_json(compare_output, {"result": "tool_error", "stdout": compare_stdout, "stderr": compare_stderr})

    ensemble_payload: dict[str, Any] | None = None
    ensemble_code: int | None = None
    if source_path is not None and source_path.exists():
        ensemble_cmd = [
            sys.executable,
            str(governance / "tools" / "governance" / "semantic_ast_ensemble.py"),
            "--target",
            str(source_path),
            "--repo-root",
            str(repo_root),
            "--label",
            label,
            "--artifact",
            str(package["artifact"]),
            "--output",
            str(ensemble_output),
            "--format",
            "json",
        ]
        completed = subprocess.run(ensemble_cmd, capture_output=True, text=True)
        ensemble_code = completed.returncode
        if ensemble_output.exists():
            try:
                ensemble_payload = json.loads(ensemble_output.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                ensemble_payload = None
        if ensemble_payload is None:
            write_json(ensemble_output, {"result": "tool_error", "stdout": completed.stdout, "stderr": completed.stderr})

    compare_findings = []
    if isinstance(compare_payload, dict):
        compare_findings = compare_payload.get("findings") or []
    ensemble_findings: list[Any] = []
    ensemble_result = None
    if isinstance(ensemble_payload, dict):
        reports = ensemble_payload.get("reports") or []
        if reports and isinstance(reports[0], dict):
            ensemble_result = reports[0].get("result")
            ensemble_findings = reports[0].get("comparison_findings") or []
    score = severity_rank(logic_payload) + (50 * len(compare_findings)) + (50 * len(ensemble_findings))
    return {
        "label": label,
        "kind": package["kind"],
        "status": (logic_payload or {}).get("result", "tool_error"),
        "score": score,
        "logic_returncode": logic_code,
        "logic_finding_count": len((logic_payload or {}).get("findings") or []),
        "extractor_returncode": compare_code,
        "extractor_result": (compare_payload or {}).get("result") if compare_payload else None,
        "extractor_finding_count": len(compare_findings),
        "ensemble_returncode": ensemble_code,
        "ensemble_result": ensemble_result,
        "ensemble_finding_count": len(ensemble_findings),
        "artifact": str(package["artifact"]),
        "corrected_tex": str(package["corrected_tex"]),
        "logic_validation": str(logic_output),
        "ast_extractor_comparison": str(compare_output) if compare_payload is not None else None,
        "ast_ensemble": str(ensemble_output) if ensemble_payload is not None else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate missing local semantic artifacts and run AST validation.")
    parser.add_argument("--target", type=Path, default=Path("volume-iii.tex"))
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--governance-root", type=Path)
    parser.add_argument("--output-root", type=Path, default=Path("build/semantic-audit/volume-iii-ast-validation"))
    parser.add_argument(
        "--kinds",
        default="definition,theorem,lemma,proposition,corollary",
        help="Comma-separated environment kinds to inventory and validate.",
    )
    parser.add_argument("--label", action="append", default=[], help="Exact label to validate. May be repeated.")
    parser.add_argument("--limit", type=int, help="Limit source artifacts generated/validated.")
    parser.add_argument("--no-generate", action="store_true", help="Only validate packages that already exist in source.")
    parser.add_argument(
        "--reviewer-mode",
        choices=("local", "llm-plan"),
        default="local",
        help=(
            "local runs deterministic Python generation/AST validation. "
            "llm-plan writes a Codex Plan-mode orchestration manifest and does not call an LLM itself."
        ),
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    governance = args.governance_root.resolve() if args.governance_root else governance_root()
    target = args.target.resolve()
    output_root = args.output_root.resolve()
    kinds = parse_kinds(args.kinds)
    labels = set(args.label)
    if not target.exists():
        fail(f"target does not exist: {target}")

    sweep = load_semantic_chapter_sweep(governance)
    registry = predicate_registry(governance)
    source_blocks = inventory_source_blocks(sweep, target, repo_root, kinds)
    existing_packages = {
        str(package["label"]): package
        for package in find_artifact_packages(repo_root / "volume-iii", repo_root, kinds, labels)
    }

    selected_blocks = [
        block
        for label, block in source_blocks.items()
        if not labels or label in labels
    ]
    if args.limit is not None:
        selected_blocks = selected_blocks[: args.limit]

    if args.reviewer_mode == "llm-plan":
        plan_path = write_llm_plan_manifest(
            output_root=output_root,
            target=target,
            repo_root=repo_root,
            governance=governance,
            selected_blocks=selected_blocks,
            existing_packages=existing_packages,
        )
        summary = {
            "schema_version": "lra.semantic-artifact-ast-validation-driver/1.0",
            "mode": "codex_plan_governed_llm_review",
            "target": str(target),
            "repo_root": str(repo_root),
            "governance_root": str(governance),
            "output_root": str(output_root),
            "source_artifacts_in_scope": len(selected_blocks),
            "plan_manifest": str(plan_path),
            "status": "plan_written_pending_codex_orchestration",
        }
        write_json(output_root / "driver-report.json", summary)
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    packages: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    generated_count = 0
    reused_count = 0
    for block in selected_blocks:
        existing = existing_packages.get(block.label)
        if existing is not None:
            packages.append(existing)
            reused_count += 1
            continue
        if args.no_generate:
            missing.append(
                {
                    "label": block.label,
                    "kind": block.env,
                    "source": f"{block.repo_relative_path}:{block.line_start}",
                    "status": "missing_artifact_package",
                }
            )
            continue
        packages.append(
            generate_package(
                sweep=sweep,
                block=block,
                repo_root=repo_root,
                governance=governance,
                output_root=output_root,
                registry=registry,
            )
        )
        generated_count += 1

    results = [run_package(package=package, governance=governance, repo_root=repo_root, output_root=output_root) for package in packages]
    results.sort(key=lambda item: (-int(item.get("score") or 0), str(item.get("label") or "")))

    summary = {
        "schema_version": "lra.semantic-artifact-ast-validation-driver/1.0",
        "mode": "local_python_ast_validation",
        "target": str(target),
        "repo_root": str(repo_root),
        "governance_root": str(governance),
        "output_root": str(output_root),
        "source_artifacts_in_scope": len(selected_blocks),
        "artifact_packages_found": len(packages),
        "artifact_packages_reused": reused_count,
        "artifact_packages_generated": generated_count,
        "missing_artifact_packages": len(missing),
        "results": results,
        "missing": missing,
    }
    write_json(output_root / "driver-report.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
