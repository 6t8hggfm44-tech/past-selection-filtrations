# Echo Noise Identifiability — Coherent Inverse-Error Mimic

**Date:** 2026-08-17  
**Status:** adversarial standard-unitary null analysis for the optional selector echo law; not a new PSF prediction

## Question

Can ordinary imperfect reversal reproduce the proposed selector relation

`nu_echo = V_pre^eta`

well enough that varying record strength at fixed circuit depth is not, by itself, discriminating?

## Product-record model

Use a controlled record interaction with per-fragment branch-state overlap

`v(theta) = |cos(theta)|`,

so for `N` independent fragments

`V_pre(theta,N) = |cos(theta)|^N`.

The optional selector postulate predicts

`nu_selector(theta,N) = |cos(theta)|^(eta N)`.

Now assume ordinary unitary quantum mechanics, but the attempted inverse has a coherent fractional amplitude mismatch: after forward record coupling of angle `theta`, the inverse leaves a residual conditional angle `epsilon theta` per fragment. The ordinary post-inverse branch overlap is then

`nu_noise(theta,N) = |cos(epsilon theta)|^N`.

This is a standard incomplete-inverse mechanism; no selector sector is required.

## Effective selector exponent

If this ordinary residual is naively fitted to the selector form, the apparent exponent is

`eta_eff(theta,epsilon) = log|cos(epsilon theta)| / log|cos(theta)|`.

The factor `N` cancels exactly. Therefore increasing the number of redundant fragments does not, by itself, break this degeneracy.

A Wolfram symbolic expansion around `theta=0` gives

`eta_eff = epsilon^2 + [epsilon^2(epsilon^2-1)/6] theta^2 + O(theta^4)`.

Thus in the weak-record regime,

`nu_noise = V_pre^(epsilon^2) [1 + higher-order curvature]`,

so an ordinary coherent inverse-amplitude mismatch is locally indistinguishable from a selector law with `eta = epsilon^2` unless the inverse mismatch is independently calibrated or the experiment spans enough record strength to resolve the higher-order curvature.

Wolfram numerical checks show the relative deviation of `eta_eff` from `epsilon^2` is only about 0.15% at `theta=0.1`, 1.5% at `theta=0.3`, 4.2% at `theta=0.5`, and 8-9% at `theta=0.7` for representative small `epsilon` values. For `epsilon=0.1`, `N=10`, the ordinary-noise and selector curves differ in recovered visibility by only about `6.8e-5` at `theta=0.3` and `5.5e-4` at `theta=0.5` if the selector fit uses `eta=0.01`.

These numbers are sanity checks, not hardware forecasts.

## Literature relevance

### Yoshimura & Sa (2025), noisy many-body Loschmidt echoes

They show that Loschmidt-echo decay under ordinary noisy reversal depends on operator growth and can show Gaussian-to-exponential regimes. This matters because equal circuit depth or gate count does not guarantee equal echo sensitivity when the underlying dynamics changes operator support/scrambling.

Source: https://arxiv.org/abs/2509.01585

### Mayer et al., mirror benchmarking

Mirror benchmarking studies circuits followed by their inverses and proves exponential survival decay under stated noise assumptions. The paper explicitly notes that coherent forward/inverse errors may cancel under one compilation relation, whereas arbitrary inverse-gate error channels change the decay parameter. It therefore supplies a standard benchmarking language for characterizing the inverse itself rather than assuming same-depth controls remove reversal error.

Source: https://arxiv.org/abs/2108.10431

### Harris, Lively & Schuhmacher (2026), verifiable benchmark circuits

They construct benchmark circuits designed to mirror an application's native-gate structure and hence its noise profile. This supports replacing a weak 'same depth / same gate count' null with pulse/native-structure-matched verifiable controls wherever feasible.

Source: https://arxiv.org/abs/2603.10224

## Consequence for the PSF echo protocol

The previous requirement to vary `V_pre` at approximately fixed circuit depth remains useful but is not sufficient. Record-strength variation commonly changes the physical interaction angle or compiled pulse realization, and an ordinary angle-dependent inverse mismatch can then track `V_pre`.

A stronger prospective null should include:

1. independent characterization of the forward and inverse record-forming operations as functions of interaction angle, sufficient to bound a residual `epsilon(theta)` before target echo data;
2. pulse/native-gate-structure-matched mirror or verifiable benchmark circuits, not merely equal depth/gate count;
3. a broad enough `theta` sweep to test the predicted selector constant-slope relation against the curvature of independently calibrated ordinary inverse-error models;
4. held-out conditions in both `theta` and `N`, because `N` alone does not break the coherent-mismatch degeneracy;
5. a predeclared standard-noise prediction band propagated into `nu_echo`, rather than subtracting an error model fitted on the selector-test data.

## Red-team status

**Result:** selector discriminator further narrowed, not defeated.  

The law remains testable in principle if `eta` and the ordinary inverse-error model are independently fixed and the held-out data distinguish the selector curve from standard-noise predictions. In the weak-record regime, however, an apparent constant power-law exponent is not by itself evidence for selector physics.

## Reproducibility note

Wolfram check performed 2026-08-17:

`Series[Log[Cos[epsilon theta]]/Log[Cos[theta]], {theta,0,4}]`

giving leading terms

`epsilon^2 + epsilon^2(epsilon^2-1) theta^2/6 + O(theta^4)`.
