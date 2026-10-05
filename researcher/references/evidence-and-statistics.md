# Evidence and Statistics

Use this reference to decide what the data support and how strongly they support it.

## Contents

- [Label the evidence tier](#label-the-evidence-tier)
- [Identify the outer statistical unit](#identify-the-outer-statistical-unit)
- [Prefer paired designs](#prefer-paired-designs)
- [Choose inference that matches the design](#choose-inference-that-matches-the-design)
- [Report a complete result](#report-a-complete-result)
- [Separate endpoint roles](#separate-endpoint-roles)
- [Preserve cohort and provenance boundaries](#preserve-cohort-and-provenance-boundaries)
- [Use a metrics embargo for blinded work](#use-a-metrics-embargo-for-blinded-work)
- [Classify failures before acting](#classify-failures-before-acting)
- [Use calibrated conclusion language](#use-calibrated-conclusion-language)

## Label the evidence tier

Do not mix evidence tiers rhetorically or numerically:

| Tier | Purpose | Permitted conclusion |
|---|---|---|
| Exploratory | generate hypotheses and debug evaluation | suggestive only |
| Development or post-hoc | choose methods, endpoints, or wording | supports design decisions, not confirmation |
| Frozen prospective | test a preregistered contrast | confirmatory within the registered scope |
| Independent replication | repeat on fresh outer units | stronger evidence of reproducibility |
| External or hardware validation | test a new source, site, platform, or physical system | supports the stated external scope |

Call a cohort fresh only when outcomes were not inspected before the protocol, success rule, and
analysis were fixed.

## Identify the outer statistical unit

Derive independence from the data-generating process:

- frames and time steps within an episode are repeated measurements;
- robots within one jointly generated trajectory are usually correlated;
- patches, tokens, branches, and views from one sample are not new samples;
- evaluation episodes may be inner units while training seeds are outer units;
- subjects, sites, environments, or pretrained checkpoints may be the outer units in other fields.

Use the highest-level independently rerandomized unit relevant to the claim. Aggregate or cluster
below that level. Never inflate sample size with frames, agents, labels, or split cells.

## Prefer paired designs

Pair methods on shared seeds, data, initializations, episodes, and evaluation noise when possible.
Analyze within-pair differences. Pairing removes nuisance variation and makes the sign of every
outer-unit effect auditable.

Check that pairing is genuine:

- the same unit exists for both methods;
- initialization and data order match where intended;
- exclusions apply symmetrically;
- no method receives extra tuning or checkpoint selection;
- missing pairs are handled by a rule fixed before outcomes.

## Choose inference that matches the design

Use the simplest justified procedure:

- exact sign-flip or paired permutation test for a small paired outer cohort;
- paired bootstrap over outer units for an effect interval;
- cluster bootstrap when episodes contain repeated lower-level observations;
- McNemar or an exact paired binary test for matched binary outcomes;
- hierarchical or mixed-effects modeling when several nested variance sources must be estimated;
- noninferiority or equivalence tests only with a scientifically justified margin fixed in advance.

Do not use a frame-level t-test, independently bootstrap both methods in a paired design, or treat
multiple benchmark splits from the same trained seed as independent replications.

State whether the interval and test target a mean, median, ratio, difference, or another estimand.
If an exact test is discrete, explain that the attainable p-values are limited by the number of
outer units.

## Report a complete result

For every decision-relevant contrast report:

- direction and definition of the effect;
- point estimate in interpretable units;
- 95% confidence interval or other declared uncertainty;
- exact or justified p-value when used;
- favorable outer-unit count;
- number and identity class of outer units;
- evaluation scope and evidence tier.

Include absolute performance when reporting relative change. Relative reductions can exaggerate
small denominators and do not reveal whether either system is useful.

A confidence interval that crosses the null does not support directional superiority. It also does
not prove equality. Report the result as unresolved unless a registered equivalence or
noninferiority analysis supports a different conclusion.

Statistical significance does not establish practical importance, mechanism, external validity, or
deployment readiness. Conversely, a scientifically important estimate with a wide interval is an
uncertain result, not automatically a useless one.

## Separate endpoint roles

Declare one primary endpoint for the central claim. Label others as:

- secondary outcomes;
- mechanism or diagnostic endpoints;
- robustness checks;
- safety or boundary checks;
- exploratory analyses.

Do not rescue a failed primary endpoint by promoting a favorable secondary endpoint after
inspection. When several endpoints jointly define success, specify the joint rule before
confirmation.

If a metric becomes central to the paper, retain the material evidence that qualifies it, including
a baseline that performs better on that metric. Compressing the presentation is acceptable;
removing the contradictory evidence is not.

## Preserve cohort and provenance boundaries

For prospective confirmation and release validation, retain:

- registration and protocol hashes;
- code, dependency, and data manifests;
- seed assignments and return codes;
- terminal artifact manifests;
- aggregation identity and run count;
- timestamps and failure audit trails.

For development, retain the input/cohort identity, configuration, outputs, and failure record needed
to reproduce it. For retrospective evidence, record the provenance that exists and mark gaps;
do not demand or invent an earlier registration. For a narrow answer, cite the existing artifact.
Use [evidence records](evidence-records.md) when several claims or source versions need tracking.

Do not combine development and confirmation, old and fresh seeds, or different protocol versions
in the primary analysis. A pooled analysis may be reported explicitly as secondary if its
heterogeneity is visible.

## Use a metrics embargo for blinded work

Before the registered terminal milestone, inspect only operational state:

- resource and process health;
- return codes;
- completion markers;
- artifact counts and hashes.

Do not read training curves, seed summaries, result JSON, scientific metrics, or selective worker
logs if doing so would unblind the analysis. At the registered unblinding milestone, verify
provenance and apply the frozen analysis before opening the result. Repeating the same calculation
on the same inputs for verification is allowed. Log discrepancies and corrections; do not select
a new endpoint, exclusion, or analysis because the first result was unfavorable. A sequential
design may have planned interim looks and stopping rules; follow those registered rules rather
than imposing a universal requirement that every unit finish before any analysis.

## Classify failures before acting

Distinguish:

- **Infrastructure failure:** pod loss, storage, network, scheduler, or hardware problem.
- **Code failure:** deterministic exception, missing dependency, corrupt artifact, or reporting bug.
- **Protocol failure:** implementation or data no longer matches the frozen registration.
- **Scientific negative:** valid run completes and the registered endpoint does not pass.

Preserve the original return code and artifacts before remediation. Fix only infrastructure or code
causes under a documented recovery rule. Do not replace a seed or change the scientific protocol
to turn a negative into a success.

## Use calibrated conclusion language

- **Supported:** “The registered paired contrast supports X within Y.”
- **Not supported:** “The experiment did not support directional improvement on X.”
- **Unresolved:** “The estimate favors X, but the interval includes the null.”
- **Mechanism-qualified:** “The crossed control is consistent with X rather than Y.”
- **Exploratory:** “This pattern motivates a fresh confirmatory test.”
- **Boundary:** “The result does not establish hardware, closed-loop, or out-of-domain performance.”

Avoid “proves,” “universally,” “robust,” “state of the art,” or “generalizes” unless the design
directly earns those words.
