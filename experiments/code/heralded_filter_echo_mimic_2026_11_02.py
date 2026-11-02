#!/usr/bin/env python3
"""Ordinary postselected-filter echo mimic; reproducible 4x4 matrix audit.
Requires numpy and scipy. No PSF selector is simulated as a physical dynamic.
"""
import numpy as np
from scipy.linalg import block_diag

SEED = 20261102
rng = np.random.default_rng(SEED)


def experiment(theta, a, phase):
    c, s = np.cos(theta), np.sin(theta)
    r = np.array([[c, -s], [s, c]], dtype=complex)
    u = block_diag(np.eye(2), r)
    k = np.kron(np.eye(2), np.diag([1.0, a * np.exp(1j * phase)]))
    initial = np.array([1, 0, 1, 0], dtype=complex) / np.sqrt(2)
    out = u.conj().T @ k @ u @ initial
    success = np.vdot(out, out).real
    # C = <X>+i<Y> = 2 rho_{10} for system S (first qubit)
    coherence = 2 * (out[2] * np.conj(out[0])
                     + out[3] * np.conj(out[1])) / success
    return success, coherence


def analytic(theta, a, phase):
    c, s = np.cos(theta), np.sin(theta)
    success = 1.0 - (1 - a * a) * s * s / 2
    coherence = (c * c + a * np.exp(1j * phase) * s * s) / success
    return success, coherence


def main():
    max_p_error = max_c_error = 0.0
    for _ in range(5000):
        theta = rng.uniform(0.0, 1.45)
        a = rng.uniform(0.0, 1.0)
        phase = rng.uniform(-np.pi, np.pi)
        observed = experiment(theta, a, phase)
        predicted = analytic(theta, a, phase)
        max_p_error = max(max_p_error, abs(observed[0] - predicted[0]))
        max_c_error = max(max_c_error, abs(observed[1] - predicted[1]))
    assert max_p_error < 2e-14, max_p_error
    assert max_c_error < 2e-14, max_c_error
    a = np.sqrt(2) - 1
    eta = (1 - a) ** 2
    print("random checks: 5000; seed", SEED)
    print("max |p error|:", max_p_error)
    print("max |C error|:", max_c_error)
    print("matched a, eta:", a, eta)
    for theta in (0.2, 0.4, 0.7):
        p, coherence = analytic(theta, a, 0.0)
        selector_comparator = np.cos(theta) ** eta
        print(theta, p, coherence.real, selector_comparator,
              coherence.real - selector_comparator)


if __name__ == "__main__":
    main()
