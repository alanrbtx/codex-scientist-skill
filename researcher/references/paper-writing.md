# Paper Writing

Use this reference to turn verified evidence into a coherent, readable scientific argument.

For changed claims, citations, or numbers, preserve their source and exact locator using
[evidence records](evidence-records.md). A localized wording edit needs only the affected passage;
the section patterns below are guidance for the corresponding section, not mandatory extra work.

## Contents

- [Choose one load-bearing sentence](#choose-one-load-bearing-sentence)
- [Calibrate the title](#calibrate-the-title)
- [Write a diagonal-readable abstract](#write-a-diagonal-readable-abstract)
- [Make the introduction argue](#make-the-introduction-argue)
- [Keep related work comparative](#keep-related-work-comparative)
- [Make Methods auditable](#make-methods-auditable)
- [Separate experimental design from results](#separate-experimental-design-from-results)
- [Report negative results with proportional weight](#report-negative-results-with-proportional-weight)
- [Write Discussion as scientific reasoning](#write-discussion-as-scientific-reasoning)
- [Keep Limitations compact and material](#keep-limitations-compact-and-material)
- [Let the conclusion close the argument](#let-the-conclusion-close-the-argument)
- [Design figures and tables around reader decisions](#design-figures-and-tables-around-reader-decisions)
- [Make the prose sound authored](#make-the-prose-sound-authored)
- [Perform an independent manuscript review](#perform-an-independent-manuscript-review)

## Choose one load-bearing sentence

Write one sentence containing the problem, mechanism, decisive result, and scope. Every major
section should help the reader understand or trust that sentence. Results that do not change the
central conclusion belong in a compact table, appendix, or may be omitted if they are not material.

Do not organize the paper as a chronological lab notebook. Order it by argumentative value:

1. why the problem matters;
2. why existing approaches leave a precise gap;
3. the proposed idea and its causal prediction;
4. the decisive comparison;
5. controls that remove alternative explanations;
6. scope, limitations, and implications.

## Calibrate the title

Make the title specific enough to select the right audience and narrow enough to survive the
weakest material result. Prefer the capability and setting over a string of fashionable nouns.

Do not put “robust,” “general,” “real-world,” “label-efficient,” or “decentralized” in the title
unless the paper directly evaluates the relevant dimensions. The title may foreground the
strongest contribution, but it must not outrun the evidence.

## Write a diagonal-readable abstract

Default to five moves:

1. the concrete problem and constraint;
2. the missing capability or question;
3. the method and what makes it different;
4. the strongest confirmatory result;
5. the scope and implication.

Use one to three decision-changing numbers by default. Do not include confidence intervals
(CIs) in the abstract; report them in Results or tables, unless the user or an applicable venue
format explicitly requires them in the abstract. Keep the key effect and its scope in the abstract.
Describe inconclusive outcomes accurately in words; omitting interval bounds must not turn an
uncertain result into a claim of improvement. Move detailed split values and secondary endpoints
to Results or a table. Put the closed-loop or deployment relevance early when that is the actual
robotics contribution.

Avoid opening with a generic field truism. Avoid a wall of metrics. State a causal or falsifiable
idea, not only a list of components.

## Make the introduction argue

Use a premise–tension–proposal–test structure:

- establish the operational need;
- explain why the constraint makes the problem nontrivial;
- identify the nearest existing solution and its missing assumption;
- introduce the proposed mechanism as a response;
- state what result would distinguish it from the alternative explanation;
- summarize contributions in evidence order.

Contributions should be claims already supported by the paper, not a table of contents. Do not call
standard implementation work a contribution merely to reach three bullets.

## Keep related work comparative

Organize by the scientific alternatives that matter to the claim. For each group explain:

- what information and target it uses;
- which deployment assumptions differ;
- what evidence it provides;
- why the remaining gap is material.

Avoid citation catalogs and novelty-by-omission. Cite direct counterexamples and narrow the claim
when necessary. Use current primary sources and preserve exact attribution.

## Make Methods auditable

Methods should let a skeptical reader reconstruct:

- inputs available at training and deployment;
- target construction and stop-gradient paths;
- architecture and parameter matching;
- losses and every nonzero weight;
- communication, action, and centralization assumptions;
- data splits, selection, and evaluation unit;
- what exists only during training.

Separate conceptual equations from implementation details, but do not hide a privileged input or
training-only component in prose. Name the actual paper output, not an easier diagnostic proxy.

## Separate experimental design from results

In Experimental Setup state the hypothesis, primary endpoint, statistical unit, matched baseline,
controls, cohorts, and success rule before presenting outcomes.

In Results lead each subsection with a claim-sized conclusion, then provide evidence, then explain
which alternative interpretation it removes. A useful paragraph rhythm is:

1. question;
2. comparison;
3. decisive result;
4. interpretation;
5. boundary.

Tables should carry dense numbers. Prose should carry meaning. Repeat only values required to
follow the argument.

## Report negative results with proportional weight

Do not hide a material negative, especially when it qualifies a headline metric or mechanism. Also
do not repeat secondary negatives until they become the paper's main story.

Use this hierarchy:

- state the registered negative or null once in Results;
- keep exact material evidence in a table or concise sentence;
- explain a genuine applicability boundary once in Limitations;
- exclude secondary negatives from Abstract and Conclusion unless they alter the central claim.

If a stronger comparator wins on a metric that the paper foregrounds, retain that trade-off even
when the proposed method wins the primary endpoint. A concise honest formulation is stronger than
deleting the comparison.

## Write Discussion as scientific reasoning

Discussion should answer:

- why the observed pattern is plausible;
- which control changed the causal interpretation;
- what the method appears to trade off;
- where the result should and should not transfer;
- what experiment would most change confidence.

Do not merely restate every number. Distinguish explanation from speculation with calibrated
language: “supports,” “is consistent with,” “suggests,” and “does not establish.”

## Keep Limitations compact and material

Include boundaries that could change a reader's decision:

- simulation-only or single-platform evidence;
- limited outer-unit count;
- missing external baseline;
- unresolved shift, subgroup, or downstream outcome;
- reliance on privileged training information;
- compute, latency, communication, or safety constraints.

Do not use Limitations as a second negative-results section. State each boundary once and connect it
to the next decisive experiment.

## Let the conclusion close the argument

Restate the confirmed contribution, why it matters, and the scope. Do not introduce new metrics,
future claims, or promotional superlatives. A conclusion should leave the reader with one accurate
sentence they can repeat.

## Design figures and tables around reader decisions

Every figure should answer one question:

- system diagram: what information flows at training and deployment;
- main result: whether the primary contrast passes;
- learning curve: how label efficiency changes across budgets;
- mechanism control: whether the suspected factor explains the effect;
- robustness plot: where the result persists or fails.

Use absolute axes, visible uncertainty, legible print-size text, and captions that state the unit,
direction, cohort, and key conclusion. Replace decorative illustrations when a result visualization
would resolve a likely reviewer objection.

## Make the prose sound authored

Prefer concrete subjects and verbs. Vary paragraph openings and sentence length. Use transitions
that express reasoning: “because,” “however,” “therefore,” “to distinguish these explanations,” and
“this matters when.”

Remove:

- generic enthusiasm and inflated adjectives;
- repetitive “we propose / we show / we demonstrate” chains;
- excessive parenthetical caveats;
- undefined acronyms and noun stacks;
- metric walls without interpretation;
- formulaic summaries at the end of every subsection.

Good scientific prose is not casual; it makes the chain of reasoning visible.

## Perform an independent manuscript review

When asked to review only the PDF, inspect only the PDF and judge the visible artifact. Do not use
hidden source, repository history, or remembered explanations to excuse what a reviewer cannot see.

Lead with a verdict, then evaluate:

1. novelty and importance;
2. technical correctness;
3. whether the experiment isolates the claimed mechanism;
4. statistical validity and evidence tier;
5. absolute and comparative performance;
6. external validity and robotics relevance;
7. reproducibility;
8. clarity, figures, and venue fit.

Separate fatal issues, likely reviewer objections, high-value fixes, and optional polish. Attach
each criticism to a page, table, figure, equation, or quoted claim.
