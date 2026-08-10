# Selector-Echo Discriminator — Prospective Dossier

**Status:** candidate operationalization of optional PSF physics; not a prediction of the base record-filtration framework  
**Opened:** 2026-08-10

## Scientific fork

The current constructive extension defines an accumulated record quantity

`Σ = -log V_pre`,

where `V_pre` is the pre-inverse root-fidelity record-similarity quantity fixed by the physical record model. Under the separately labeled selector postulate, the selector branch overlap is

`|<q_h|q_h'>| = exp(-ηΣ)`.

If an ideal inverse restores every ordinary non-selector branch degree of freedom to a common state while leaving the selector degree of freedom untouched, the residual system visibility is therefore

`ν_echo = exp(-ηΣ) = V_pre^η`.

This is a conditional prediction of the optional selector law only. Standard unitary quantum mechanics and the base PSF framework predict complete restoration under a genuinely global exact inverse.

## Product-record specialization

For independent record fragments with root-fidelity factors `v_k`,

`V_pre = ∏_k v_k`,

so the optional selector law gives

`ν_echo = ∏_k v_k^η`.

For identical fragments, `V_pre=v^N` and `ν_echo=v^(ηN)`.

Maity, Onggadinata and Koh (2026) provide a useful standard-unitary reference model with conditional environment overlap `Γ_N(t)=cos^N(2 g_Z t)`. If a PSF experimental instantiation identifies the two conditional pure environment states in that model as the physical record states, then `V_pre=|Γ_N|` and the optional selector fork becomes

`ν_echo = |cos(2 g_Z t)|^(η_PSF N)`.

The notation `η_PSF` should be used in this comparison to avoid confusing the selector parameter with unrelated parameters in the reference paper.

## Finite-dimensional sanity check

Toy model: one system qubit begins in `|+>` and `n` environment qubits begin in `|0...0>`. CNOT fanout from the system to every environment qubit creates a GHZ-like redundant record. Applying the exact inverse fanout restores the system to `|+>` and `⟨X⟩=1` for every `n`.

A direct finite-dimensional numerical check for `n=1,2,3,4` reproduced this standard-unitary result. As a bookkeeping check only, if the two GHZ branch coherences are externally multiplied by a hypothetical factor `κ` after record formation and that factor is not reversed, the post-uncompute system state is `1/2 [[1,κ],[κ,1]]`, hence `⟨X⟩=κ`. This verifies how an independently specified residual branch overlap appears in the echo observable; it does not derive or validate the PSF selector law.

## Prospective protocol skeleton

1. **Predeclare the physical model.** Fix the record-forming interaction, the accessible record algebra/filtration, the branch alternatives, and which degrees of freedom count as ordinary reversible records versus the proposed selector sector.
2. **Calibrate record strength on separate runs.** Estimate `V_pre` or a rigorously related observable without disturbing the runs later used for the echo measurement.
3. **Fix `η_PSF` before target echo data.** Prefer a physically independent calibration. If that is impossible, use a pre-registered calibration subset and held-out test subset; never fit `η_PSF` on the target datum being claimed as a prediction.
4. **Run the echo without intermediate record measurement.** Apply the compiled inverse to every ordinary controlled branch degree of freedom and measure final system X/Y coherence or fringe visibility.
5. **Use matched-control nulls.** Include same-depth/same-gate-count circuits that do not create the designated record, and vary interaction angle/record distinguishability at approximately fixed circuit depth so `V_pre` changes without simply increasing ordinary error exposure.
6. **Cross the controls.** Also vary circuit depth at matched `V_pre` to determine whether any residual follows hardware error rather than stored record evidence.
7. **Audit hidden records.** Test leakage, spectator modes, residual entanglement, environment reset, readout backaction, classical feed-forward, and compilation asymmetry. An uncontrolled environment that retains which-path information is a standard explanation, not selector evidence.
8. **Prospective statistical test.** Compare the independently characterized standard-error null with the predeclared curve `log ν_echo = η_PSF log V_pre`, using held-out conditions and correction for the measured inverse fidelity.

## Identifiability boundary

One nontrivial echo point cannot test the selector exponent if `η_PSF` is fit after the fact, because for any `0<V_pre<1` and `0<ν_echo<1`,

`η_PSF = log(ν_echo)/log(V_pre)`.

Predictive content therefore requires a common parameter fixed independently or prospectively, followed by multiple held-out conditions. A convincing experiment must also show that ordinary error models do not generate the same apparent log-linear relation.

## Experimental platform relevance

Superconducting-circuit Quantum Darwinism experiments have already generated tunable branching states and redundant environment records with controlled conditional unitaries, providing a plausible architecture class for a reversible-record echo study. This does not imply that the existing experiments tested PSF or achieved the globally controlled inverse required here.

## Main blockers

- a physically complete specification of the selector degree of freedom `Q`;
- a complete linear and no-signalling dynamics, or a proof that the phenomenological overlap law admits one;
- an independent or prospectively valid calibration for one common `η_PSF`;
- a physically derived, predeclared record filtration rather than an epistemically chosen one after data collection;
- matched-noise/error models strong enough to rule out incomplete reversal and hidden records;
- quantitative power analysis for realistic echo fidelities and record strengths.

## Primary literature used in this dossier

- Maity, Onggadinata & Koh (2026), *Exact Tradeoff Between Quantum Error Correction and Quantum Darwinism: An Information-Theoretic No-Go Theorem*: https://arxiv.org/abs/2608.03944
- Zhu et al. (2025), *Observation of Quantum Darwinism and the Origin of Classicality with Superconducting Circuits*: https://arxiv.org/abs/2504.00781
- Strasberg, Schindler, Wang & Winter (2026), *Approximate Decoherence, Recoherence and Records in Isolated Quantum Systems*: https://arxiv.org/abs/2601.19703
- Riedel, Zurek & Zwolak (2012), *The Rise and Fall of Redundancy in Decoherence and Quantum Darwinism*: https://arxiv.org/abs/1205.3197
- Schindler et al. (2012), *Undoing a quantum measurement*: https://arxiv.org/abs/1211.1791

## Falsification / revision triggers

Revise or abandon this candidate discriminator if a complete selector dynamics yields a different echo law, if the proposed `η_PSF` cannot be independently/prospectively identified, if matched standard-unitary noise models reproduce the predeclared residual curve, or if a physically defensible selector sector cannot be distinguished from ordinary uncontrolled environment degrees of freedom.
