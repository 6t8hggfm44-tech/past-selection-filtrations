# Echo discriminator power and calibration requirements

**Date:** 2026-08-24  
**Status:** adversarial design analysis for optional selector physics; not a prediction of base PSF

## Question

After the 2026-08-17 coherent inverse-amplitude mimic, is the higher-order curvature separating the optional selector law from the matched standard-unitary null statistically measurable in a realistic interaction-strength sweep?

## Models under comparison

Use the same product-record specialization as the prior identifiability note:

`V_pre(theta,N)=cos(theta)^N`, for `0<theta<pi/2`,

and optional selector law

`nu_selector(theta,N)=cos(theta)^(N eta)`.

The adversarial coherent-mismatch null is chosen to match the selector model to quadratic order by setting `epsilon=sqrt(eta)`:

`nu_null(theta,N)=cos(sqrt(eta) theta)^N`.

This is intentionally the difficult local null. It does not assert that real hardware has exactly this mismatch law.

## Symbolic separation

Wolfram was used to expand the log-ratio:

`log nu_null - log nu_selector`

with result

`N eta(1-eta) theta^4/12 + N eta(1-eta^2) theta^6/45 + 17 N eta(1-eta^3) theta^8/2520 + O(theta^10)`.

Thus the models agree through the quadratic term and separate first at fourth order in the log echo.

For the raw echo expectation,

`Delta nu = nu_null - nu_selector = N eta(1-eta) theta^4/12 + O(theta^6)`

in the weak-record regime.

## Information-theoretic consequence

Assume a final binary `X`/parity measurement with outcomes `+1/-1` and mean `nu`, so the Bernoulli probability is `p=(1+nu)/2`. For the two fixed models above, Wolfram gives the small-angle Kullback-Leibler divergence per target shot

`D_KL(selector || null) = N eta (1-eta)^2 theta^6 / 288 + O(theta^8)`.

Therefore the amount of information available per target shot collapses as `theta^6` when the experiment remains in the weak-record regime. This is a structural consequence of local model matching, not merely a numerical inconvenience.

Using a normal-approximation one-sided test with alpha=0.05 and 80% power, and temporarily assuming the null curve is known exactly with no calibration/systematic uncertainty, the required target-shot count has asymptotic form

`M approximately 890.29 / [N eta (1-eta)^2 theta^6]`.

This is an optimistic lower-bound-style design calculation, not a hardware forecast. Drift, multiple held-out points, readout error, calibration uncertainty, leakage, non-Markovianity and model uncertainty can only increase practical resource requirements.

## Illustrative numerical checks

For `N=8`, the same idealized normal approximation gives:

| eta | theta | V_pre | nu_null | nu_selector | Approx. target shots |
|---:|---:|---:|---:|---:|---:|
| 0.01 | 0.4 | 0.518 | 0.99362 | 0.99344 | 2.58e6 |
| 0.01 | 0.7 | 0.117 | 0.98058 | 0.97878 | 7.62e4 |
| 0.01 | 1.0 | 0.00726 | 0.96073 | 0.95194 | 6.61e3 |
| 0.01 | 1.3 | 2.62e-5 | 0.93446 | 0.89988 | 7.59e2 |
| 0.05 | 0.4 | 0.518 | 0.96847 | 0.96764 | 5.73e5 |
| 0.05 | 0.7 | 0.117 | 0.90628 | 0.89832 | 1.79e4 |
| 0.05 | 1.0 | 0.00726 | 0.81735 | 0.78173 | 1.71e3 |
| 0.05 | 1.3 | 2.62e-5 | 0.70973 | 0.59010 | 2.36e2 |
| 0.10 | 0.4 | 0.518 | 0.93784 | 0.93633 | 3.29e5 |
| 0.10 | 0.7 | 0.117 | 0.82068 | 0.80697 | 1.10e4 |
| 0.10 | 1.0 | 0.00726 | 0.66574 | 0.61110 | 1.20e3 |
| 0.10 | 1.3 | 2.62e-5 | 0.49860 | 0.34822 | 2.17e2 |

The table shows why simply collecting more weak-record points is a poor strategy. The discriminating information resides disproportionately at stronger interactions where the fourth- and higher-order curvature becomes appreciable.

## Calibration-uncertainty condition

For the coherent-mismatch null,

`d nu_null / d epsilon = -N theta tan(epsilon theta) nu_null`.

