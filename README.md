# Codex Scientist Skill

![Codex Scientist: Research faster. Write with evidence.](assets/codex-scientist-banner.png)

`Researcher` is an evidence-first Codex skill for scientific judgment and paper development.
It helps audit novelty, design comparisons, interpret results, and turn verified evidence into
clear prose. It scales the workflow to the request: a question gets an answer, an abstract edit
gets an abstract, and a submission gets the corresponding artifact checks.

The installable `researcher/` package contains instructions only. Development tools and fictional
evaluation fixtures live outside it. No private research data, model weights, or credentials are
included. The workflow's research-quality and productivity benefits have not been established by
these small synthetic tests.

## What it covers

- Functional prior-art comparisons and bounded novelty claims.
- Matched experiments, appropriate controls, and independent confirmation.
- Statistical units, pairing, uncertainty, and exploratory versus confirmatory evidence.
- Claim-to-source records with exact locations and numeric derivations.
- Paper writing, localized revisions, negative findings, and manuscript review.
- PDF/source checks, submission packaging, and destination verification.

Claim types have distinct evidence requirements, not a mandatory sequence. A valid downstream
result does not first need a transfer or mechanism study. Repeating an unchanged frozen analysis
for verification is allowed; changing an analysis after seeing results does not make it prospective.

## GPT-6 Astra and GPT-6.1 Sol

The guidance preserves the user's selected model and existing authorization. When model selection
is requested, `gpt-6.1-sol` is a candidate for bounded implementation and editing; `gpt-6-astra` is a
candidate for difficult synthesis and conflicting evidence. This is a routing hypothesis to test
on the actual workload, not a measured ranking.

See [GPT-6 workflow](researcher/references/gpt-6-workflow.md) for effort selection, long-task state,
bounded delegation, API/host distinctions, and official sources checked on 2026-10-05. Installing
the skill does not switch models or change global configuration.

## Installation

Ask Codex to install the `researcher` subdirectory with its skill installer:

```text
Use $skill-installer to install the researcher skill from
https://github.com/alanrbtx/codex-scientist-skill/tree/v0.2.0/researcher
```

Use `tree/main/researcher` instead for the latest development revision. For a manual installation:

```sh
git clone --branch v0.2.0 https://github.com/alanrbtx/codex-scientist-skill.git
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/codex-scientist-skill/researcher" "$HOME/.agents/skills/researcher"
```

Choose an unused destination; preserve any existing skill installation. For one project, place or
link `researcher/` under that project's `.agents/skills/`. See the official
[Codex skills documentation](https://developers.openai.com/codex/skills) for discovery details.

## Usage and complete examples

Invoke `$researcher` explicitly, or let Codex select it for requests matching its description.
Ordinary grammar and formatting edits need no scientific workflow.

```text
Use $researcher to audit this idea against the supplied papers and identify the narrowest
supported novelty claim.

Use $researcher to interpret this paired evaluation, including the independent unit and uncertainty.

Use $researcher to rewrite only this abstract around its strongest verified result.
```

Three [fictional worked examples](examples/novelty.md) include sources, a request, a finished answer,
and the checks that matter:

| Example | Decision |
| --- | --- |
| [Novelty audit](examples/novelty.md) | Reject broad priority when a functional counterexample exists. |
| [Uncertain result](examples/uncertain-result.md) | Preserve an inconclusive comparison without claiming equality. |
| [Abstract edit](examples/abstract.md) | Return the requested text with the verified effect and scope. |

## Repository layout

```text
researcher/
  SKILL.md                         # Concise entry point
  agents/openai.yaml               # Codex UI metadata
  references/
    research-design.md
    evidence-and-statistics.md
    evidence-records.md
    paper-writing.md
    submission-audit.md
    gpt-6-workflow.md
examples/                           # Three complete synthetic examples
evals/                              # 12 decision fixtures, schema, published results
scripts/                            # Offline validators and opt-in model runner
tests/                              # Grader and validation regression checks
.github/workflows/validate.yml       # Offline CI
VERSION                             # Release version
```

References load when relevant during ordinary use. The evaluation suite deliberately supplies all
references to isolate the instruction-pack comparison; it does not test native skill activation.

## Validation and evaluation

Use Python 3.10 or newer. Offline checks require only the pinned development dependency:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

CI checks skill metadata, local Markdown links, common private-data patterns, fixture structure,
and grader regressions. Model calls are separate and require an explicit `--execute` flag and
bounded run settings. See [evaluation instructions](evals/README.md) and the
[v0.2.0 report](evals/results/v0.2.0/README.md) for methods, actual responses, failures, and limits.
A passing fixture score is not evidence of real-world research quality or productivity.

## Privacy and contributing

Keep contributions general and free of confidential project details. The skill operates within
its host's permissions; it grants no access by itself. Automated private-data checks cover common
patterns, so review new public artifacts as well. Keep local traces in ignored `evals/runs/` and
publish only sanitized synthetic results.

Put core decisions in `SKILL.md` and details in directly linked references. Add a targeted fixture
when fixing a behavioral failure. Review generated prose as well as structured scores. Before a
release, pass offline checks, update `VERSION`, and tag the verified commit as `v<VERSION>`; CI
checks that a release tag matches the version file.

## License

[MIT](LICENSE).
