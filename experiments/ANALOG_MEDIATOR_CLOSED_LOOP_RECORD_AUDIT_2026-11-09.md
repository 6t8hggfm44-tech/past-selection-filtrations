# Analog mediator closed-loop audit: transient records despite a perfect endpoint return

**Assessed:** 2026-11-09. **Priority:** P1/EXP-2026-001–003, P7. **Status:** exact, elementary ordinary-quantum countermodel to treating *analog endpoint return* as pathwise record nullity; not new dynamics, not evidence of an optional selector, not a certification of any specific hardware gate.  
**Current approved basis:** *The Accessible Quantum Past*, author-approved manuscript 9.0.2 (2026-09-07), DOI https://doi.org/10.5281/zenodo.22647510, Sections 8, 10, 11. P0-9.0.2 reconciliation completed 2026-09-14.

## Physical motivation and historical sources

Gorshkov et al., *Cavity-mediated cross-cross-resonance gate*, first preprint **2025-06-03**, arXiv:2506.03239, revised **2026-10-08**, accepted *PRX Quantum* **2026-10-06**, DOI https://doi.org/10.1103/1nt2-f7gl, propose a two-transmon gate via a cavity whose phase-space trajectory encloses a spin-dependent area. It is a **proposal**, not an experimental PSF test; the exact toy Hamiltonian below is an *illustration of the closed-loop mechanism*, **not a verified reconstruction of their full transmon-cavity drive**. Earlier direct experimental precedent is Leibfried et al., *Experimental demonstration of a robust, high-fidelity geometric two ion-qubit phase gate*, *Nature* 422, 412–415 (2003), DOI https://doi.org/10.1038/nature01492, which demonstrates an ion-qubit geometric phase gate based on state-dependent coherent motional displacements.

This architecture matters because the September 7 PSF compiled-path audit already showed temporary branch records in **digital** uncomputation. A native **analog mediator loop can do the same**, even while generating the intended perfect entangling gate. Therefore “native/analog” is not *by itself* a mechanism-null certificate. This is a concrete platform warning, **not** a theorem that all analog conditional gates create records.

## Exactly solvable ordinary model

Use units with ħ=1. A single oscillator (a,a†), initially in its vacuum |0>, couples to a Hermitian, time-independent system operator S (with eigenvalues s) via an interaction-frame, spin-dependent force

    H_I(t)=g S [a exp(-i δ t)+a† exp(i δ t)],   g,δ real, δ≠0.

S commutes with a,a† and the Hamiltonian at all times. The forced-oscillator Magnus series terminates at second order because the Hamiltonian commutator is proportional to S² and commutes with every H_I(t). One obtains exactly

    U(t)=D[α(t) S] exp[i Φ(t) S²],
    α(t)=g(1-exp(i δ t))/δ,
    Φ(t)=(g/δ)² [δ t−sin(δ t)],

where D(β)=exp(β a†−β* a). The branch s evolves the mediator to |s α(t)> and accumulates phase exp[i Φ(t)s²].

For any pair s,r, the *magnitude of the mediator branch overlap* is

    V_sr(t)=|<r α(t)|s α(t)>|
           =exp[-(s−r)²|α(t)|²/2]
           =exp[-2(s−r)² (g/δ)² sin²(δ t/2)].

Its ordinary record action is Σ_sr(t)=−log V_sr(t). Unless g=0, s=r, or t is a closure instant, this action is positive despite the entirely unitary Hamiltonian.

For the first closed loop T=2π/|δ| (take δ>0 for the following phase), α(T)=0, V_sr(T)=1, and

    U(T)=exp[i 2π(g/δ)² S²] ⊗ I_bus.

Choose S=Z₁+Z₂. Then S²=2I+2Z₁Z₂ and the system gate, up to global phase, is exp[i 4π(g/δ)² Z₁Z₂]. For g/δ=1/4 it is the entangling Ising phase exp[iπ Z₁Z₂/4], **with the mediator exactly returned to vacuum at T**.

Nevertheless at t=T/2:

    V_(s=2,r=0)=exp[-8(g/δ)²]=exp(-1/2)=0.6065306597;
    V_(s=2,r=−2)=exp[-32(g/δ)²]=exp(-2)=0.1353352832.

The same pulse therefore implements a nontrivial final qubit gate and transiently imprints sharply distinguishable states in the bus. Perfect final restoration is *not* trajectory-wide branch indistinguishability.

