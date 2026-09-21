# Native spectator hidden-record budget for a pathwise PSF null

**Date:** 2026-09-21  
**Status:** material P1 red-team increment; ordinary-unitary control analysis, not selector evidence  
**Baseline:** PSF manuscript 9.0.2 (2026-09-07)

## Question

The 2026-09-07 compiled-path audit showed that a logically no-record control can transiently create a record when the desired `ZX` interaction is digitally synthesized. A proposed repair was to use a native/analog conditional Hamiltonian for which the intended environment is prepared in a common generator eigenstate. Does that native path by itself guarantee a mechanism-null trajectory?

No. A native path can remain null on the intended environment while simultaneously writing branch information into spectators, control modes, leaked levels, or other hidden degrees. This note gives a minimal exact model that turns that qualitative concern into a quantitative pathwise budget.

## Minimal native model

Let the system qubit be `S`, the intended environment qubit be `E`, and one spectator qubit be `R`. Consider the direct conditional Hamiltonian

`H = (1/2) Z_S ⊗ (J X_E + g X_R)`.

Prepare the intended no-record control state

`|psi_0> = |+x>_E ⊗ |0z>_R`.

For the two `Z_S` branches, the environment/spectator states differ by opposite evolution under `A = J X_E + g X_R`. Their complex branch overlap is therefore

`chi(t) = <psi_0| exp(i t A) |psi_0>`.

Because the two terms commute and `|+x>_E` is an eigenstate of `X_E`,

`chi(t) = exp(i J t) cos(g t)`.

Hence the intended environment contributes only a branch-dependent phase and remains record-null in magnitude, but the spectator produces

`V_hidden(t) = |cos(g t)|`.

The associated hidden evidence action is

`Sigma_hidden(t) = -log |cos(g t)|`

and, for `|g t| << 1`,

`Sigma_hidden(t) = (g^2 t^2)/2 + (g^4 t^4)/12 + O((g t)^6)`.

Thus replacing a digital synthesis by a direct native `ZX` interaction removes the specific CNOT-path failure but does not establish a trajectory-wide null unless all relevant branch-conditioned couplings are also controlled.

## General spectator formula

For a conditional spectator term `(g/2) Z_S ⊗ B` and spectator state `rho`, the branch coherence multiplier is the characteristic function

`chi_R(t) = Tr[rho exp(i g t B)]`,

so

`V_R(t) = |chi_R(t)|`,

`Sigma_R(t) = -log |chi_R(t)|`.

Expanding around `t=0` gives

`Sigma_R(t) = (g^2 t^2 / 2) Var_rho(B) + O((g t)^4)`.

Therefore a hidden mode is pathwise null to quadratic order precisely when the prepared state has zero variance in the branch-conditioned generator. In the exact pure-state case, preparing a generator eigenstate makes that coupling contribute only phase and gives unit overlap for all times.

For a qubit spectator with `B=X` and Bloch component `r_x=Tr(rho X)`,

`chi_R(a) = cos(a) + i r_x sin(a)`, where `a=g t`,

`|chi_R(a)|^2 = cos^2(a) + r_x^2 sin^2(a)`,

and

`Sigma_R(a) = ((1-r_x^2)/2) a^2 + ((1-4 r_x^2+3 r_x^4)/12) a^4 + O(a^6)`.

The extremes are informative: `|r_x|=1` is exactly null for this coupling, while `r_x=0` gives the full `|cos(a)|` hidden-record factor.

## Multiple commuting hidden modes

For independent spectators with a product initial state and commuting conditional generators,

`V_hidden(t) = product_k |Tr[rho_k exp(i g_k t B_k)]|`,

and the actions add. In the weak-coupling regime,

`Sigma_hidden(t) ≈ (t^2/2) sum_k g_k^2 Var_{rho_k}(B_k)`.

A prospective pathwise-null tolerance `Sigma_hidden(t) <= delta` for all `0 <= t <= T` therefore implies the approximate budget

`sum_k g_k^2 Var_{rho_k}(B_k) <= 2 delta / T^2`.

This is not a universal hardware theorem: noncommuting, driven, correlated, leaked, or non-Markovian modes require a time-ordered/open-system generalization. It is a concrete certificate for the simplest hidden-mode sector and a diagnostic target for Hamiltonian tomography.

## Independent symbolic checks

Wolfram Language exact algebra was used on 2026-09-21.

1. For `A = J X_E + g X_R` and `|+x>_E |0z>_R`, exact matrix exponentiation returned
   `chi(t) = exp(i J t) cos(g t)`; subtracting the claimed expression simplified identically to zero.
2. For a general qubit spectator `rho=(I+r_x X+r_y Y+r_z Z)/2`, exact algebra returned
   `chi(a)=cos(a)+i r_x sin(a)` and
   `|chi(a)|^2=cos^2(a)+r_x^2 sin^2(a)`.
3. The exact series of `-log |chi(a)|` begins
   `((1-r_x^2)/2)a^2 + ((1-4r_x^2+3r_x^4)/12)a^4 + O(a^6)`.

These calculations are exhaustive for the stated two-level commuting model but do not certify a real device.

## Hardware relevance

Sundaresan et al., *PRX Quantum* **1**, 020318 (2020), experimentally showed that cross-resonance control can create unwanted entanglement between a target qubit and target spectators through residual interactions, and that optimized target rotary pulses reduce those spectator errors. This is direct physical support for treating the spectator manifold as part of the mechanism-relevant trajectory rather than assuming that a calibrated logical `ZX` term is the whole interaction.

A current hardware-level complement is Tango et al., *Physical Review Letters* **137**, 110202 (2026), which models microwave-control-line crosstalk with a quantum Hamiltonian and finds especially stringent crosstalk requirements for cross-resonance gates. That result concerns gate infidelity, not PSF record distinguishability, so it supports the nuisance-control premise without supplying the hidden-record bound used here.

Public sources:
- Sundaresan et al.: https://doi.org/10.1103/PRXQuantum.1.020318 ; https://arxiv.org/abs/2007.02925
- Tango et al.: https://doi.org/10.1103/m9p9-z6hl

## Red-team consequence

**The native/analog repair is necessary but not sufficient.** A credible no-record Ramsey calibration must certify the *entire accessible hidden conditional generator*, not merely prepare the intended environment in an eigenstate of the intended `ZX` term. A direct interaction can be exactly null in `E` yet non-null in `R`.

For P1, the device-specific ordinary-model certificate should therefore include a predeclared hidden-record budget, with measured or bounded conditional couplings and prepared-state variances propagated into `Sigma_hidden(t)` (or a stronger time-ordered generalization). This quantity must be below the experiment's selector-discrimination tolerance before the calibration arm can be called pathwise mechanism-null.

## What this does not show

- It is entirely standard unitary quantum mechanics.
- It does not establish the optional selector or increase empirical support for N5.
- It does not prove that any particular superconducting device has a hidden record of this size.
- It does not replace Section 8's all-compatible-channel target certificate; rather, it identifies one physical family that a device-level enlargement must bound.
- It does not resolve P7's question of whether a selector, if it exists, responds to transient records. It strengthens the experimental need to settle or conservatively budget that question.

## Next attack

Choose a concrete native interaction and obtain an effective driven Hamiltonian including the leading spectator/leakage/control-mode terms. For each branch-conditioned term, map calibrated couplings and state-preparation uncertainty into a trajectory-level overlap/action band. Then combine that band with the Section 8 compatible-process certificate and the forward/inverse calibration model before any selector-vs-null shot optimization.