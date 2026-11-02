# Ordinary heralded-filter echo mimic: an exact postselection red-team model

**Assessment date:** 2026-11-02  
**Priority:** P1 / EXP-2026-001; proposed RT-2026-016  
**Status:** exact elementary two-qubit ordinary-quantum model, checked by Wolfram symbolic algebra and independent numerical matrices. This is **not new selector dynamics**, not a model of complete global reversal, and not a device-level noise certificate.  
**Manuscript baseline:** author-approved *The Accessible Quantum Past*, manuscript 9.0.2 (2026-09-07), DOI https://doi.org/10.5281/zenodo.22647510, especially Secs. 8, 10, 11.  
**Experimental prior art:** Lee, Cao, Joglekar and Murch, *Nonlinear quantum evolution of a dissipative superconducting qubit*, first arXiv version 2025-10-29, published *Physical Review Research* **8**, 043089 on 2026-10-23, DOI https://doi.org/10.1103/7w9t-c5xf ; https://arxiv.org/html/2510.25836 . They experimentally observe postselection-induced *effective* nonlinearity in a superconducting transmon, while the full three-level dynamics remain linear. They **did not implement this specific echo-mimic circuit**.

## Question

Can an entirely ordinary **heralded**, non-trace-preserving operation between record creation and a nominal echo leave a residual visibility law that resembles the optional PSF selector law `nu_echo=V_pre^eta`? A conditioned data subset is not governed by the same unconditional CPTP map assumed in the manuscript's Sec. 8 local-slot theorem.

## Exact circuit and formulas

Let system S begin in `|+>=(|0>+|1>)/sqrt(2)` and environment E begin in `|0>`. Apply the controlled rotation

    U_theta = |0><0|_S ⊗ I_E + |1><1|_S ⊗ R_y(2 theta)_E,

where `R_y(2 theta)|0>=c|0>+s|1>`, `c=cos(theta)`, `s=sin(theta)`, and `0<=theta<pi/2`. The preinverse environment-branch overlap is `V_pre=c`.

A success-heralded ordinary filter on E has Kraus operator

    K_success = |0><0| + a exp(i varphi)|1><1|,   0<=a<=1.

The failure Kraus operator `K_fail=sqrt(1-a^2)|1><1|` completes a **trace-preserving quantum instrument** when both outcomes are kept. Condition on success, then invert only `U_theta` (do NOT invert the unitary dilation/record of the filtering apparatus).

With the paper's system convention `C=<X>+i<Y>=2(rho_S)_{10}`, exact matrix propagation gives

    p_success(theta,a) = [1+c^2+a^2 s^2]/2
                       = 1-(1-a^2)s^2/2,

    C_success(theta,a,varphi)
        = [c^2+a exp(i varphi)s^2]/p_success(theta,a).

At `varphi=0`, `C_success` is real nonnegative and its magnitude is the postselected echo visibility. For a fixed `a`, the small-angle expansion is

    C_success(theta,a,0)
      = 1 - [(1-a)^2/2] theta^2
        + [(1-a)^2(-1+3a^2)/12] theta^4 + O(theta^6).

Meanwhile `(cos theta)^eta=1-eta theta^2/2+(eta^2/8-eta/12)theta^4+O(theta^6)`. Therefore **for any fixed `0<=eta<=1`**, an ordinary `a=1-sqrt(eta)` produces the same quadratic selector-like echo deficit. This is a *local mimic*, not an exact equality for arbitrary angles or any selector evidence.

Stronger special case: at

    a = sqrt(2)-1;    eta = (1-a)^2 = 6-4sqrt(2) ≈ 0.3431457505,

the two ordinary-filter and optional-selector predictions coincide **through order theta^4**, with

    C_success(theta,a,0) - (cos theta)^eta
      = (17 sqrt(2)/3 - 8) theta^6 + O(theta^8)
      ≈ 0.01387685345 theta^6 + O(theta^8).

For `theta=0.4` rad, the exact ordinary postselected echo is `0.9722376842` and the selector power comparator is `0.9721778301`, a difference of `0.0000598541`; yet the filter's success probability is `0.9371859028`. This is a toy-model comparison at a single predeclared `eta` value, not a claim that selection alone can mimic every selector exponent globally.

## What exposes or defeats this mimic

1. **Keep every herald outcome.** The nonzero, angle-dependent loss `1-p_success=(1-a^2)sin^2(theta)/2` is a calibrated nuisance witness. A deterministic selector experiment with an independently justified ideal inverse should not silently discard these failures.
2. **Calibrate the filter as an instrument, not only a conditional channel.** The probability `p_success` fixes `a^2` within this simple family, but **does not constrain `varphi`**. Two filters with the same acceptance rates and different phase create different complex Ramsey outputs, so phase-sensitive calibration is mandatory.
3. **A trivial no-record arm can miss the nuisance.** When `theta=0`, E always starts/passes as `|0>`, so `p_success=1` and `C_success=1` for every `a,varphi`; that control alone does not bound the filter acting on the record-forming target.
4. **Retain all compatible ordinary instruments/processes.** A fitted `a` from target visibility is no independent calibration. If process conditioning, readout exclusion, or leakage-heralding occurs, include success/failure probability, conditional complex coherence and independent controls in one joint compatible ordinary set. General instruments may have hidden phases, correlated ancillas, context changes, or non-Markovian memory beyond this example.
5. **Full inverse boundary.** If one physically reverses `U_theta` AND the filter's unitary dilation, including its herald/ancilla record, then ordinary global unitary QM gives a complete ideal echo. This example therefore does **not** evade the program's exact-reversal null; it shows why a postselected, partial-inverse protocol cannot be advertised as complete reversal.

## Verification and prior-art discipline

- **Wolfram exact matrix calculation:** 4x4 controlled rotation, environment filter including `exp(i varphi)`, and the inverse gave the stated `p_success`, `C_success`, and zero symbolic residual against both formulas. Wolfram's fourth-order series gave the coefficients above. At `a=sqrt(2)-1`, `eta=6-4sqrt(2)`, the first nonzero comparator difference is exactly `(17sqrt(2)/3-8)theta^6`.
- **Independent numerical check:** 5,000 fixed-seed (`20261102`) random tuples `theta in [0,1.45]`, `a in [0,1]`, `varphi in [-pi,pi]` propagated by explicit scipy 4x4 matrices; maximum absolute residuals `5.56e-16` for both p and C.
- **Reproducibility:** `experiments/code/heralded_filter_echo_mimic_2026_11_02.py`.
- **Novelty status:** ordinary textbook quantum instruments/conditional normalization. Original contribution of this dossier is an explicit PSF P1-specific null construction and fourth-order matching point, not invention of postselection, effective nonlinearity or recovery.

## Research decision

**Material P1 narrowing only.** An echo report must specify whether it is unconditional or herald-conditioned, identify all excluded outcomes, and build an **instrument-complete calibration-compatible target set**, not treat postselected visibility as a deterministic CPTP experiment. This cannot increase EXP-2026-001 past L3, cannot establish N5 and does not justify changing the approved manuscript. The next decisive experimental step remains a measured time-resolved physical Hamiltonian with hidden-mode and context uncertainty combined with herald/loss diagnostics.
