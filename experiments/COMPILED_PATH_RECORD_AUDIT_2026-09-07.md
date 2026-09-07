# Compiled-path record audit for the no-record Ramsey control

**Date:** 2026-09-07  
**Status:** red-team design result for optional selector physics; not evidence for PSF  
**Primary problem:** P1 experimental discriminator  
**Related:** RT-2026-008; `experiments/NO_RECORD_RAMSEY_CONTROL_2026-08-31.md`

## Question

The 2026-08-31 control is mechanism-null at the level of the **effective** symmetric gate

`U_ZX(theta)=exp[-i theta Z_S \otimes X_E / 2]`

when the environment is prepared in `|+_x>`: the environment branch states differ only by phase and have overlap magnitude one. Does that remain true throughout a realistic digital implementation built from fixed entangling gates and one-qubit rotations?

This matters because an optional PSF selector coupled to record formation may be path-sensitive. A logical input-output map with final `V=1` is not automatically a mechanism-null physical trajectory.

## Exact CZ/CNOT-style decomposition

A standard exact decomposition is

`U_ZX(theta) = (I \otimes H) CNOT_{S->E} (I \otimes R_z(theta)) CNOT_{S->E} (I \otimes H)`.

This identity was independently checked numerically by direct 4x4 matrix multiplication for multiple `theta`; maximum elementwise disagreement was at floating-point roundoff (`~2e-16`). Wolfram was attempted twice on 2026-09-07 but the connector returned an MCP 404, so this run used an independent NumPy matrix check rather than claiming Wolfram corroboration.

## Adversarial branch-overlap trajectory

Take the system branch alternatives `|0>_S` and `|1>_S`.

### Nominal no-record preparation `|+_x>_E`

At the logical input, the branch environment states coincide, so `|<e_0|e_1>|=1`.

1. The first `H_E` maps `|+_x>` to `|0_z>`; overlap remains 1.
2. The first CNOT maps the conditional environment states to `|0_z>` for the `S=0` branch and `|1_z>` for the `S=1` branch. Their overlap is **exactly 0**.
3. `R_z(theta)` adds phases but the two environment states remain orthogonal; overlap remains 0.
4. The second CNOT uncomputes the environment back to the same computational state in both branches; the branch overlap returns to unit modulus, with relative phase `exp(i theta)`.
5. The final Hadamard restores the environment to `|+_x>`; the final branch-overlap magnitude is again 1.

Thus the effective no-record gate has a **transient maximally distinguishable record** under this exact digital compilation even though its final designated environment overlap has modulus one.

### Nominal record-forming preparation `|0_z>_E`

The same decomposition has the opposite timing:

1. The first `H_E` maps `|0_z>` to `|+_x>`.
2. The first CNOT does not distinguish the branches because `X|+_x>=|+_x>`; overlap remains 1.
3. `R_z(theta)` preserves equality of the branch environment states at this point.
4. The second CNOT creates the intended final record, with branch-overlap magnitude `|cos(theta)|`.
5. The final Hadamard preserves that overlap magnitude.

A direct numerical branch-state check at `theta=0.7` gave overlap magnitudes for the no-record arm `1,1,0,0,1,1` across input/H/CNOT/Rz/CNOT/H and for the record arm `1,1,1,1,|cos 0.7|,|cos 0.7|`.

## Consequence for the selector test

This is a concrete counterexample to the assumption that **same effective gate + final `V=1`** is sufficient to make the calibration arm selector-null.

Two interpretations are possible, and the incomplete selector dynamics does not yet choose between them:

1. **Path-sensitive / accumulated-record interpretation.** If the selector responds when branch-distinguishing records become physically available during the control trajectory, the digital no-record arm is not mechanism-null at all; it briefly creates a perfect one-fragment record. Repeating the compiled interaction across fragments could repeatedly activate the putative mechanism even though every fragment is returned to a common final state.
2. **Endpoint-only interpretation.** If the selector law is defined to depend only on the designated post-gate `V_pre`, then the no-record arm remains null by definition. But this introduces a substantive path-independence/time-locality rule: transient perfect records are physically irrelevant to the selector once uncomputed. That rule must be stated and justified in a complete selector dynamics rather than assumed from the effective gate notation.

Therefore the present phenomenological law does not yet uniquely predict the result of a digitally compiled calibration sequence without a microscopic rule specifying **when** record distinguishability contributes to `Sigma` and which transient hardware degrees belong to the physical filtration.

## Design repair: require pathwise mechanism nulling

A direct Hamiltonian implementation of

`U(t)=exp[-i phi(t) Z \otimes X / 2]`

avoids the specific digital pathology in the ideal model. For environment input `|+_x>`, the conditional branch states remain `|+_x>` up to opposite phases for **every intermediate `phi(t)`**, so the designated branch-overlap magnitude stays 1 throughout the trajectory. For input `|0_z>`, the branch overlap evolves as `|cos phi(t)|`.

