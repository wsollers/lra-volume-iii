from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE_ROOT = REPO_ROOT.parent / "lra-governance"


@dataclass(frozen=True)
class Predicate:
    name: str
    args: tuple[str, ...]


@dataclass(frozen=True)
class Quantifier:
    kind: str
    var: str
    domain: str
    body: object


@dataclass(frozen=True)
class Relation:
    left: str
    op: str
    right: str


@dataclass(frozen=True)
class Iff:
    left: object
    right: object


@dataclass(frozen=True)
class Not:
    body: object


@dataclass(frozen=True)
class And:
    parts: tuple[object, ...]


@dataclass(frozen=True)
class FormalReadingSpec:
    label: str
    ambient: tuple[object, ...]
    quantified_statement: object
    predicate_reading: object
    negated_quantified_statement: object
    negation_predicate_reading: object


def tex_atom(node: object) -> str:
    if isinstance(node, Predicate):
        if node.name == "OrderedSet":
            return rf"P=\mathsf{{OrderedSet}}({node.args[0]},{node.args[1]})"
        if node.name == "Subset":
            return rf"{node.args[0]}\subseteq {node.args[1]}"
        return rf"\operatorname{{{node.name}}}({','.join(node.args)})"
    if isinstance(node, Relation):
        return f"({node.left}{node.op} {node.right})"
    if isinstance(node, Quantifier):
        q = r"\exists" if node.kind == "exists" else r"\forall"
        return rf"({q} {node.var}\in {node.domain}){tex_atom(node.body)}"
    if isinstance(node, Iff):
        return rf"{tex_atom(node.left)}\Longleftrightarrow {tex_atom(node.right)}"
    if isinstance(node, Not):
        return rf"\neg{tex_atom(node.body)}"
    if isinstance(node, And):
        return r"\land ".join(tex_atom(part) for part in node.parts)
    raise TypeError(f"unsupported AST node: {node!r}")


def tex_display_with_ambient(ambient: tuple[object, ...], body: object) -> str:
    return r",\qquad ".join([*(tex_atom(part) for part in ambient), tex_atom(body)])


def normalize_tex(tex: str) -> str:
    tex = re.sub(r"%.*", "", tex)
    tex = tex.strip()
    tex = re.sub(r"\.\s*$", "", tex)
    tex = re.sub(r"\s+", "", tex)
    tex = tex.replace(r"\left", "").replace(r"\right", "")
    tex = tex.replace(r"\,", "")
    return tex


def extract_label_tail(source: str, label: str) -> str:
    marker = rf"\label{{{label}}}"
    index = source.find(marker)
    if index < 0:
        raise ValueError(f"label not found: {label}")
    return source[index:]


def extract_remark_display(label_tail: str, remark_title: str) -> str:
    pattern = re.compile(
        re.escape(rf"\begin{{remark*}}[{remark_title}]")
        + r"\s*\\\[(.*?)\\\]\s*"
        + re.escape(r"\end{remark*}"),
        re.DOTALL,
    )
    match = pattern.search(label_tail)
    if not match:
        raise ValueError(f"remark block not found: {remark_title}")
    return match.group(1).strip()


