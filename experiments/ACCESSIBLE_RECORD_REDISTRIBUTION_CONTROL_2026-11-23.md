# Accessible-record redistribution at fixed global decoherence: an adversarial P1 control candidate

**Date assessed:** 2026-11-23  
**Status:** exact, finite-dimensional **ordinary-quantum calculation** and *conditional* PSF experiment-design proposal; **not** a calibrated device protocol, selector prediction without additional premises, proof of new physics, or originality claim for the underlying qubit-chain dynamics.

## New public source and source chronology

Sugumi Kanno and Jiro Soda, *Entanglement, records, and quantum recovery in qubit chains*, arXiv:2611.26368v1, submitted **2026-11-19**: https://arxiv.org/abs/2611.26368 ; full HTML https://arxiv.org/html/2611.26368v1 . The paper explicitly distinguishes locally readable records, entanglement, accessible phase and recovery in controlled-rotation chains. It finds environment-only redistribution can change fragment records while leaving the source qubit's reduced state unchanged. It **postdates** approved PSF 9.0.2 (2026-09-07) and the original November 2025 PSF preprint, so is contemporary convergence and a useful ordinary-QM design input, not earlier priority against PSF. The branch-state unitary structure here is their model, not a new PSF mathematical construction.

**Terminology trap:** The authors' phase-visibility quantity in §2.4 is not in general the PSF *root fidelity* envelope of conditional record states. Their branch trace distinguishability for a given fragment is directly comparable to PSF's accessible-record trace distinguishability. Keep both notions and actual interferometric visibility separate.

## Exact three-qubit model

Take a source qubit S and environment qubits E1,E2, initially |0> on both environments. Let U1 be S-controlled R_y(theta) on E1 and U2 be E1-controlled R_y(chi) on E2. On the two source branches, after U=U2 U1,

r0=|00>,
r1=c|00>+s d|10>+s e|11>,

where c=cos(theta/2), s=sin(theta/2), d=cos(chi/2), e=sin(chi/2), and 0<=theta,chi<=pi. This is a conventional *pure unitary* circuit.

**Full environmental root fidelity:** V_all=|<r0|r1>|=c, independent of chi. Thus, before inverse, the reduced-system coherence in an equal superposition is independent of chi. **Exact complete physical inverse:** U1† U2† U2 U1=I, and ordinary S echo visibility is 1 for every chi.

**Observer restricted to E2**: The branch-zero record state is rho_0^E2=|0><0|; the branch-one state is

rho_1^E2 =
[[c²+s²d², s²de],
 [s²de,     s²e²]].

For PSF's *record-state root fidelity* on the algebra A=B(E2), the result is

V_E2=sqrt(1-s²e²),
Sigma_E2=−log V_E2,
D_E2=(1/2)||rho_0^E2−rho_1^E2||_1=s² e.

The E2 Z-population difference is s² e², but its transverse (X) branch-expectation difference is 2 s² d e. For theta,chi both small and of the same order, the optimal D_E2 signal scales as theta² chi (cubic), while the Z-only population signal scales as theta² chi² (quartic). This is a **measurement-selection** warning, not an exotic effect. The relation V_E2²−V_all²=s²d²>=0 checks fidelity data processing under restriction E1E2->E2.

For theta=pi/2 and chi in {0,pi/2,pi}, the columns (V_all,V_E2,D_E2,Sigma_E2,Z-population difference) are:
- chi=0: (0.7071067812,1,0,0,0)
- chi=pi/2: (0.7071067812,0.8660254038,0.3535533906,0.1438410362,0.25)
- chi=pi: (0.7071067812,0.7071067812,0.5,0.3465735903,0.5).

**Wolfram check, 2026-11-23:** Constructed 4-component conditional vectors and traced out E1 to obtain rho_1^E2, V_E2, D_E2, values above, and V_E2²−V_all²=s²d². Exact algebra is independently reproducible using the supplied r0/r1 amplitudes; no device data. The evaluator returned the equivalent expression V_E2 = Sqrt[3+Cos[chi]+Cos[theta]−Cos[chi] Cos[theta]]/2.

## Experimental-method opportunity, strictly conditional

