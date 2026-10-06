# PSF Experimental Candidate Registry

**Established:** 2026-10-05  
**Purpose:** Master index for candidate experiments that could support a future standalone experimental PSF paper.

| ID | Candidate | Platform | Primary fork | Readiness | Status | Main blocker | Core sources |
|---|---|---|---|---:|---|---|---|
| EXP-2026-001 | Native conditional-record echo with calibrated no-record Ramsey control | Superconducting transmons / CR or related native conditional gate | Standard QM: complete ideal recoherence under global inverse; optional selector: residual `nu_echo=V_pre^eta` | L3 | active | Need complete scheduled-pulse ordinary-null certificate; axis rotation, common drift, spectators, leakage, controls and memory remain live | `experiments/ECHO_DISCRIMINATOR.md`; `NO_RECORD_RAMSEY_CONTROL_2026-08-31.md`; `COMPILED_PATH_RECORD_AUDIT_2026-09-07.md`; `NATIVE_SPECTATOR_HIDDEN_RECORD_BUDGET_2026-09-21.md`; `COMMON_DRIFT_COMMUTATOR_NULL_2026-09-28.md`; `CROSS_RESONANCE_PAULI_NULL_DIAGNOSTIC_2026-10-05.md` |
| EXP-2026-002 | Tunable-coupler conditional echo with spectator-suppressed trajectory | Superconducting tunable-coupler CZ/ZZ-style architecture | Same selector-vs-global-reversal fork, but using trajectory-engineered conditional coupling | L2 | active | Need an explicit native Hamiltonian path demonstrating bounded trajectory-wide hidden record action, not just low gate infidelity/leakage | L-2026-020 and P1 |
| EXP-2026-003 | Engineered-reservoir active recoherence test | Circuit QED / photonic cat + finite reservoir | Distinguish natural loss of spontaneous recoherence from deliberately implemented microscopic reversal; optional selector would require residual after calibrated inverse | L1 | active | Existing work shows unitary emergent irreversibility, not a controlled global inverse; must establish whether reservoir+bus can be reversed well enough for a discriminating test | L-2026-027; RT-2026-004 |
| EXP-2026-004 | Reversible measurement / distributed-record scaling test | Trapped ions or other high-control few-body platform | Scale from known reversible measurement toward multiple controlled record fragments and test restoration after explicit inverse | L1 | active | Need a concrete redundant-record architecture and physically meaningful selector-sensitive scaling beyond ordinary reversible measurement | L-2026-008; RT-2026-004 |
| EXP-2026-005 | Redundant-record Darwinism circuit followed by controlled inverse | Multi-qubit superconducting processor | Create tunable redundant records, then deliberately uncompute them and compare held-out echo against calibrated ordinary family | L2 | active | Published Darwinism demonstrations establish record formation but not yet the full PSF-grade inverse/null/calibration protocol | L-2026-007; P1 |

## Notes on current ranking

### EXP-2026-001 — lead candidate
This is currently the most developed candidate because the repository already contains explicit selector and ordinary-null formulas, calibration-power analysis, a mechanism-null control concept, and multiple red-team attacks. Its weakness is precisely why it remains L3 rather than L4: the device-level scheduled trajectory has not yet been certified.

### EXP-2026-002 — hardware alternative
This is deliberately kept separate from EXP-2026-001. A tunable-coupler trajectory may avoid some CR-specific axis and control-line issues, but low leakage or high fidelity is not equivalent to low hidden record action.

### EXP-2026-003 — conceptually valuable cross-platform candidate
Recent engineered-reservoir work is especially useful because it naturally realizes many environmental degrees of freedom and emergent loss of recoherence under unitary dynamics. It is not yet a PSF discriminator because spontaneous non-revival is not the same as failure of a controlled global inverse.

### EXP-2026-004 — small-system control benchmark
The purpose is not to claim few-body measurement reversal tests PSF directly. The value would be a high-control platform in which the number and strength of deliberately written records can be scaled while preserving reversible access to the relevant environment.

### EXP-2026-005 — record-first architecture
This starts from demonstrated Quantum-Darwinism-style redundant-record generation and asks whether a full calibrated inverse can be added. It may merge with EXP-2026-001 if the optimal implementation turns out to be the same hardware/protocol; keep separate until that is established.

## Promotion rule

Do not promote any entry above L3 unless the calibration data define a held-out target-prediction band for the complete justified ordinary process family. Do not promote any entry to L5 merely because the hardware can generate decoherence, redundancy, or apparent irreversibility.

## Future expansion targets

The research agent should actively look for mature experimental precedents in trapped ions, neutral atoms, cavity/circuit QED, photonics, spin ensembles, and other platforms where both **record creation and sufficiently complete reversal** are controllable. Add a new candidate only when the literature supports a concrete architecture, not just a conceptual analogy.