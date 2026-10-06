# PSF Experimental Database

**Purpose:** Maintain a structured, cumulative catalog of experimentally actionable tests related to Past-Selection Filtrations (PSF), with the explicit long-term goal of supporting a standalone experiments paper that other groups could implement.

This database is **not** an evidence ledger for whether PSF is true. It is a design and comparison layer. Every candidate must distinguish:

- standard unitary/base-PSF predictions,
- optional selector/new-physics predictions,
- ordinary experimental mimics,
- calibration requirements,
- physical implementation assumptions,
- and what result would actually discriminate among them.

The detailed derivations remain in `experiments/`, `red-team/LOG.md`, `literature/LEDGER.md`, and the current manuscript/research state. This database points to those sources rather than duplicating them.

## Files

- `REGISTRY.md` — master table of candidate experiments/platforms.
- `ENTRY_TEMPLATE.md` — required schema for adding a candidate.
- `PAPER_PIPELINE.md` — criteria for promoting candidates into a future experiments paper.
- `entries/` — one structured dossier per mature candidate experiment.

## Maintenance rules

1. **No selector inflation.** A candidate remains ordinary-QM-compatible unless a predeclared measurement separates the complete calibration-compatible ordinary model family from the selector prediction.
2. **No gate-label shortcuts.** Record-nullness and reversal quality must be evaluated on the actual physical trajectory, including spectators, leakage, control modes, drift, retained memory, and other calibrated degrees of freedom.
3. **All-compatible-model rule.** Do not optimize shot counts until calibration implies a sufficiently narrow held-out target-prediction band for all justified ordinary channels/processes.
4. **Platform diversity matters.** Prefer multiple physically distinct architectures rather than overfitting the program to one superconducting implementation.
5. **Negative results stay.** A platform ruled out by an ordinary mimic, uncontrollable hidden record, or insufficient identifiability remains in the registry with status `blocked` or `retired`.
6. **Literature provenance.** Every experimental precedent must have a literature-ledger entry or direct public citation.
7. **Readiness is earned.** A candidate is not `paper-ready` until it has a concrete protocol, explicit standard-QM null, optional PSF prediction, calibration plan, failure-mode audit, and implementability argument.

## Readiness levels

- **L0 — idea:** qualitative concept only.
- **L1 — formalized:** explicit observables and competing predictions exist.
- **L2 — null-audited:** major ordinary mimics and hidden-record pathways identified.
- **L3 — platform-mapped:** mapped to a concrete experimental architecture with measurable controls.
- **L4 — protocol-complete:** calibration, holdout, nuisance uncertainty and acceptance criteria are specified.
- **L5 — paper-ready:** sufficiently mature to appear as an experimentally actionable proposal in a standalone PSF experiments paper.

The weekly research agent should update this database only for material experimental progress.