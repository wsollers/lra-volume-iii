# Theorem Route Update Workflow

Use this workflow when theorem/proof source changes in the leaf repo and route
artifacts need to be refreshed.

1. Validate the Phase 1 proof-stub invariant:

   ```bash
   python scripts/validate_leaf_proofs.py --root . --strict
   ```

2. Generate theorem routes:

   ```bash
   python scripts/generate_theorem_routes.py --root .
   ```

3. Review generated artifacts:

   ```text
   build/knowledge/theorem-routes.json
   build/knowledge/theorem-routes.yaml
   ```

4. If a previous route snapshot existed, review:

   ```text
   build/knowledge/route-diff.json
   build/knowledge/route-diff.md
   ```

The update is valid only when route generation reports `status: PASS`.

Route records are generated from leaf source. Do not edit route artifacts as the
canonical source of theorem identity.
