# No-record Ramsey control for a superconducting selector-echo test

**Date:** 2026-08-31  
**Status:** prospective design increment for optional selector physics; not a prediction of base PSF  
**Primary problem:** P1 experimental discriminator

## Question

Can the leading coherent inverse-amplitude nuisance `epsilon` be calibrated with a control that uses the same record-interaction pulse family but does **not** itself create a distinguishable record, so that the calibration channel is not automatically contaminated by the optional selector effect it is supposed to test?

## Platform anchor

Zhu et al. (2025) experimentally realize tunable conditional system-environment interactions on a superconducting processor, using up to ten environment qubits. Their conditional gates are compiled into CZ gates and single-qubit rotations; the reported processor has approximately `T1 ~ 130 microseconds`, single-qubit fidelity around `0.9997`, and two-qubit CZ fidelity around `0.998`. This is a concrete architecture in which a PSF-style controlled record-formation / inverse experiment is at least structurally implementable.

The present note does **not** assert that Zhu et al.'s exact randomized conditional gate already supplies the control below. Instead, it isolates a symmetric conditional-rotation subfamily that can be compiled from the same class of controls and has an analytically useful common-eigenstate null.

## Symmetric record gate

For one environment qubit, define the ideal conditional interaction

`U(theta) = |0><0|_S \otimes R_x(+theta) + |1><1|_S \otimes R_x(-theta)`,

with

`R_x(a)=exp(-i a X/2)`.

Prepare the system in `|+>`.

### Record-forming input

Prepare the environment qubit in `|0_z>`. The two conditional environment branch states are

`|e_0> = R_x(+theta)|0>` and `|e_1> = R_x(-theta)|0>`.

Their overlap is

`<e_0|e_1> = cos(theta)`.

For `N` independent fragments prepared identically,

`V_pre(theta,N)=|cos(theta)|^N`,

matching the product-record specialization used in the existing echo identifiability analysis.

### Mechanism-null / no-record input

Instead prepare each environment qubit in the common generator eigenstate `|+_x>`.

Then

`R_x(+theta)|+_x> = exp(-i theta/2)|+_x>`,

`R_x(-theta)|+_x> = exp(+i theta/2)|+_x>`.

The environment states are identical up to phase, so the branch-overlap magnitude is exactly one:

`|<e_0|e_1>| = 1`.

Thus this control uses the same conditional interaction amplitude and pulse family but, ideally, creates no distinguishable environmental record. Under the optional selector law with `Sigma=-log V`, this control has `Sigma=0` and therefore no selector suppression.

This is the key design feature: the hypothesized mechanism is nulled while the coherent control error remains observable.

## Coherent inverse-amplitude mismatch

Use the same ordinary null as RT-2026-006. Suppose the attempted pulse inverse leaves a fractional residual conditional rotation `epsilon theta`. For the record-forming `|0_z>` input, the standard-unitary residual branch overlap is

`nu_null(theta,N)=|cos(epsilon theta)|^N`.

This is exactly the nuisance that locally mimics the selector law with apparent `eta approximately epsilon^2`.

For the no-record `|+_x>` input, however, the same residual produces only branch-dependent phases:

`<e_0^res|e_1^res> = exp(i epsilon theta)`

per fragment, and therefore

`C_no-record = exp(i N epsilon theta)`

for `N` fragments in the ideal factorized model.

The control therefore converts the nuisance from a hard-to-separate **visibility loss** into a coherent **Ramsey phase** that can be estimated independently from the record-forming echo.

## Wolfram verification

A direct symbolic matrix check on 2026-08-31 gave:

- record-forming branch overlap: `cos(theta)`;
- record-forming residual overlap: `cos(epsilon theta)`;
- no-record branch overlap: `exp(i theta)`, modulus `1`;
- no-record residual overlap: `exp(i epsilon theta)`, modulus `1`.

These are exact for the ideal one-fragment symmetric model.

## Calibration Fisher information

Read out the system Ramsey phase after the no-record sequence. With a `Y`-quadrature binary measurement chosen so

`p_+(epsilon) = [1 + sin(N epsilon theta)]/2`,

the classical Fisher information per shot is exactly

