# Volume III Pointwise Function Algebra Enhancement Process

## Purpose

This process file coordinates the enhancement of Volume III Analysis function
material with a complete pointwise real-valued function
algebra/order/boundedness/sup-inf package.

Target repository:

`F:\repos\lra-volume-iii`

Primary target section:

`volume-iii/book-analysis-i/functions/notes/real-valued-functions/notes-real-valued-functions.tex`

This is an enhancement to Volume III function material. Do not duplicate Volume
I composition or inverse theory. Cross-reference Volume I material in prose
where useful.

## Required Repo Grounding

Before editing, read:

1. `F:\repos\AGENTS.md`
2. `F:\repos\lra-volume-iii\AGENTS.md`
3. `F:\repos\lra-volume-iii\README.md`

Then read targeted governance docs from `lra-governance`:

- `docs/workflows/add-theorem-with-proof-stub.md`
- `docs/governance/proof-standards.md`
- `docs/governance/dependency-standards.md`
- `docs/governance/atomic-artifact-standards.md`
- `docs/governance/notation-standards.md`
- `docs/governance/tikz-style-guide.md`

## Non-Negotiable Rules

- Proofs must be stubs only.
- Every theorem/proposition/corollary added must have a proof stub.
- Proof stubs must use the exact proof-stub structure required by governance.
- TikZ figures must be standalone `figure-*.tex` files containing only
  `tikzpicture`.
- Do not duplicate Volume I composition/inverse definitions or theorems.
- Cross-volume references to Volume I should be prose references unless Volume
  III root supports hard labels.
- Use `\lambda` for scalar multiplication, not `c`, because `c` is used for
  near-point/limit base points.
- Generic predicates must stay generic:
  - `AtPointOperation(Op, f_tuple, x)`
  - `PointwiseOperation(Op, f_tuple, A)`
  - `AtPointRelation(Rel, f_tuple, x)`
  - `PointwiseRelation(Rel, f_tuple, A)`
  - `PointwiseRelationNear(Rel, f_tuple, c, A)`
  - `BoundedAwayFromZero(f, A)`
  - `BoundedAwayFromZeroNear(f, c, A)`
  - `UniformlyBoundedFamily(F, I, A)`
- Do not add separate canonical predicates such as `PointwiseLessThan` or
  `PointwiseLessEqual`.

## Startup Prompt For A New Context

Use this prompt in the next Codex context:

> You are working in `F:\repos\lra-volume-iii`. Read `F:\repos\AGENTS.md`,
> then the repo-local `AGENTS.md` and `README.md`. Read
> `docs/process/volume-iii-pointwise-function-algebra-process.md` completely.
> Work through the chunk list in order. Before editing a chunk, inspect
> existing Volume III function material and avoid duplicates. Add proofs only
> as stubs. Add standalone TikZ files only where listed. After each chunk, run
> governance validation. Build affected roots only at the specified build
> gates. Do not duplicate Volume I composition/inverse material; add prose
> cross-references only.

## Existing Volume I Cross-Reference Targets

Composition and inverse material already exists in Volume I:

- Volume I Functions: Function Equality
- Volume I Functions: Composition
- Volume I Functions: Associativity of Composition
- Volume I Functions: Identity and Composition
- Volume I Functions: Injectivity and Surjectivity Under Composition
- Volume I Functions: Inverse Function
- Volume I Functions: Characterization of Inverse Functions
- Volume I Functions: Inverse of a Composition
- Volume I Functions: One-Sided Inverses and Function Properties
- Volume I Functions and Order: Injective Maps Are Bijections Onto Their Images

In Volume III, add only prose background/cross-reference remarks to this
material.

## Files To Modify

Primary function files:

- `volume-iii/book-analysis-i/functions/notes/real-valued-functions/notes-real-valued-functions.tex`
- `volume-iii/book-analysis-i/functions/notes/real-valued-functions/index.tex`
- `volume-iii/book-analysis-i/functions/proofs/real-valued-functions/index.tex`
- `volume-iii/book-analysis-i/functions/chapter.yaml`

Limits files, only if adding near-point limit theorem refinements:

- `volume-iii/book-analysis-ii/continuity/notes/limits/notes-limits.tex`
- `volume-iii/book-analysis-ii/continuity/notes/limits/index.tex`
- `volume-iii/book-analysis-ii/continuity/proofs/limits/index.tex`
- `volume-iii/book-analysis-ii/continuity/chapter.yaml`

Governance canonical files, only if missing generic predicates/structures:

- `lra-governance/predicates.yaml`
- `lra-governance/structures.yaml`
- `lra-governance/notation.yaml`
- relevant governance docs/index notes if local pattern requires them

## Files To Add

Function proof stubs:

`volume-iii/book-analysis-i/functions/proofs/real-valued-functions/prf-*.tex`

Limits proof stubs, only if limits chunk is implemented:

`volume-iii/book-analysis-ii/continuity/proofs/limits/prf-*.tex`

TikZ source files:

