# Skill evaluation

The 12 cases in `cases.json` are synthetic, closed-book decision fixtures. Each includes a request,
source records, deterministic expectations, and a separate manual rubric. Nothing is a real paper
citation or experimental result. Expected answers and rubrics never enter evaluated prompts.

## What is measured

The grader checks the decision, numeric fidelity, independent-unit count, exact supplied source
locations, unnecessary proposed experiments/questions, and presence of a requested deliverable.
It rejects missing or duplicate case IDs and malformed output. A correct structured verdict can
still accompany bad prose: inspect every `answer` and `deliverable` against `manual_rubric` before
calling a run successful. Do not treat an unreviewed deterministic score as scientific quality.

The baseline receives the same tasks, source data, output schema, and definitions of verdict
labels. Neither arm must infer an unpublished scoring vocabulary. The skill arm additionally
receives the current `SKILL.md` and references. This measures an explicitly supplied instruction
pack, not native skill discovery or progressive loading. `should_trigger` is a future native
activation expectation, not a scored assertion that the skill actually triggered. PDF-only means
a visible excerpt fixture; it does not test PDF rendering. Each arm is one batch with 12 tasks,
so cases share context and are not independent repeated trials.

## Offline checks

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These require no model credentials and run in CI. Test responses constructed from expectations
validate the grader only; they are not model results.

## Bounded live comparison

Use an installed, authenticated Codex CLI with the flags checked by the runner. First print a plan:

```sh
python3 scripts/run_evals.py --out evals/runs/comparison-001
```

Then explicitly authorize up to four model calls, each with a 240-second timeout:

```sh
python3 scripts/run_evals.py --execute --max-calls 4 --timeout-seconds 240 \
  --models gpt-6-astra gpt-6.1-sol --effort medium --out evals/runs/comparison-001
```

The output directory must be new. The runner preserves model IDs, disables host skill discovery,
project instructions, ordinary execution tools, multi-agent work, and web search for this closed
corpus. It ignores user configuration while retaining the existing Codex login. It captures raw
traces locally, flags unexpected completed tool items, and stops at the first backend/isolation/
output error without retrying or substituting a model. Host-enforced policy still applies. Inspect
traces before assuming isolation in a different CLI version. Do not run the suite against private
research artifacts. Ordinary CI and skill use never invoke the model runner.

Report the model, effort, skill/corpus/prompt hashes, backend, trials, failed checks, and manual
review separately. Token usage and latency are recorded when returned by the CLI; pricing is not
inferred. Unsupported models, timeouts, or unavailable credentials are infrastructure outcomes,
not failed scientific decisions. One small fixture suite cannot establish general model rankings
or a research-productivity gain.

## Another authorized evaluation host

Prepare prompts without access to hidden grading data:

```sh
python3 scripts/evaluate.py prepare --arm baseline --out evals/runs/baseline-prompt.txt
python3 scripts/evaluate.py prepare --arm skill --out evals/runs/skill-prompt.txt
```

Run each prompt in a fresh context on each named model. Save the returned JSON object containing
`responses`, then grade it:

```sh
python3 scripts/evaluate.py grade evals/runs/responses.json --out evals/runs/grade.json
```

Record the actual backend and settings. Imported output does not supply a verified tool trace,
usage, or latency; leave those measurements unavailable. Never copy a previous arm's answers into
a new trial. Inspect prose manually, and publish only sanitized summaries, not local raw traces.

See [OpenAI's skill evaluation guidance](https://developers.openai.com/blog/eval-skills).

## Published comparison

See [the v0.2.0 evaluation report](results/v0.2.0/README.md), including the initial pilot,
changes made after manual inspection, fresh comparison, and sanitized model responses.
