# RUNNERS — the AC runner module

> **Reality check.** `playwright` is **verified** against product spec packages. `kotlin-test` is
> **verified** as a runner for Kotlin/JVM unit and presentation tests; it is **not yet verified**
> against a spec-package AC file. `maestro` is **verified** for mobile UI flows in general; it is
> **not yet verified** against a spec-package `ac.flow.yaml`. Do not bind a runner on the assumption
> that an unverified row is proven for this format.
> **Requires first:** `SKILL.md` (scope), `FORMAT.md` (where the AC file sits).

The format says "executable AC, colocated with the thing it proves." It does not say *how* it runs.
That is a per-project binding, selected from this registry via `.willgt/skills.yaml` `test_runner`.

The registry is **discovered, not designed**: a runner is added when a real project needs one and it
has been verified to work there. An entry describing a runner nobody has run is a guess.

---

## 1. Binding

In `.willgt/skills.yaml` (see `SETUP.md`):

```yaml
spec_root: spec/
test_runner: playwright        # registry id, below — or auto | jest | pytest | kotlin-test | maestro | other:<cmd>
```

Anything reading the package resolves the runner from that file. **Never assume Playwright** —
that assumption is what makes a format quietly web-only. `auto` means detect from the AC file
extension when possible.

---

## 2. Registry

| id | Runs | AC file in the screen folder | Command shape | Status |
|---|---|---|---|---|
| `playwright` | Web UI, end to end | `ac.spec.ts` | `npx playwright test <path>` | **Verified** against product spec packages |
| `kotlin-test` | KMP / JVM unit + presentation logic | `<Screen>Test.kt` | `./gradlew :shared:testDebugUnitTest --tests <class>` | **Verified** as a runner; **not yet verified** against a spec-package AC file |
| `maestro` | Android / iOS UI on a device or emulator | `ac.flow.yaml` | `maestro test <path>` | **Verified** for mobile UI flows; **not yet verified** against a spec-package `ac.flow.yaml` |

---

## 3. What a runner must provide

A candidate qualifies only if all four hold. If one fails, it is not a runner — it is a manual check
wearing a runner's name.

1. **Runs one feature's AC in isolation**, by path or id. A runner that only runs the whole suite
   cannot gate a single handoff.
2. **Exit code is the verdict.** Zero = green; non-zero = red. No parsing of prose logs to decide.
3. **Colocated AC.** The AC file lives next to the thing it proves (screen folder or package).
4. **RED is observable.** The same command can fail for a real assertion failure, or red means nothing.

Point 4 is not theoretical. A browser-closed error and a genuine assertion failure both exit
non-zero; a runner that cannot tell them apart cannot gate work.

HTTP 200 plus a failing assertion is not yet a product failure. That pair cannot tell a stale
environment from a product bug — say which layer the green (or red) run proved.

---

## 4. Adding a runner

1. Prove it meets §3 on a real package in a real project.
2. Add a registry row with an honest Status (`verified` / `not yet verified` for this format).
3. Document the AC filename and command shape.
4. At triage, add the row, set `test_runner` in `.willgt/skills.yaml`, and update the evals.
