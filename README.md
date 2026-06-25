# lra-volume-iii

**Volume III: Classical Analysis** — Overleaf-ready standalone repository.

## Structure

```text
volume-iii.tex          — full-volume root (Overleaf main document)
volume-iii-<book>.tex   — individual book roots
common/               — shared LaTeX infrastructure supplied by lra-common; ignored here
bibliography/         — per-book bibliography shards
volume-iii/             — all LaTeX content for this volume
```

## Overleaf

Upload or checkout `common/` beside this repository's TeX roots, then set the main document to `volume-iii.tex` for the full volume or to one of the book roots:

```text
volume-iii-bounds-sequences-and-series.tex, volume-iii-continuity.tex, volume-iii-differentiation.tex, volume-iii-integration.tex
```

`common/` is ignored by git in this volume repo; edit shared infrastructure in `lra-common`.

## Building locally

```powershell
python F:\repos\lra-governance\tools\governance\build_volume_docker.py --root F:\repos\lra-volume-iii --common-root F:\repos\lra-common
```
