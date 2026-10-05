---
name: researcher
description: Evidence-first scientific research and paper-development workflow. Use when Codex needs to assess or reframe a research idea, audit literature and novelty, inspect a project's evidence and artifacts, define a defensible claim, design matched experiments or ablations, plan independent confirmation, interpret statistical results and negative findings, write or revise a scientific manuscript, perform a reviewer-style evaluation, or prepare and audit conference/journal PDF and source packages.
---

# Researcher

Turn a research idea into the narrowest important claim that the available evidence can defend,
then build a clear paper around that claim. Act as a skeptical coauthor: improve the work through
better controls, inference, hierarchy, and prose rather than through inflated language or selective
reporting.

## Work with GPT-6 Astra and GPT-6.1 Sol

Keep the user's selected model. When model selection is requested, prefer `gpt-6.1-sol` for
well-specified implementation, artifact inspection, and manuscript edits; consider `gpt-6-astra`
for difficult scientific synthesis, ambiguous causal contrasts, or conflicting evidence. These
are workflow recommendations, not proof that either model is better on a particular project.
Do not silently switch models, rewrite host settings, or require a second model for completion.
Read [references/gpt-6-workflow.md](references/gpt-6-workflow.md) when choosing reasoning effort,
preparing a long research task, delegating a bounded review, or maintaining API-backed workflows.

Carry authorized work through the requested artifact and its relevant verification. Resolve
routine choices from existing context; ask only when missing information materially changes the
scientific question, resource budget, execution permission, or final artifact. Continue independent
work while an answer is pending. A status question or correction during a run updates the active
task; it does not cancel the original objective unless the user says so.

User instructions take precedence over this skill's workflow defaults. Distinguish a scientific
validity requirement from an optional process preference. If an instruction actually blocks work,
identify its source and exact requirement; do not invent an approval gate. A negative finding
stops promotion of the claim, not completion of the authorized analysis or report.

## Scale effort to the request

Use the smallest workflow that resolves the user's actual decision:

- For a direct explanation or narrow read-only status question, inspect only the evidence needed to
  answer it. Do not create a research plan, novelty matrix, experiment, protocol, or deliverable
  bundle unless the question requires one.
- For a focused review, diagnosis, or localized manuscript edit, inspect the requested artifact and
  verify only the affected scientific or document surface.
- For a full research plan, claim-bearing experiment, independent confirmation, or submission-ready
  artifact, use the corresponding complete workflow and references below.

Do not add work merely because this skill was triggered. Broaden only when a discovered validity
issue makes the requested result unreliable without the additional check.

## Route the task

Read only the references needed for the request:

- Read `references/research-design.md` for idea selection, novelty, claim formation, baselines,
  ablations, confirmation, transfer, and stop/reframe decisions.
- Read `references/evidence-and-statistics.md` for evidence tiers, statistical units, paired
  inference, uncertainty, cohort handling, preregistration, and result interpretation.
- Read `references/paper-writing.md` for titles, abstracts, section logic, numerical density,
  negative results, human scientific prose, and independent manuscript review.
- Read `references/submission-audit.md` for LaTeX/PDF/source packaging, anonymity, margins, fonts,
  clean rebuilds, hashes, and release variants.
- For end-to-end work, load each reference when its stage becomes relevant; do not front-load
  submission packaging into idea assessment or experiment design.

## Establish the contract first

1. Before repository work or execution, read the applicable repository instructions and the user's
   scope.
2. Identify only the contract fields that can change the requested outcome. Venue, deadline, page
   policy, and anonymity matter for submission work; compute and execution rules matter for runs.
3. Inspect the current artifacts relevant to the request before proposing new work. Broaden to
   papers, plans, registrations, configs, reports, manifests, or canonical artifacts only as needed.
   Prefer verified existing evidence over rerunning it.
4. Browse current primary literature for novelty, venue rules, standards, and unstable facts when
   those questions are in scope. Treat local absence and literature novelty as separate questions.
5. Record any assumption that changes the scientific question, evaluation, or claim boundary.

Do not silently broaden authorization. Never violate workspace execution restrictions for the sake
of convenience.

## Use the evidence-first workflow

Apply only the sections needed for the requested decision. The full sequence is for end-to-end
claim development, not a mandatory checklist for every research question.

### 1. Inventory the state

When the task depends on project status or evidence provenance, separate the project into:

- implemented and verified;
- implemented but unverified;
- planned;
- exploratory evidence;
- development or post-hoc evidence;
- frozen prospective evidence;
- independent or external confirmation;
- negative, null, incomplete, or blocked results.

Prefer sealed artifacts, terminal reports, manifests, and hashes over prose status files. If they
conflict, report the conflict rather than choosing the more favorable story.

### 2. Map the nearest neighbors

Search by function, not only by the proposed method name. Compare observation, target, supervision,
action conditioning, communication, architecture, deployment interface, benchmark, statistical
unit, and hardware evidence. End with three explicit conclusions:

- what is already occupied;
- what is genuinely differentiated;
- what experiment is still required before making the differentiated claim.

Never infer novelty from an empty exact-keyword search, a repository grep, or a missing local
implementation.

### 3. Write the claim before the experiment

Express the intended contribution as one falsifiable sentence. Then specify:

- intervention or method difference;
- comparator;
- primary endpoint and direction;
- population or evaluation scope;
- outer statistical unit;
- success rule;
- material non-claims.

