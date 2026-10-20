# CHANGELOG

## [0.3.0] — 2026-10-20

### Changed
- First-run config via `.willgt/skills.yaml` (`skills/spec-package/SETUP.md`).
- Impact records under `.willgt/impact/`; work items use `work_item_ref` when set.
- RDF/JSON-LD export = the link-name mapping table (no separate binary).

## [0.2.0] — 2026-10-16

### Changed
- Format status: `touches` and `protected_ac` are optional spec-package 2.1.0 fields (decision owner approved); `depends_on` stays in the impact record.

## [0.1.0] — 2026-10-16

### Added
- `SKILL.md`: intake run (Product) and technical-design run (implementer). Candidates proposed as questions; only Product-confirmed links recorded. `protected_ac` on work items; verifier reruns them. Link names affects / related_test / derived_from mapped to OSLC CM 3.0 and PROV-O.
- `templates/impact-record.yaml`.
- `evals/evals.json`: 6 evals.
