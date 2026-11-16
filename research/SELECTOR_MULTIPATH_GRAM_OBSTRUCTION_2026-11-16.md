# Conditional multi-alternative selector Gram obstruction — 2026-11-16

**Status:** exact finite-dimensional mathematical red-team result, with Wolfram check and independent validation-companion record `PSF-V-2026-002`. **Not** new physics, a result of a hardware test, or a contradiction of the author-approved two-path-only manuscript 9.0.2.

**Source:** P. J. Bavaro, *The Accessible Quantum Past*, 9.0.2 (September 7, 2026), DOI https://doi.org/10.5281/zenodo.22647510, Section 11: optional pure-selector overlap law `|<q_h|q_k>|=V_hk^eta` in a **predeclared class of two-path experiments**, together with its expressly stated multi-alternative Gram-positivity boundary.

## Exact three-record obstruction

Let the three valid pure qubit record states be
`r_0=|0>`, `r_1=(|0>+|1>)/sqrt(2)`, `r_2=|1>`.
Their root fidelities are `V_01=V_12=2^(-1/2)` and `V_02=0`. A universal joint three-alternative extension with one selector Hilbert space Q, one pure `q_h` per alternative, and the *same* `eta>0` on all pairs would prescribe `|<q_0|q_1>|=|<q_1|q_2>|=a=2^(-eta/2)` and `<q_0|q_2>=0`.

Every Hermitian normalized 3x3 Gram matrix with those moduli has `det G=1-2 a^2 = 1-2^(1-eta)`, regardless of selector phases or Q dimension. PSD is necessary for a Gram matrix, so **every 0<eta<1 fails** for this admissible triple. Equivalently, the selector would demand that the intermediate state have squared overlap `2^(-eta)` with each of two orthogonal endpoints, and their probabilities would sum to `2^(1-eta)>1`.

At eta=1 this triple saturates PSD and is realized by the original record vectors. For eta>1 this particular triple admits `q_0=|0>, q_2=|1>, q_1=a|0>+a|1>+sqrt(1-2a^2)|2>`. This shows `eta>=1` is *necessary and sufficient for this triple*, **not** generally sufficient for all 3-or-more state families.

### Robustness against rank-deficiency objections

Let `rho_h=(1-epsilon)|r_h><r_h|+epsilon I/2` with `epsilon=1/100`, making all three record states faithful. Writing `r=1-epsilon=.99` gives `V_01=V_12=sqrt(1-r^2/2)=.714107834994...` and `V_02=sqrt(1-r^2)=.141067359797...`. At eta=1/2, the *maximum possible determinant over all complex Gram phases* is

`max det G = 1-2(V_01)^(2 eta) - (V_02)^(2 eta) + 2 (V_01)^(2 eta)(V_02)^eta = -0.0328604347041... < 0`.

Thus positivity fails even with strictly positive records and optimally chosen selector phases. For each fixed eta in (0,1), continuity of this determinant in epsilon supplies a sufficiently small positive epsilon with the same failure.

### Reproducibility

2026-11-16 Wolfram Language exact algebra:
```wolfram
Clear[a, eta]; g={{1,a,0},{a,1,a},{0,a,1}};
{Det[g], Eigenvalues[g],
 FullSimplify[Det[g] /. a->2^(-eta/2)],
 FullSimplify[Reduce[(Det[g] /. a->2^(-eta/2))>=0 && eta>0,eta,Reals]],
 N[Eigenvalues[g /. a->2^(-1/4)],12]}
```
Returns `{1-2 a^2,{1,1-sqrt(2)a,1+sqrt(2)a},(2^eta-2)/2^eta,eta>=1,{2.189207115...,1,-.189207115...}}`; eta=1/2 determinant `-.41421356237...`.

Full-rank check:
```wolfram
r=99/100; v01=Sqrt[1-r^2/2]; v02=Sqrt[1-r^2];
a=Sqrt[v01]; c=Sqrt[v02]; detMax=1-2 a^2-c^2+2 a^2 c;
{FullSimplify[detMax<0],N[detMax,16]}
```
Returns `{True,-0.0328604347041093...}`.

## Prior-art and scope assessment

The linear-algebra mechanism is standard Gram positivity / fractional entrywise-power fragility, related to FitzGerald & Horn, “On fractional Hadamard powers of positive definite matrices,” *J. Math. Anal. Appl.* 61 (1977) 633–642, https://doi.org/10.1016/0022-247X(77)90167-6. **No standalone mathematical novelty claimed.**

The manuscript already explicitly limits its postulate to designated two-path experiments and warns of multi-alternative PSD constraints. This result **quantifies one such constraint**: a naive universal common-Q extension with eta<1 is mathematically impossible for simple physical record triples. It does not refute independent pairwise implementations, context-specific selector degrees, an altered multi-path law, or eta>=1 restricted families. It neither derives a complete, linear/no-signalling dynamics nor establishes fundamental record selection. The illustrative small-eta selector echo law must not be silently generalized to all triples.

## Research action

- Keep C1–C8 base claims, N5 unestablished, and EXP-2026-001 readiness unchanged.
- Add a concrete **P7 gate**: before claiming a multi-path extension, require an explicit jointly PSD Q overlap kernel for every admitted physical record family, including faithful, noncommuting and orthogonal records; state whether eta may depend on context and what physical principle restricts admissible H.
- Retain the **P1 priority** of a device-specific all-compatible ordinary calibration/trajectory target certificate; this mathematical result does not supply one.
- Do not revise or circulate manuscript 9.0.2 based solely on this extension-level boundary. No independent human review is claimed.

**Validation:** https://github.com/6t8hggfm44-tech/psf-validation/blob/main/claims/PSF-V-2026-002.md.
