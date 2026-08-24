# PSF Research State

**Status date:** 2026-08-24  
**Canonical manuscript basis:** July 2026 revision  
**Purpose:** Machine- and human-readable current epistemic state of the Past-Selection Filtrations research program.

## 1. Research thesis

PSF models an observer's accessible past using increasing algebras of records. The July 2026 formulation separates the base record-filtration framework and its mathematical consequences from optional additional physical postulates concerning settled records and future-invariance. The base framework is not presently claimed to produce a failure of unitary quantum mechanics by itself.

## 2. Established framework/results — baseline

### C1 — Accessible-record filtration
**Status:** foundational construction  
**Confidence:** high that this accurately states the current framework  
Candidate past alternatives are represented through compatible record states on increasing accessible von Neumann algebras.

### C2 — Conditional expectations / expected lifts
**Status:** mathematical structure under additional hypotheses  
**Confidence:** high  
Faithful normal state-preserving conditional expectations provide expected lifts, equivariance structure, and martingale machinery where they exist. They are not themselves treated as physical outcome selection.

### C3 — Distinguishability / visibility structure
**Status:** proved results in current manuscript; requires independent continuing verification  
**Confidence:** high, provisional to red-team review  
The framework develops root-fidelity visibility bounds, monotonicity/data-processing consequences, trace-distance and Chernoff relations, fragmented-record bounds, and correlated-record bounds.

### C4 — AQFT distinction
**Status:** current formulation  
**Confidence:** high, subject to specialist review  
The manuscript distinguishes globally modular-invariant expected nests from half-sided modular inclusions; the latter need not provide vacuum-preserving expectations and may instead support restriction-based filtrations.

### C5 — Delayed-choice / future-operation structure
**Status:** mathematical results under stated assumptions plus constructive physical extension  
**Confidence:** medium-high  
Normalizer/equivariance results and finite-dimensional approximate bounds are mathematical claims. Any interpretation as physical settledness must remain separately labeled and must not be inferred merely from the algebraic result.

## 3. Novelty ledger — current assessment

| ID | Claim area | Confidence in substantive novelty | Closest known territory | Threat | What would settle it |
|---|---|---:|---|---|---|
| N1 | PSF synthesis: accessible past as increasing record-algebra structure with quantitative record/coherence analysis | Medium | redundant-record objective past; Quantum Darwinism/SBS; consistent histories; OAQEC/recoverable logical subalgebras; quantum filtrations/operator algebras | Medium-high | priority-aware theorem/definition comparison separating the temporal filtration + compatible record realization + quantitative visibility synthesis from older objective-past and algebraic-accessibility work |
| N2 | Specific visibility / record-access synthesis and bounds | Medium-high | fidelity monotonicity, distinguishability, Chernoff theory, redundant records; recent QEC–Darwinism tradeoffs | Medium | theorem-by-theorem comparison with prior literature, including Maity–Onggadinata–Koh 2026 |
| N3 | Delayed-choice equivariance / future-invariance formulation | Medium | normalizers, conditional expectations, quantum instruments, delayed-choice literature | Medium-high | targeted prior-art search plus assumption-level theorem comparison |
| N4 | AQFT expected-vs-restriction filtration treatment in PSF context | Medium | Takesaki theory, modular inclusions, AQFT | Medium-high | specialist literature audit |
| N5 | Distinctive physical prediction from optional additional postulates | Unestablished | interpretations of QM, decoherence, objective-collapse and modified-dynamics proposals | Critical/open | independently specify selector dynamics, calibration, physical filtration and a quantitatively predictive ordinary inverse-noise model; then test the predeclared echo law against held-out standard-unitary nulls |

**2026-08-10 narrowing of N1:** The broad ideas “objective past from redundant accessible records” and “classical/objective information as locally accessible/recoverable operator-algebraic substructure” are not defensible as standalone novelty claims. Riedel–Zurek–Zwolak (2013) is direct conceptual prior art for an objective past built from redundant records. Girard–Cheng–Cao (2026) gives a substantive OAQEC formulation of accessible/recoverable logical subalgebras and their centers, although it postdates the November 2025 PSF preprint and therefore does not by itself establish priority against PSF. The surviving candidate novelty is narrower: the particular ordered temporal record-filtration synthesis, compatible realization of past alternatives, and its quantitative visibility/access machinery. This remains unresolved rather than defeated.

Numerical percentages are intentionally avoided until enough independent audits exist to justify calibration.

## 4. Critical open problems