def registered_names() -> set[str]:
    names: set[str] = set()
    for filename in ("predicates.yaml", "structures.yaml", "relations.yaml", "notation.yaml"):
        path = GOVERNANCE_ROOT / filename
        if not path.exists():
            continue
        for match in re.finditer(r"^\s+name:\s+([A-Za-z][A-Za-z0-9]*)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE):
            names.add(match.group(1))
    names.add("Subset")
    return names


def ast_predicate_names(node: object) -> set[str]:
    if isinstance(node, Predicate):
        return {node.name}
    if isinstance(node, Quantifier):
        return ast_predicate_names(node.body)
    if isinstance(node, Iff):
        return ast_predicate_names(node.left) | ast_predicate_names(node.right)
    if isinstance(node, Not):
        return ast_predicate_names(node.body)
    if isinstance(node, And):
        names: set[str] = set()
        for part in node.parts:
            names |= ast_predicate_names(part)
        return names
    return set()


def bounded_above_spec() -> FormalReadingSpec:
    p = Predicate("OrderedSet", ("S", r"\leq"))
    ambient = (
        p,
        Predicate("Subset", ("A", "S")),
        Predicate("IsNonempty", ("A",)),
    )
    upper_bound = Predicate("UpperBound", ("u", "A", "P"))
    bounded_above = Predicate("BoundedAbove", ("A", "P"))
    quantified = Quantifier(
        "exists",
        "u",
        "S",
        Quantifier("forall", "x", "A", Relation("x", r"\leq", "u")),
    )
    negated_quantified = Quantifier(
        "forall",
        "u",
        "S",
        Quantifier("exists", "x", "A", Relation("u", "<", "x")),
    )
    predicate_reading = Iff(
        bounded_above,
        Quantifier("exists", "u", "S", upper_bound),
    )
    negation_predicate_reading = Iff(
        Not(bounded_above),
        Quantifier("forall", "u", "S", Not(upper_bound)),
    )
    return FormalReadingSpec(
        label="def:bounded-above",
        ambient=ambient,
        quantified_statement=quantified,
        predicate_reading=predicate_reading,
        negated_quantified_statement=negated_quantified,
        negation_predicate_reading=negation_predicate_reading,
    )


def expected_blocks(spec: FormalReadingSpec) -> dict[str, str]:
    return {
        "Standard quantified statement": tex_atom(spec.quantified_statement),
        "Predicate reading": tex_display_with_ambient(spec.ambient, spec.predicate_reading),
        "Negated quantified statement": tex_atom(spec.negated_quantified_statement),
        "Negation predicate reading": tex_display_with_ambient(spec.ambient, spec.negation_predicate_reading),
    }


def validate_spec_registry(spec: FormalReadingSpec) -> list[str]:
    available = registered_names()
    nodes = (
        *spec.ambient,
        spec.quantified_statement,
        spec.predicate_reading,
        spec.negated_quantified_statement,
        spec.negation_predicate_reading,
    )
    used: set[str] = set()
    for node in nodes:
        used |= ast_predicate_names(node)
    return sorted(name for name in used if name not in available)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        default="volume-iii/book-analysis-i/bounding/notes/bounds-extremals/notes-upper-lower-bounds.tex",
    )
    parser.add_argument(
        "--self-test-bad-bounded-above",
        action="store_true",
        help="Run against an embedded copy of the original circular bounded-above reading.",
    )
    args = parser.parse_args()

    spec = bounded_above_spec()
    missing = validate_spec_registry(spec)
    if missing:
        print("missing registered names:")
        for name in missing:
            print(f"  {name}")
        return 1

    if args.self_test_bad_bounded_above:
        source = r"""
\begin{definition}[Bounded Above]
\label{def:bounded-above}
\end{definition}
\begin{remark*}[Standard quantified statement]
\[
  A\neq\varnothing
  \quad\text{and}\quad
  (\exists u\in S)(\forall x\in A)(x\leq u).
\]
\end{remark*}
\begin{remark*}[Predicate reading]
\[
  S\in\mathbf{Set},\qquad A\subseteq S,\qquad P=\mathsf{OrderedSet}(S,\leq),\qquad
  \operatorname{BoundedAbove}(A,P).
\]
\end{remark*}
\begin{remark*}[Negated quantified statement]
\[
  A=\varnothing
  \quad\text{or}\quad
  (\forall u\in S)(\exists x\in A)(u<x).
\]
\end{remark*}
\begin{remark*}[Negation predicate reading]
\[
  S\in\mathbf{Set},\qquad A\subseteq S,\qquad P=\mathsf{OrderedSet}(S,\leq),\qquad
  \neg\operatorname{BoundedAbove}(A,P).
\]
\end{remark*}
"""
    else:
        source = (REPO_ROOT / args.file).read_text(encoding="utf-8")
    label_tail = extract_label_tail(source, spec.label)
    failures: list[str] = []
    for title, expected in expected_blocks(spec).items():
        actual = extract_remark_display(label_tail, title)
        if normalize_tex(actual) != normalize_tex(expected):
            failures.append(title)
            print(f"{title}: mismatch")
            print(f"  expected: {expected}")
            print(f"  actual:   {actual}")
        else:
            print(f"{title}: ok")

    if failures:
        print(f"formal reading validation failed for {spec.label}: {', '.join(failures)}")
        return 1
    print(f"formal reading validation passed for {spec.label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
