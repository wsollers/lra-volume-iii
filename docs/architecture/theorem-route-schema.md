# Theorem Route Schema

The Volume III Phase 2.5 route artifact schema is:

```text
schema: lra.theorem_routes
schema_version: 1
```

The JSON and YAML artifacts are generated at:

```text
build/knowledge/theorem-routes.json
build/knowledge/theorem-routes.yaml
```

## Top-Level Fields

Required top-level fields:

- `schema`
- `schema_version`
- `generated_at`
- `source_repo`
- `source_commit`
- `route_version`
- `route_count`
- `routes`

`route_count` must equal the number of records in `routes`.

## Stable Identity

`theorem_id` is the stable identity field. It must be a proof-bearing theorem
label:

- `thm:*`
- `prop:*`
- `lem:*`
- `cor:*`

This value must not change when a theorem statement file or proof file moves.

## Movable Path Fields

`theorem_tex` and `proof_tex` are current source paths. They are validated for
existence, but they are not stable identities. During proof-folder refactors,
these paths may change while `theorem_id` and usually `vault_path` stay fixed.

No active route may point into archived legacy folders such as:

```text
archive/**
legacy-orphan-proofs/**
```

## Route Fields

Essential route fields:

- `theorem_id`
- `title`
- `type`
- `theorem_tex`
- `proof_tex`
- `proof_label`
- `vault_path`

If an essential field is missing, route validation fails.

Optional route fields:

- `volume`
- `chapter`
- `section`
- `subsection`
- `tags`
- `dependencies`
- `source_commit`
- `route_version`

If an optional field is missing, route validation warns but does not fail.

Each route also carries `source_repo` so future importers can trace the owning
leaf repo.

## Vault Path

`vault_path` is derived from stable volume and chapter classification plus the
theorem id slug:

```text
<volume>/<chapter>/<slug-from-theorem-id>
```

The proof vault will later use `vault_path` as the durable target for proof
attempts. That importer should treat `theorem_id` as the identity key and
`proof_tex` as the current source location, not as a durable key.

## Validation

Run schema and route validation with:

```bash
python scripts/generate_theorem_routes.py --root . --validate-only
```

The command checks required fields, malformed theorem/proof labels, duplicate
theorem ids, route collisions, vault path collisions, source path existence,
and accidental references to archived legacy proof material.
