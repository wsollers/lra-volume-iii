#!/usr/bin/env python3
r"""Migrate existing leaf proof files toward the proof-stub invariant.

Default mode is dry-run. The script makes only conservative changes:

* add ``\LRAProofFor{...}`` when a unique high-confidence theorem target exists;
* normalize existing proof files to contain professional and detailed sections;
* create TODO proof stubs for still-missing proof-bearing theorem labels.

It never moves proof files, deletes proof files, deletes existing proof content,
or changes theorem/proof labels.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path


PROOF_BEARING_ENVS = {"theorem", "proposition", "lemma", "corollary"}
BEGIN_ENV_RE = re.compile(
    r"\\begin\{(?P<env>theorem|proposition|lemma|corollary)\}(?:\[(?P<title>[^\]]*)\])?",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
PROOF_FOR_RE = re.compile(r"\\LRAProofFor\{([^{}]+)\}")
HYPERREF_RE = re.compile(r"\\hyperref\[([^\]]+)\]")
PROOF_VAULT_RE = re.compile(r"\\ProofVaultURL\{([^{}]*)\}")
PROOF_ENV_RE = re.compile(r"\\begin\{proof\}(?P<body>.*?)\\end\{proof\}", re.DOTALL)


@dataclass
class TheoremNode:
    env: str
    label: str
    title: str
    path: Path
    line: int


@dataclass
class ProofFile:
    path: Path
    text: str
    labels: list[str]
    proof_for: list[str]
    hyperrefs: list[str]
    title_text: str


@dataclass
class Action:
    action: str
    path: str
    theorem_id: str | None = None
    confidence: str | None = None
    reason: str | None = None
    details: dict = field(default_factory=dict)


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


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def slug_from_label(label: str) -> str:
    return label.split(":", 1)[1] if ":" in label else label


def proof_label_for(theorem_id: str) -> str:
    return f"prf:{slug_from_label(theorem_id)}"


def proof_filename_for(theorem_id: str) -> str:
    return f"prf-{slug_from_label(theorem_id)}.tex"


def iter_tex_files(root: Path, part: str):
    for path in sorted(root.rglob("*.tex")):
        if any(piece.startswith(".") for piece in path.parts):
            continue
        if part in path.parts:
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


def discover_theorems(root: Path) -> tuple[list[TheoremNode], list[Action]]:
    theorems: list[TheoremNode] = []
    reports: list[Action] = []
    for path in iter_tex_files(root, "notes"):
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        for match in BEGIN_ENV_RE.finditer(text):
            env = match.group("env")
            end = find_matching_end(text, env, match.end())
            body = text[match.end():end]
            labels = [label for label in LABEL_RE.findall(body) if label.split(":", 1)[0] in {"thm", "prop", "lem", "cor"}]
            if not labels:
                reports.append(Action("missing_theorem_label", rel(path, root), reason=f"{env} has no theorem/proof-bearing label", details={"line": line_number(text, match.start())}))
                continue
            title = (match.group("title") or slug_from_label(labels[0]).replace("-", " ").title()).strip()
            theorems.append(TheoremNode(env=env, label=labels[0], title=title, path=path, line=line_number(text, match.start())))
    return theorems, reports


def discover_proofs(root: Path) -> list[ProofFile]:
    proofs: list[ProofFile] = []
    for path in iter_tex_files(root, "proofs"):
        if path.name == "index.tex" or "exercises" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        cleaned = strip_comments(text)
        labels = [label for label in LABEL_RE.findall(cleaned) if label.startswith("prf:")]
        if not labels and not path.stem.startswith("prf-"):
            continue
        title_match = re.search(r"\\begin\{(?:theorem|proposition|lemma|corollary)\*\}(?:\[([^\]]*)\])?", cleaned)
        proofs.append(
            ProofFile(
                path=path,
                text=text,
                labels=labels,
                proof_for=PROOF_FOR_RE.findall(cleaned),
                hyperrefs=HYPERREF_RE.findall(cleaned),
                title_text=(title_match.group(1) if title_match and title_match.group(1) else ""),
            )
        )
    return proofs


def infer_target(proof: ProofFile, theorem_by_label: dict[str, TheoremNode], labels_by_slug: dict[str, list[str]]) -> tuple[str | None, str, str]:
    existing = [target for target in proof.proof_for if target in theorem_by_label]
    if len(set(existing)) == 1:
        return existing[0], "existing", "existing \\LRAProofFor target"
    if len(set(proof.proof_for)) > 1:
        return None, "ambiguous", "multiple existing \\LRAProofFor targets"

    return_refs: list[str] = []
    for block in re.finditer(r"\\begin\{remark\*\}\[Return\](?P<body>.*?)\\end\{remark\*\}", proof.text, re.DOTALL):
        return_refs.extend(HYPERREF_RE.findall(block.group("body")))
    linked = [ref for ref in return_refs if ref in theorem_by_label]
    if len(set(linked)) == 1:
        return linked[0], "high", "unique theorem return/link target"
    if len(set(linked)) > 1:
        return None, "ambiguous", "multiple theorem hyperref targets"

    candidates: set[str] = set()
    for proof_label in proof.labels:
        if proof_label.startswith("prf:"):
            candidates.update(labels_by_slug.get(slug_from_label(proof_label), []))
    if len(candidates) == 1:
        return next(iter(candidates)), "high", "proof label root match"
    if len(candidates) > 1:
        return None, "ambiguous", "proof label root matches multiple theorem labels"

    stem = proof.path.stem
    if stem.startswith("prf-"):
        candidates.update(labels_by_slug.get(stem.removeprefix("prf-"), []))
    if len(candidates) == 1:
        return next(iter(candidates)), "high", "proof filename root match"
    if len(candidates) > 1:
        return None, "ambiguous", "proof filename root matches multiple theorem labels"

    if proof.title_text:
        scored = []
        proof_title = proof.title_text.lower()
        for label, node in theorem_by_label.items():
            score = SequenceMatcher(None, proof_title, node.title.lower()).ratio()
            if score >= 0.9:
                scored.append((score, label))
        scored.sort(reverse=True)
        if len(scored) == 1 or (len(scored) > 1 and scored[0][0] - scored[1][0] >= 0.08):
            return scored[0][1], "medium", "title similarity"
        if scored:
            return None, "ambiguous", "title similarity matches multiple theorem labels"

    return None, "unmatched", "no conservative theorem target found"


def insert_lra_proof_for(text: str, theorem_id: str) -> tuple[str, bool]:
    if PROOF_FOR_RE.search(strip_comments(text)):
        return text, False
    label_match = re.search(r"\\label\{prf:[^{}]+\}", text)
    insertion = f"\n\\LRAProofFor{{{theorem_id}}}"
    if label_match:
        return text[:label_match.end()] + insertion + text[label_match.end():], True
    return f"\\LRAProofFor{{{theorem_id}}}\n" + text, True


def normalize_bodies(text: str) -> tuple[str, bool]:
    lower = strip_comments(text).lower()
    has_prof = bool(re.search(r"professional\s+(standard\s+)?proof", lower))
    has_detail = bool(re.search(r"detailed\s+(learning\s+)?proof", lower))
    if has_prof and has_detail:
        return text, False

    migration_comment = "% MIGRATION TODO: Existing proof content preserved; detailed/professional companion body needs review.\n"
    proof_match = PROOF_ENV_RE.search(text)
    if proof_match and not has_prof and not has_detail:
        body = proof_match.group("body").strip()
        replacement = (
            "\\textbf{Professional Standard Proof.}~\\\\\n"
            f"{migration_comment}"
            "\\begin{proof}\n"
            f"{body or 'TODO.'}\n"
            "\\end{proof}\n\n"
            "\\textbf{Detailed Learning Proof.}~\\\\\n"
            "TODO: Expand the professional proof into a detailed learning proof.\n"
        )
        return text[:proof_match.start()] + replacement + text[proof_match.end():], True

    addition = ""
    if not has_prof:
        addition += (
            "\n\\textbf{Professional Standard Proof.}~\\\\\n"
            f"{migration_comment}"
            "TODO: Write the compact canonical proof.\n"
        )
    if not has_detail:
        addition += (
            "\n\\textbf{Detailed Learning Proof.}~\\\\\n"
            f"{migration_comment}"
            "TODO: Expand the proof into a detailed learning proof.\n"
        )
    return text.rstrip() + "\n" + addition + "\n", True


def ensure_dependency_remark(text: str) -> tuple[str, bool]:
    lower = strip_comments(text).lower()
    if re.search(r"dependenc|proof[-\s]*structure", lower):
        return text, False
    addition = (
        "\n\\begin{remark*}[Proof structure]\n"
        "TODO: Record the proof strategy and major logical moves.\n"
        "\\end{remark*}\n\n"
        "\\begin{dependencies}\n"
        "\\begin{itemize}\n"
        "  \\item TODO: Add mathematical dependency links.\n"
        "\\end{itemize}\n"
        "\\end{dependencies}\n"
    )
    return text.rstrip() + "\n" + addition, True


def ensure_clearpage(text: str) -> tuple[str, bool]:
    if "\\clearpage" in text or "\\newpage" in text:
        return text, False
    return text.rstrip() + "\n\n\\clearpage\n", True


def normalize_existing_proof(text: str, theorem_id: str) -> tuple[str, dict[str, bool]]:
    changed = {"inserted_lra_proof_for": False, "normalized_bodies": False, "added_dependency_remark": False, "added_clearpage": False}
    text, did = insert_lra_proof_for(text, theorem_id)
    changed["inserted_lra_proof_for"] = did
    text, did = normalize_bodies(text)
    changed["normalized_bodies"] = did
    text, did = ensure_dependency_remark(text)
    changed["added_dependency_remark"] = did
    text, did = ensure_clearpage(text)
    changed["added_clearpage"] = did
    return text, changed


def proof_dir_for(theorem: TheoremNode) -> Path:
    parts = list(theorem.path.parts)
    if "notes" in parts:
        idx = parts.index("notes")
        parts[idx] = "proofs"
        # Current leaf convention still commonly uses proofs/notes. Do not
        # refactor folders in this phase; create stubs in the existing notes
        # proof bucket for the owning chapter/topic.
        return Path(*parts[:idx + 1]) / "notes"
    return theorem.path.parent / "proofs" / "notes"


def stub_text(theorem: TheoremNode) -> str:
    proof_label = proof_label_for(theorem.label)
    theorem_env = theorem.env if theorem.env in {"theorem", "proposition", "lemma", "corollary"} else "theorem"
    return (
        "\\newpage\n"
        "\\phantomsection\n"
        f"\\label{{{proof_label}}}\n"
        f"\\LRAProofFor{{{theorem.label}}}\n\n"
        "\\begin{remark*}[Return]\n"
        f"\\hyperref[{theorem.label}]{{Return to {theorem.env.title()}}}\n"
        "\\end{remark*}\n\n"
        f"\\begin{{{theorem_env}*}}[{theorem.title}]\n"
        "TODO: Restate the theorem/proposition/lemma/corollary for this proof file.\n"
        f"\\end{{{theorem_env}*}}\n\n"
        "\\textbf{Professional Standard Proof.}~\\\\\n"
        "TODO: Write the compact canonical proof.\n\n"
        "\\textbf{Detailed Learning Proof.}~\\\\\n"
        "TODO: Write the expanded learning proof.\n\n"
        "\\begin{remark*}[Proof structure]\n"
        "TODO: Record the proof strategy and major logical moves.\n"
        "\\end{remark*}\n\n"
        "\\begin{dependencies}\n"
        "\\begin{itemize}\n"
        "  \\item TODO: Add mathematical dependency links.\n"
        "\\end{itemize}\n"
        "\\end{dependencies}\n\n"
        "\\clearpage\n"
    )


def migrate(root: Path, *, apply: bool, limit: int | None) -> dict:
    theorems, theorem_reports = discover_theorems(root)
    theorem_by_label = {node.label: node for node in theorems}
    labels_by_slug: dict[str, list[str]] = {}
    for label in theorem_by_label:
        labels_by_slug.setdefault(slug_from_label(label), []).append(label)
    proofs = discover_proofs(root)

    actions: list[Action] = theorem_reports[:]
    matched_targets: dict[str, list[Path]] = {}
    already_linked = 0
    newly_linked = 0
    normalized = 0
    ambiguous = 0
    unmatched = 0
    changed_files = 0
    remaining_budget = limit

    for proof in proofs:
        target, confidence, reason = infer_target(proof, theorem_by_label, labels_by_slug)
        proof_rel = rel(proof.path, root)
        if target is None:
            if confidence == "ambiguous":
                ambiguous += 1
                actions.append(Action("ambiguous_proof", proof_rel, confidence=confidence, reason=reason))
            else:
                unmatched += 1
                actions.append(Action("unmatched_orphan_proof", proof_rel, confidence=confidence, reason=reason))
            continue
        matched_targets.setdefault(target, []).append(proof.path)
        if proof.proof_for:
            already_linked += 1
        new_text, changes = normalize_existing_proof(proof.text, target)
        did_change = new_text != proof.text
        if changes["inserted_lra_proof_for"]:
            newly_linked += 1
        if changes["normalized_bodies"]:
            normalized += 1
        if did_change:
            if remaining_budget is not None and remaining_budget <= 0:
                actions.append(Action("limit_skipped", proof_rel, theorem_id=target, confidence=confidence, reason="limit reached"))
                continue
            if apply:
                proof.path.write_text(new_text, encoding="utf-8", newline="")
            changed_files += 1
            if remaining_budget is not None:
                remaining_budget -= 1
            actions.append(Action("normalize_existing_proof", proof_rel, theorem_id=target, confidence=confidence, reason=reason, details=changes))
        else:
            actions.append(Action("already_normalized", proof_rel, theorem_id=target, confidence=confidence, reason=reason))

    generated_stubs = 0
    missing_targets = []
    existing_paths = {proof.path.resolve() for proof in proofs}
    for theorem in theorems:
        if theorem.label in matched_targets:
            continue
        stub_dir = root / proof_dir_for(theorem)
        stub_path = stub_dir / proof_filename_for(theorem.label)
        if stub_path.resolve() in existing_paths or stub_path.exists():
            actions.append(Action("stub_path_exists_unmatched", rel(stub_path, root), theorem_id=theorem.label, reason="path exists but proof was not matched"))
            missing_targets.append(theorem.label)
            continue
        if remaining_budget is not None and remaining_budget <= 0:
            actions.append(Action("limit_skipped_stub", rel(stub_path, root), theorem_id=theorem.label, reason="limit reached"))
            missing_targets.append(theorem.label)
            continue
        if apply:
            stub_dir.mkdir(parents=True, exist_ok=True)
            stub_path.write_text(stub_text(theorem), encoding="utf-8", newline="")
        generated_stubs += 1
        changed_files += 1
        if remaining_budget is not None:
            remaining_budget -= 1
        actions.append(Action("generate_stub", rel(stub_path, root), theorem_id=theorem.label, confidence="n/a", reason="no matched proof file"))

    theorem_target_counts = {target: len(paths) for target, paths in matched_targets.items()}
    duplicate_targets = {target: count for target, count in theorem_target_counts.items() if count > 1}
    duplicate_labels: dict[str, list[str]] = {}
    proof_label_seen: dict[str, list[str]] = {}
    for proof in proofs:
        for label in proof.labels:
            proof_label_seen.setdefault(label, []).append(rel(proof.path, root))
    for label, paths in proof_label_seen.items():
        if len(paths) > 1:
            duplicate_labels[label] = paths

    errors = []
    if duplicate_labels:
        errors.append({"code": "duplicate_proof_labels", "labels": duplicate_labels})
    if duplicate_targets:
        errors.append({"code": "multiple_proofs_for_theorem", "targets": duplicate_targets})

    return {
        "root": str(root),
        "mode": "apply" if apply else "dry-run",
        "theorem_count": len(theorems),
        "expected_proof_count": len(theorems),
        "proof_file_count": len(proofs),
        "already_linked_proofs": already_linked,
        "newly_linked_proofs": newly_linked,
        "generated_stub_count": generated_stubs,
        "existing_proofs_wrapped_or_normalized": normalized,
        "ambiguous_proofs": ambiguous,
        "unmatched_orphan_proofs": unmatched,
        "theorem_targets_still_missing": len(missing_targets),
        "duplicate_labels": duplicate_labels,
        "changed_files": changed_files,
        "errors": errors,
        "warnings": [],
        "actions": [asdict(action) for action in actions],
    }


def print_text(report: dict) -> None:
    print("Leaf proof invariant migration")
    for key in [
        "root",
        "mode",
        "theorem_count",
        "expected_proof_count",
        "proof_file_count",
        "already_linked_proofs",
        "newly_linked_proofs",
        "generated_stub_count",
        "existing_proofs_wrapped_or_normalized",
        "ambiguous_proofs",
        "unmatched_orphan_proofs",
        "theorem_targets_still_missing",
        "changed_files",
    ]:
        print(f"{key}: {report[key]}")
    print(f"duplicate_labels: {len(report['duplicate_labels'])}")
    print(f"errors: {len(report['errors'])}")
    for action in report["actions"][:80]:
        print(f"{action['action']} {action['path']} {action.get('theorem_id') or ''} {action.get('reason') or ''}".rstrip())
    if len(report["actions"]) > 80:
        print(f"... {len(report['actions']) - 80} more actions")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Migrate existing proof files to the Phase 1 proof-stub invariant.")
    parser.add_argument("--root", type=Path, default=Path("."))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview changes. This is the default.")
    mode.add_argument("--apply", action="store_true", help="Apply conservative migration changes.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--interactive", action="store_true", help="Reserved for future manual ambiguity resolution.")
    parser.add_argument("--strict", action="store_true", help="Return nonzero if duplicate-label or ambiguity errors are reported.")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args(argv)

    report = migrate(args.root.resolve(), apply=args.apply, limit=args.limit)
    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print_text(report)

    if args.strict and (report["errors"] or report["ambiguous_proofs"] or report["unmatched_orphan_proofs"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
