# Structural Atlas — Figures & Exposition

A self-contained set of TikZ plates and LaTeX write-ups for an analysis / measure /
gauge-integration chapter, all sharing one house style. Everything here compiles with
`pdflatex` and depends only on **`structural-atlas.sty`** (kept in this folder).

For each deliverable: `*.tex` is the editable source, `*.pdf` is the rendered output,
`*-preview.png` is a quick raster for browsing. The canonical TikZ style guide lives in
`../../../../lra-governance/docs/governance/tikz-style-guide.md`; this folder is figure
source only, not a style-guide source of truth.

## The package
- **`structural-atlas.sty`** — colors, axis/probe/dropline/dot styles, `\glowcurve`
  (gradient fill + halo + stroke), `\glowstroke` (halo + stroke, no fill), `\atlascaption`.

## Differentiation
- **`atlas-demo`** — *Atlas I*: MVT, IVT, Rolle, concavity, 2nd-derivative tests, Lipschitz.
- **`fig-lipschitz-correct`** — the geometrically honest $C^{1,1}$ figure (descent-lemma
  parabola sandwich), correcting the source's $C^{0,1}$/$C^{1,1}$ conflation.

## Integration — construction
- **`integration-atlas`** — *Atlas II*: left/mid/right Riemann sums, lower/upper Darboux
  sums, the squeeze, refinement, tagged partition, and the gauge (δ-fine) panel.
- **`quadrature-atlas`** — *Atlas III*: trapezoid, Simpson, and oscillation
  ($U-L=\sum\omega_f\,\Delta x$).

## Integration — failures
- **`failures-atlas`** — *Atlas IV*: Dirichlet, Thomae, unbounded, pointwise-limit.
- **`integration-failures`** — prose: Lebesgue's criterion, oscillation, a proof that
  Thomae is integrable, each failure traced to the hypothesis it violates. Embeds Atlas IV.

## The gauge integrals (McShane / Henstock–Kurzweil)
- **`fig-mcshane`** — the McShane integral: the untethered tag, δ-fine containment, = Lebesgue.
- **`hk-vs-mcshane`** — *Atlas V*: tethered vs free tag, side by side.
- **`integration-lattice`** — *Atlas VI*: $\mathcal R\subsetneq\mathcal L=$McShane$\subsetneq\mathcal{HK}$,
  one witness per frontier.
- **`gauge-integrals`** — prose: gauge framework, both δ-finenesses, Cousin's lemma,
  McShane = Lebesgue, Henstock's unconditional FTC, the $\mathcal{HK}\setminus\mathcal L$
  witness. Embeds Atlas V and VI.

## Rebuilding
From this folder: `pdflatex <name>.tex`. The two prose docs (`integration-failures`,
`gauge-integrals`) embed plate PDFs, so build the plates first (or just keep the shipped
PDFs in place). Run prose docs twice if you add cross-references.

## Known simplifications (deliberate; see each chat note)
- Riemann/Darboux panels park the integrand's peak on a partition node, so per-cell
  sup/inf land at endpoints; the `\riemannbars` macro is a teaching prop, not a general
  sup/inf engine.
- Simpson's arcs nearly coincide with the curve (it's exact to degree 3) — not a bug.
- The gauge/McShane figures spotlight one cell's tag for legibility; in reality all tags
  are free.
