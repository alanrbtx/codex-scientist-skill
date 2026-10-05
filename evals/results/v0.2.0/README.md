# v0.2.0 synthetic evaluation — 2026-10-05

The revised suite returned **12/12 structured checks for every model/arm**. This is a regression
smoke test, not evidence that the skill improves research quality or that either model is better.

## Setup

We ran 12 fictional closed-book tasks in each fresh Codex app subagent context, on
`gpt-6-astra` and `gpt-6.1-sol`, at `medium` effort, with and without the supplied skill. One batch
per arm shares context across tasks. Both arms received identical sources and an output schema;
the skill arm additionally received `SKILL.md` and all six references. Expected answers and manual
rubrics were withheld. Neither arm was given real research data.

The orchestrating assistant read every response against the rubric, including the generated
abstracts. This was model-assisted inspection, not independent human review. Numbers, decisions,
source locations, and output shape were also checked by the deterministic grader.

## Results

| Round | Model | Arm | Structured | Manual cases without findings |
| --- | --- | --- | --- | --- |
| Pilot | Astra | Baseline | 8/12 | 11/12 |
| Pilot | Astra | Skill | 10/12 | 12/12 |
| Pilot | Sol | Baseline | 8/12 | 11/12 |
| Pilot | Sol | Skill | 11/12 | 11/12 |
| Revised | Astra | Baseline | 12/12 | 12/12 |
| Revised | Astra | Skill | 12/12 | 12/12 |
| Revised | Sol | Baseline | 12/12 | 11/12 |
| Revised | Sol | Skill | 12/12 | 12/12 |

The pilot's structured failures were status-label mismatches, not incorrect numerical results.
The baseline lacked definitions distinguishing `open`, `unresolved`, and `not_supported`.
This made the pilot unsuitable for a comparative quality claim. The revised shared schema defines
all labels for both arms; expected scientific outcomes and source facts remain unchanged.

Manual inspection found an actual fidelity error in Sol's pilot skill abstract: it added "95%"
to a source that said only "CI". We clarified the skill's instruction to preserve unspecified
interval levels and methods. The fresh revised skill response did not repeat that error.
The two pilot baselines and revised Sol baseline also omitted the interval bounds in
`null-difference`, despite its rubric asking to preserve the CI; their directional conclusions
were correct. All these findings remain visible in the per-case report.

Because the same fixtures informed these changes, the revised suite is not a held-out evaluation.
It does not justify a causal attribution to the new wording or a general model ranking.

## Reproducible records

[report.json](report.json) records per-case checks, manual findings, model settings, and SHA-256
hashes of the corpus, grader, schema, prompts, skill packs, and responses. Each round retains its
exact public synthetic prompts and unedited responses:

| Round | Prompts | Astra responses | Sol responses |
| --- | --- | --- | --- |
| Pilot | [Baseline](pilot/baseline-prompt.txt), [skill](pilot/skill-prompt.txt) | [Baseline](pilot/astra-baseline.json), [skill](pilot/astra-skill.json) | [Baseline](pilot/sol-baseline.json), [skill](pilot/sol-skill.json) |
| Revised | [Baseline](revised/baseline-prompt.txt), [skill](revised/skill-prompt.txt) | [Baseline](revised/astra-baseline.json), [skill](revised/astra-skill.json) | [Baseline](revised/sol-baseline.json), [skill](revised/sol-skill.json) |

Regrade a response from the repository root:

```sh
python3 scripts/evaluate.py grade evals/results/v0.2.0/revised/astra-skill.json
```

## Backend and measurement limits

Codex CLI 0.156.1 with the available ChatGPT login rejected `gpt-6.1-sol` as unsupported. A bounded
runner check recorded `backend_error` and stopped. The scientific outputs above were therefore
collected with separately configured app subagents, not that failed CLI call. No unsupported model
was silently substituted. Raw local infrastructure traces are not published.

For these imported app outputs, token usage, latency, and a verified tool trace are unavailable.
The model tasks permitted tools only for reading the prepared prompt and saving the answer;
full isolation from host instructions was not attested. Native skill discovery, progressive
loading, browsing, actual PDF rendering, experiment execution, costs, and end-to-end research
productivity are untested. Additional independent tasks and repeated trials are needed to assess
those outcomes.
