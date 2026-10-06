# PSF Experiments Paper Pipeline

## Goal

Build a future standalone paper whose central contribution is a set of **experimentally actionable PSF tests**, not merely a discussion of interpretation.

A strong paper should ideally contain several physically distinct implementations so that the experimental program does not depend on one device architecture or one nuisance model.

## Minimum inclusion standard for a candidate

A candidate can enter the paper only when it has:

1. a concrete preparation → record formation → reversal/recoherence → readout protocol;
2. a mathematically explicit standard-QM/base-PSF prediction;
3. a mathematically explicit optional-selector prediction, if the experiment targets selector physics;
4. a predeclared physical filtration/record metric sufficient to define the tested quantity;
5. a complete-enough ordinary-null model for the actual platform;
6. independent calibration of nuisance directions used in the target prediction;
7. a held-out region/parameter set on which the competing predictions differ;
8. a statement of what positive, negative, and null results would mean;
9. an engineering feasibility argument grounded in demonstrated hardware capabilities;
10. no unresolved ordinary mimic large enough to absorb the proposed PSF signal.

## Desired paper portfolio

Target **3–6 mature experiments across at least 2–3 platform families**, for example:

- superconducting circuits with native conditional interactions and controlled reversal;
- circuit-QED / engineered-reservoir recoherence tests;
- trapped-ion or neutral-atom reversible-record experiments;
- photonic/interferometric record-erasure architectures;
- other platforms only when the full relevant environment can be sufficiently controlled.

These are portfolio categories, not claims that each is presently viable.

## Candidate progression

**L0 → L1:** write the explicit competing predictions.  
**L1 → L2:** adversarially enumerate ordinary mimics and hidden records.  
**L2 → L3:** map the abstract protocol to native hardware operations and known literature.  
**L3 → L4:** construct calibration-compatible target prediction bands and holdout tests.  
**L4 → L5:** produce a protocol detailed enough that an external experimental group could assess cost, controls, sequence, measurements, and falsification criteria without reverse-engineering the theory paper.

## Paper architecture when mature

1. Experimental question and theory-independent logic
2. Common definitions: record overlap, echo visibility, ordinary null, optional selector
3. Cross-platform design principles
4. Candidate experiment 1
5. Candidate experiment 2
6. Candidate experiment 3+
7. Calibration/identifiability framework
8. Shared failure modes and negative controls
9. Statistical decision rules
10. Interpretation of possible outcomes
11. Hardware requirements / collaboration opportunities

## Important boundary

A technically impressive decoherence, irreversibility, redundancy, or recoherence experiment is not automatically a PSF test. It becomes a PSF discriminator only when the ordinary calibration-compatible family and the optional PSF prediction make prospectively separable target predictions.