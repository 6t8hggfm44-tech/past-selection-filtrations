# EXP-2026-001 — Native Conditional-Record Echo with Calibrated No-Record Ramsey Control

## Identity
- **ID:** EXP-2026-001
- **Title:** Native Conditional-Record Echo with Calibrated No-Record Ramsey Control
- **Platform family:** superconducting transmons / cross-resonance or related native conditional interaction
- **Status:** active
- **Readiness:** L3 — platform-mapped
- **Primary PSF question:** Can a calibrated record-forming interaction followed by a sufficiently complete physical inverse distinguish the optional selector law from every ordinary process compatible with independent calibration?
- **Related manuscript sections:** 8, 10, 11
- **Related open problems/red-team entries:** P1; RT-2026-004 through RT-2026-012 as applicable

## Scientific fork
- **Preparation / record-forming operation:** Prepare a coherent system superposition and couple it conditionally to one or more environment fragments with calibrated native interactions that generate branch-distinguishing records.
- **Ordinary standard-QM/base-PSF prediction:** Under an exact global inverse acting on all relevant ordinary degrees of freedom, the system coherence is fully restored. Under realistic noise, the held-out target must lie within the complete calibration-compatible ordinary prediction band.
- **Optional selector prediction:** Under the current phenomenological selector law, a stored pre-inverse record overlap may leave residual echo visibility `nu_echo=V_pre^eta`, conditional on a separately fixed/calibrated `eta` and a physically specified filtration/record rule.
- **Primary observable:** recovered system coherence / Ramsey or parity visibility after the inverse.
- **What would count as discrimination:** held-out target data outside the prospectively frozen ordinary-compatible prediction set and consistent with a predeclared selector prediction across multiple conditions.
- **What would not count as discrimination:** generic echo loss, loss of spontaneous recoherence, depth-dependent decay, leakage, residual entanglement, a fitted post hoc exponent, or any effect absorbable by a calibration-compatible ordinary channel.

## Physical implementation
- **Native interaction:** preferably direct or trajectory-engineered conditional `ZX` or `ZZ`-type coupling rather than a logically equivalent compilation that transiently writes uncontrolled records.
- **Forward protocol:** create controlled record strength over tunable interaction angle and fragment count.
- **Inverse / recoherence protocol:** pulse-level or otherwise physically characterized inverse, not merely reuse of a logically self-inverse gate label.
- **Readout:** system Ramsey quadrature / parity visibility, supplemented by calibration observables for coherent and incoherent nuisance directions.
- **Required controllable degrees of freedom:** system, intended record fragments, dominant spectators/leakage levels, relevant control modes, and timing/context that materially changes the effective channel.
- **Relevant experimental precedents:** superconducting Quantum Darwinism circuits; cross-resonance Hamiltonian tomography; robust phase estimation; cycle/context calibration; spectator suppression and pulse-inverse work.

## Ordinary-null model
- **Calibration-compatible process family:** start from Section 8-style compatible-set inference for declared local/shared-context channels, then enlarge for device-specific leakage, spectators, joint noise, non-Markovian memory, control modes and drift when calibration permits them.
- **Leading coherent mimics:** inverse-amplitude mismatch; conditional-axis misalignment; common-drift commutator terms; coherent residual couplings.
- **Leading incoherent mimics:** stochastic gate/channel noise, decoherence during forward/inverse evolution, context-dependent cycle error.
- **Hidden-record pathways:** transient records created by digital compilation; spectators; leaked levels; control-line modes; branch-conditioned ancillary degrees of freedom.
- **Leakage / spectator / control-mode risks:** explicit and currently unresolved at the full scheduled-trajectory level.
- **Memory / non-Markovian risks:** retained-environment correlations can make calibration and target channels differ despite nominally identical gate labels.
- **Drift/context risks:** calibration must match timing, neighboring operations, pulse schedule and relevant hardware context.

## Calibration and holdout
- **Independent nuisance calibration:** common-eigenstate Ramsey/RPE-style calibration for coherent mismatch where physically valid; Hamiltonian tomography for conditional/common axes; CER/CAFE-like contextual error estimates where justified; leakage/spectator characterization.
- **Selector-parameter calibration, if applicable:** `eta` may not be fit from the held-out target. It must be independently fixed or prospectively calibrated on a disjoint set.
- **Holdout variables:** interaction strength, record redundancy/fragment number, reversal rounds, or other predeclared conditions chosen to expose higher-order differences between the ordinary family and selector law.
- **Prospective acceptance criteria:** trajectory-wide ordinary record action in the nominal no-record arm must stay below a declared bound; the complete ordinary target-prediction interval must be narrower than the selector-vs-null separation over the held-out region.
- **Target-prediction uncertainty band:** not yet complete.
- **Power/sample-size analysis:** preliminary weak-record scaling exists, but final shot optimization is deferred until the device-specific identifiability certificate exists.

## Feasibility
- **Current experimental capability:** record formation, redundant-environment circuits, Hamiltonian tomography, robust coherent-error calibration, pulse/context calibration, spectator/leakage mitigation and inverse-style benchmarking all exist separately in modern superconducting platforms.
- **Missing capability:** one integrated experiment demonstrating that these controls jointly bound the complete ordinary target prediction tightly enough for a selector test.
- **Hardest engineering requirement:** controlling or certifying all branch-conditioned hidden degrees of freedom through both record writing and reversal.
- **Estimated readiness rationale:** L3 because the abstract protocol is mapped to real hardware primitives and failure modes, but the scheduled-pulse model and held-out ordinary prediction band are not yet complete.

## Evidence and derivations
- **Experiment dossiers:** `experiments/ECHO_DISCRIMINATOR.md`; `ECHO_NOISE_IDENTIFIABILITY_2026-08-17.md`; `ECHO_POWER_CALIBRATION_2026-08-24.md`; `NO_RECORD_RAMSEY_CONTROL_2026-08-31.md`; `COMPILED_PATH_RECORD_AUDIT_2026-09-07.md`; `NATIVE_SPECTATOR_HIDDEN_RECORD_BUDGET_2026-09-21.md`; `COMMON_DRIFT_COMMUTATOR_NULL_2026-09-28.md`; `CROSS_RESONANCE_PAULI_NULL_DIAGNOSTIC_2026-10-05.md`.
- **Literature ledger entries:** relevant entries include L-2026-007, 009–023, 024, 027, and any future platform-specific updates.
- **Red-team entries:** RT-2026-004 through RT-2026-012 where relevant.
- **Code/symbolic checks:** multiple finite-dimensional and symbolic checks are recorded in the underlying dossiers.

## Next decisive step
Model one real scheduled CR/ECR or tunable-coupler pulse trajectory as time-dependent common and conditional generators, include dominant spectators/leakage/control modes, and propagate the nominal blind preparation through both branches to obtain a calibrated trajectory-wide `Sigma_ordinary(t)` uncertainty envelope. Determine whether any held-out region remains in which the complete ordinary family and selector prediction are prospectively separable.

## Change log
- **2026-10-05:** entry created from the accumulated P1 experimental program.
