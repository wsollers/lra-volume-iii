# Proof Folder Refactor Workflow

Proof folder refactors may move `proof_tex` paths, but they must not change
stable theorem ids.

Before moving proof files:

1. Run strict proof validation.
2. Generate a route snapshot.
3. Confirm every route has `theorem_id`, `theorem_tex`, `proof_tex`,
   `proof_label`, and `vault_path`.

After moving proof files:

1. Preserve each proof label.
2. Preserve each `\LRAProofFor{...}` association.
3. Update local proof routers such as `proofs/**/index.tex`.
4. Rerun:

   ```bash
   python scripts/validate_leaf_proofs.py --root . --strict --refactor-mode
   python scripts/generate_theorem_routes.py --root .
   ```

Review the route diff. Expected changes are usually `moved_proof_tex` entries.
Unexpected changes to `theorem_id` or `vault_path` indicate a route stability
problem that should be fixed before syncing.
