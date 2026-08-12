# Codex Scientist Skill

Codex Scientist Skill packages `Researcher`, an evidence-first Codex skill that accelerates
scientific research from an initial idea to a submission-ready paper. It shortens the repeated
work of mapping prior art, sharpening claims, designing decisive experiments, interpreting
results, and turning verified evidence into clear scientific prose.

The speed comes from a reusable research workflow, not from lowering the evidence bar. Researcher
acts as a skeptical coauthor: it keeps claims tied to artifacts, separates exploration from
confirmation, surfaces material limitations, and helps researchers spend more time on scientific
judgment and less time rebuilding the same process.

The skill is domain-agnostic and instruction-only. It contains no datasets, experimental results,
model weights, credentials, private project paths, or executable workloads.

## What it accelerates

- audits literature and separates local implementation gaps from genuine novelty;
- turns ideas into falsifiable claim–evidence contracts;
- designs matched baselines, mechanism controls, ablations, and independent confirmation;
- protects statistical-unit, pairing, cohort, provenance, and preregistration integrity;
- distinguishes exploratory, development, confirmatory, replication, and external evidence;
- writes and revises titles, abstracts, introductions, results, discussions, and limitations;
- reports negative or unresolved findings honestly and with proportional emphasis;
- performs reviewer-style manuscript evaluations;
- audits PDF, LaTeX source, anonymity, margins, fonts, archives, hashes, and release variants.

## Repository layout

```text
codex-scientist-skill/
├── README.md
├── LICENSE
└── researcher/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── research-design.md
        ├── evidence-and-statistics.md
        ├── paper-writing.md
        └── submission-audit.md
```

`SKILL.md` contains the core workflow. The four references are loaded only when relevant, keeping
the initial context compact.

## Installation

### With the Codex skill installer

Ask Codex to install the `researcher` subdirectory from this repository:

```text
Use $skill-installer to install the researcher skill from
https://github.com/<your-account>/codex-scientist-skill/tree/main/researcher
```

Replace `<your-account>` with the repository owner's GitHub account after publication.

### Manual user installation

Codex loads personal skills from `$HOME/.agents/skills`:

```bash
git clone https://github.com/<your-account>/codex-scientist-skill.git "$HOME/codex-scientist-skill"
mkdir -p "$HOME/.agents/skills"
ln -s "$HOME/codex-scientist-skill/researcher" "$HOME/.agents/skills/researcher"
```

Codex detects skill changes automatically. Restart Codex if the skill does not appear.

### Repository-scoped installation

To make the skill available only inside one project, place or link it under the project root:

```text
.agents/skills/researcher/
```

See the official [OpenAI skill documentation](https://developers.openai.com/codex/skills) for
skill discovery and distribution details.

## Usage

Invoke the skill explicitly with `$researcher`, or let Codex select it when a request matches its
description.

Example prompts:

```text
Use $researcher to audit this research idea and identify the narrowest defensible novelty claim.
```

```text
Use $researcher to design a matched confirmatory experiment, including the statistical unit,
primary endpoint, controls, success rule, and stop conditions.
```

```text
Use $researcher to review only this PDF as an independent conference reviewer.
```

```text
Use $researcher to rewrite this abstract around the strongest verified result without hiding
material negative evidence.
```

## Design principles

Researcher follows several strict defaults:

1. Evidence precedes prose.
2. Novelty is established through functional nearest neighbors, not exact-keyword absence.
3. The outer statistical unit follows the data-generating process.
4. Development evidence is not presented as independent confirmation.
5. Representation metrics do not automatically establish downstream or deployment performance.
6. Material negative evidence is retained once, clearly and proportionally.
7. Public, anonymous, author-identified, and internal artifacts remain separate.
8. Copies, builds, uploads, and releases are not called successful until the destination is checked.

## Privacy and data access

This repository is self-contained and does not include or connect to private research data. The
skill does not embed internal project names, paths, results, identifiers, hashes, email addresses,
API keys, or service credentials.

When invoked, the skill operates within the permissions of its host. It may inspect files or use
tools that the user has already made available to Codex, but it does not grant new access or send
data anywhere by itself. Review the host's permissions and repository instructions before using it
with sensitive material.

## Contributing

Keep contributions general, evidence-first, and free of project-specific or confidential details.
Preserve progressive disclosure: put the core decision workflow in `SKILL.md` and detailed guidance
in a directly linked file under `references/`.

Before submitting a change, validate the `researcher/` directory with the current Codex
`skill-creator` validator and scan the complete repository for secrets, private paths, and
organization-specific identifiers.

## License

Released under the [MIT License](LICENSE).