`I_epsilon = N^2 theta^2`

where the chosen quadrature is nonsingular. (`X` and `Y` measurements, or robust phase-estimation schedules, can be combined to avoid phase-wrap / blind-point problems.)

Therefore an ideal Cramer-Rao calibration bound is

`Var(epsilon_hat) >= 1/(M_cal N^2 theta^2)`.

The previous power note required, in the weak-angle matched-null analysis,

`sigma_epsilon/epsilon < (1-eta) theta^2 / 47.04`

if the 95% calibration half-width is to be below half the selector-null gap. At the hardest local match `epsilon=sqrt(eta)`, the no-record Ramsey control would require approximately

`M_cal > 47.04^2 / [eta (1-eta)^2 N^2 theta^6]`

or

`M_cal > 2212.7616 / [eta (1-eta)^2 N^2 theta^6]`.

For comparison, the optimistic target-shot requirement from the previous binary-echo calculation was

`M_target approximately 890.29 / [N eta (1-eta)^2 theta^6]`.

Their idealized ratio is therefore

`M_cal/M_target approximately 2.48544/N`.

Illustrative values at `eta=0.05`, `theta=1.0`:

- `N=4`: `M_cal ~3065`, `M_target ~4932`;
- `N=8`: `M_cal ~766`, `M_target ~2466`;
- `N=10`: `M_cal ~490`, `M_target ~1973`.

These are not hardware forecasts. They show only that, in the symmetric ideal model, coherent mismatch need not be intrinsically calibration-dominant if it can be mapped into a high-information no-record phase channel.

## Why this is scientifically useful

The prior red-team result showed that a coherent inverse mismatch can masquerade as the selector exponent and that weak-record target data are information-starved. The present construction gives a candidate way to estimate that nuisance without using the target echo itself and without generating the designated record that the optional selector law responds to.

This is stronger than a same-depth control: it attempts to preserve the native mechanism-bearing pulse exposure while changing only the environment preparation so that the record overlap has unit modulus.

It also supplies an explicit example of the general calibration principle suggested by Pan et al. (2026): a nuisance that is poorly identified in one measurement basis can become well-conditioned after a deliberate measurement/control redesign.

Rudinger et al. (2025) independently demonstrate that robust phase estimation can give Heisenberg-limited high-precision estimates of coherent errors in entangling gates on superconducting hardware. That literature does not prove the PSF control works, but it makes phase-amplified coherent calibration a realistic experimental primitive rather than a purely formal device.

## Adversarial limitations

This control resolves only one important nuisance direction in an idealized gate family.

1. **Common-eigenstate requirement.** Zhu et al.'s randomized `U^0_k,U^1_k` rotations need not share a common eigenstate. The experimental PSF gate should therefore use a deliberately symmetric conditional subfamily if this control is adopted. This is a design restriction, not yet a demonstrated hardware implementation.

2. **Compilation/context dependence.** A logical symmetric gate compiled into CZ plus one-qubit rotations may have different leakage, spectator coupling, Stark shifts or crosstalk for `|0_z>` and `|+_x>` environment preparations. Same logical gate does not guarantee same physical nuisance channel.

3. **Stochastic and incoherent errors.** The Ramsey phase isolates coherent mismatch efficiently but does not by itself determine T1/T2 loss, Pauli stochastic errors, leakage, spectator entanglement, measurement error, drift or non-Markovian memory.

4. **Correlated fragments.** The `N^2 theta^2` Fisher scaling assumes a coherent common residual phase and factorized control structure. Independent per-fragment random errors, crosstalk or correlated noise can change the scaling and invalidate the simple product null.

5. **Hidden records.** `V=1` is true for the designated environment degrees in the ideal model. A physical implementation must still verify that control electronics, spectator qubits, leaked levels, resonators or other accessible degrees do not carry branch-distinguishing records that would make `Sigma` nonzero under the chosen physical filtration.

6. **Selector-model dependence.** The claim that the no-record control is selector-free uses the present optional law's dependence on `Sigma=-log V`. A later complete selector dynamics could couple to other features of the control and would require re-analysis.

