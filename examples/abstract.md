# Example: revise only the abstract

All inputs are fictional, provided for demonstration.

## Request and inputs

Rewrite the following two-sentence abstract using only the supplied evidence. Do not propose runs.

Draft: “Our robot controller generalizes universally. It improves everything through a novel latent model.”

`evaluation`, table 2: on 16 paired simulation seeds from one benchmark, the proposed controller
reduces final position error by 12% relative to a matched baseline; the reported interval is
[4%, 19%]. No hardware or distribution-shift experiment was performed.

## Expected response

“Our robot controller reduces final position error by 12% relative to a matched baseline on one
simulation benchmark across 16 paired seeds (reported interval: 4–19%). This result supports
improved control within the evaluated simulation setting.”

Evidence: `evaluation`, table 2. The edit removes unsupported universal generalization without
turning a localized rewrite into a research plan.

## Why

The abstract leads with the supported result, keeps its units and scope, and does not introduce
extra claims or require a new experiment before completing the requested edit.
