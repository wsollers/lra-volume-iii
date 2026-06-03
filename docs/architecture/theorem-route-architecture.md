# Theorem Route Architecture

The theorem route layer connects leaf-authored theorem/proof source to later
proof-vault consumers. It is generated data, not canonical mathematical source.

## Stable Identity

The stable object is the proof-bearing theorem-like label:

- `thm:*`
- `prop:*`
- `lem:*`
- `cor:*`

These labels are `theorem_id` values in route artifacts. They must remain
stable when notes or proof files move during folder refactors.

Definitions and axioms may be extracted as knowledge nodes by broader explorer
tooling, but they are not Phase 2 proof-route obligations unless explicitly
marked.

## Movable Source Paths

Route records distinguish identity from file location:

- `theorem_id` is stable.
- `theorem_tex` is the current theorem statement source path.
- `proof_tex` is the current proof stub/source path.
- `proof_label` is the `prf:*` proof location label.

The `theorem_tex` and `proof_tex` paths may change during source refactors. A
path move should produce a route diff without changing `theorem_id`.

## Proof Association

The canonical proof-to-theorem association is:

```tex
\LRAProofFor{<theorem_id>}
```

Route generation may inspect return links and label-root conventions as legacy
fallbacks, but `\LRAProofFor` wins whenever it is present.

## Vault Path

`vault_path` is durable proof-vault routing data. It derives from stable volume
and chapter classification plus the theorem id slug:

```text
<volume>/<chapter>/<slug-from-theorem-id>
```

The proof vault will consume these paths in a later phase. The leaf repo does
not perform proof-vault sync in Phase 2.

Route artifacts use the explicit schema documented in
`theorem-route-schema.md`:

```text
schema: lra.theorem_routes
schema_version: 1
```

## Ownership

Leaf volume repos own theorem/proof source files. `Learning-Real-Analysis` is an
assembled integration repo and must not be used as the canonical authoring
source for theorem/proof files. `lra-proof-vault` consumes generated route
artifacts later; it does not own theorem identity.
