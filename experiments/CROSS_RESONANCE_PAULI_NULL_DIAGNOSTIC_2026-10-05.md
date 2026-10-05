# Cross-resonance Pauli null diagnostic

**Date:** 2026-10-05  
**Status:** P1 experimental-design / red-team result  
**Baseline:** approved PSF manuscript 9.0.2 (2026-09-07)  
**Scope:** static block-diagonal two-qubit screening model. Not a device certificate and not evidence for selector physics.

## Effective Hamiltonian and branch reduction

Ward et al. (arXiv:2601.20458) use the effective cross-resonance Hamiltonian

$$
H/\hbar=\tfrac12(\Omega_{IX}IX+\Omega_{IY}IY+\Omega_{IZ}IZ+\Omega_{ZI}ZI+
\Omega_{ZX}ZX+\Omega_{ZY}ZY+\Omega_{ZZ}ZZ).
$$

Conditioned on control (Z=\pm1), the target Hamiltonians are, up to the branch-dependent scalar (ZI) phase,

$$
H_\pm/\hbar=\tfrac12(A\pm B),\quad
A=\mathbf a\cdot\boldsymbol\sigma,\ 
\mathbf a=(\Omega_{IX},\Omega_{IY},\Omega_{IZ}),
$$

$$
B=\mathbf b\cdot\boldsymbol\sigma,\quad
\mathbf b=(\Omega_{ZX},\Omega_{ZY},\Omega_{ZZ}).
$$

Ward's block-diagonal model explicitly excludes control leakage, which must remain a separate ordinary channel in a PSF null.

## Conditional-axis misalignment is quadratic

For a pure target preparation with Bloch vector (\mathbf n), the leading branch-record action is

$$
\Sigma(t)=-\log V(t)
=\frac{t^2}{2}\operatorname{Var}_{\mathbf n}(B)+O(t^3)
=\frac{t^2}{2}\bigl(|\mathbf b|^2-(\mathbf b\cdot\mathbf n)^2\bigr)+O(t^3).
$$

Therefore a preparation blind to the ideal (ZX) term is not necessarily blind to the full measured conditional interaction. For the nominal (+X) preparation,

$$
\boxed{\Sigma_{\rm axis}(t)
=\frac{t^2}{2}(\Omega_{ZY}^2+\Omega_{ZZ}^2)+O(t^3).}
$$

A Wolfram exact check for (B=bX+dZ), (A=0), and (|+x\rangle) returned

$$
V(t)^2=1-\frac{d^2}{b^2+d^2}\sin^2(\sqrt{b^2+d^2}\,t)
$$

and

$$
\Sigma(t)=\frac{d^2t^2}{2}
+\frac{d^2(-2b^2+d^2)t^4}{12}+O(t^6),
$$

confirming the quadratic coefficient.

## Exact axis alignment exposes the quartic common-drift term

If the target is prepared in an eigenstate of the full (B), the quadratic term vanishes. RT-2026-011 gives

$$
\Sigma_{\rm common}(t)
=\frac{t^4}{8}\operatorname{Var}_{\psi_B}(i[A/2,B])+O(t^5).
$$

For Pauli vectors, (i[A/2,B]=-(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma), so in a (B)-eigenstate

$$
\boxed{\Sigma_{\rm common}(t)
=\frac{t^4}{8}|\mathbf a\times\mathbf b|^2+O(t^5).}
$$

A separate Wolfram finite-series check at (\mathbf a=(1,2,3)), (\mathbf b=(4,0,0)) returned (\Sigma=26t^4+O(t^6)), matching (|\mathbf a\times\mathbf b|^2/8=26).

Near the ideal (B\simeq\Omega_{ZX}X),

$$
\Sigma_{\rm common}(t)
\simeq\frac{t^4\Omega_{ZX}^2}{8}(\Omega_{IY}^2+\Omega_{IZ}^2).
$$

Thus a common (IX) term parallel to the ideal conditional axis is harmless to this specific branch-record mechanism, while common (IY/IZ) terms are not.

## Hardware relevance and limits

Ward et al. report that (ZY) is phase-calibrated toward zero; (IX/IY) are addressed by a target cancellation drive; residual (ZZ) is a significant conditional coherent-error source; and (IZ) is their largest identified coherent-error contribution before compensation. They also report control leakage and an unexplained residual error budget. Those error-per-gate values cannot be substituted for (\Sigma): gate infidelity is not branch distinguishability.

For a CR-style PSF calibration arm, the acceptance order should be: (1) bound the actual conditional axis and preparation alignment, (2) after alignment bound the common/conditional commutator, (3) separately include leakage, spectators, control modes, retained memory and drift, and (4) preserve every calibration-compatible ordinary process in the Section-8-style target set.

This static calculation is only a screening diagnostic. An ECR gate is a scheduled, time-dependent echo sequence. The next device-specific step is to reconstruct or obtain (A(t),B(t)) for an actual scheduled pulse, propagate the proposed blind preparation through both branches, and produce an uncertainty band for (V(t)) and (\Sigma_{\rm ordinary}(t)). If the conditional axis varies so that no common blind state exists over the path, that is a negative result for the simple Ramsey-null construction.

**Public source:** https://arxiv.org/abs/2601.20458
