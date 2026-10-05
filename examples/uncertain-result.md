# Example: interpret an uncertain paired result

The aggregate below is synthetic and supplied as an already computed artifact.

## Request and inputs

Can the paper claim improvement on its registered endpoint?

`run-R1`, table 1: twelve independent paired training seeds; method minus baseline success rate
is +2 percentage points, with a registered 95% interval of [-1, +5] percentage points. No
noninferiority or equivalence margin was registered. There are 100 episodes within each seed.

## Expected response

Directional improvement is unresolved: +2 percentage points, 95% interval [-1, +5], across 12 paired
training seeds (`run-R1`, table 1). The result establishes neither superiority nor equivalence.
The episodes do not increase the number of independent training seeds. Report this result without
changing the endpoint or rerunning toward a favorable outcome.

## Why

The interval includes the relevant null, and no equivalence analysis supports an equality claim.
The conclusion preserves the stated independent unit and the original prospective question.
