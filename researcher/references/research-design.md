# Research Design

Use this reference to turn a broad idea into a falsifiable, defensible contribution.

## Contents

- [Start from the scientific question](#start-from-the-scientific-question)
- [Place the intended claim on a ladder](#place-the-intended-claim-on-a-ladder)
- [Audit novelty by function](#audit-novelty-by-function)
- [Build a claim-evidence matrix](#build-a-claim-evidence-matrix)
- [Design matched comparisons](#design-matched-comparisons)
- [Choose controls that remove alternative explanations](#choose-controls-that-remove-alternative-explanations)
- [Freeze the confirmatory protocol](#freeze-the-confirmatory-protocol)
- [Test the claim at the correct level](#test-the-claim-at-the-correct-level)
- [Select work by expected information gain](#select-work-by-expected-information-gain)

## Start from the scientific question

Write the problem in four layers:

1. **Observation:** what information is available to the method at training and deployment?
2. **Mechanism:** what representation, objective, architecture, or interaction is proposed?
3. **Outcome:** what measurable behavior should change because of that mechanism?
4. **Scope:** on which population, benchmark, environment, and deployment regime should it hold?

Do not begin with a method name and search for a problem. State the failure mode or missing
capability first, then ask whether the proposed mechanism is the shortest credible way to address
it.

## Place the intended claim on a ladder

Claims become progressively harder to defend:

1. **Existence:** the system can be trained or made to work.
2. **Comparative:** it outperforms a matched alternative on a registered endpoint.
3. **Mechanistic:** the improvement is caused by the proposed factor.
4. **Transfer:** it persists under a specified distribution shift.
5. **Downstream:** it improves a task or closed-loop outcome.
6. **Deployment:** it works under real operational constraints.

Do not skip levels. A lower representation loss does not establish downstream control, and
simulation does not establish deployment. Choose the highest level directly supported by the
planned evidence and name the remaining levels as non-claims.

## Audit novelty by function

Search current primary literature and official project artifacts using several descriptions of the
function, not only the proposed acronym. Include:

- the task and deployment setting;
- observation and target modalities;
- self-supervision or supervision;
- action conditioning and temporal horizon;
- communication and centralization assumptions;
- architecture and bottleneck;
- evaluation benchmark and statistical unit;
- hardware, simulation, or external-validation evidence.

Build a nearest-neighbor matrix with one row per relevant work and these columns:

| Work | Observation | Prediction target | Training signal | Deployment information | Main evaluation | Claim overlap |
|---|---|---|---|---|---|---|

End the audit with:

- **Occupied:** the strongest claim already demonstrated by prior work.
- **Differentiator:** the narrow, material difference in the proposed work.
- **Missing evidence:** the experiment needed to establish that difference.

Local repository absence, an empty exact-keyword search, or a new combination of familiar
components is not sufficient evidence of novelty. Avoid “first” unless the search is unusually
complete and the claim is precisely bounded.

## Build a claim-evidence matrix

Before launching experiments or rewriting the paper, fill one row per intended claim:

| Claim | Comparator | Primary endpoint | Outer unit | Required control | Evidence tier | Non-claim |
|---|---|---|---|---|---|---|

Every headline claim must have one decisive endpoint. If a claim needs several loosely related
metrics to appear true, it is probably too broad.

## Design matched comparisons

Hold constant everything not under test:

- data, splits, preprocessing, augmentations, and labels;
- initialization, training budget, optimizer, and selection rule;
- model width, bottleneck, effective capacity, and deployment interface;
- inference inputs, communication budget, controller, and evaluation episodes.

Parameter count alone is not matching. Also compare information access, training-only heads,
pretrained sources, tuning budget, and the opportunity to select a favorable checkpoint.

Use a strong external baseline when making a field-level superiority claim. An internal ablation
can identify a mechanism but usually cannot establish competitiveness.

## Choose controls that remove alternative explanations

Prefer a small crossed or factorial design over many decorative ablations. Useful controls include:

- same architecture with a different objective;
- same objective with a different encoder or pretraining source;
- removal of an input shortcut or privileged variable;
- matched-capacity reconstruction or predictive baseline;
- randomization of coordinate frame, ordering, or nuisance features;
- frozen versus independently trained upstream checkpoints;
- downstream evaluation with the representation held fixed.

State in advance what each result pattern would imply. An interaction is often more informative
than two isolated wins because it tests whether the effect depends on the suspected mechanism.

## Freeze the confirmatory protocol

Before seeing confirmatory outcomes, record:

- exact code and data identities;
- seeds and assignment to compute;
- primary and secondary endpoints;
- exclusions and failure handling;
- thresholds and direction of success;
- baseline selection and hyperparameter grids;
- statistical unit and inference procedure;
- aggregation command and when metrics may be opened.

Separate exploratory tuning, development evaluation, independent confirmation, and external
validation. Reuse of a frozen protocol is valuable; reuse of inspected data as if it were sealed is
not.

Do not substitute a failed seed, tune after partial outcomes, or pool old and new cohorts without
labeling the pooled analysis secondary.

## Test the claim at the correct level

- Evaluate prediction or representation claims with absolute quality and matched comparisons.
- Evaluate label efficiency with full learning curves or predeclared low-label summaries.
- Evaluate robustness across independently meaningful shifts, not just more corruptions.
- Evaluate control claims in closed loop with task-level outcomes.
- Evaluate decentralization with actual information-flow and communication constraints.
- Evaluate deployment claims on hardware or state clearly that evidence is simulation-only.

Use the cited field's experimental conventions as a starting point, but do not imply sim-to-real
transfer from visual realism or physics alone.

## Select work by expected information gain

Prioritize the experiment that most cleanly separates competing explanations. A useful ranking is:

1. fatal validity check;
2. matched baseline or leakage control;
3. independent confirmation of the load-bearing result;
4. mechanism-isolating factorial control;
5. external or downstream validation;
6. optional breadth and polish.

Stop or reframe when direct prior work occupies the claim, the matched comparison reverses it, the
registered interval includes the null for a directional claim, or the intended deployment regime
was never evaluated. A narrower result with clear causal isolation is usually stronger than a
broad collection of favorable metrics.
