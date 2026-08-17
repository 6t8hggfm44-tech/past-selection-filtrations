# Red-Team Log

The red team is rewarded for finding errors, prior art, hidden assumptions, overclaims, and empirical indistinguishability—not for defending PSF.

## Attack template

### RT-YYYY-NNN — Attack title
- **Target claim:**
- **Attack:**
- **Method:** literature / derivation / finite-dimensional counterexample / numerical test / conceptual analysis
- **Result:** survives / weakened / fails / unresolved
- **Evidence:**
- **Required change:**
- **Next attack:**

## Initial attacks queued

### RT-2026-001 — Redescription challenge
**Target:** novelty and physical significance of base PSF framework.  
**Attack:** Attempt to reconstruct the framework entirely from standard decoherence + noncommutative filtration/data-processing machinery and identify what, if anything, remains distinct.  
**Status:** in progress.  
**2026-08-10 result:** Broad novelty language must be narrowed. Riedel–Zurek–Zwolak (2013) already ties an “objective past” to redundant locally accessible records of consistent histories. Girard–Cheng–Cao (2026) formulates classical/objective information through locally recoverable logical von Neumann subalgebras and their centers. Neither source found so far duplicates PSF's full ordered temporal record-filtration + compatible record-realization + visibility synthesis, and the 2026 OAQEC paper postdates PSF's November 2025 preprint.  
**Required change:** Do not claim novelty for “objective past from records” or operator-algebraic accessibility alone; keep novelty theorem/architecture-specific and priority-aware.  
**Next attack:** Search pre-2025 quantum probability/OAQEC/causal-decoherence literature for an increasing temporal algebra of records materially equivalent to PSF.

### RT-2026-002 — Delayed-choice assumption challenge
**Target:** delayed-choice/future-operation claims.  
**Attack:** Determine whether the normalizer/state-preservation assumptions make the invariance result effectively automatic or physically too restrictive.  
**Status:** queued.

### RT-2026-003 — AQFT expectation challenge
**Target:** relativistic generalization.  
**Attack:** Verify all existence claims for conditional expectations and distinguish them from half-sided modular inclusion/restriction results.  
**Status:** queued.

### RT-2026-004 — Empirical-null challenge
**Target:** constructive physical extension / N5.  
**Attack:** Assume ordinary unitary QM and environmental decoherence; attempt to reproduce every proposed observable effect. Any effect that survives becomes a candidate discriminator.  
**Method:** literature comparison + explicit reversible-record toy model + algebraic derivation.  
**Result:** weakened / conditional discriminator isolated.  
**Evidence:** Standard unitary models can create redundant records and later erase or recohere them; redundancy can also decay under many-body dynamics. Controlled experiments/theory already demonstrate unitary branching and measurement/recovery reversibility. In a minimal fanout record model, an initial system `|+>` and `n` environment `|0>` qubits evolve to a GHZ-like record state under CNOT fanout; the exact inverse restores system `X` visibility to 1 for every `n`. A finite-dimensional numerical sanity check for `n=1..4` reproduced this exactly. If an extra branch-coherence factor `κ` is inserted after record formation and left untouched by the inverse, the recovered system state is `1/2[[1,κ],[κ,1]]` and `<X>=κ`; this merely verifies how an independently specified residual overlap would appear in the echo observable—it is not a derivation of PSF physics.  
**PSF fork:** In the optional selector law, `Σ=-log V` and `ν_echo=exp(-ηΣ)`, hence `ν_echo=V_pre^η`. The base framework and standard unitary QM instead give a complete ideal echo under a genuinely global inverse.  
**Required change:** Treat `V_pre^η` as a prediction only of the optional selector postulate. Any experimental claim must independently fix `η`, the physical filtration/record states, and the ordinary inverse-noise model before examining target echo data. A residual visibility deficit that scales only with circuit depth, gate error, leakage, or uncontrolled records is not discriminating evidence.  
**Next attack:** Build matched-depth/matched-noise protocols in which `V_pre` changes while ordinary physical error budget is held fixed, and derive statistical identifiability against standard decoherence/error models.

### RT-2026-005 — Selector-parameter identifiability challenge
**Target:** optional selector law `ν_echo=V_pre^η`.  
**Attack:** Ask whether `η` is genuinely predictive or can be fitted post hoc to an observed residual.  
**Method:** algebraic identifiability analysis.  
**Result:** weakened / unresolved operationally.  
**Evidence:** For any single nontrivial pair `(0<V_pre<1, 0<ν_echo<1)`, one can choose `η = log(ν_echo)/log(V_pre)`. Therefore one echo datum cannot test the law if `η` is fit from that datum. Multiple experiments with a common predeclared `η` predict a straight-line relation `log ν_echo = η log V_pre`; this becomes falsifiable only when `η` is calibrated independently or fixed on a calibration set and tested prospectively on held-out conditions.  
**Required change:** Supply an explicit independent calibration protocol or a prospective calibration/holdout design consistent with the manuscript's requirement that one common `η` be fixed before the echo test.  
**Next attack:** Determine whether a physically distinct calibration experiment can identify `η` without already assuming the selector echo effect, and test whether ordinary hardware error can generate the same log-linear relation.

### RT-2026-006 — Coherent inverse-amplitude mimic
**Target:** empirical identifiability of `ν_echo=V_pre^η` after introducing matched-depth controls.  
**Attack:** Construct a standard-unitary incomplete-inverse model in which the same physical parameter that changes record strength also changes reversal error, and test whether it generates an apparent selector exponent.  
**Method:** analytic product-record derivation + Wolfram series/numerical checks + mirror-benchmarking literature comparison.  
**Result:** weakened / a stronger null is required.  
**Evidence:** Let the designated per-fragment record overlap be `v(theta)=|cos(theta)|`, so `V_pre=|cos(theta)|^N`. If the ordinary attempted inverse leaves a coherent residual conditional angle `epsilon theta` per fragment, then standard unitary QM gives `ν_noise=|cos(epsilon theta)|^N`. Fitting this ordinary residual to a selector power law gives `eta_eff=log|cos(epsilon theta)|/log|cos(theta)|`; `N` cancels exactly. Wolfram gives `eta_eff = epsilon^2 + epsilon^2(epsilon^2-1) theta^2/6 + O(theta^4)`. Hence in the weak-record regime an ordinary coherent inverse-amplitude mismatch locally reproduces the selector form with apparent `eta≈epsilon^2`, and increasing record redundancy alone does not break the degeneracy. Mirror-benchmarking theory independently shows that inverse-circuit survival depends on the forward/inverse error-channel relation, while verifiable benchmark-circuit work motivates controls matched to native-gate structure/noise profile rather than gate count alone. See `experiments/ECHO_NOISE_IDENTIFIABILITY_2026-08-17.md`.  
**Required change:** Treat fixed depth/gate count as insufficient. Independently characterize angle-dependent forward/inverse calibration before target data; use pulse/native-structure-matched controls; propagate a predeclared ordinary-noise prediction band; and sweep interaction strength broadly enough that held-out data can resolve higher-order curvature or other model-specific differences.  
**Next attack:** Derive power/sample-size requirements for distinguishing a constant selector exponent from an independently calibrated `epsilon(theta)` null under realistic uncertainty, and search for a control construction with identical native pulses but no designated record formation.
