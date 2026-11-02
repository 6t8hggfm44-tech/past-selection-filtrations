# Experimental Tests of the Accessible Quantum Past: Recoherence, Record Information, and Identifiability

**Peter James Bavaro**  
**Working draft 0.1 — November 2, 2026 — NOT submitted, approved, or published**

> **Editorial status.** This is an independent, deliberately provisional *second-paper* draft, not a revision or addendum to the author-approved PSF manuscript 9.0.2. Theoretical bounds and hardware claims require independent proof and source checks before submission. This file contains no private correspondence or unpublished governance material. Future editing and Overleaf conversion are deferred.

## Abstract

Reversible quantum interactions can imprint distinguishable records of alternative system histories into environmental degrees of freedom. Under an exact inverse of the complete unitary evolution, standard quantum mechanics restores the original coherence, whereas incomplete reversal, uncontrolled spectators, non-Markovian memory, leakage, and conditional postselection can all produce apparent residual decoherence. We develop an experimental-design framework for distinguishing ordinary recoherence limitations from a conditional, optional record-selection hypothesis associated with Past-Selection Filtrations (PSF). In the phenomenological selector model, an independently specified pre-inverse branch visibility V_pre and fixed selector parameter η give a residual echo law ν_echo=V_pre^η. This is **not** a prediction of the base record-filtration mathematics, nor is the selector empirically established. We organize experimental controls around calibrated *sets* of compatible ordinary channels and processes, pathwise branch-distinguishability certificates, phase-sensitive nuisance calibration, and held-out model discrimination. Exact finite-dimensional countermodels show how coherent inverse mismatch, transient records in logically equivalent compilations, spectator coupling, rotating conditional axes, and heralded filtering can imitate or contaminate the proposed signature. We outline several candidate hardware implementations, ranking their readiness and identifying measurements required before any claim of anomalous record persistence is warranted. The contribution is a falsifiable protocol and an adversarial experimental agenda, not a report of new-physics detection.

## 1. Introduction

Quantum Darwinism and decoherent-histories approaches describe how environmental records can make alternatives accessible and apparently classical. Yet records produced by unitary interactions need not be permanently settled: an ideal inverse acting on all relevant degrees of freedom can erase which-branch information and restore interference. The operational question is not whether ordinary decoherence occurs, but whether a controlled record-creation-and-reversal experiment can prospectively distinguish a specified additional physical law from the entire experimentally compatible family of ordinary quantum processes.

The Accessible Quantum Past [1] formulates accessible records through increasing operator algebras, derives coherence/visibility results under explicit assumptions, and distinguishes that base construction from optional stronger physical hypotheses. Its Section 8 gives a complete local-channel target set in a *declared restricted model*, not unrestricted device tomography; Section 10 specifies an ordinary registration interaction with fresh/reused memory. We take these results as motivation and scope constraints, not as evidence that the selector exists.

The present paper's independent aim is experimental: to identify what an external laboratory must calibrate, predeclare, and measure to make a record-selection test interpretable. The primary null is ordinary quantum dynamics, including incomplete reversal and calibrated open-system effects. We explicitly retain conventional models consistent with the calibration data, rather than selecting one convenient noise fit.

## 2. Operational hypothesis and the competing null

### 2.1 Branch records and visibility

Consider a system qubit S initially in |+> and an environment E in |e>. A controlled unitary creates

|Ψ_pre> = (|0>|e_0> + |1>|e_1>)/sqrt(2),

with branch visibility V_pre = |<e_0|e_1>|. The record action is Σ_pre = −log V_pre where V_pre>0. For independent fragments with overlaps v_k, V_pre = product_k v_k; this factorization is **not** assumed for correlated environments.

If U_write is exactly reversed globally, U_write† U_write = I and the initial system coherence returns to one. Base PSF does not modify this prediction.

### 2.2 Optional selector fork

For an additional, explicitly *hypothetical* selector with a stored pre-inverse record action, a conditional echo model is

ν_selector = exp(−η Σ_pre) = V_pre^η,

where η must be fixed independently or on predeclared calibration conditions. The physical meaning of the stored action, whether transient intermediate records contribute, and the complete selector dynamics remain unresolved. No Born-rule derivation, no-signalling completion, or empirical observation is claimed here. An experiment cannot estimate η solely from the same held-out echo it purports to predict.