1. **Experimental discriminator.** A concrete conditional fork remains isolated for the optional selector law. With the manuscript definition `Σ=-log V` and selector overlap/echo law `ν_echo=exp(-ηΣ)`, the operational prediction is `ν_echo=V_pre^η` after an ideal inverse restores all ordinary non-selector branch degrees. Standard unitary QM and base PSF predict complete restoration under a genuinely global exact inverse. The empirical null is substantially stronger than a generic gate-error model. In a product-record model with `V_pre=|cos(theta)|^N`, an ordinary coherent inverse-amplitude mismatch leaving residual angle `epsilon theta` gives `ν_noise=|cos(epsilon theta)|^N`; in the weak-record regime this is locally equivalent to a selector law with apparent `eta≈epsilon^2`, and `N` cancels from the fitted exponent. The 2026-08-24 power analysis sharpens the consequence: for the adversarial locally matched null `epsilon=sqrt(eta)`, selector and null agree through quadratic order, `log ν_null-log ν_selector = N eta(1-eta)theta^4/12+O(theta^6)`, and for a binary X/parity readout the per-shot KL divergence is only `N eta(1-eta)^2 theta^6/288+O(theta^8)`. Thus weak-record testing is intrinsically information-poor against this null; merely adding more near-zero-angle points is not an efficient discriminator. Under an optimistic fixed-model normal approximation (one-sided alpha 0.05, 80% power, no nuisance uncertainty), the target-shot requirement behaves as `M≈890.29/[N eta(1-eta)^2 theta^6]`. Calibration is also stringent at small angle: a simple criterion that the 95% uncertainty in coherent mismatch be less than half the selector-null gap gives `sigma_epsilon/epsilon < (1-eta)theta^2/47.04` asymptotically. These are design scalings, not hardware forecasts. Pulse-inverse/KIK and context-aware coherent-error calibration literature provide concrete candidate control tools, but they do not eliminate leakage, drift, higher-order/time-ordering or non-Markovian systematics. Major blockers remain: complete selector dynamics, independent `η` calibration, a physically fixed filtration/record model, a platform-specific independently characterized forward/inverse noise model with uncertainty, and a held-out interaction-strength region that has enough discriminating curvature without introducing uncontrolled strong-coupling systematics.
2. **Prior-art audit.** Search older and terminology-diverse literature for constructions materially equivalent to the core record-filtration synthesis; include priority-aware comparison because some close 2026 algebraic work postdates the 2025 PSF preprint.
3. **Independent proof audit.** Re-derive central results without relying on manuscript prose; actively seek counterexamples and hidden assumptions.
4. **Physical meaning of state-preserving expectations / normalizer restrictions.** Determine how restrictive the mathematical hypotheses are in realistic physical models.
5. **Correlated records.** Clarify which product-record bounds survive correlations and whether stronger general results are possible. Recent exact QEC–Darwinism tradeoff work provides an adjacent benchmark but not yet a duplicate theorem.
6. **AQFT scope.** Verify exactly where expected filtrations exist and where only restriction filtrations are justified.
7. **Constructive extension.** Separate theorem, conjecture, optional postulate, and interpretation; test each additional axiom for consistency and empirical content.

## 5. Standing red-team questions

- Is PSF merely a redescription of decoherence, quantum trajectories, consistent histories, Quantum Darwinism, OAQEC, or causal/algebraic decoherence under unfamiliar terminology?
- Does any claimed theorem follow immediately from standard data processing, Takesaki theory, martingale convergence, or another known theorem such that novelty must be narrowed?
- Are conditional expectations being assigned physical meaning beyond what their mathematical role warrants?
- Does future-invariance become tautological after restricting the admissible operation class?
- Can a small finite-dimensional counterexample break any claimed monotonicity, equivariance, or interpretation?
- Does the framework produce any empirical content absent additional postulates?
- Can the proposed selector-echo residual be distinguished from ordinary circuit-depth/gate/decoherence error at matched physical control cost?
- Is the selector parameter `η` identifiable independently, or can it be fitted post hoc to any observed echo deficit?
- Can angle-dependent coherent inverse mismatch, gate-dependent noise, operator-growth-dependent noise sensitivity, or hidden records reproduce an apparent constant selector exponent over the experimental range?
- Is the nuisance-calibration measurement itself informative about the relevant coherent/incoherent error directions, or can a fixed readout basis be locally blind to the parameter being treated as calibrated?
- Does moving to stronger interaction strengths to gain statistical discrimination introduce leakage, nonlinear control, drift, non-Markovianity or record-model failure that erases the nominal information gain?

## 6. Epistemic rules

- **Proved**, **standard theorem**, **derived consequence**, **conjecture**, **interpretation**, and **optional physical postulate** are different statuses and must never be conflated.
- A literature similarity is not prior art until assumptions and conclusions are compared.
- Absence of discovered prior art is not proof of novelty.
- Failed attacks are recorded, not deleted.
- Negative results count as research progress.
- Any change to a novelty assessment must include the evidence and reason.
- For empirical novelty, compare against an explicit standard-dynamics null under the same controls; a residual that can be explained by incomplete reversal is not evidence for new physics.
- Matching only circuit depth or gate count is not enough when the same interaction parameter changes both record strength and the ordinary reversal-error channel; calibrate the forward/inverse operation itself and use native-structure-matched controls where feasible.
- Formal model separation is not enough for a useful experiment: quantify prospective discriminating information and nuisance-calibration uncertainty before selecting the test regime. A regime in which rival models agree to low order may require prohibitive samples even though they differ mathematically.

## 7. Current priority

**Highest-value target:** make the optional selector echo law operationally falsifiable against the strengthened standard-noise null by constructing a platform-specific prospective design. Independently identify or prospectively calibrate `η`; characterize the physical record states/filtration; use pulse-level/context-aware measurements to identify forward/inverse coherent and incoherent nuisance parameters with uncertainty; freeze the standard-noise prediction; then optimize held-out `(theta,N)` conditions for expected likelihood/KL separation subject to leakage, drift, nonlinear-control and non-Markovian constraints. Do not concentrate the experiment in the weak-record regime merely because the selector relation looks locally log-linear there.  
**Parallel target:** systematic, priority-aware prior-art and independent proof audit of the base framework, especially operator-algebraic record accessibility and quantitative redundancy/coherence tradeoffs.

## 8. Change protocol

Every agent run should read this file first, inspect the supporting ledgers, perform its work, and modify this state only when warranted. Material changes must also be entered in `decisions/DECISION_LOG.md`. Do not erase superseded conclusions; Git history and the decision log must preserve why they changed.
