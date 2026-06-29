# Structural Atlas — TikZ Style Guide

A house style for figures in the analysis / differential-geometry notes. The goal
is a consistent visual language: **warm paper, muted jewel-tone curves, soft glow
fills, gray probe-lines, small-caps captions.** Every figure should read as a *probe*
of a structure, not decoration.

All of this lives in `structural-atlas.sty`. Drop that on your `TEXINPUTS` path (or
beside the document) and `\usepackage{structural-atlas}`.

---

## 1. Design philosophy

| Principle | What it means in practice |
|---|---|
| **The glow carries the curve** | One signature element — a vertical gradient fill under the curve plus a soft two-layer halo on the stroke. Everything else stays flat and quiet so the curve dominates. |
| **Gray is for scaffolding** | Axes and droplines are muted (`atlasink`, `atlasgray`), never competing with the colored curve. |
| **One hue per concept** | Each theorem owns a color (MVT/Lipschitz = blue, IVT = green, Rolle = red, …). Reuse the hue when the same idea recurs across chapters. |
| **Probes, not clutter** | Secants, tangents, level lines are thin "probes" (`atlas probe`). A figure should have at most a handful. |

---

## 2. Palette

Defined once in the package; change them there and every figure updates.

| Name | Hex | Role |
|---|---|---|
| `atlaspaper` | `#F4EFE4` | warm cream background |
| `atlasink` | `#33312E` | axes, text, feature dots |
| `atlasgray` | `#9A958C` | dashed droplines |
| `atlasblue` | `#2E6F9E` | primary curve / MVT / Lipschitz |
| `atlasgreen` | `#4C8C3F` | IVT path, secants |
| `atlasred` | `#C0473B` | Rolle, tangents |
| `atlasgold` | `#D69A2A` | convexity |
| `atlasmagenta` | `#B84A86` | inflection |
| `atlasteal` | `#2A9D9A` | local minimum |
| `atlasorange` | `#D17A2E` | local maximum |
| `atlasconegreen` | `#6BA84F` | Lipschitz cone / bounding parabolas |

---

## 3. Core styles

Apply as TikZ keys.

- `atlas` — put on the `tikzpicture` env; paints the cream background rectangle.
- `atlas axes` — muted, arrow-tipped (`Stealth`), `0.7pt`.
- `atlas curve` — the crisp curve stroke (`1.5pt`, round caps/joins). Pair with a color.
- `atlas probe` — thin straight auxiliary line (secant, tangent, level line).
- `dropline` — dashed gray guide from a feature down to an axis.
- `atlas dot` — solid feature dot with a thin paper-colored rim.
- `atlas label` — text/math node in `atlasink`.

```latex
\begin{tikzpicture}[atlas, scale=0.82]
  \draw[atlas axes] (0,0)--(5,0);
  \draw[atlas axes] (0,0)--(0,4);
  % ... curve + probes ...
\end{tikzpicture}
```

---

## 4. The `\glowcurve` macro (the signature look)

One call draws three layered things: (1) the gradient fill clipped under the curve,
(2) a soft two-layer halo, (3) the crisp stroke on top.

```latex
\glowcurve{ color=atlasblue, domain=0.5:4.5, axis=0, top=4.6, expr={0.16*\x*\x+0.2*\x+0.55} }
```

### Keys

| Key | Default | Meaning |
|---|---|---|
| `color` | `atlasblue` | curve + glow color |
| `domain` | `0:1` | `a:b`, the x-range of the plot |
| `axis` | `0` | y-value of the baseline the fill drops to |
| `top` | `6` | top of the fill rectangle — **set ≥ the curve's max** |
| `expr` | `{\x}` | function of `\x`, **always braced** |
| `samples` | `100` | plot samples (raise for sharp wiggles) |
| `stroke` | `1.5pt` | crisp stroke width |
| `fillmax` | `24` | glow opacity (%) near the curve |
| `fillmin` | `2` | glow opacity (%) near the axis |
| `halo` | `5pt` | width of the soft halo |

### Two worked calls

```latex
% a downward parabola (a local-max bump), teal
\glowcurve{ color=atlasteal, domain=0.1:2.1, axis=0, top=3, expr={2.6-0.7*(\x-1.1)*(\x-1.1)} }

% a wave with more samples
\glowcurve{ color=atlasgreen, domain=0.4:4.6, axis=0, top=4.6, samples=160,
            expr={1.1+0.52*\x+0.45*sin(132*\x)} }
```

---

## 5. Captions

Two-line, small-caps, tabular-cell safe (built on `\shortstack`):

```latex
\atlascaption{1}{Mean Value Theorem (MVT)}{The Tangent Guard}
```

→ *Figure 1.* **Mean Value Theorem (MVT):** / **The Tangent Guard**

---

## 6. Layout

**A single panel** is just a `standalone` document using the package — it compiles on
its own *and* can be `\input` into a larger file. Keep one panel per file
(`fig-mvt.tex`, `fig-ivt.tex`, …) for clean version control.

**A poster / plate** (like the atlas) is a `tabular` of panels with `\atlascaption`
rows between them, all wrapped in a single `[atlas]` `tikzpicture` node so the cream
background spans the whole plate. See `atlas-demo.tex` for the full template.

---

## 7. Typography upgrade (optional)

The atlas was rendered with Latin Modern. For a closer match to the printed look,
install and load a Palatino-class face **before** the package:

```latex
\usepackage{newpxtext}   % body + small caps
\usepackage{newpxmath}   % matching math
\usepackage{structural-atlas}
```

The small-caps title/captions sharpen noticeably.

---

## 8. Gotchas (hard-won)

- **`top` must exceed the curve's maximum**, or the fill clips flat across the peak and
  leaves a hard horizontal edge.
- **`pgfmath` trig is in degrees.** `sin(70*\x)` is degrees; for radians write
  `sin(70*\x r)`. Pick one convention and keep your `expr` and any hand-computed
  slopes consistent.
- **Brace every `expr`** — bare commas (e.g. inside `max(...)`) will break the key parser.
- **Raise `samples`** for high-frequency curves; the default `100` aliases sharp wiggles.
- For derivative slopes computed by hand (tangents), differentiate the *same* `expr`
  you plotted — mismatches here are the most common "why isn't my tangent tangent" bug.

---

## 9. Minimal panel template

```latex
\documentclass[border=8pt]{standalone}
\usepackage{structural-atlas}
\begin{document}
\begin{tikzpicture}[atlas, scale=0.9]
  \glowcurve{ color=atlasblue, domain=0:4, axis=0, top=4, expr={0.2*\x*\x} }
  \draw[atlas axes] (0,0)--(4.6,0);
  \draw[atlas axes] (0,0)--(0,4);
  \node[atlas dot] at (2,0.8){};
  \draw[dropline] (2,0.8)--(2,0);
  \node[atlas label,below] at (2,-0.05){$c$};
\end{tikzpicture}
\end{document}
```