### 2.3 Complete ordinary prediction family

Let D_cal denote independently collected calibration outcomes and M_cal the family of standard-QM channels/processes compatible with them at a declared uncertainty level. The ordinary held-out target set is

C_QM(x | D_cal) = { predicted echo distribution at target setting x from M : M in M_cal }.

The experimentally relevant discriminator is separation between the predeclared selector distribution and the *whole* C_QM, not merely a point estimate of a fitted noise model. Section 8 of [1] solves one restricted environment-local CPTP-slot example; leakage, joint errors, correlated initial states, context drift, and multi-time memory generally require larger models. A violation of a restricted certificate alone does not falsify standard quantum mechanics.

## 3. Why straightforward echo deficits are inconclusive

### 3.1 Coherent inverse mismatch

For N product-record fragments with V_pre=|cos θ|^N, an ordinary coherent inverse-angle residual εθ produces

ν_noise = |cos(εθ)|^N.

At weak interaction, log ν_noise/log V_pre approaches ε². Thus a fixed ordinary calibration mismatch can imitate a selector exponent η≈ε², and increasing N does not remove this degeneracy. The first distinguishing curvature is weak; the earlier idealized binary-readout analysis found information scaling as θ^6 against a locally matched nuisance model [internal dossier A]. This is a design warning, not a hardware shot forecast.

### 3.2 A logically no-record gate can write transient records

A symmetric conditional ZX interaction has a common-eigenstate calibration preparation that is record-null at the effective endpoint. But its exact H–CNOT–Rz–CNOT–H compilation can temporarily make the environment branch states orthogonal and subsequently uncompute them. The endpoint gate identity does not certify trajectory-wide record absence [internal dossier B]. Whether the optional selector responds to such transient records must be specified, not silently inferred.

### 3.3 Spectators, common drift, and conditional-axis motion

A nominally direct ZX interaction can still imprint branch information on spectators. In a simple commuting spectator model the hidden action begins as g²t² Var(B)/2. Even without spectators, a common Hamiltonian that fails to preserve the conditional-generator eigenspace can create records. For H_±(t)=H_0(t)±B(t)/2 and initial pure P_0, an exact pathwise no-record condition in the declared closed finite-dimensional model is

[U_0(t)† B(t) U_0(t), P_0] = 0 for every t.

A rotating interaction-picture conditional axis generally defeats an initially aligned state [internal dossiers C–E]. These are conventional unitary mechanisms, not selector effects.

### 3.4 Approximate no-record controls

Define B_I(t)=U_0(t)†B(t)U_0(t), δ(t)=sqrt(Var_ψ0 B_I(t)), and J(t)=integral_0^t δ(s)ds. For the declared closed pure-state branch model, the projective-geometric bound

arccos V(t) ≤ J(t)

gives V(t)≥cos J(t) when J(t)<π/2. A related complex-reference bound constrains Ramsey-phase bias using cosh J−1 [internal dossiers F–G]. Both must be rechecked against established geometric speed-limit/perturbation results before independent novelty is claimed. Neither is a certificate for unmodeled device degrees.

### 3.5 Heralding and postselection

Conditional success-only statistics can look nonlinear despite linear underlying dynamics. A two-qubit heralded-filter countermodel reproduces the optional echo's low-order weak-angle expansion for a tuned ordinary filter, while its complete success/failure distribution remains an observable conventional explanation [internal dossier H]. Experiments must report *all* heralding outcomes and model the filter's complex response. Successful-subensemble visibility alone cannot establish the selector.

## 4. Proposed experimental protocol

**Stage A — physical specification.** Predeclare the system, record fragments, accessible algebra/filtration, environmental preparation, write pulse, attempted inverse, full timing, measured observables, and any selector-stage rule. Distinguish a genuine global inverse from a logical inverse or a naturally occurring revival.

**Stage B — mechanism-null and nuisance controls.** Prepare a common-eigenstate/near-blind calibration arm where possible, but audit the complete scheduled pulse trajectory and hidden modes. Reconstruct or bound the conditional Hamiltonian in the common interaction frame. Use complementary Ramsey quadratures and context-matched coherent/incoherent calibration; independently characterize leakage, spectator effects, retained memory, and heralding.