7. **Phase wrapping / readout blindness.** A single fixed Ramsey quadrature can become blind at special phases. Use both quadratures and/or robust phase estimation, and predeclare a phase-unwrapping schedule.

## Prospective superconducting protocol

### Stage A — choose the record gate
Use a symmetric conditional-rotation family with a known common generator eigenstate. Compile it using the same native CZ + one-qubit control stack used for record formation.

### Stage B — coherent-mismatch calibration with mechanism nulled
Prepare the system in `|+>` and each environment qubit in the common eigenstate (`|+_x>` in the toy model). Execute forward plus pulse inverse. Measure system `X` and `Y` over a predeclared grid of `(theta,N)` and fit the common coherent residual `epsilon(theta)` before any record-forming target data are examined.

Use robust phase-estimation / error-amplification techniques where appropriate to obtain a confidence region for the coherent nuisance model.

### Stage C — independent incoherent/leakage calibration
Use context-aware fidelity estimation, echoed leakage amplification, cycle-error reconstruction / cycle benchmarking, leakage-sensitive readout and native-structure-matched controls to estimate stochastic, leakage and context-dependent error terms with uncertainty.

### Stage D — validate factorization / correlations
Check whether the inferred coherent phase is consistent across fragment identity, fragment count and scheduling. A significant `N`- or context-dependent residual outside the predeclared model is evidence that the simple factorized null is inadequate and must be expanded **before** target data.

### Stage E — freeze the standard null
Combine Stages B-D into a predictive ordinary-noise distribution for held-out record-forming conditions. Freeze model form, nuisance posteriors/confidence regions and exclusion criteria.

### Stage F — held-out record-forming echo
Switch only the environment preparation to the record-forming state (`|0_z>` in the toy model), create `V_pre<1`, apply the characterized pulse inverse, and measure the echo. Compare with the frozen standard-noise prediction and the separately predeclared selector prediction.

## Predeclared failure tests

The proposed control should be rejected or revised if any of the following occur before target unblinding:

- no-record echo magnitude shows unexplained systematic decay with `theta` or `N` beyond the calibrated ordinary-noise model;
- inferred `epsilon(theta)` differs materially across fragment identities or `N` in a way not captured by the frozen null;
- leakage/spectator signatures depend strongly on the record-forming versus no-record environment preparation;
- the common-eigenstate preparation itself produces hidden branch information in the physical implementation;
- calibration uncertainty propagated to the record-forming echo remains comparable to or larger than the selector-null separation in the held-out region.

A target residual that falls inside the frozen standard-noise band is not evidence for selector physics.

## Literature used in this increment

- Zhu et al., **Observation of Quantum Darwinism and the Origin of Classicality with Superconducting Circuits** (2025), arXiv:2504.00781 — controlled redundant-record platform and CZ compilation.
- Rudinger et al., **Heisenberg-limited calibration of entangling gates with robust phase estimation** (2025), arXiv:2502.06698 — high-information coherent-error calibration on superconducting CZ hardware.
- Carignan-Dugas et al., **The Error Reconstruction and Compiled Calibration of Quantum Computing Cycles** (2023), arXiv:2303.17714 — cycle-context error reconstruction and coherent calibration.
- Zhang et al., **High-Precision Calibration Workflow Achieves Above 99.9% CZ Gate Fidelity on a Scalable Superconducting Processor** (2026), arXiv:2607.01422 — CAFE/ELEA feasibility and leakage/coherent-error control.
- Henao, Santos & Uzdin (2023) and Bar, Santos & Uzdin (2026) — operational pulse-inverse construction and higher-order residual warnings, already recorded in the literature ledger.

## Research-state consequence

**Material progress, no canonical claim change.** The coherent inverse-amplitude degeneracy identified in RT-2026-006 remains real for record-forming target data, but it now has a concrete candidate independent calibration channel that is mechanism-null in the ideal symmetric model. P1 is therefore narrowed from “find a way to identify coherent mismatch independently” to “validate whether a symmetric common-eigenstate no-record control remains nuisance-faithful on real compiled hardware, then complete the stochastic/leakage/correlation null.”

The canonical assessment that a distinctive empirical prediction remains unestablished without optional selector dynamics is unchanged.