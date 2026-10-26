"""Adversarial numerical checks for 2026-10-26 complex phase-reference bound.

Requires numpy, scipy; deterministic seed. This checks specified finite-dimensional
ordinary-unitary toy models, not a native device or selector physics.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm

SEED = 20261026
rng = np.random.default_rng(SEED)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
p = np.array([1, 0], dtype=complex)


def quality(chi, phase, J):
    deviation = abs(chi - np.exp(-1j * phase))
    ceiling = np.cosh(J) - 1
    if not deviation <= ceiling + 1e-9:
        raise AssertionError((deviation, ceiling, J))
    return deviation / ceiling if ceiling > 0 else 0.0


# Conditional axes vary by segment; common generator H0=0, so J
# and phi are exact sums over segment values.
ratios = []
for num_segments in range(2, 12):
    for case in range(120):
        dt = 0.075 + 0.035 * rng.random()
        phi = J = 0.0
        up, um = p.copy(), p.copy()
        for _ in range(num_segments):
            b = rng.normal(scale=2)
            dx, dy = rng.normal(scale=0.75, size=2)
            B = b * Z + dx * X + dy * Y
            phi += b * dt
            J += np.hypot(dx, dy) * dt
            up = expm(-1j * B * dt / 2) @ up
            um = expm(+1j * B * dt / 2) @ um
        ratios.append(quality(np.vdot(um, up), phi, J))
print("H0=0 cases:", len(ratios), "maximum ratio:", max(ratios))


# General piecewise noncommuting H0 and B. Gauss-Legendre quadrature
# approximates J and phi within each finite-duration constant segment.
nodes, weights = leggauss(20)
rng = np.random.default_rng(SEED)  # independent seeded second batch
ratios = []
for case in range(150):
    phi = J = 0.0
    u0 = np.eye(2, dtype=complex)
    up, um = p.copy(), p.copy()
    for segment in range(5):
        dt = 0.08 + 0.08 * rng.random()
        h = rng.normal(size=3) * 1.8
        b = rng.normal(size=3) * 2.1
        H0 = h[0] * X + h[1] * Y + h[2] * Z
        B = b[0] * X + b[1] * Y + b[2] * Z
        for node, weight in zip(nodes, weights):
            local_t = (node + 1) * dt / 2
            u = expm(-1j * H0 * local_t) @ u0
            bi = u.conj().T @ B @ u
            mean = np.vdot(p, bi @ p).real
            delta = np.linalg.norm(bi @ p - mean * p)
            J += weight * dt / 2 * delta
            phi += weight * dt / 2 * mean
        up = expm(-1j * (H0 + B / 2) * dt) @ up
        um = expm(-1j * (H0 - B / 2) * dt) @ um
        u0 = expm(-1j * H0 * dt) @ u0
    ratios.append(quality(np.vdot(um, up), phi, J))
print("noncommuting H0,B cases:", len(ratios), "maximum ratio:", max(ratios))
print("Numerical checks passed; this is not a proof or a device-level calibration.")