The internal environment-to-environment coupling chi is a **candidate orthogonal intervention**: at fixed theta, one can change the evidence accessible *on E2* without changing full-environment overlap, reduced-S coherence, or the ideal complete-reversal QM prediction. The optional two-path selector postulate of manuscript §11 **does not specify this experiment's outcome without additional physical choices**. If and only if the physical record algebra is independently fixed to E2 at a predeclared stage, with the selector driven by Sigma_E2 at that stage, and eta fixed prospectively, its *conditional phenomenological* fork is

nu_sel(theta,chi|eta) = V_E2^eta = (1−s²e²)^(eta/2)

against ideal ordinary complete echo nu_QM=1. For a competing hypothesis in which selector action follows *all* E1E2 records, the conditional selector fork depends on V_all=c and is **independent of chi**. If E1 is actually accessible at that stage, E2-only V is not the correct PSF evidence action. The contrast therefore pressures P7 to specify the physical filtration, observer interface, record availability and stage/path rule independently; a later redefinition based on an observed residual would invalidate discrimination.

**Do not overinterpret fixed full decoherence:** Changing chi changes actual U2 pulse exposure, inverse demands, coupling crosstalk, leakage, spectators, and environmental correlations; realistic ordinary residuals can therefore be chi-dependent. A calibration-compatible full multi-time ordinary process *set* is required, not the ideal nu_QM=1 alone. Separate E2 probe trials used for state tomography alter the protocol; those are calibration trials, not the same undisturbed echo trials. Readout must include phase-sensitive X/Y observables where needed, not just Z populations. A measured restricted-fidelity change is entirely ordinary QM.

## How to advance P1 rather than overclaim

1. Define platform-native U1/U2, timing and whether E1 is physically inaccessible versus merely ignored. The algebra B(E2) and measurement capabilities must be justified in the hardware context.
2. Predeclare a fixed E2 access interface, candidate stage or trajectory rule, and eta (or a disjoint calibration procedure); preserve the alternative all-E1E2 prediction as an adversarial selector specification check.
3. Characterize native U1, U2 and their inverses under each chi using comprehensive phase-sensitive process/instrument calibration, including memory, spectators, leakage, and context transfer. The source paper's exact ideal unitary is not a device certificate.
4. Form the **entire** ordinary compatible echo target set from calibration before holding out the chi sweep. Optimize statistical power only after a finite-width separated prediction band exists. Prefer an ordinary-null / nuisance-sensitive arm actually matched to U2 exposure.
5. Compare this candidate to EXP-2026-005 (record-first multi-qubit circuits) and EXP-2026-001 (native conditional-gate echo) without changing current readiness. This is a controlled toy-case design insight, not a new experimentally certified candidate.

## Multi-time characterization prior art

- Giarmatzi et al., *Multi-time quantum process tomography on a superconducting qubit*, *Quantum* **9**, 1952 (2025; journal publication 2025-12-18), https://doi.org/10.22331/q-2025-12-18-1952 . Hardware multi-time correlated-noise tomography with sequential measure-and-prepare interventions; full characterization **within its assumed accessible experimental process and trusted operations**, not automatic certification of all hidden degrees.
- Roy, Srivastava, Giarmatzi & Gilchrist, *Practical Tomography of Multi-Time Processes*, arXiv:2604.01482 (2026-04-01), https://arxiv.org/abs/2604.01482 . Theoretical one-coherent-ancilla construction for an informationally complete family of multi-time probes, avoiding midcircuit measurement/reset in the ideal protocol; implementation, conditioning and trustworthy controls remain to be established.
- Relevant longstanding quantum Darwinism, consistent histories and existing PSF Section 8 process-tensor citations: no claim that the source qubit-chain dynamics, local state tomography or generic environment-only redistribution originated with PSF.

## Epistemic verdict / canonical-state boundary

**Material P1 design increment and red-team specification boundary.** Identified a distinct, calculable record-accessibility intervention at fixed full-state decoherence and ordinary ideal echo, plus an E2 population-only blind spot. It does **not** produce a device-specific all-compatible ordinary target-prediction certificate, independently justify a selector-path postulate, establish selector physics, change manuscript 9.0.2, supersede the November 16 P7 Gram no-go, alter N1–N5 novelty, or promote EXP readiness. Carry this proposal into the P1/EXP-2026-005 control-design comparisons only after hardware path access is physically specified.