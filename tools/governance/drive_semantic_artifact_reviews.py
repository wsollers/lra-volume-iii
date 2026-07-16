#!/usr/bin/env python3
"""Generate and locally validate semantic artifact packages from TeX blocks.

This driver intentionally does not call an external reviewer or external LLM.
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

    compare_findings = []
    if isinstance(compare_payload, dict):
        compare_findings = compare_payload.get("findings") or []
    score = severity_rank(logic_payload) + (50 * len(compare_findings))
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
        "artifact": str(package["artifact"]),
        "corrected_tex": str(package["corrected_tex"]),
        "logic_validation": str(logic_output),
        "ast_extractor_comparison": str(compare_output) if compare_payload is not None else None,
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