## Adversarial boundary and nuisance checks

1. **Counterexamples to overgeneralization:** If s=r (e.g. a decoherence-free subspace), g=0, or the bus is constrained to remain unforced along the chosen pair of branches, the mediator is record-null throughout. This dossier does not declare every native analog interaction record-producing. The claim is existential and implementation-specific.
2. **Timing/detuning mismatch:** If a nominal closing pulse actually ends at δT=2π+ε, then V_sr(T)=exp[-(s−r)²(g/δ)²(1−cos ε)]=1−(s−r)²(g/δ)²ε²/2+O(ε⁴) in the weak-error regime. It is an ordinary coherent residual; a logical-gate fidelity or endpoint average cannot alone identify its origin. **Correction/precision:** the exponent before approximation is −(s−r)²(g/δ)²(1−cos ε), equivalent to −(s−r)²(g/δ)² |1−e^{iε}|²/2. The leading residual is −(s−r)²(g/δ)² ε²/2.
3. **Accessibility limit:** A distinguishable unmeasured oscillator state at an intermediate instant is an *available physical correlation*, not automatically an irreversible registered outcome or an observer-accessible cumulative record. A mid-loop cavity measurement generally perturbs the protocol. Whether the optional selector responds to this transient requires an independently specified filtration, physical access interface and accumulation/stage rule (P7). It cannot be inferred from ordinary branch overlap alone.
4. **No fundamental-physics inference:** The bus returns exactly and ordinary quantum mechanics permits full recoherence. This does not contradict base PSF. Real proposals include dispersive coupling and higher levels; nothing here bounds a specific device's omitted modes, heating, loss, context drift or readout backaction.
5. **Source chronology:** Gorshkov et al. first appeared June 2025, *before* the first November 2025 PSF preprint; PRX Quantum acceptance in October 2026 is not the date on which this gate idea originated. The older 2003 ion experiment establishes even earlier geometric-displacement precedent.

## Independent checks (2026-11-09)

- Analytic derivation: integrate the linear force in the first Magnus term and the scalar S² commutator in the second; higher Magnus terms vanish. Coherent-state overlap gives V_sr exactly.
- Wolfram Language (real g, δ>0): simplified V_(2,0)(t) to exp[4g²(cos δt−1)/δ²], returned exp(−8g²/δ²) at half-period and 1 at closure; for g/δ=1/4 returned 0.606530659712633..., and for pair (2,−2) at half-period 0.135335283236613....
- Independent scipy time-domain Schrödinger integration, oscillator Fock truncation n=25, explicit time-dependent H(t), DOP853 with rtol=1e−11 and atol=1e−12: at t=π (δ=1, g=1/4) |<ψ₀|ψ₂>|=0.60653065971303, |<ψ₋₂|ψ₂>|=0.1353352832373024, bus vacuum return probability for branch 2 =0.3678794411719234; at t=2π both overlaps were >0.9999999999994 and bus return probability >0.9999999999994. This is numerical corroboration of a standard exact formula, **not proof of a hardware implementation**.

### Minimal reproducibility recipe

For integer dimension d≥25, let a_{n−1,n}=√n (n=1,...,d−1), a†=aᵀ, start ψ(0)=|0>. For each s∈{−2,0,2}, numerically integrate dψ_s/dt = −i (g s [a e^{-iδt}+a† e^{iδt}]) ψ_s, δ=1,g=1/4. At t=π and 2π compare |ψ_r†ψ_s| with the closed formula. For the full exactly soluble infinite oscillator no truncation is needed.

## Experimental-program implication

Before using a cavity, resonator, tunable coupler, motional mode or other coherent mediator as a “no-record” calibration, characterize **the branch-conditioned mediator trajectory**, not merely its residual excitation at the end. Distinguish (i) coherent transient distinguishability, (ii) records that physically escape into loss/readout channels, and (iii) a defined, observer-accessible cumulative record. Keep these distinctions separate in P1 and P7. In candidate platforms where the intended entangling phase requires a closed displacement loop, a mid-loop record-null assumption is generally unsafe, although another carefully prepared calibration pair may be null.

**Outcome:** material P1 platform-specific red-team extension and historical-prior-art/context update; **no change** to N1–N5, the 9.0.2 manuscript, empirical support, or EXP-2026-001 L3 readiness. The next decisive step remains a measured full scheduled device model and an all-calibration-compatible ordinary target-prediction certificate.