**Stage C — compatible-set inference.** Construct a calibration uncertainty set of ordinary processes. Propagate all members to held-out target predictions, including model expansion when calibration fails. Predeclare confidence coverage and how drift, model mismatch, and empty feasible sets will be handled.

**Stage D — frozen predictions and holdout.** Freeze the ordinary set, selector parameter, physical filtration, target settings, analysis code, and decision threshold before examining held-out data. Use multiple record strengths, fragment numbers, or reversal rounds only where calibration certifies comparable physical contexts.

**Stage E — interpretation.** A result inside the ordinary prediction band is inconclusive for selector physics. A result outside a restricted band first motivates an expanded ordinary model and independent replication. A persistent, independently reproduced discrepancy against a well-supported ordinary family could motivate further tests of additional physics, but does not uniquely identify the PSF selector.

## 5. Candidate hardware implementations

| ID | Platform and concept | Current research maturity | Decisive missing capability |
|---|---|---|---|
| EXP-2026-001 | Superconducting native conditional-record echo with Ramsey control | L3, lead design | Scheduled-pulse, device-wide compatible ordinary prediction certificate |
| EXP-2026-002 | Tunable-coupler conditional echo | L2 | Trajectory-wide hidden-record bound, not just gate fidelity |
| EXP-2026-003 | Circuit-QED cat plus engineered reservoir | L1 | Controlled global inverse beyond spontaneous recoherence |
| EXP-2026-004 | High-control reversible-measurement / distributed-record scaling | L1 | Explicit scalable record and selector-sensitive holdout |
| EXP-2026-005 | Quantum-Darwinism redundant-record circuit plus inverse | L2 | PSF-grade inverse and nuisance calibration |
| EXP-2026-006 | Mesoscopic nanoparticle pointer reversal | L1 | PSF-specific action, noise certificate and hardware feasibility |

These maturity labels reflect the project registry, not external laboratory endorsements. The manuscript should not claim that any current platform is ready to demonstrate new PSF physics.

## 6. Statistical decision design

Let p_QM(y|x,M) be the held-out readout distribution for ordinary model M in the calibration-compatible family, and p_sel(y|x,η) the selector prediction. Experimental design should maximize *worst-case prospective distinguishability*, for example

inf_{M in M_cal} D_KL[p_sel(·|x,η) || p_QM(·|x,M)],

subject to calibration coverage, bounded hidden records, leakage, stability, and feasible preparation/readout. A nominally high-information strong interaction can activate unmodeled noise and become less informative in practice. Any quoted power or sample size must include uncertainty in M_cal and η and must be checked for robustness to misspecification.

A full protocol should specify preregistered primary/secondary observables, data-exclusion rules, success/failure denominators, systematic-error sensitivity, multiple-testing treatment, and replication criteria. No final device-specific power calculation is currently justified.

## 7. Relation to prior literature and novelty

Redundant records of histories and objective-past ideas precede PSF [2–4]. Quantum Darwinism and decoherent histories supply substantial physical context, while more recent work relates redundant past records to history consistency [5]. Standard Loschmidt/Boltzmann echo theory and measurement-reversal demonstrations already show that residual decoherence can arise from incomplete inversion [6–8]. Quantum computing calibration, pulse-inverse methods, and time-dependent Hamiltonian tomography provide practical nuisance-characterization tools [9–12]. The specific contribution sought here is a *cross-platform, adversarially calibrated experimental-discriminator framework* that preserves all justified ordinary alternatives. This is a candidate synthesis requiring further priority review, not an established claim of mathematical or physical firstness.

## 8. Limitations and outstanding questions

The selector is phenomenological and incomplete; the physical stage/path rule for Σ is unsettled. No proposed experiment yet has a complete device-level target-prediction identifiability certificate. The geometric and complex-reference bounds need independent literature/proof audit. Existing platforms demonstrate pieces of the required control stack but not a validated PSF-specific test. Correlated records, unknown hidden modes, non-Markovian noise, calibration-transfer failure, and selective reporting can all defeat naive inference. A null result can constrain only the specified selector family and parameter range, not every conceivable extension of PSF.

## 9. Conclusion

