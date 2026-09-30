# Common-Drift Commutator Contamination of a Nominal No-Record Control

**Date:** 2026-09-28  
**Status:** red-team / experimental-design result  
**Baseline:** PSF manuscript 9.0.2 (2026-09-07)

**Formatting correction (2026-09-30):** restored lost LaTeX escapes and math delimiters only. Equations, assumptions, scope, and conclusions are unchanged. The plain-text commutator expression is also preserved in the contemporaneous [P1 queue](../open-problems/QUEUE.md).

## Question

Does preparing the environment in an eigenstate of the intended conditional interaction suffice to make the common-eigenstate Ramsey calibration arm physically no-record?

## Minimal countermodel

Let the two system-conditioned environment Hamiltonians be

$$
H_{\pm} = \frac{1}{2}(h Z \pm g X),
$$

with initial environment state $|+x\rangle$.  When $h=0$, the state is an eigenstate of the conditional generator and the two branches differ only by phase, so the branch-overlap magnitude remains one.

With a noncommuting branch-independent drift $hZ/2$, exact two-level evolution gives

$$
V(t)^2
=
1-\frac{4g^2h^2}{(g^2+h^2)^2}
\sin^4\!\left(\frac{\sqrt{g^2+h^2}\,t}{2}\right).
$$

Thus $V(t)<1$ generically even though the preparation was exactly blind to the intended $X$ generator at $t=0$.  The short-time evidence action is

$$
\Sigma(t)=-\log V(t)=\frac{g^2h^2t^4}{8}+O(t^6).
$$

## General short-time criterion

For

$$
H_{\pm} = H_0 \pm B/2
$$

and a nominal blind state satisfying $B|\psi\rangle=b|\psi\rangle$, the first nonzero contamination is governed by the failure of the common dynamics to preserve the $B$-eigenspace.  The leading term is

$$
\Sigma(t)
=
\frac{t^4}{8}\operatorname{Var}_{\psi}\!\left(i[H_0,B]\right)
+ O(t^5),
$$

subject to the stated smooth finite-dimensional short-time expansion.

The practical message is narrower than a new theorem about selector physics: a common-eigenstate preparation is only a mechanism-null control if the full ordinary dynamics preserves the blind manifold, or if departures are prospectively bounded.

## Cross-resonance interpretation

For an effective cross-resonance-type Hamiltonian written schematically as

$$
H_{\mathrm{eff}}=\frac{1}{2}(I\otimes A + Z\otimes B),
$$

the corresponding static leading diagnostic is

$$
\Sigma_{\mathrm{common}}(t)
\simeq
\frac{t^4}{8}\operatorname{Var}_{\psi}\!\left(i[A/2,B]\right).
$$

This should be treated as one term in a larger trajectory-wide ordinary null that also includes spectators, leakage, control modes, memory, drift, and calibration-compatible joint processes.

## Interpretation

This is entirely standard unitary quantum mechanics.  It is **not evidence for the optional PSF selector**.  It further narrows RT-2026-008: logical endpoint nulling, intended-target pathwise nulling, and absence of spectator records are still insufficient if ordinary common dynamics rotates the environment out of the intended conditional-generator eigenspace.

The experimental acceptance condition should therefore test the physical trajectory, not merely the preparation and endpoint:

1. reconstruct or bound the common and conditional Hamiltonian components in the actual scheduled pulse context;
2. propagate the nominal blind preparation under both conditioned branches;
3. bound the resulting trajectory-wide ordinary record action;
4. retain all ordinary processes consistent with calibration;
5. optimize selector-vs-null statistics only after the held-out ordinary prediction band is sufficiently narrow.

## Literature connection

Echoed cross-resonance error-budget work reports effective Hamiltonian components beyond the intended $ZX$ interaction and emphasizes higher-order residuals arising through noncommuting terms.  This supplies a physically relevant setting for the commutator mechanism above.  Separately, imperfect-record / Quantum-Darwinism models with local fields reinforce that alignment with a conditional interaction axis need not remain record-null under additional dynamics.

## Status

- Advances P1 by converting another qualitative nuisance into a quantitative trajectory-level diagnostic.
- Does not change N5: distinctive selector physics remains unestablished.
- Does not alter the accepted manuscript.