- `figure-pointwise-operation-lift.tex`
- `figure-at-point-on-set-near-point.tex`
- `figure-pointwise-order-envelope.tex`
- `figure-bounded-away-zero.tex`
- `figure-sup-subadditivity-strict.tex`
- `figure-common-maximum-sum.tex`

Place TikZ files beside `notes-real-valued-functions.tex`.

## Chunk Protocol

Process one chunk at a time.

For each chunk:

1. Inspect existing labels and content first.
2. Add only missing definitions/environments.
3. If an item exists, revise minimally instead of duplicating.
4. Add quick-reference rows to the local `index.tex`.
5. Add proof stubs for theorem-like environments.
6. Register theorem-like environments in `chapter.yaml`.
7. Run the validation gate.
8. Stop and summarize before moving to the next chunk if validation fails.

## Chunk 1: Generic Lift Layer

Add or revise definitions:

- `def:at-point-operation`
- `def:pointwise-operation-on-set`
- `def:at-point-relation`
- `def:pointwise-relation-on-set`
- `def:pointwise-relation-near-point`

Add theorem-like environments:

- `prop:pointwise-operation-evaluation`
- `prop:pointwise-relation-evaluation`
- `prop:pointwise-relation-near-unpacking`

Required blocks:

- definition/proposition boxes
- standard quantified statement
- predicate reading
- interpretation
- dependencies
- proof stubs for propositions

Add toolkit remark:

- fix an input
- reduce to real algebra/order
- requantify over the set
- near point: shrink deleted neighborhoods

Add TikZ:

- `figure-pointwise-operation-lift.tex`
- `figure-at-point-on-set-near-point.tex`

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

## Chunk 2: Named Pointwise Algebra

Add or revise definitions:

- `def:pointwise-sum-of-functions`
- `def:pointwise-difference-of-functions`
- `def:pointwise-product-of-functions`
- `def:pointwise-scalar-multiple-of-a-function`
- `def:pointwise-absolute-value-of-a-function`
- `def:pointwise-maximum-of-two-functions`
- `def:pointwise-minimum-of-two-functions`
- `def:pointwise-quotient-of-functions`
- `def:pointwise-reciprocal-of-a-function`

Add theorem-like environments:

- `thm:function-algebra-closure`
- `thm:function-quotient-closure`
- `prop:pointwise-max-min-absolute-value-formulas`
- `prop:pointwise-max-min-bounds`
- `prop:quotient-undefined-when-denominator-vanishes`

Required blocks:

- theorem/proposition boxes
- standard quantified statement
- interpretation
- quotient failure mode
- dependencies
- proof stubs

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

## Chunk 3: Pointwise Order

Add or revise definitions/remarks:

- `def:pointwise-equality-on-set`
- examples of `PointwiseRelation(<=,(f,g),A)`, `<`, `=`, `>=`, `>`

Add theorem-like environments:

- `thm:pointwise-order-laws`
- `prop:strict-pointwise-order-implies-weak`
- `thm:pointwise-order-arithmetic`
- `prop:pointwise-product-order-nonnegative`
- `prop:reciprocal-order-reversal`
- `prop:quotient-order-sign-controlled`
- `prop:no-unconditional-quotient-order-law`

Required negation block:

\[
\neg(f\le g\text{ on }A)\iff \exists x\in A,\ f(x)>g(x).
\]

Required contrapositive/failure-mode blocks:

- if functions are not equal on the same domain, some input separates them
- no unconditional quotient order law

Add TikZ:

- `figure-pointwise-order-envelope.tex`

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

## Chunk 4: Boundedness And Bounded Away

Add or revise definitions:

- `def:function-bounded-near-point`
- `def:function-bounded-away-from-zero`
- `def:function-bounded-away-from-zero-near`
- `def:uniformly-bounded-family`

Do not duplicate existing bounded above/below/bounded definitions. Revise only
if needed.

Add theorem-like environments:

- `thm:bounded-iff-absolute-value-bounded-above`
- `prop:boundedness-restriction`
- `prop:boundedness-not-preserved-under-extension`
- `prop:bounded-away-from-zero-implies-nonzero`
- `prop:bounded-away-from-zero-near-implies-nonzero-near`
- `thm:bounded-away-from-zero-gives-bounded-reciprocal`
- `thm:local-bounded-away-from-zero-gives-local-bounded-reciprocal`
- `thm:uniform-boundedness-transfer-under-pointwise-limit`

Required negation blocks:

\[
\neg\operatorname{Bounded}(f,A)\iff
\forall K\ge0,\exists x\in A,\ |f(x)|>K.
\]

\[
\neg\operatorname{BoundedAwayFromZero}(f,A)\iff
\forall\epsilon>0,\exists x\in A,\ |f(x)|<\epsilon.
\]

Required failure modes:

- nowhere zero does not imply bounded away from zero
- bounded on a subset does not imply bounded on an extension

Add TikZ:

- `figure-bounded-away-zero.tex`

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

## Chunk 5: Bounded Function Algebra

Add theorem-like environments:

- `thm:bounded-function-algebra-closure`
- `thm:bounded-functions-form-commutative-ring`
- `thm:bounded-functions-form-real-vector-space`
- `thm:bounded-away-quotient`

