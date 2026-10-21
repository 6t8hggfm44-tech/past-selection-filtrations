# Transverse-action pathwise no-record certificate

**Assessment:** 2026-10-19
**Status:** ordinary finite-dimensional quantum mechanics; original control-design application of standard geometry, not a new general theorem or evidence for selector physics.
**Approved manuscript basis:** *The Accessible Quantum Past*, v9.0.2, 2026-09-07, https://doi.org/10.5281/zenodo.22647510, Sections 8, 10 and 11.
**Related:** `experiments/TIME_DEPENDENT_CONDITIONAL_AXIS_NULL_2026-10-12.md`, P1, EXP-2026-001, RT-2026-013.

## Statement

For a normalized pure initial environment state |ψ₀⟩, let P₀=|ψ₀⟩⟨ψ₀| and Q₀=I−P₀. Suppose the modeled environment branch Hamiltonians are

    H_±(t) = H₀(t) ± B(t)/2,

where H₀ and B are piecewise-continuous finite-dimensional self-adjoint operators. Let U₀(t) be the common H₀ propagator and B_I(t)=U₀(t)† B(t) U₀(t). Define

    δ(t) = ||Q₀ B_I(t)|ψ₀⟩|| = sqrt(Var_ψ₀(B_I(t))),
    J(t) = integral[0,t] δ(s)ds,
    V(t) = |⟨ψ₋(t)|ψ₊(t)⟩|.

Then

    arccos V(t) ≤ J(t).

Consequently, when J(t)<π/2,

    V(t) ≥ cos J(t)
    Σ(t) = -log V(t) ≤ -log(cos J(t)).

This is a *one-sided lower bound on modeled branch visibility*. When J(t)≥π/2 the bound reduces to V(t)≥0, and cos J must not be used as a negative physical visibility lower bound. If δ=0 throughout, the exact shared-eigenspace no-record criterion from the October 12 dossier is recovered.

## Derivation

In the H₀ interaction frame the ± branch generators are ±B_I/2. Decompose

    D = P₀ B_I P₀ + Q₀ B_I Q₀,
    T = P₀ B_I Q₀ + Q₀ B_I P₀.

D preserves the line P₀. Because T is Hermitian and has only off-diagonal P₀/Q₀ blocks, ||T||=||Q₀ B_I|ψ₀⟩||=δ. Under each ±D/2 comparison evolution, the initial state stays on the same ray P₀, up to a phase. Under the full ±(D+T)/2 evolution, the projective path-length distance from that reference ray is bounded by (1/2)∫δ using the standard time-dependent Duhamel/quantum speed estimate. The Fubini–Study triangle inequality bounds the angle between the two branch rays by ∫δ.

This geometric estimate uses standard projective-state geometry, not a new general speed-limit theorem. Relevant prior art: J. Anandan and Y. Aharonov, *Geometry of quantum evolution*, Phys. Rev. Lett. 65, 1697 (1990), https://doi.org/10.1103/PhysRevLett.65.1697.

## Short-time consistency with the previous red-team result

If B_I(0)|ψ₀⟩=b|ψ₀⟩ and H₀, B are differentiable, put

    K = dot B(0) + i[H₀(0),B(0)].

Then δ(t)=t sqrt(Var_ψ₀ K)+O(t²), J(t)=(t²/2)sqrt(Var_ψ₀ K)+O(t³), and the upper bound on action is

    -log cos J(t) = t⁴ Var_ψ₀(K)/8 + O(t⁵).

It agrees at leading order with the exact ordinary branch-action expansion derived in the October 12 rotating-axis audit. For constant B, K reduces to i[H₀,B], recovering the September 28 common-drift diagnostic.

For the rotating-axis toy model H₀=0, B(t)=Ω(cos ωt X+sin ωt Y), initial |+X⟩, δ(t)=Ω|sin ωt| and J=Ω(1−cos ωt)/ω on 0≤ωt≤π for Ω,ω>0. Its exactly computed branch visibility satisfies

    V²=1−[Ω²ω²/(Ω²+ω²)²][1−cos(t sqrt(Ω²+ω²))]².

With Ω=1.7 and ω=0.9, checks returned:

| t | Exact V | Certified cos J |
|---:|---:|---:|
| 0.05 | 0.9999981739876961 | 0.9999981717895678 |
| 0.20 | 0.9995431367396993 | 0.9995343781759196 |
| 0.50 | 0.9842189553879346 | 0.9823716966250511 |
| 1.00 | 0.8309339997115676 | 0.7552658216672016 |

Wolfram symbolic series confirmed both the exact action and the upper bound begin at Ω²ω²t⁴/8; their sixth-order terms differ, so the bound is not generally exact.

## Conservative conditional Hamiltonian uncertainty tube

If the same known initial pure state is used and a separately justified simultaneous deterministic envelope applies,

    ||H₀(t)−H₀hat(t)||≤ε_H(t),
    ||B(t)−Bhat(t)||≤ε_B(t),

then Duhamel yields

    ||U₀(t)−U₀hat(t)||≤ integral[0,t] ε_H(s)ds.

Therefore

    δ(t)≤δhat(t)+ε_B(t)+2||Bhat(t)|| integral[0,t] ε_H(s)ds,

where δhat=||Q₀ U₀hat† Bhat U₀hat |ψ₀⟩||. Let J_star be the integral of this RHS. Every member of this *declared finite-dimensional closed/pure Hamiltonian family* satisfies V≥cos J_star if J_star<π/2.

These deterministic norm envelopes do not inherit statistical coverage from hardware metrics; simultaneous statistical coverage and calibration-to-target transport must be independently established.

## Independent checks and adversarial boundaries

Exact symbolic and numerical rotating-axis checks were performed. Independent time-ordered matrix-evolution tests used random Hermitian 2×2, 3×3 and 4×4 generators, including 48 static-common and 54 time-dependent-common tests across multiple time scales; no violation was found above 2e−4 numerical tolerance. These tests are corroboration, not a replacement for the derivation. If J≥π/2, the Fubini–Study angle bound becomes insufficient to lower-bound V strictly.

A hidden spectator can carry branch information even if the modeled intended fragment has δ=0. Likewise, coherent two-branch Hamiltonians do not by themselves certify open-system leakage, control modes, memory, preparation error, or contextual multitime noise. This bound is a *partial calibration-control guarantee* only; it is not Section 8's complete local-slot target prediction set and not a device-specific all-compatible-ordinary-process discriminator.

## Research disposition

P1 gains a computable approximate physical-null test for a declared finite-dimensional scheduled Hamiltonian: bound a time-resolved transverse conditional generator, propagate full calibration uncertainty, then enlarge to spectator, leakage and retained-memory models. Do **not** optimize target shots, promote EXP-2026-001 beyond L3, modify 9.0.2, or infer fundamental selector dynamics from this ordinary-QM result.
