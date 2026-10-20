# screens/<screen_id>/ac.feature — TEMPLATE
#
# Signed by: Design / Product.  Executed by: the bound AC runner (see RUNNERS.md).
# Required for: every type except `agentic` — see TYPES.md §3, where the acceptance
# model is an open problem because output is non-deterministic.
#
# "Signed" means a named person accepted it. Unsigned AC gates nothing.
#
# ACCEPTABLE
#   - Observable behavior: what a user or caller can see or do.
#   - Deny paths. An AC with only happy paths is half an AC — most real defects
#     live in the refusal.
#   - Referencing region and action ids from screen.yaml by name.
#
# NOT ACCEPTABLE
#   - Implementation detail: internal function names, table columns, framework calls.
#     Those change without the behavior changing, and the test breaks for no reason.
#   - "The page looks correct" — not observable, not checkable.
#   - Asserting only that an element is visible. Visibility is not behavior: a debug
#     stub can pass that and ship a screen that does nothing.
#   - Loosening a Then-clause so an implementation passes. If the AC is wrong, change
#     it deliberately and re-sign it — never quietly to make red go away.

Feature: <screen or capability name>
  # Signed-off-by: <name>  <date>

  Scenario: <the main path, named for the outcome not the click>
    Given <the starting state, including entitlement or auth where it matters>
    When <the user or caller does one thing>
    Then <what is observably true afterwards>

  Scenario: <a deny path — required>
    Given <the state that should block it>
    When <the same attempt>
    Then <what the user sees instead>
    And <confirmation that nothing was written or changed>

  Scenario: <empty or boundary case>
    Given <no data, or the edge of a range>
    When <the surface is opened>
    Then <the empty state named in screen.yaml is shown>