Add corollaries:

- `cor:bounded-sum`
- `cor:bounded-difference`
- `cor:bounded-product`
- `cor:bounded-scalar-multiple`
- `cor:bounded-absolute-value`
- `cor:bounded-max-min`
- `cor:bounded-quotient-by-bounded-away-denominator`

Add toolkit remark:

- build global constants
- use triangle inequality
- use product bound
- quotient bound equals numerator bound divided by denominator lower bound

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

## Chunk 6: Supremum / Infimum Of Functions

Add or revise definitions:

- `def:function-supremum-on-set`
- `def:function-infimum-on-set`
- `def:pointwise-supremum-family`
- `def:pointwise-infimum-family`

Add theorem-like environments:

- `thm:function-supremum-existence`
- `thm:function-infimum-existence`
- `thm:supremum-monotone-under-pointwise-order`
- `thm:infimum-monotone-under-pointwise-order`
- `prop:supremum-monotonicity-converse-fails`
- `thm:pointwise-supremum-evaluation`
- `thm:pointwise-infimum-evaluation`
- `thm:supremum-subadditivity`
- `thm:infimum-superadditivity`
- `thm:supremum-negation`
- `thm:infimum-negation`
- `thm:supremum-scalar-multiple`
- `thm:infimum-scalar-multiple`
- `cor:finite-family-pointwise-supremum-is-maximum`
- `cor:finite-family-pointwise-infimum-is-minimum`
- `thm:common-maximum-gives-sum-maximum`
- `thm:common-minimum-gives-sum-minimum`
- `prop:common-extremum-converse-fails`

Required failure modes:

- `sup f <= sup g` does not imply `f <= g`
- `sup(f+g) <= sup f + sup g` can be strict
- common maximum theorem converse fails
- scalar `sup_{x in A} f(x)` differs from pointwise family `sup_alpha f_alpha`

Add TikZ:

- `figure-sup-subadditivity-strict.tex`
- `figure-common-maximum-sum.tex`

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

## Chunk 7: Limits Cross-Link

Only implement if missing or insufficient:

- `thm:comparison-function-limits`
- `thm:squeeze-theorem-near-point-form`

Place in:

`volume-iii/book-analysis-ii/continuity/notes/limits/notes-limits.tex`

Use dependency text pointing to the new `def:pointwise-relation-near-point`.

Validation gate:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

Build gate for this chunk:

```powershell
python ..\lra-governance\tools\governance\build_volume_docker.py --root . --common-root ..\lra-common --tex-root volume-iii-functions-continuity-and-differentiation.tex --output-dir build\digital
```

If this root fails for unrelated pre-existing differentiation/Taylor errors,
record exact file/line errors and continue only if the new limits material is
not implicated.

## Proof Stub Template

Every proof stub must follow this shape:

```tex
\newpage
\phantomsection
\label{prf:<slug>}
\LRAProofFor{<env-label>}

\begin{remark*}[Return]
\hyperref[<env-label>]{Return to <Environment Type>}
\end{remark*}

\begin{<environment-type>*}[<Title>]
<Restate the theorem/proposition/corollary exactly enough for proof context.>
\end{<environment-type>*}

\begin{proof}[Professional Standard Proof]
\LRAProofBodyStart
TODO: professional standard proof for <slug>.
\end{proof}

\begin{proof}[Detailed Learning Proof]
\LRAProofBodyStart
TODO: detailed learning proof for <slug>.
\end{proof}

\begin{remark*}[Proof structure]
\end{remark*}

\begin{dependencies}
\begin{itemize}
  \item TODO: dependencies.
\end{itemize}
\end{dependencies}

\clearpage
```

Use `theorem*`, `proposition*`, or `corollary*` to match the source
environment.

## TikZ Requirements

Each TikZ file:

- must contain only `tikzpicture`
- must use shared LRA TikZ styles/macros where available
- must not define document preambles
- must not contain `figure` wrappers
- must be input from the notes file inside a normal figure environment
- must follow `lra-governance/docs/governance/tikz-style-guide.md`

## Final Build Gates

After all chunks that affect Analysis I functions:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

Then build:

```powershell
python ..\lra-governance\tools\governance\build_volume_docker.py --root . --common-root ..\lra-common --tex-root volume-iii-bounds-sequences-and-series.tex --output-dir build\digital
```

If limits chunk was added, also build:

```powershell
python ..\lra-governance\tools\governance\build_volume_docker.py --root . --common-root ..\lra-common --tex-root volume-iii-functions-continuity-and-differentiation.tex --output-dir build\digital
```

Record any pre-existing build failures separately from failures caused by the
new material.

## Completion Criteria

The work is complete only when:

- all chosen chunks are implemented
- all theorem-like environments have proof stubs
- notes index and proof index are updated
- chapter YAML is updated
- governance validation has zero errors
- affected root builds either pass or fail only for documented pre-existing
  unrelated issues
- new TikZ files compile without local errors
- final status lists every modified and added file
