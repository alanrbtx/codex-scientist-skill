# GPT-6 research workflow

Checked against official OpenAI documentation on 2026-10-05. Research-specific routing below is a
starting policy to evaluate on the user's work. OpenAI's family prompting guidance describes
observations from Astra and recommends evaluating its transfer to other GPT-6 models.

## Model and effort selection

Preserve the user's model and effective reasoning effort. This skill is instruction-only: a model
name does not change the session or authorize API usage. When selection is requested:

| Research task | Candidate | Completion evidence |
| --- | --- | --- |
| Bounded code change, artifact extraction, localized prose revision | `gpt-6.1-sol` | Requested diff or artifact with targeted checks |
| Novelty synthesis, hard derivation, confounded experiment, contradictory results | `gpt-6-astra` | Source-grounded conclusion, alternatives, and a decisive contrast |
| Broad execution with one difficult decision | Keep the current model; isolate that decision | Reusable evidence and a resolved decision without restarting completed work |

For a new configuration, `medium` is a reasonable baseline; `low` can fit mechanical checks.
Consider `high` for difficult design or interpretation and `xhigh` or `max` when the decision
merits extra reasoning. More effort cannot supply missing data, fix leakage, or make exploratory
results confirmatory. Preserve an existing effective setting before comparing changes.

The documented API efforts for both models are `low`, `medium`, `high`, `xhigh`, and `max`.
Neither accepts `none` or `minimal`. Codex and other hosts can expose different settings:
use the live host's supported choices, and do not copy a host-only value into an API request.

When a model comparison is requested, hold the task, tools, inputs, and acceptance criteria fixed.
Use representative claim interpretation, a bounded patch, or a manuscript edit. Compare artifact
correctness, unsupported claims, completion, latency, and cost where measured. Do not benchmark
models or consume API budget just because this reference was loaded.

## Give the model a decision contract

Specify the requested outcome, canonical inputs, scope, execution environment, and observable
completion condition. Include budget and stop rules for experiments. Avoid a universal research
checklist for a single file edit or evidence lookup.

Example for an artifact-grounded analysis:

> Decide whether the existing paired evaluation supports the draft's central claim. Inspect the
> named protocol, raw-unit table, and aggregate. Preserve the registered endpoint and exclusions.
> Return the effect, uncertainty, evidence tier, and one supported claim sentence. Resolve routine
> choices from the files; ask only if a missing scientific decision prevents a valid conclusion.
> Do not start another run unless the user authorizes it.

For an execution request, replace that last constraint with the authorized compute budget and
expected artifact. The example does not prohibit execution already authorized by the user.

## Preserve long-task state

For multi-stage work, keep a compact checkpoint in the project's existing plan or run record:

- objective, user corrections, authorization, and remaining acceptance criteria;
- canonical source, protocol, cohort, run IDs, artifact paths, and verified hashes;
- completed checks, failed approaches, and unresolved scientific decisions;
- active tool or job handles, next safe action, and stop or resume rule.

After compaction, interruption, or a model change, read that record and recheck live state where
it can have drifted. Do not repeat completed runs or treat an old summary as new evidence. Retrieve
only the logs, passages, and artifacts needed for the next decision, even with a large context.

## Parallel work and independent review

Use subagents only when the user or applicable instructions authorize delegation and the host
provides it. Suitable tasks include independent literature branches, a statistics audit, or a
review of a finished manuscript. A localized edit usually needs no delegation.

Assign a bounded question, allowed inputs, write ownership, and output with source locations and
uncertainties. Avoid concurrent edits to the same file or run state. For a blind review, provide
raw artifacts and the question without the author's preferred verdict. The parent verifies
consequential claims against sources. Model agreement is not an independent experimental
replication and cannot replace held-out evidence.

## Verification and follow-through

Choose checks that can detect meaningful failures: an incorrect contrast, wrong cohort, broken
resume path, unsupported sentence, missing citation, or clipped figure. Preserve release and
confirmation requirements; avoid full-suite reruns for unrelated prose fixes. Finish the requested
artifact and relevant checks, or report the concrete blocker. A plan alone does not fulfill an
implementation request.

## API workflows, only when in scope

Both models require the Responses API for tool calling; Chat Completions supports requests without
tools. Omit `temperature`, `top_p`, and log-probability options for these reasoning models.
Preserve tool-call/result identities and supported conversation state. Use the host's existing
compaction and pending-tool handling; implement lifecycle features only when requested. Check
current documentation before changing a harness. API options do not define Codex settings or
prove account availability.

## Sources

- [GPT-6 prompting and migration guidance](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices)
- [GPT-6 Astra model](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [GPT-6.1 Sol model](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