At the locally matched value `epsilon=sqrt(eta)`, calibration uncertainty in `epsilon` produces an uncertainty band in the null. As a simple design criterion, require the 95% calibration half-width to be less than half the selector-null gap:

`1.96 |d nu_null/d epsilon| sigma_epsilon < Delta nu/2`.

In the weak-record limit this requires approximately

`sigma_epsilon/epsilon < (1-eta) theta^2 / 47.04`.

Thus calibration precision becomes severe at small interaction angle even before target-shot noise is considered. For example, the leading-order criterion is roughly 0.34% relative precision at `theta=0.4`, 1.0% at `theta=0.7`, and 2.1% at `theta=1.0` when `eta` is small. Exact numerical values deviate at larger angles but the qualitative conclusion is unchanged.

This is not a claim that such precision is impossible. It is a requirement that must be demonstrated by an independent calibration protocol rather than inferred from the target echo residual.

## Literature-assisted control design

### Pulse inverse rather than gate-level self-inverse

Henao, Santos & Uzdin (2023) define a pulse inverse by reversing the schedule of the effective interaction Hamiltonian and inverting its sign, including for logically self-inverse gates such as CNOT/CPhase. Their experiments/analysis show that ordinary gate insertion can implement the wrong noise amplification when the noise does not commute with the ideal gate.

Bar, Santos & Uzdin (2026) extend this to Layered KIK and explicitly track higher-order Magnus terms. Their analysis is useful to PSF because it supplies a concrete operational language for the forward/inverse pair while also warning that a realizable pulse inverse is not the mathematical adjoint of the full noisy channel. Markovianity and higher-order terms remain assumptions/nuisances.

### Context-sensitive coherent-error calibration

Debroy et al. (2023) introduce Context-Aware Fidelity Estimation (CAFE), using repeated target subcircuits so coherent error accumulation can be distinguished from incoherent error growth in the actual spatial/temporal context.

Zhang et al. (2026) combine error-amplification and CAFE-style calibration on an 84-qubit superconducting processor, reporting a best CZ fidelity above 99.9% and coherent error contribution around 0.007%, with automated stability monitoring over nine hours. This is platform-specific feasibility evidence that coherent calibration can reach a regime relevant to PSF control design; it is not evidence that the complete PSF null can be characterized to the required accuracy.

Pan et al. (2026) provide the complementary warning: for coherent over-rotation faults, a single fixed-basis histogram can have singular Fisher information at zero angle and be locally unable to identify the coherent fault; extra measurement settings can restore identifiability. Therefore the PSF calibration stage must be designed for the nuisance parameter, not assumed identifiable from the same echo observable.

## Adversarial interpretation

**Result:** the selector echo remains testable in principle, but the weak-record regime is a poor discriminating regime against the locally matched coherent-mismatch null. The experiment should not be designed around a near-zero-angle power-law fit.

A credible design now needs two distinct information channels:

1. an **independent nuisance-calibration channel** that identifies forward/inverse coherent mismatch, leakage and relevant noise in the native pulse/circuit context; and
2. a **held-out selector-test channel** spanning interaction strengths strong enough that the selector-vs-null curvature is experimentally resolvable.

Optimizing only the target-shot count tends to favor very strong records (`V_pre` extremely small), which may introduce new leakage, nonlinear-control and calibration problems. The final design therefore requires a joint optimization over statistical information and nuisance/systematic error, not simply maximal `theta` or maximal redundancy.

## Reproducibility

Wolfram checks performed 2026-08-24 included:

- series of `N (Log[Cos[Sqrt[eta] theta]] - eta Log[Cos[theta]])` through eighth order;
- series of `nu_null-nu_selector` and both binary-measurement variances;
- small-angle limit `theta^6 M -> 144 (z_alpha+z_beta)^2/[N eta(1-eta)^2]`;
- Bernoulli KL limit `D_KL/theta^6 -> N eta(1-eta)^2/288`;
- numerical shot-count and calibration-precision grids.

## Next design step

Build a platform-specific prospective protocol in which the record interaction and its pulse inverse are characterized with a CAFE/error-amplification-style calibration suite on dedicated calibration runs, fit a predeclared nuisance model with uncertainty, freeze it, then optimize held-out `theta,N` points by expected likelihood/KL separation subject to leakage and calibration constraints. The selector parameter `eta` must remain independently fixed or prospectively calibrated on a separate subset.