from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "tex" / "figures"

DOCUMENT_TAGS = (
    r"\documentclass",
    r"\begin{document}",
    r"\end{document}",
    r"\usepackage",
)


def validate_fragment(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for tag in DOCUMENT_TAGS:
        if tag in text:
            errors.append(f"{path}: contains forbidden document tag {tag}")

    if r"\caption{" not in text:
        errors.append(f"{path}: missing \\caption{{...}}")
    if r"\label{" not in text:
        errors.append(f"{path}: missing \\label{{...}}")

    figure_starts = list(re.finditer(r"\\begin\{figure\}(?:\[([^\]]*)\])?", text))
    if not figure_starts:
        errors.append(f"{path}: missing figure environment")

    for match in figure_starts:
        placement = match.group(1)
        if placement != "H":
            found = f"[{placement}]" if placement is not None else "no placement"
            errors.append(f"{path}: figure must use [H], found {found}")

    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate TeX figure fragments for required structure and forbidden document tags."
    )
    parser.add_argument(
        "--figure-dir",
        type=Path,
        default=FIGURE_DIR,
        help="Directory containing figure fragment .tex files. Defaults to tex/figures under the repo root.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    figure_dir = args.figure_dir.resolve()

    if not figure_dir.exists():
        print(f"figure directory not found: {figure_dir}", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in sorted(figure_dir.glob("*.tex")):
        errors.extend(validate_fragment(path))

    if errors:
        print("Figure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Figure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