This suggests a stronger experimental requirement:

> A mechanism-null calibration arm should be audited at the pulse/Hamiltonian trajectory level, not only at the compiled logical input-output level. Where the hypothesized mechanism can accumulate over time, require the relevant record distinguishability to remain nulled throughout the physical trajectory, within a predeclared filtration and hidden-mode model.

A native or engineered analog `ZX`/`ZZ` interaction is therefore preferable to an arbitrary decomposition into fixed maximally entangling gates if the selector is path-sensitive. Cross-resonance superconducting gates provide an established experimental route to effective `ZX` interactions, while tunable-coupler and Hamiltonian-engineering work provides alternative routes to controlled interaction paths. This is a platform-design lead, not proof that any existing device already meets the PSF null requirements.

## New literature relevant to the repair

### Liu & Zhang (accepted PRL 2026) — multiround time-reversal error separation

`Distinguishing Coherent and Incoherent Errors in Multi-Round Time-Reversed Dynamics via Scramblons`, arXiv:2601.04856; accepted by *Physical Review Letters* 2026-09-01.

- In chaotic/SYK settings, coherent and incoherent errors have different accumulation laws across repeated time-reversal rounds: incoherent error accumulates linearly in round number, while coherent error crosses from quadratic to linear accumulation.
- This does not apply automatically to the simple PSF record circuit, but it supplies a concrete additional nuisance-identification axis: **round-number scaling** can be prospectively tested rather than collapsing all reversal error into one visibility parameter.
- If adopted, the PSF platform must first verify that the relevant scaling survives its non-chaotic structured circuit and hardware regime.

### Wang et al. (PRL 2026) — spectator leakage suppression during CZ gates

`Spectator Leakage Suppression via Invariant Subspace Engineering for CZ Gates in Superconducting Quantum Circuits`, *Phys. Rev. Lett.* 137, 100802, published 2026-09-04.

- Demonstrates Hamiltonian engineering with a tunable coupler that confines near-resonant spectator dynamics to an invariant subspace and reports leakage suppression to order `10^-4` with up to three simultaneous spectator qubits.
- This is not a PSF result, but it shows that trajectory-level Hamiltonian engineering can materially suppress one of the exact hidden-record/nuisance channels that the PSF test must control.
- It does not remove the need to verify branch-dependent spectator information below the selector-null separation.

### Chen & Wang (PRApplied 2026) — pulse-level crosstalk suppression

`Scalable suppression of XY crosstalk by pulse-level control in superconducting quantum processors`, *Phys. Rev. Applied* 26, 034001, published 2026-09-01.

- Uses frequency modulation and dynamical decoupling to suppress residual `XY` crosstalk in multi-qubit superconducting layouts.
- Relevant as feasibility evidence that the physical control path, not merely gate labels, can be deliberately engineered and characterized.

### Patterson et al. (2019) — direct effective ZX interaction

`Calibration of the cross-resonance two-qubit gate between directly-coupled transmons`, *Phys. Rev. Applied* 12, 064013 (2019), arXiv:1905.05670.

- Experimentally calibrates a direct cross-resonance `ZX` interaction using Hamiltonian tomography and repeated-gate amplification.
- Provides historical proof of principle for implementing the symmetric interaction as a physical interaction Hamiltonian rather than synthesizing it from two fixed CNOT/CZ gates.
- The reported fidelity is not sufficient evidence for a PSF experiment; the relevance is the available interaction primitive and calibration method.

## Red-team conclusion

**Result:** the 2026-08-31 no-record Ramsey idea survives only after a stronger condition is added. Its logical common-eigenstate construction is correct, but a standard fixed-entangler digital decomposition can make the nominal no-record arm transiently maximally record-forming. The experimental design must therefore validate mechanism nulling over the actual pulse trajectory, or the selector dynamics must explicitly state and justify why transient records do not contribute.

This is a **material narrowing of P1**, not evidence for selector physics and not a change to the base PSF mathematical novelty assessment.

## Next attack

1. Choose one realizable native/analog interaction family (cross-resonance `ZX`, tunable `ZZ` with basis rotation, or another calibrated conditional Hamiltonian) and model its full driven trajectory including leaked levels and spectators.
2. Define a pathwise record metric `V(t)` for the predeclared physical filtration and test whether the no-record arm satisfies `|V(t)|=1` within uncertainty for all relevant times, not just at the logical endpoint.
3. Measure/calibrate branch-dependent leakage and spectator information during the same pulse family.
4. Test whether multiround forward/inverse scaling can separate coherent and incoherent nuisance terms in the chosen structured circuit.
5. Only after those checks, restore the Ramsey Fisher-information calculation and optimize held-out `(theta,N)` target points.
