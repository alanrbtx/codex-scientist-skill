# Evidence records

Use a record when several claims, sources, or versions must remain traceable. For a small answer,
an exact inline citation is enough. Reuse an existing project table instead of creating duplicates.

## Minimal record

| Claim ID and exact claim | Source identity | Exact locator | Evidence tier | Finding / derivation | Verification status | Scope |
| --- | --- | --- | --- | --- | --- | --- |
| C1: method A lowers error on the registered cohort | `results.json`, protocol P1, run R1 | `paired.mean_difference`, `paired.ci95` | Frozen prospective | A minus B; negative is better | Verified against named aggregate | Specified cohort and endpoint only |

Use stable identities: a paper DOI or versioned URL, repository revision and file, dataset version,
run ID, or content hash when available. A filename alone is insufficient when copies can diverge.
Locators can be page/section/table, JSON key, CSV row and column, or source line and revision.
Do not invent locators or hashes; say which identity could actually be checked.

Distinguish these statuses:

- **Verified:** the named source and supporting content were inspected.
- **Reported only:** another document states the result; its underlying evidence was not checked.
- **Missing:** the required source or location is unavailable.
- **Conflicting:** inspected sources disagree; retain both identities and resolve the discrepancy.

These are verification states, not statistical evidence tiers. Reading an exploratory result does
not turn it into confirmation. A stored summary does not count as newly verified evidence.

## Literature and citations

Read the passage that supports the attributed claim. Check title, authors, year/version, and DOI or
URL against the primary source. Preserve whether a result is experimental, theoretical, simulated,
or measured on hardware. Record a theorem's assumptions when they determine applicability.

A search snippet, abstract, or review can identify a candidate source. If only that material was
available, state that boundary; do not imply that the full method or result was inspected. Never
supply a plausible-looking citation to fill a gap. In novelty searches, state the search scope and
compare the closest counterexample rather than claiming exhaustive absence.

## Numeric lineage

For a derived number, retain the input locations, formula, units, direction, cohort, and rounding.
For example, distinguish relative reduction `(baseline - method) / baseline` from an absolute
percentage-point difference. Record denominators and missing units where they affect the result.
Preserve the source's interval level and method. If it says only "CI", do not silently add "95%",
bootstrap, or another convention. Keep those details unspecified until verified.

When raw units and an aggregate disagree, preserve both and check code/config/cohort identity.
Correct a reporting or calculation error transparently; do not silently choose the favorable
version. A post-outcome change to the scientific analysis must be labeled as such.

## Lightweight handoff

An existing project note can hold the current objective, canonical source/protocol/run identities,
completed checks, unresolved decisions, active job handles, remaining budget, and next action.
For interrupted work, reconcile the note with current artifacts before retrying. Do not create
these records for ordinary grammar edits or require unavailable retrospective registrations.
