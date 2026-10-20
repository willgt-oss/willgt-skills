# CHANGELOG

## [2.1.0] — 2026-10-16

decision owner-approved edits to the locked format. All backwards compatible: no existing file or template changes meaning; the new fields are optional and nothing is backfilled.

### Added
- `IMPLEMENTATION.md` step 9: mutation gate for backend and capability packages (remove the guard in a scratch copy, show the AC fails; source-text probes labelled `static`, never the only AC for a runtime rule).
- `FORMAT.md` shared registry files: timestamp-based Flyway numbering (`V<YYYYMMDDHHMM>__name.sql`). Existing `V<n>` files keep their names.
- `FORMAT.md` optional impact fields `touches` and `protected_ac`; `templates/PRD.md` (`## Touches`, `## Protected AC`) and `templates/flow.yaml` (`touches`), all optional.
- `evals/check-templates.py`: checks the optional fields are present and marked optional.

### Unchanged
- `depends_on` is not added. The epic/sprint registry is not part of this format.