An interpretable test of record-selection physics requires more than observing decoherence or failure of spontaneous revival. It requires a prospective, physically matched comparison between an explicit optional selector model and the entire experimentally supported ordinary-quantum prediction family. Existing countermodels and control tools make this agenda concrete but also show why a residual echo alone is not compelling evidence. The next milestone is one complete, independently audited, device-specific protocol. Until then, this paper remains a working experimental-methodology proposal rather than a claim of observed new physics.

## References — working list, verify bibliography before submission

[1] P. J. Bavaro, *The Accessible Quantum Past: Record Information, Coherence Bounds, and Echo Tests*, manuscript 9.0.2 (2026). https://doi.org/10.5281/zenodo.22647510

[2] C. J. Riedel, W. H. Zurek, and M. Zwolak, *The Objective Past of a Quantum Universe: Redundant Records of Consistent Histories* (2013). https://arxiv.org/abs/1312.0331

[3] J. J. Halliwell, *Somewhere in the Universe: Where Is the Information Stored When Histories Decohere?* (1999). Bibliographic details to verify against ledger L-2026-032.

[4] W. H. Zurek, foundational Quantum Darwinism literature. Specific citation(s) to select in bibliographic review.

[5] P. Strasberg, *Redundant Records of the Past: Unifying Quantum Darwinism and Decoherent Histories* (2026). https://arxiv.org/abs/2610.09845

[6] C. Petitjean and P. Jacquod, Boltzmann-echo work (2006). Full bibliographic details to verify against L-2026-033.

[7] M. Schindler et al., *Undoing a Quantum Measurement* (2012). https://arxiv.org/abs/1211.1791

[8] J. Zheng et al., *Emergence of irreversible decoherence from unitary dynamics* (2025/2026). https://arxiv.org/abs/2510.15730

[9] H. Henao, J. Santos, and R. Uzdin, pulse-based inverse evolution (2023). https://arxiv.org/abs/2303.05001

[10] T. Rudinger et al., robust phase-estimation coherent gate calibration (2025). Bibliographic details to verify against PSF ledger.

[11] Siva et al., *Time-Dependent Hamiltonian Reconstruction Using Continuous Weak Measurements* (2023). https://doi.org/10.1103/PRXQuantum.4.040324

[12] Carignan-Dugas et al., *The Error Reconstruction and Compiled Calibration of Quantum Computing Cycles* (2023). https://arxiv.org/abs/2303.17714

**Internal evidence trail (not manuscript citations):** \`experiments/ECHO_DISCRIMINATOR.md\`; \`ECHO_NOISE_IDENTIFIABILITY_2026-08-17.md\`; \`ECHO_POWER_CALIBRATION_2026-08-24.md\`; \`COMPILED_PATH_RECORD_AUDIT_2026-09-07.md\`; \`NATIVE_SPECTATOR_HIDDEN_RECORD_BUDGET_2026-09-21.md\`; \`COMMON_DRIFT_COMMUTATOR_NULL_2026-09-28.md\`; \`CROSS_RESONANCE_PAULI_NULL_DIAGNOSTIC_2026-10-05.md\`; \`TIME_DEPENDENT_CONDITIONAL_AXIS_NULL_2026-10-12.md\`; \`TRANSVERSE_ACTION_PATHWISE_BOUND_2026-10-19.md\`; \`COMPLEX_PHASE_REFERENCE_CERTIFICATE_2026-10-26.md\`; \`HERALDED_FILTER_ECHO_MIMIC_2026-11-02.md\`; \`experimental-database/REGISTRY.md\`.

## Development checklist

- [ ] Independently audit all displayed formulas and hypotheses.
- [ ] Complete the prior-art/bibliography pass, including older decoherence and quantum-control sources.
- [ ] Choose one device and reconstruct a time-resolved Hamiltonian with calibration uncertainty.
- [ ] Specify the selector path/stage rule or explicitly present multiple alternatives.
- [ ] Build a device-wide ordinary compatible-process target set and frozen holdout.
- [ ] Turn one candidate into a laboratory-ready protocol with full success/failure accounting.
- [ ] Prepare figures, data/code availability statements, and a journal-specific LaTeX version.
- [ ] Obtain author approval before external circulation, Overleaf transfer, or submission.