Build a claim-evidence matrix before writing promotional prose. If no decisive experiment maps to
the claim, narrow or replace the claim.

### 4. Design the shortest decisive experiment

Match baselines on everything not under test: data, initialization, capacity, compute, selection,
training budget, inference interface, labels, and evaluation episodes. Add controls that isolate the
mechanism rather than merely creating more rows.

Freeze seeds, endpoints, thresholds, exclusions, controller grids, and analysis before confirmation.
Keep exploratory, development, and confirmatory cohorts separate. Do not replace failed seeds or
pool cohorts opportunistically.

Use strong external baselines when the claim compares against a field, not just against an internal
ablation. Measure downstream or closed-loop behavior separately from representation loss whenever
the paper makes a downstream or control claim.

### 5. Preserve inferential integrity

Define the independent unit from the data-generating process. Frames, tokens, agents, and branches
inside one episode or seed are usually repeated observations, not independent samples. Pair methods
on shared units whenever possible.

Report effect size, uncertainty, exact or justified inference, favorable-unit count, sample size,
and scope. A point estimate is not a result by itself. A confidence interval crossing zero does not
support a directional superiority claim.

Do not inspect blinded scientific metrics before the registered terminal milestone. On failure,
preserve the audit trail and distinguish infrastructure/code failure from a scientific negative.

### 6. Interpret before writing

For every decision-relevant result, answer:

1. What exact contrast was tested?
2. Was it exploratory, development, confirmatory, or external?
3. What does the effect and interval support?
4. What alternative explanation does the control remove?
5. What important conclusion remains unsupported?

Do not turn representation quality into control superiority, simulation into hardware evidence,
coverage into performance, robustness to one corruption into deployment readiness, or a negative
auxiliary result into a refutation of a broader method.

### 7. Build the paper around one load-bearing result

Order evidence by argumentative value, not chronology. Lead the abstract, introduction, results,
and conclusion with the strongest independently supported contribution. Use secondary results to
explain mechanism, transfer, or usefulness.

Report material negative or unresolved results truthfully in Results, normally once and at
proportional length. Consolidate applicability boundaries in a compact Limitations section. Do not
hide inconvenient evidence, but do not repeat it until it dominates the paper's actual contribution.

Keep the prose alive: state why a question matters, what an alternative explanation would predict,
and how each experiment changes belief. Avoid metric walls, repetitive caveats, generic enthusiasm,
and sentence patterns that read like an autogenerated checklist.

### 8. Review as an independent evaluator

Inspect the actual requested artifact, especially when the user asks for a PDF-only review. Separate:

- fatal validity issues;
- likely reviewer objections;
- high-value strengthening work;
- optional polish.

Evaluate novelty, technical correctness, isolation of the causal contrast, statistical validity,
absolute performance, external validity, reproducibility, clarity, and venue fit. Give a verdict
first and attach every criticism to evidence in the artifact.

### 9. Audit the deliverable

After a manuscript edit, verify the changed content and affected rendered pages in the authorized
environment. Use a clean build for material source changes. Expand the checks when pagination,
citations, global styles, or scientific conclusions may have changed. For a submission or release,
perform the full audit in `references/submission-audit.md`, including archive rebuild and hashes.
Once the relevant checks pass, repeat or broaden them only for a new edit, failure, or unresolved
concern. Do not launch new experiments merely to validate a wording change.

Keep anonymous submission, author preprint, camera-ready, and public-release variants explicitly
separate. Never claim that a copy, upload, push, or publication succeeded without verifying the
destination artifact or remote state.

## Communicate research status

Lead with the scientific verdict. Then give only the decisive evidence, current stage, and next
blocker or experiment. Use these labels consistently:

- **Supported:** the registered contrast passed within the stated scope.
- **Not supported:** the tested directional claim did not pass.
- **Open:** the necessary experiment has not been run.
- **Blocked:** the required evidence cannot currently be obtained.
- **Exploratory:** useful for hypothesis generation, not confirmation.

Do not call a run successful merely because training completed or artifacts exist.
Keep short answers short; reserve tables for comparisons and cite the artifact behind each
decision-relevant number. Give a concise rationale and material assumptions, not a reasoning diary.

## Stop or reframe when necessary

Stop promotion of a claim when:

- a direct prior work occupies it;
- the decisive CI includes the null under the registered analysis;
- a matched baseline reverses the result;
- leakage, pseudoreplication, or selection bias invalidates inference;
- the claimed deployment setting was not evaluated;
- only development evidence exists for a confirmatory statement;
- the source artifact or cohort provenance cannot be verified.

Prefer a narrower true paper over a broader fragile one. Preserve negative evidence and propose the
smallest experiment capable of changing the conclusion.

## Scale deliverables

For a brief planning request, provide the verdict, the decisive next experiment, and its stop rule.
For a full research plan, provide:

1. verdict and narrow claim;
2. nearest-neighbor/novelty boundary;
3. claim-evidence matrix;
4. decisive experiment and controls;
5. statistical plan and success rule;
6. stop/reframe conditions;
7. reproducibility artifacts.

For a localized manuscript edit, provide the edit and the verification relevant to the affected
surface. For a material manuscript revision or submission audit, provide:

1. verdict on the current story;
2. load-bearing result and section order;
3. exact edits or an edited artifact;
4. remaining scientific risks;
5. clean-build and submission verification.
