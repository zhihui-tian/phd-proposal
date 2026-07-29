# Detailed PhD Proposal Outline

## Document purpose

This document was created in Stage 3 and revised in Stage 4 after committee-style review. It is a detailed architecture for the proposal, not a full prose draft. Each subsection specifies:

- its purpose;
- its central argument;
- manuscript evidence;
- proposed future content;
- an expected figure or table;
- missing information or decisions.

## Status convention

- **COMPLETED PRIOR WORK:** Neighborhood-driven anisotropy/lattice-pinning study and 3D-PRIMME. The 3D-PRIMME manuscript is currently under review.
- **ONGOING WORK - STABLE PRELIMINARY RESULTS:** All results reported in the experimental-surrogate manuscript.
- **ONGOING WORK:** Multi-window experimental analysis.
- **PROPOSED FUTURE WORK:** Aim 2 paired reference-surrogate comparisons and the unfinished components of Aims 1 and 3.
- `[AUTHOR INPUT REQUIRED]`: information that must ultimately come from the author.
- `[NEEDS LITERATURE SUPPORT]`: claims that require sources beyond the three manuscripts.
- `[NEEDS QUANTITATIVE CRITERION]`: prospective success thresholds to be fixed before final analysis.

## Locked dissertation logic

> **Physically controlled simulation rules -> scalable simulation-trained surrogate -> reliable experimental learning -> paired validation within simulation and experiment -> physical interpretation**

The proposal must present this as one causal research program. It must not read as three manuscripts placed side by side.

## Overarching research question

**How can local, physics-guided machine learning progress from learning physically controlled simulation dynamics to learning reliably from sparse 4D experimental observations, distinguish experimental information from simulator and surrogate errors, and ultimately support physical interpretation of mesoscale grain growth?**

## Central hypothesis

**Local grain-growth evolution is sufficiently encoded in carefully curated neighborhood observations to support reliable three-dimensional prediction across held-out experimental conditions; empirical uncertainty and sensitivity assessment can identify the domain in which those predictions are trustworthy, while paired validation of simulation-trained predictions against simulation and experiment-trained predictions against experiment can establish which learned relationships are reliable enough for subsequent physical interpretation.**

## Aim synopsis

| Aim | Scientific question | Maturity |
|---|---|---|
| Aim 1. Reliable and generalizable learning from sparse 4D experiments | Under what data-curation, training, and validation conditions can an experiment-trained surrogate be trusted? | Stable single-window preliminary results; multi-window analysis ongoing; core empirical uncertainty/generalization work proposed |
| Aim 2. Paired validation in simulation and experiment | How faithfully does each surrogate reproduce its own reference domain: \(S\) versus \(\hat{S}\), and \(E\) versus \(\hat{E}\)? | Proposed future work |
| Aim 3. Input- and output-side interpretation of experimentally learned evolution rules | Which spatial information does the reliable experiment-trained operator use, and how is it converted into local evolution decisions? | Simulation-domain method development and preliminary evidence completed; experimental transfer proposed |

## Recommended narrative balance

- Background and motivation: approximately 20-25%.
- Completed foundations: approximately 20-25%.
- Experimental preliminary work: approximately 15-20%.
- Proposed aims, integration, risk, and timeline: approximately 35-45%.

Exact page allocations depend on the program's proposal format. `[AUTHOR INPUT REQUIRED]`

---

# Front Matter: Title

## Recommended title

**From Controlled Simulations to 4D Experiments: Local Machine Learning of Grain-Growth Dynamics**

- **Purpose:** Communicate the causal movement from simulation physics to experimental learning without claiming that interpretation is already complete.
- **Central argument:** The dissertation's novelty lies in progressively replacing prescribed simulation supervision with measured 4D evolution while preserving a local, physics-guided learning framework.
- **Manuscript evidence:** Neighborhood control of simulation behavior; scalable local learning in 3D-PRIMME; direct training from lab-DCT data. [Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17; 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15; Experimental surrogate manuscript, §§2-5, PDF pp. 3-17]
- **Proposed future content:** Aim 1 multi-window reliability, Aim 2 paired simulation and experimental validation, and Aim 3 interpretation.
- **Expected visual:** None.
- **Missing information:** Confirm whether the program prefers a short conceptual title or a descriptive title with a subtitle. `[AUTHOR INPUT REQUIRED]`

## Alternative titles

1. **Predictive and Interpretable Machine Learning for Mesoscale Grain Growth**
2. **Physics-Guided Local Learning of Simulated and Experimental Grain Growth**
3. **Experimentally Grounded Surrogate Learning for Three-Dimensional Grain Growth**
4. **Learning Mesoscale Grain-Growth Rules Across Simulation and Experiment**

- **Purpose:** Provide title options with different emphasis.
- **Central argument:** Titles 2-4 emphasize the established simulation-to-experiment sequence; Title 1 is now supported by the incorporated Aim 3 method-development evidence.
- **Manuscript evidence:** Same cross-manuscript sequence as §1.1.
- **Proposed future content:** Revisit the preferred title after the Aim 3 experimental transfer determines the final claim level.
- **Expected visual:** None.
- **Missing information:** Final achieved Aim 3 claim level after experimental validation.

---

# Front Matter: Abstract

The final abstract should be written only after the body is stable. At outline stage, it should follow the five-part structure below.

## Problem and significance

- **Purpose:** Establish why reliable prediction of three-dimensional grain growth matters.
- **Central argument:** Grain growth is governed by local boundary evolution but manifests through long-time, large-volume statistical behavior; direct simulation is computationally demanding, while a surrogate's validity depends on its training labels.
- **Manuscript evidence:** Grain-growth motivation and computational limitations. [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2]
- **Proposed future content:** One sentence connecting prediction to experimentally observed dynamics.
- **Expected visual:** None.
- **Missing information:** Application context most important to the committee - general microstructure control, ceramics, or broader materials design. `[AUTHOR INPUT REQUIRED]`

## Completed foundations

- **Purpose:** Establish feasibility without allowing prior work to dominate the abstract.
- **Central argument:** Completed work shows, first, that neighborhood design controls simulation artifacts and anisotropy and, second, that a local 3D surrogate can learn and scale those controlled simulation rules.
- **Manuscript evidence:** Neighborhood-dependent anisotropy and pinning; 3D-PRIMME scaling, kinetics, topology, and anisotropy. [Source: Neighborhood manuscript, §§5-7, PDF pp. 10-17; 3D-PRIMME manuscript, §§3-5, PDF pp. 6-15]
- **Proposed future content:** None; label as completed foundations.
- **Expected visual:** None.
- **Missing information:** None.

## Research gap

- **Purpose:** Identify the ceiling of simulation supervision.
- **Central argument:** A simulation-trained surrogate cannot learn experimentally relevant behavior that the simulator does not contain, but experimental labels introduce registration, linkage, sampling, and measurement uncertainty.
- **Manuscript evidence:** Simulation idealization and experimental-label challenges. [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2; Experimental surrogate manuscript, §1, PDF pp. 1-3]
- **Proposed future content:** Express the gap as reliability plus source-of-error separation, not merely "more data are needed."
- **Expected visual:** None.
- **Missing information:** None.

## Preliminary experimental evidence and aims

- **Purpose:** Show that the proposed research is feasible.
- **Central argument:** Stable preliminary results demonstrate direct training from one curated DCT interval and held-out evaluation; the proposal will extend reliability across windows, compare each surrogate with its own reference domain, and interpret only validated learned relationships.
- **Manuscript evidence:** Curation, direct training, replicate results, held-out distributions, topology, grain kinetics, and drift. [Source: Experimental surrogate manuscript, §§2-5, Figs. 1-6 and Table 1, PDF pp. 3-17]
- **Proposed future content:** One sentence per aim.
- **Expected visual:** None.
- **Proposed future content:** Input-side scale attribution, output-side response probing, and the evidence ladder from model interpretation to physical attribution.

## Expected contribution

- **Purpose:** End with the dissertation-level payoff.
- **Central argument:** The work will establish when experimental 4D data can train trustworthy local surrogates, determine what experiment adds beyond controlled simulation, and create a defensible route from prediction to physical interpretation.
- **Manuscript evidence:** Cross-manuscript synthesis.
- **Proposed future content:** Final phrasing should match achieved Aim 3 scope.
- **Expected visual:** None.
- **Proposed future content:** State the final Aim 3 claim at the strongest evidentiary level supported by the experimental transfer.

---

# 1. Introduction and Research Vision

## 1.1 The multiscale prediction problem

- **Purpose:** Introduce grain growth as a local-interaction process whose consequences must be predicted over large spatial and temporal scales.
- **Central argument:** Grain-boundary migration is local, but useful microstructure prediction requires large three-dimensional systems, long rollouts, and statistical fidelity.
- **Manuscript evidence:** Locality and computational scaling motivation. [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2]
- **Proposed future content:** Connect large-scale prediction to experimental observation and material-specific behavior.
- **Expected visual:** **Figure 1A**, schematic connecting local boundary updates to grain-scale topology and macroscopic grain-size statistics.
- **Missing information:** External literature on material-property relevance and current computational limits. `[NEEDS LITERATURE SUPPORT]`

## 1.2 Why the training source matters

- **Purpose:** Establish the proposal's governing principle.
- **Central argument:** Machine-learning surrogates reproduce rules present in their labels; therefore, the physical content of a simulator or experiment must be understood before surrogate accuracy can be interpreted.
- **Manuscript evidence:** Neighborhood-dependent simulation behavior and 3D-PRIMME label construction. [Source: Neighborhood manuscript, §§3-6, PDF pp. 6-16; 3D-PRIMME manuscript, §§2.1-2.2, PDF pp. 2-5]
- **Proposed future content:** Use this principle to motivate Aim 2's two paired fidelity assessments.
- **Expected visual:** **Figure 1B**, causal flow: training source -> learned local operator -> rollout behavior -> validation.
- **Missing information:** Literature on simulation bias and data-driven surrogate error. `[NEEDS LITERATURE SUPPORT]`

## 1.3 Progressively removing assumptions

- **Purpose:** Present the dissertation as a sequence rather than three projects.
- **Central argument:** Neighborhood work controls the simulation teacher; 3D-PRIMME learns that teacher; experimental training replaces prescribed dynamics with measured dynamics; comparison and interpretation then become scientifically meaningful.
- **Manuscript evidence:** Full cross-manuscript sequence. [Source: Neighborhood manuscript, Conclusions, PDF pp. 15-17; 3D-PRIMME manuscript, Conclusion, PDF p. 15; Experimental surrogate manuscript, Introduction and Discussion, PDF pp. 1-3 and 15-17]
- **Proposed future content:** Aims 1-3.
- **Expected visual:** **Figure 1C**, the proposal's main causal roadmap.
- **Proposed future content:** Use the multiscale attribution and full-Jacobian studies to complete the final interpretation arrow.

## 1.4 Overarching question and central hypothesis

- **Purpose:** State the proposal's testable intellectual core.
- **Central argument:** Reliable local experimental learning and source-aware comparison can bridge prediction and physical interpretation.
- **Manuscript evidence:** Feasibility foundations from all three manuscripts.
- **Proposed future content:** State the overarching question and central hypothesis exactly as given in the document-control section.
- **Expected visual:** None; optionally a boxed hypothesis.
- **Missing information:** Committee preference for one central hypothesis versus an overarching objective. `[AUTHOR INPUT REQUIRED]`

---

# 2. Completed Foundations: From Simulation Physics to 3D Surrogate Learning

**Section status: COMPLETED PRIOR WORK**

## 2.1 Neighborhood-dependent simulation physics

### Stochastic update rules and lattice pinning as a training-data problem

- **Purpose:** Introduce MCP, MF, and N-MCP, then reframe lattice pinning from an isolated numerical issue into a label-quality issue for surrogate learning.
- **Central argument:** Stochastic models provide efficient labels, but their local update rules and neighborhoods encode effective anisotropy and kinetic variability. Artificial inclination preference therefore alters the rules presented to a surrogate and must be controlled before simulation training can be interpreted physically.
- **Manuscript evidence:** MCP/MF formulation, N-MCP, and lattice-pinning behavior. [Source: Neighborhood manuscript, §§1-3 and §5.1, Eqs. 1-12, PDF pp. 3-7 and 10-11]
- **Proposed future content:** None; use as completed foundation.
- **Expected visual:** **Figure 3A**, MCP versus Gaussian-neighborhood inclination distributions.
- **Missing information:** Confirm which final figure panels are preferred for proposal reuse. `[AUTHOR INPUT REQUIRED]`

### Neighborhood-to-anisotropy framework

- **Purpose:** Explain the physical mechanism by which a numerical neighborhood shapes effective interfacial behavior.
- **Central argument:** The kernel's directional moments define an effective inclination-dependent interfacial energy and Wulff response; discrete sampling and stochasticity regulate how that response appears.
- **Manuscript evidence:** Continuous and discrete kernel analysis. [Source: Neighborhood manuscript, §§3.2-3.3, Eqs. 9-12, PDF pp. 6-7]
- **Proposed future content:** Use one central equation and a conceptual explanation rather than reproducing the entire derivation.
- **Expected visual:** **Figure 3B**, neighborhood shapes paired with theoretical and measured inclination distributions.
- **Missing information:** Final equation/notation choices for consistency with the proposal. `[AUTHOR INPUT REQUIRED]`

### Completed results

- **Purpose:** Summarize the evidence that neighborhood choice controls anisotropy.
- **Central argument:** Gaussian sampling suppresses strong lattice-aligned preferences; reshaped, square, and star neighborhoods create graded anisotropy; rotating the neighborhood rotates the inclination response; MF sampling produces lower von Neumann-Mullins scatter than MCP/N-MCP in the reported comparison.
- **Manuscript evidence:** Figs. 2-9 and Conclusions. [Source: Neighborhood manuscript, §§5-7 and Supplementary materials, PDF pp. 10-21]
- **Proposed future content:** None.
- **Expected visual:** **Figure 3C**, compact three-panel summary: isotropy, controlled anisotropy, rotation test. **Table 3**, method versus pinning, statistical scatter, and computational cost.
- **Missing information:** Final figure selection and whether runtime belongs in the main proposal. `[AUTHOR INPUT REQUIRED]`

### Enabling role for 3D-PRIMME

- **Purpose:** Make the first causal transition explicit.
- **Central argument:** The neighborhood study supplies the physical rationale for choosing and diagnosing the MF simulation teacher used by 3D-PRIMME; it does not directly compare surrogate performance across neighborhoods.
- **Manuscript evidence:** MF kernel control in both manuscripts. [Source: Neighborhood manuscript, §§3-6, PDF pp. 6-16; 3D-PRIMME manuscript, §2.1, PDF pp. 2-3]
- **Proposed future content:** A one-paragraph bridge into Section 2.2.
- **Expected visual:** Reuse Figure 1C arrow from Foundation 1 to Foundation 2.
- **Missing information:** None.

---

## 2.2 Simulation-trained 3D-PRIMME

**Section status: COMPLETED PRIOR WORK; MANUSCRIPT UNDER REVIEW**

### Local architecture and physics regulation

- **Purpose:** Describe how 3D-PRIMME converts grain-ID maps into a scalable local evolution operator.
- **Central argument:** The interface-site representation, observation window, and action window remove arbitrary grain-ID meaning while constraining updates to local boundary geometry.
- **Manuscript evidence:** Architecture, Fig. 1, Table 1, and Eqs. 5-7. [Source: 3D-PRIMME manuscript, §2.2, PDF pp. 3-5]
- **Proposed future content:** Clarify that "physics-regulated" refers to representation and locality, not universal physical truth.
- **Expected visual:** **Figure 4A**, simplified 3D-PRIMME workflow adapted from manuscript Fig. 1.
- **Missing information:** Confirm whether architecture details should be reproduced or referenced. `[AUTHOR INPUT REQUIRED]`

### Controlled simulation training data

- **Purpose:** Connect model learning to the simulation teacher.
- **Central argument:** Isotropic and inclination-dependent MF data provide known local rules that test whether the architecture can recover kinetics and directional behavior.
- **Manuscript evidence:** 200 isotropic and 200 anisotropic sequences; \(100^3\) domains; two-state training sets; [111]-biased covariance. [Source: 3D-PRIMME manuscript, §2.1, PDF pp. 2-3]
- **Proposed future content:** None; completed feasibility foundation.
- **Expected visual:** **Figure 4B**, isotropic versus anisotropic training-data construction.
- **Missing information:** None.

### Completed performance results

- **Purpose:** Establish feasibility for experimental learning.
- **Central argument:** A local operator trained from minimal supervision reproduces major MF kinetics and topology, has low training-replicate variability, scales from \(100^3\) to \(1024^3\), and learns prescribed inclination dependence.
- **Manuscript evidence:** Window sensitivity, replicate uncertainty, spatial scaling, data efficiency, and anisotropy. [Source: 3D-PRIMME manuscript, §§3.1-3.5, Figs. 2-8, PDF pp. 6-13]
- **Proposed future content:** None.
- **Expected visual:** **Figure 4C**, spatial-extrapolation morphology; **Figure 4D**, quantitative scaling curves; and **Figure 4E**, inclination distributions. **Table 4**, training domain, largest test domain, supervision amount, rollout length, and metrics.
- **Missing information:** Choose a small subset of results to avoid over-weighting completed work. `[AUTHOR INPUT REQUIRED]`

### Scientific lesson and limitation

- **Purpose:** Make the second causal transition.
- **Central argument:** 3D-PRIMME demonstrates scalable recovery of the MF rule, not universal grain-growth physics; its geometry-only representation and simulation supervision define the ceiling that motivates experiment.
- **Manuscript evidence:** Introduction, Discussion, and Conclusion. [Source: 3D-PRIMME manuscript, §1 and §§4-5, PDF pp. 1-2 and 13-15]
- **Proposed future content:** Transition directly to Section 2.3.
- **Expected visual:** **Figure 4D**, "high fidelity to teacher does not imply high fidelity to experiment."
- **Missing information:** None.

---

## 2.3 What the completed foundations establish—and what they cannot establish

### The simulator ceiling

- **Purpose:** State why the dissertation cannot stop at 3D-PRIMME.
- **Central argument:** A surrogate cannot infer mechanisms absent from its labels; improving model accuracy against MF cannot establish fidelity to an experiment.
- **Manuscript evidence:** Simulation idealization statements and experimental manuscript framing. [Source: 3D-PRIMME manuscript, §1, PDF p. 1; Experimental surrogate manuscript, §1, PDF pp. 1-3]
- **Proposed future content:** External examples of simulation-experiment discrepancies in grain-boundary motion.
- **Expected visual:** **Figure 5A**, two error sources: simulator discrepancy and surrogate approximation.
- **Missing information:** Literature examples and citations. `[NEEDS LITERATURE SUPPORT]`

### Distinguishing three kinds of agreement

- **Purpose:** Prevent overclaiming.
- **Central argument:** Voxel agreement, statistical agreement, and mechanistic agreement are different; a model can preserve grain-size statistics while diverging at topology or individual-grain level.
- **Manuscript evidence:** Declining voxel accuracy but stable simulation statistics; experimental size agreement with topology and rate limitations. [Source: 3D-PRIMME manuscript, §3.1, PDF pp. 6-7; Experimental surrogate manuscript, §4, PDF pp. 9-14]
- **Proposed future content:** Use this hierarchy as the validation logic for Aims 1-3.
- **Expected visual:** **Table 5**, prediction level, metric, what it supports, and what it cannot establish.
- **Missing information:** None.

### Why direct experimental training is the necessary next test

- **Purpose:** Complete the transition from completed foundations to ongoing work.
- **Central argument:** Direct experimental supervision allows measured evolution to define the target, but only after coherent acquisition artifacts are removed and residual uncertainty is measured.
- **Manuscript evidence:** Experimental manuscript Introduction. [Source: Experimental surrogate manuscript, §1, PDF pp. 1-3]
- **Proposed future content:** Lead into experimental challenges and preliminary work.
- **Expected visual:** Figure 5A extended to show the experimental branch.
- **Missing information:** None.

---

# 3. Experimental Foundation and Remaining Research Gap

## 3.1 Challenges of learning from sparse 4D experiments

### Temporally sparse but spatially rich data

- **Purpose:** Explain why one scan pair may still support local learning.
- **Central argument:** A 4D experiment contains few time intervals but many local boundary-centered training examples; these examples are spatially overlapping and cannot be treated as independent evidence of generalization.
- **Manuscript evidence:** Approximately \(8 \times 10^5\) local examples and the limitation of the random 80/20 split. [Source: Experimental surrogate manuscript, §3, PDF pp. 8-9]
- **Proposed future content:** Blocked or cross-window validation in Aim 1.
- **Expected visual:** **Figure 5B**, few time states -> many local patches -> need group-level validation.
- **Missing information:** Statistical treatment of overlapping samples. `[NEEDS LITERATURE SUPPORT]`

### Registration, distortion, linkage, and clipping

- **Purpose:** Define experimental curation as part of the scientific method, not preprocessing detail.
- **Central argument:** Voxel-level labels inherit coherent scan motion, residual distortion, identity mismatch, and surface clipping; these defects can be learned as spurious dynamics.
- **Manuscript evidence:** Curation protocol and drift comparison. [Source: Experimental surrogate manuscript, §2 and Fig. 1, PDF pp. 3-7]
- **Proposed future content:** Multi-window and registration-sensitivity analysis in Aim 1.
- **Expected visual:** **Figure 5C**, artifact pathway and curation gate.
- **Missing information:** Final multi-window registration design. **ONGOING WORK**

### Detection limits and acquisition uncertainty

- **Purpose:** Explain why small-grain statistics and individual-grain validation require confidence-aware analysis.
- **Central argument:** Detection limits, segmentation churn, unlinked grains, and unresolved porosity produce structured label uncertainty rather than simple independent noise.
- **Manuscript evidence:** Approximately 20-micrometer confidence limit, unlinked voxels, and porosity discussion. [Source: Experimental surrogate manuscript, §§2-3 and §5, PDF pp. 5-8 and 15-17]
- **Proposed future content:** Threshold sensitivity and uncertainty decomposition in Aim 1.
- **Expected visual:** **Table 6**, experimental uncertainty source, affected label/metric, current mitigation, and future test.
- **Missing information:** Instrument-specific confidence calibration. `[NEEDS LITERATURE SUPPORT]`

### Validation must be directional and multilevel

- **Purpose:** Define the standard of evidence for experimental learning.
- **Central argument:** Aggregate loss and grain-size statistics can miss coherent drift, topology error, or individual-grain underprediction; validation must span field, direction, topology, grain, and population levels.
- **Manuscript evidence:** Drift, size distributions, faces per grain, and grain-volume change. [Source: Experimental surrogate manuscript, §4, Figs. 3-6 and Table 1, PDF pp. 9-15]
- **Proposed future content:** Aim 1 metric hierarchy and empirical uncertainty/sensitivity analysis; formal calibration is optional.
- **Expected visual:** **Figure 5D**, multilevel validation pyramid.
- **Missing information:** Prospective success thresholds. `[NEEDS QUANTITATIVE CRITERION]`

---

## 3.2 Experimental data curation and direct training

**Section status: ONGOING WORK WITH STABLE PRELIMINARY RESULTS**

### Dataset and experimental window

- **Purpose:** Establish the measured training source.
- **Central argument:** A five-state lab-DCT annealing series of undoped alumina provides voxelized grain-ID maps at uniform two-hour increments; one curated volume is used for training and held-out evaluation.
- **Manuscript evidence:** Dataset description, full volume, voxel size, annealing states, and analysis-window statistics. [Source: Experimental surrogate manuscript, §2, PDF pp. 3 and 5-7]
- **Proposed future content:** Multiple windows from the same experimental volume. **ONGOING WORK**
- **Expected visual:** **Figure 6A**, full specimen with selected and future candidate windows.
- **Missing information:** Number and location of planned additional windows. `[AUTHOR INPUT REQUIRED]`

### Interpolation-free curation and label construction

- **Purpose:** Establish label fidelity.
- **Central argument:** Residual-driven window selection, integer affine registration, in-place trimming, and overlap-based linkage remove major coherent artifacts without smoothing or synthesizing grain labels.
- **Manuscript evidence:** Fig. 1 and §2. [Source: Experimental surrogate manuscript, Fig. 1 and §2, PDF pp. 4-7]
- **Proposed future content:** Test reproducibility across additional windows and registration choices.
- **Expected visual:** **Figure 6B**, before/after boundary mismatch and rollout drift.
- **Missing information:** Final multi-window registration acceptance criteria. `[NEEDS QUANTITATIVE CRITERION]`

### Direct experimental training

- **Purpose:** Demonstrate feasibility of the central experimental-learning step.
- **Central argument:** The unmodified 3D-PRIMME architecture can be trained directly on T0 -> T1 experimental grain-ID maps using 797,712 boundary-centered samples and evaluated on later states.
- **Manuscript evidence:** Model, label construction, training split, and replicates. [Source: Experimental surrogate manuscript, §3, PDF pp. 8-9]
- **Proposed future content:** Cross-window training/evaluation and uncertainty analysis.
- **Expected visual:** **Figure 6C**, experimental label construction and rollout.
- **Missing information:** Whether future windows will be used for training, testing, or both. `[AUTHOR INPUT REQUIRED]`

## 3.3 Stable preliminary results

- **Purpose:** Establish feasibility while reporting limitations honestly.
- **Central argument:** The model reproduces early coarsening and resolvable grain-size distribution shape with low drift across three replicates, but misses late slowdown and held-out topology at matched steps and underpredicts individual-grain change magnitudes.
- **Manuscript evidence:** Figs. 2-6 and Table 1. [Source: Experimental surrogate manuscript, §4, PDF pp. 9-15]
- **Proposed future content:** Use all reported results as stable preliminary evidence; do not relabel them as completed dissertation aims.
- **Expected visual:** **Figure 7**, compact preliminary-results composite: trajectory, size distribution, topology, grain-level kinetics, and drift. **Table 7**, metric, favorable result, limitation, and implication for Aim 1.
- **Missing information:** Select which panels fit the proposal page budget. `[AUTHOR INPUT REQUIRED]`

## 3.4 Remaining gap motivating the proposed aims

- **Purpose:** Convert limitations into Aim 1 tasks.
- **Central argument:** One material, one window, one training interval, geometry-only features, readout artifacts, and uncertain temporal mapping limit current generalization; multi-window analysis is the immediate ongoing extension.
- **Manuscript evidence:** Experimental Discussion and Conclusions. [Source: Experimental surrogate manuscript, §5, PDF pp. 15-17]
- **Proposed future content:** Multi-window study design; blocked validation; uncertainty decomposition.
- **Expected visual:** Fold present limitation -> Aim 1 response -> validation metric into **Core Table 3**.
- **Missing information:** Detailed multi-window protocol and current completion status. `[AUTHOR INPUT REQUIRED]`

---

# 4. Proposed Research: Specific Aims

- **Purpose:** Present the remaining research as a dependency chain.
- **Central argument:** Aim 1 establishes trust; Aim 2 validates each learned operator against its own reference domain; Aim 3 interprets only relationships shown to be reliable in those paired comparisons.
- **Manuscript evidence:** Cross-manuscript synthesis and experimental limitations.
- **Proposed future content:** Aims 1-3 below.
- **Expected visual:** Fold the three-aim dependency diagram into **Core Figure 1**, the causal research roadmap.
- **Proposed future content:** Input-side scale attribution and output-side response/Jacobian probing, applied only after the Aim 1-2 reliability gates.

## 4.1 Aim 1 - Establish reliable and generalizable learning from sparse 4D experiments

**Status:** Single-window results are stable preliminary evidence; multi-window analysis is ongoing; uncertainty/generalization components are proposed.

### Scientific question

Under what curation, registration, linkage, training, and validation conditions can an experiment-trained local surrogate be trusted beyond its exact training pair?

### Hypothesis

If voxel-level labels are curated with direction-sensitive registration checks and evaluated across independent experimental windows and temporal partitions, then experiment-trained local operators will reproduce held-out evolution at field, population, topology, and individual-grain levels; uncertainty arising from model, curation, and data variability will increase with realized error and identify unsupported conditions.

### Rationale

The stable single-window results show feasibility and expose multilevel failure modes. Multiple windows plus empirical uncertainty and sensitivity analysis are required to distinguish a generally reliable operator from one specialized to a favorable window. Full probabilistic calibration is desirable but is not required for the core Aim 1 claim.

### Completed preliminary evidence

- residual-driven window selection;
- integer registration and in-place trimming;
- grain linkage;
- direct T0 -> T1 training;
- three replicate models;
- held-out T2-T4 evaluation;
- grain-size, topology, grain-level, and drift analyses.

[Source: Experimental surrogate manuscript, §§2-5, PDF pp. 3-17]

### Boundary between the current manuscript and the proposed extension

| Dimension | Current experimental manuscript | Aim 1 extension |
|---|---|---|
| Spatial coverage | One curated experimental window | Multiple prespecified windows from the same volume |
| Replication | Three model initializations | Model, window, and curation variability |
| Validation structure | Held-out evolution within the same field of view | Grouped spatial and temporal validation |
| Sensitivity analysis | Threshold, padding, drift, and readout checks within one window | Cross-window robustness and a prespecified multilevel reliability matrix |
| Claim supported | Feasibility of direct experimental training | Defined domain of applicability beyond the original training pair/window |

This matrix prevents completed or stable preliminary results from being presented as future work.

### Scope hierarchy

**Core Aim 1 work required for completion**

- curate and analyze a minimum viable set of multiple windows from the current DCT volume;
- use grouped window/time-pair validation;
- quantify empirical variability across windows, model replicates, and key curation choices;
- apply a prespecified multilevel reliability matrix;
- define a practical domain-of-applicability or abstention rule.

**Optional extensions, pursued only if the core work is complete**

- full probabilistic uncertainty calibration or formal prediction intervals;
- external datasets or transfer to additional materials;
- extensive architecture/readout comparisons;
- broad registration, linkage, or detection-threshold sweeps beyond the prespecified sensitivity set.

### Proposed methodology

1. Define additional admissible windows from the current DCT volume.
2. Apply the same curation, registration, trimming, and linkage protocol to each window.
3. Prespecify a minimal sensitivity set covering window placement, key registration/linkage decisions, detection threshold, and readout.
4. Define grouped training and validation splits at the window and time-pair level.
5. Train replicate models with fixed architecture and evaluation definitions.
6. Evaluate field morphology, rigid drift, voxel/boundary updates, grain count, \(\langle R\rangle^2\), normalized size distribution, topology, and individual-grain change.
7. Decompose uncertainty from initialization, training window, registration/linkage, and detection threshold.
8. Test whether empirical variability or a chosen uncertainty score is associated with realized held-out error.
9. Define a practical domain-of-applicability or abstention rule.
10. Attempt full probabilistic calibration only if the minimum multi-window analysis and schedule permit it.

### Required data

- current five-state lab-DCT dataset;
- raw and curated grain-ID maps;
- additional windows from the same volume;
- cross-frame linkage and registration diagnostics;
- replicate experiment-trained models;
- optional orientation data if reliable, but not required for core Aim 1.

### Quantitative validation criteria

- registration residual by axis; preliminary gate: no more than 0.05 voxel per axis; [Source: Experimental surrogate manuscript, §2, PDF p. 7]
- rollout rigid drift relative to uncurated and single-window preliminary baselines;
- trajectory errors in grain count and \(\langle R\rangle^2\);
- distribution distance, including detection-limit sensitivity;
- topology/face-count error;
- individual-grain sign accuracy and magnitude calibration where linkage supports it;
- between-replicate and between-window variability;
- association between empirical uncertainty/sensitivity and held-out error, plus retained accuracy after abstention;
- optional formal uncertainty calibration if data support it.

Success requires reproducibility across prespecified windows and replicates, not only acceptable performance in one selected window. Exact thresholds remain `[NEEDS QUANTITATIVE CRITERION]`.

### Expected outcome

A validated protocol for converting sparse 4D grain-ID maps into direct supervision, plus an experiment-trained surrogate with explicitly defined limits of applicability.

### Risks

- additional windows contain stronger non-rigid distortion;
- linkage yield is inadequate outside the original window;
- detection limits dominate cross-window differences;
- windows are not statistically independent;
- uncertainty ensembles miss systematic measurement bias;
- the May 2027 schedule limits the number of window/training combinations.

### Alternative strategies

- use blocked cross-window validation rather than claim cross-material generalization;
- restrict training to high-confidence boundary events;
- use identity-agnostic metrics where linkage is insufficient;
- bootstrap grains/boundaries/spatial blocks rather than overlapping voxels;
- report a domain-of-applicability score if full probabilistic calibration is underdetermined;
- predefine a minimum viable window set to protect the schedule.

### Deliverables

- multi-window curated experimental dataset;
- cross-window robustness and empirical uncertainty/sensitivity analysis;
- validated experiment-trained model(s);
- explicit trust/abstention criterion;
- manuscript or dissertation chapter on reliable experimental surrogate learning.

### Aim 1 visual and table plan

- **Core Figure 5:** Multi-window design, grouped train/test partition, and compact reliability matrix.
- **Core Table 3:** Current-manuscript evidence versus Aim 1 extension.
- **Core Table 4:** Data perturbation, expected artifact, diagnostic, and acceptance criterion.

### Missing information

- number and placement of additional windows;
- which frame pairs will be used for training versus validation;
- compute budget for replicate/window combinations;
- final quantitative success thresholds.

`[AUTHOR INPUT REQUIRED]` and `[NEEDS QUANTITATIVE CRITERION]`

## 4.2 Aim 2 - Validate simulation-trained and experiment-trained surrogates against their respective reference domains

**Status:** PROPOSED FUTURE WORK

### Scientific question

How faithfully does a simulation-trained surrogate reproduce simulation reference evolution, and how faithfully does an experiment-trained surrogate reproduce experimental reference evolution?

### Hypothesis

Within their respective domains, the simulation-trained surrogate will reproduce the kinetics, statistics, topology, and supported local evolution behavior of the simulation reference, while the experiment-trained surrogate will reproduce the corresponding supported behavior of the curated experimental reference within the domain established by Aim 1. The two paired comparisons will reveal which behaviors each learned operator reproduces reliably and where each departs from its own supervision source.

### Paired two-domain design

| Pair | Reference | Learned prediction | Primary comparison |
|---|---|---|---|
| Simulation pair | \(S\): MF-generated reference evolution under documented neighborhood physics | \(\hat{S}\): rollout from the simulation-trained model | \(S\) versus \(\hat{S}\) |
| Experimental pair | \(E\): curated DCT reference evolution | \(\hat{E}\): rollout from the experiment-trained model | \(E\) versus \(\hat{E}\) |

The analysis contains four data products, but the primary comparisons are **within domain**:

\[
S \leftrightarrow \hat{S}
\qquad\text{and}\qquad
E \leftrightarrow \hat{E}.
\]

It does not require \(S\) and \(E\) to share a common initial state or time coordinate, and it does not use \(d(S,E)\) as a primary Aim 2 outcome. Cross-pair synthesis may compare metric-specific fidelity patterns only when definitions are commensurate; it must not be presented as a direct trajectory comparison.

### Metric policy confirmed by the author

Aim 2 will begin with the metrics already used in the corresponding manuscripts; additional metrics may be added later.

| Pair | Initial metric source | Metrics already available |
|---|---|---|
| \(S\) versus \(\hat{S}\) | 3D-PRIMME manuscript | \(\langle r\rangle^2\) coarsening kinetics, average face count, topology-size relation, normalized radius distribution, voxel-wise accuracy, morphology, and inclination distributions where applicable |
| \(E\) versus \(\hat{E}\) | Experimental surrogate manuscript | grain-count and size/coarsening trajectories, normalized grain-size distributions with detection-limit sensitivity, face-count topology, linked individual-grain evolution, morphology, rigid drift, and replicate variability |

These manuscript-specific metric sets are sufficient to start Aim 2. A common cross-pair metric set is optional rather than a prerequisite. [Source: 3D-PRIMME manuscript, §§2.3 and 3.1-3.5, PDF pp. 5-13; Experimental surrogate manuscript, §4, PDF pp. 9-15]

### Rationale

Each model must first be evaluated against the type of evolution on which it was trained. Comparing \(\hat{S}\) directly with \(\hat{E}\) would conflate differences in supervision with approximation error. The paired design instead asks two controlled questions: whether simulation-trained learning faithfully represents simulated evolution, and whether experiment-trained learning faithfully represents measured evolution.

### Completed preliminary evidence

- controlled MF neighborhood physics; [Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17]
- simulation-trained 3D-PRIMME performance; [Source: 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15]
- stable experiment-trained preliminary results; [Source: Experimental surrogate manuscript, §§2-5, PDF pp. 3-17]
- shared statistical and grain-level evaluation concepts.

The unified paired analysis has not yet been completed.

### Proposed methodology

1. Select documented MF reference trajectories \(S\) and initialize \(\hat{S}\) from the corresponding simulation states.
2. Select curated experimental reference trajectories \(E\) from Aim 1 and initialize \(\hat{E}\) from the corresponding experimental states.
3. Reuse the metrics and definitions reported in the corresponding manuscript, documenting any later additions separately.
4. Quantify \(d(S,\hat{S})\) for simulation-domain surrogate fidelity.
5. Quantify \(d(E,\hat{E})\) for experimental-domain surrogate fidelity.
6. Evaluate kinetics, normalized size distributions, topology, individual-grain evolution, and local update behavior where each reference supports the metric.
7. Repeat the simulation comparison across simulation/model replicates and the experimental comparison across model replicates and available Aim 1 windows.
8. Report pair-specific uncertainty, failure modes, and domain of applicability.
9. Compare the two fidelity profiles only where metrics are already commensurate; a new common metric set is optional.
10. Treat any direct \(S\)-versus-\(E\) physical comparison as a distinct follow-on study requiring its own alignment design, not as a required Aim 2 result.

Here \(d\) denotes a metric-specific reference-to-prediction difference, not one universal scalar.

### Required data

- MF reference trajectories and corresponding simulation-trained rollouts;
- curated experimental reference trajectories from Aim 1 and corresponding experiment-trained rollouts;
- replicate models within each domain;
- manuscript-defined analysis metrics plus pair-appropriate thresholds and uncertainty estimates.

### Quantitative validation criteria

- simulation-pair fidelity \(d(S,\hat{S})\) across prespecified metrics;
- experimental-pair fidelity \(d(E,\hat{E})\) across prespecified metrics;
- reproducibility across model replicates and available reference trajectories/windows;
- sensitivity to pair-specific thresholds and measurement limitations;
- explicit identification of metrics for which fidelity is and is not achieved.

Success is assessed independently for the two pairs. The simulation-trained model is successful only if it meets prespecified criteria against \(S\); the experiment-trained model is successful only if it meets prespecified criteria against \(E\). Good performance in one pair cannot compensate for poor performance in the other. Exact thresholds remain `[NEEDS QUANTITATIVE CRITERION]`.

### Expected outcome

A paired fidelity map showing what the simulation-trained surrogate reproduces from simulated evolution and what the experiment-trained surrogate reproduces from experimental evolution, together with pair-specific errors, uncertainties, and limits of applicability.

### Risks

- sparse experimental states limit the resolution of \(E\)-versus-\(\hat{E}\) validation;
- the manuscript-specific metric sets are not identical;
- aggregate metrics obscure local failure within either pair;
- model variability is small relative to measurement or simulation variability;
- the remaining PhD schedule limits extensive simulator or architecture sensitivity studies.

### Alternative strategies

- retain pair-specific manuscript metrics and use only naturally commensurate metrics for optional cross-pair synthesis;
- use identity-agnostic experimental metrics when linkage is inadequate;
- report normalized rather than absolute-rate metrics when a pair lacks defensible time calibration;
- treat alternative MF neighborhoods as a limited sensitivity analysis, not a new aim;
- report separate simulation and experimental validation conclusions if cross-pair metric comparability is weak.

### Deliverables

- simulation reference-versus-simulation-trained benchmark;
- experimental reference-versus-experiment-trained benchmark;
- paired metric-specific fidelity and uncertainty analysis;
- manuscript or dissertation chapter on domain-specific validation of learned grain-growth operators.

### Aim 2 visual and table plan

- **Core Figure 6:** Two paired comparisons, \(S \leftrightarrow \hat{S}\) and \(E \leftrightarrow \hat{E}\), with pair-specific fidelity results.
- **Core Table 5:** Metric-specific values for \(d(S,\hat{S})\) and \(d(E,\hat{E})\), including replicate and measurement uncertainty.

### Missing information

- final simulation reference trajectories and replicate policy;
- final experimental windows/intervals available from Aim 1;
- any additional metrics the author chooses to add beyond the two manuscripts;
- quantitative fidelity criteria for each pair.

`[AUTHOR INPUT REQUIRED]` and `[NEEDS QUANTITATIVE CRITERION]`

## 4.3 Aim 3 - Interpret experimentally learned evolution rules through input- and output-side probing

**Status:** PROPOSED AIM WITH COMPLETED SIMULATION-DOMAIN METHOD DEVELOPMENT

### Scientific question

Which spatial information does a reliable experiment-trained operator use, how is that information transformed into local evolution decisions, and which response signatures can be related reproducibly to measurable grain-boundary geometry?

### Hypothesis

Reliable local operators will exhibit a reproducible hierarchy of spatial information and a localized, symmetry-consistent response structure. Short-range neighborhoods will carry the dominant transition information, while additional spatial scales will improve trajectory-level fidelity. After numerical artifacts are controlled, scale dependence and output sensitivities that reproduce across experimental windows will be associated with curvature, topology, and inclination descriptors.

### Rationale

Aim 1 establishes the domain in which the experiment-trained operator is trustworthy, and Aim 2 determines which behaviors it reproduces from experiment. Aim 3 then interrogates that validated operator from two complementary directions: input-side analysis asks which spatial scales are used, and output-side analysis asks how perturbations of those inputs change the predicted transition field. Simulation-trained models provide controlled method-development and bias-detection cases rather than substitutes for experimental interpretation.

### Completed preliminary evidence

- **Input side:** Across ten seeds, a multiscale \(7^3/9^3/11^3\) model improves the simulated grain-radius trajectory relative to matched single-scale models while preserving voxel accuracy. Scale-mixer norms emphasize smaller windows, with diminishing contributions from larger and closely spaced windows. A longer prediction gap produces a small shift toward larger scales.
- **Output side:** Model confidence has a U-shaped association with a curvature proxy at two-grain boundaries but not when triple junctions are pooled into the same population. Mean action fields are compact and centered. A full \(729\times729\) input–output Jacobian pipeline is verified against an analytic symmetric function to machine precision.
- **Interpretability audit:** Jacobian probing revealed a storage-axis bias caused by the padding implementation. Cubic-group sample symmetrization removes the systematic bias without changing validation loss. The corrected model exhibits a center dip, a nearest-neighbor sensitivity ring, approximately isotropic decay, and direction-specific input–output routing.
- These results establish feasible interpretation tools and physically suggestive signatures; they do not yet establish an experimental mechanism.

### Proposed methodology

#### Aim 3A: Input-side scale attribution

- Train matched single-scale and multiscale experiment-based models for Aim 1-eligible windows.
- Summarize scale-mixer importance by \(I_s=\lVert W_s\rVert_1/\sum_r\lVert W_r\rVert_1\).
- Test parameter-based rankings through scale removal, scale masking, and matched single-scale performance.
- Evaluate stability across model initializations, experimental windows, and prediction horizons.

#### Aim 3B: Output-side response probing

- Compute confidence and entropy as functions of curvature proxy and boundary topology, separating two-grain boundaries from higher-order junctions.
- Summarize mean action-likelihood fields to measure response center, width, and anisotropy.
- Compute the full Jacobian \(J_i(m,n)=\partial p_i(m)/\partial K_i(n)\), ensemble absolute sensitivity, total input sensitivity, signed means, and sign agreement.
- Quantify spatial range, symmetry, center-versus-neighbor structure, and directional routing.

#### Aim 3C: Evidence control and physical attribution

- Reproduce the pipeline on controlled isotropic and prescribed-anisotropy simulations.
- Audit cubic rotations/reflections, axis permutations, padding choices, sample size, and model replicates before interpreting experimental asymmetry.
- Apply the audited pipeline to reliable experiment-trained models.
- Advance a signature from model interpretation to physical attribution only when it reproduces across eligible windows and models, aligns with a measurable descriptor after appropriate geometric stratification, and survives a held-out or controlled test.
- Require an additional falsifiable prediction or intervention before making a candidate mechanism claim.

### Required data

- existing multiscale and Jacobian simulation studies;
- symmetry-controlled simulation checkpoints;
- reliable experiment-trained checkpoints and held-out predictions from Aims 1-2;
- local neighborhood, curvature-proxy, topology, and inclination descriptors derived from registered grain-ID volumes.

### Validation criteria

- report replicate- or bootstrap-based uncertainty for all interpretation summaries;
- require agreement between scale-mixer ranking and at least one functional scale ablation;
- require output signatures to be stable to sample size, aggregation choice, cubic coordinate transformations, and eligible-window partition;
- require consistent effect direction and held-out or controlled replication for physical attribution;
- freeze exact map-similarity and descriptor-effect tolerances after Aim 1 defines the eligible windows and before the final Aim 3 comparison.

### Expected outcome

A scale-resolved and spatially resolved account of how reliable experiment-trained models convert local microstructure into evolution decisions, with each finding assigned explicitly to model interpretation, physical attribution, or candidate mechanism testing.

### Risks and alternatives

- If mixer weights are unstable, use scale ablation and matched single-scale performance as the primary input-side evidence.
- If voxel-level Jacobians are noisy, aggregate by radial shell, direction, boundary class, or grain.
- If experimental curvature or inclination is resolution-limited, use controlled simulation tests to establish the claim ceiling.
- If no unique physical attribution survives, report validated model interpretation without escalating to mechanism discovery.

### Deliverables

- reproducible scale-attribution results for simulation- and experiment-trained operators;
- symmetry-audited action-field and full-Jacobian maps;
- an evidence matrix separating interpretation, attribution, and mechanism testing;
- dissertation chapter/manuscript on interpretable experimental grain-growth learning.

### Aim 3 visual and table plan

- **Aim 3 preliminary figure A:** Existing input-side results: multiscale \(\langle r^2\rangle\) trajectories and learned scale-mixer weights.
- **Aim 3 preliminary figure B:** Working curvature-conditioned confidence placeholder; replace the incorrect ``all boundary voxels'' header with the final two-grain-boundary version.
- **Aim 3 preliminary figure C:** Existing output-side results: full-Jacobian central slices and the shell-averaged radial sensitivity profile.
- **Core Figure 7:** Two-branch interpretation workflow: multiscale inputs \(\rightarrow\) scale attribution; local outputs \(\rightarrow\) action field and Jacobian; both converge on geometry-controlled testing.
- **Core Table 6:** Interpretation evidence matrix listing response, physical descriptor, reproducibility check, independent test, and claim ceiling.

---

## 4.4 Dependency and integration across aims

### Scientific dependency

- **Purpose:** Demonstrate that the aims are sequential rather than parallel.
- **Central argument:** Aim 1 validates the experimental operator; Aim 2 evaluates \(S\) against \(\hat{S}\) and \(E\) against \(\hat{E}\); Aim 3 interprets only relationships that are reliable within the relevant pair.
- **Manuscript evidence:** Completed foundations and experimental limitations.
- **Proposed future content:** Decision gates:
  - Aim 1 gate: cross-window reliability;
  - Aim 2 gate: each surrogate meets prespecified fidelity criteria against its own reference domain;
  - Aim 3 gate: attribution stable enough for physical testing.
- **Expected visual:** Reuse **Core Figure 1**.
- **Missing information:** Numerical gate values. `[NEEDS QUANTITATIVE CRITERION]`

### Shared data, models, and metrics

- **Purpose:** Show efficiency and feasibility.
- **Central argument:** The same curated experimental data, PRIMME architecture, replicate policy, and multilevel metrics support all three aims, reducing duplicated effort.
- **Manuscript evidence:** Shared architecture/evaluation pipeline between 3D-PRIMME and experimental manuscript. [Source: Experimental surrogate manuscript, §3, PDF pp. 8-9]
- **Proposed future content:** Version-controlled data/model registry and frozen evaluation definitions.
- **Expected visual:** Include shared resources in **Core Table 8**, core/optional scope and schedule.
- **Missing information:** Compute and storage resources. `[AUTHOR INPUT REQUIRED]`

### Interpretation of positive and negative outcomes

- **Purpose:** Make the proposal robust to non-confirmatory results.
- **Central argument:** Failure to generalize, failure of either paired reference-surrogate comparison, or non-identifiable attribution are scientifically informative outcomes that narrow the valid domain of the surrogate.
- **Manuscript evidence:** Current preliminary results already show metric-dependent success and failure. [Source: Experimental surrogate manuscript, §4, PDF pp. 9-15]
- **Proposed future content:** Prespecify how claims change under each result.
- **Expected visual:** Fold the decision tree into **Core Figure 7**.
- **Missing information:** Committee preference for formal go/no-go criteria. `[AUTHOR INPUT REQUIRED]`

---

# 5. Expected Outcomes, Contributions, and Scientific Impact

## 5.1 Simulation-physics and surrogate-model foundations

- **Purpose:** State the coupled physical and computational foundation established by the completed work.
- **Central argument:** Neighborhood design clarifies and controls the physical content of stochastic simulation labels, while local 3D learning demonstrates that those controlled rules can be learned efficiently and applied across larger spatial and temporal domains.
- **Manuscript evidence:** Neighborhood and 3D-PRIMME manuscripts. [Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17; 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15]
- **Proposed future content:** Present both studies as one completed enabling foundation rather than separate future aims.
- **Expected visual:** None; reference the completed-foundation figures in Section 2.
- **Missing information:** None.

## 5.2 Experimental-learning contribution

- **Purpose:** State the main proposed dissertation contribution.
- **Central argument:** The project will define when sparse 4D grain-ID maps can serve as trustworthy supervision and how experimental reference behavior differs from simulation and surrogate predictions.
- **Manuscript evidence:** Stable preliminary experiment-trained results. [Source: Experimental surrogate manuscript, §§2-5, PDF pp. 3-17]
- **Proposed future content:** Multi-window Aim 1 and the two paired Aim 2 validations.
- **Expected visual:** None; reference Core Figures 5-6.
- **Missing information:** Final number of windows; any metrics added beyond the two manuscripts are optional and can be supplied later. `[AUTHOR INPUT REQUIRED]`

## 5.3 Source-aware validation contribution

- **Purpose:** Separate validation claims by supervision and reference domain.
- **Central argument:** The simulation-trained operator must be evaluated against simulation, while the experiment-trained operator must be evaluated against experiment; success in one pair cannot substitute for evidence in the other.
- **Manuscript evidence:** 3D-PRIMME and experimental surrogate metrics. [Source: 3D-PRIMME manuscript, §§2.3 and 3, PDF pp. 5-13; Experimental surrogate manuscript, §4, PDF pp. 9-15]
- **Proposed future content:** Complete the paired Aim 2 validation and assign metric-specific pass, partial-pass, or fail interpretations.
- **Expected visual:** None; reference the paired-comparison figure in Aim 2.
- **Missing information:** Final quantitative criteria. `[NEEDS QUANTITATIVE CRITERION]`

## 5.4 Physical-science contribution

- **Purpose:** State the longer-term scientific value without overclaiming.
- **Central argument:** Validated experimental operators and pair-specific fidelity analysis create a defensible basis for identifying physically meaningful dependencies in measured grain evolution.
- **Manuscript evidence:** Controlled simulation foundations plus the completed multiscale and full-Jacobian method-development studies.
- **Proposed future content:** Aim 3.
- **Expected visual:** Reference Core Figure 7.
- **Proposed future content:** Transfer the audited interpretation pipeline to Aim 1-eligible experiment-trained models.

---

# 6. Research Timeline and Dissertation Plan

## 6.1 Planning assumptions

- **Purpose:** Demonstrate feasibility through May 2027.
- **Central argument:** Work must be prioritized by dependency, with writing and analysis overlapping rather than occurring sequentially at the end.
- **Manuscript evidence:** Current statuses: completed foundations, stable single-window results, ongoing multi-window work, proposed paired Aim 2 validation.
- **Proposed future content:** Backward plan from May 2027.
- **Expected visual:** **Core Figure 8**, compact Gantt chart and chapter map.
- **Missing information:** Exact proposal, dissertation, manuscript, and defense deadlines. `[AUTHOR INPUT REQUIRED]`

## 6.2 Provisional schedule: August 2026-May 2027

| Period | Primary research activity | Writing/deliverable | Decision gate |
|---|---|---|---|
| Aug-Sep 2026 | Complete multi-window selection, curation, registration, and linkage design for Aim 1 | Draft dissertation/proposal background and completed-foundation sections | Are enough windows of acceptable quality available? |
| Oct-Nov 2026 | Train/evaluate cross-window replicate models; quantify multilevel robustness | Draft Aim 1 methods and preliminary-results chapter | Does performance reproduce beyond the original window? |
| Dec 2026 | Complete Aim 1 uncertainty/domain-of-applicability analysis; freeze evaluation pipeline | Finalize Aim 1 figures/tables and manuscript outline | Is the experimental operator reliable enough for paired Aim 2 validation? |
| Jan-Feb 2027 | Assemble \(S\)-\(\hat{S}\) and \(E\)-\(\hat{E}\) trajectories and freeze pair-specific metrics | Draft Aim 2 methods and paired benchmark section | Are both comparisons defined against their respective references? |
| Mar 2027 | Complete both paired fidelity analyses | Finalize Aim 2 figures/tables; draft chapter/manuscript | Which metrics pass or fail in each pair? |
| Feb-Apr 2027, overlapping | Transfer input-side scale attribution and output-side response probing to reliable experiment-trained models | Complete Aim 3 figures, evidence matrix, and synthesis | Which signatures support model interpretation, physical attribution, or a candidate mechanism? |
| Apr 2027 | Integrate aims, limitations, contributions, and conclusions | Full dissertation/proposal revision; committee feedback | Are all claims consistent with achieved evidence? |
| May 2027 | Final analyses, formatting, submission, and defense preparation | Final dissertation/manuscript package | Completion |

This schedule is intentionally front-loaded toward Aim 1 because Aim 2 and Aim 3 depend on it.

## 6.3 Scope-control rules

- **Purpose:** Protect completion against over-expansion.
- **Central argument:** The minimum dissertation contribution should not depend on external datasets, new materials, or exhaustive simulator variants.
- **Manuscript evidence:** One material and one current experimental series are sufficient for demonstrated feasibility but limit transfer claims.
- **Proposed future content:**
  - Core Aim 1: multiple windows within the current volume.
  - Core Aim 2: one documented simulation-reference pair and one documented experimental-reference pair.
  - Core Aim 3: transfer the existing multiscale and Jacobian methods to validated outputs from Aims 1-2.
  - Optional extensions: external dataset, additional materials, extensive neighborhood sweeps.
- **Expected visual:** **Core Table 8**, core versus optional work, shared resources, and schedule protection.
- **Missing information:** Minimum number of experimental windows and model replicates that will constitute the Aim 3 eligible set. `[AUTHOR INPUT REQUIRED]`

### Schedule drop rules

1. Protect the minimum multi-window Aim 1 analysis and both core Aim 2 paired comparisons before adding any external dataset or material.
2. If window/model combinations exceed the available time or compute budget, retain the prespecified minimum window set and replicate count; drop broad hyperparameter and readout sweeps.
3. If full probabilistic uncertainty calibration is not supported, report empirical variability, sensitivity, and a domain-of-applicability rule.
4. If the two pairs do not support the same metrics, preserve the strongest valid pair-specific assessments and limit cross-pair synthesis to the common subset.
5. If either surrogate fails its prespecified within-domain criteria, report that failure and do not substitute the other pair's performance.
6. Restrict Aim 3 to the existing multiscale/Jacobian methods and validated outputs from Aims 1-2; do not make completion depend on a new experimental campaign.

---

## 6.4 Expected dissertation chapters

### Provisional chapter structure

| Chapter | Working title | Primary role | Maturity |
|---|---|---|---|
| 1 | Introduction: Learning Grain-Growth Dynamics Across Simulation and Experiment | Overarching question, background, causal program | To be written |
| 2 | Neighborhood-Driven Anisotropy and Lattice Pinning in Stochastic Grain-Growth Models | Establish physical control of simulation labels | Completed prior work |
| 3 | A Physics-Regulated Neural Framework for Learning 3D Grain-Growth Dynamics | Establish scalable local surrogate learning | Completed prior work; under review |
| 4 | Experimentally Grounded Learning: Curation, Direct Training, and Cross-Window Reliability | Stable single-window evidence plus Aim 1 multi-window reliability | Ongoing work; stable preliminary results and proposed extensions |
| 5 | Domain-Specific Validation of Simulation-Trained and Experiment-Trained Surrogates | Aim 2 paired comparisons | Proposed |
| 6 | Input- and Output-Side Interpretation of Experimentally Learned Evolution Rules | Aim 3 | Method development completed; experimental application proposed |
| 7 | Integrated Conclusions and Future Directions | Cross-aim synthesis and limitations | To be written |

- **Purpose:** Show how manuscripts and aims become one dissertation.
- **Central argument:** Chapters follow the causal logic even when they align partly with manuscripts; the intellectual integration occurs through common training-source, local-operator, and validation questions.
- **Manuscript evidence:** All three manuscripts.
- **Proposed future content:** Chapters 4-7.
- **Expected visual:** Fold the chapter-to-research-question map into **Core Figure 8**.
- **Missing information:** University dissertation format and whether manuscript-style chapters are permitted. `[AUTHOR INPUT REQUIRED]`

### Cross-chapter integration

- **Purpose:** Prevent a paper-compilation appearance.
- **Central argument:** Every chapter should explicitly state:
  - what assumption is controlled or removed;
  - what evidence it contributes to the central hypothesis;
  - what limitation motivates the next chapter.
- **Manuscript evidence:** Cross-manuscript causal sequence.
- **Proposed future content:** Shared notation, metrics, and transition paragraphs across chapters.
- **Expected visual:** Core Figure 8.
- **Missing information:** None.

---

# 7. Conclusion

## 7.1 Proposal conclusion structure

- **Purpose:** Close the proposal by answering why the full program is necessary.
- **Central argument:** Reliable and interpretable learning requires more than a powerful neural architecture: the simulation teacher must be physically diagnosed, the experimental teacher must be curated and uncertainty-aware, and each learned operator must be validated against its own reference before physical interpretation.
- **Manuscript evidence:** Neighborhood control, 3D-PRIMME scalability, and stable direct experimental training. [Source: Neighborhood manuscript, Conclusions, PDF pp. 15-17; 3D-PRIMME manuscript, Conclusion, PDF p. 15; Experimental surrogate manuscript, §5, PDF pp. 15-17]
- **Proposed future content:** Summarize expected Aim 1 reliability, Aim 2 paired validation, and Aim 3 interpretation.
- **Expected visual:** None; optionally reuse the causal roadmap in miniature.
- **Proposed future content:** Revise the final claim to the achieved level: model interpretation, physical attribution, or candidate mechanism.

## 7.2 Final dissertation-level contribution statement

- **Purpose:** Provide the sentence the committee should remember.
- **Central argument:** The dissertation will establish a source-aware framework for learning mesoscale grain-growth dynamics that controls simulation-label physics, validates simulation-trained and experiment-trained operators against their respective references, and supports physically grounded interpretation.
- **Manuscript evidence:** Full program.
- **Proposed future content:** Revise from future to achieved tense only after the aims are completed.
- **Expected visual:** None.
- **Missing information:** None at outline stage.

---

# Consolidated Figure and Table Plan

The earlier section-level visual labels are panel candidates, not separate required figures. The proposal should use approximately eight core figures and eight core tables; detailed diagnostics belong in appendices, supplementary material, or the dissertation chapters.

## Core figures

1. **Causal roadmap:** local-to-macroscopic problem, training source, three-aim dependency, and decision gates.
2. **Completed simulation-physics foundation:** neighborhood geometry, inclination response, anisotropy, and pinning.
3. **Completed computational foundation:** 3D-PRIMME workflow, scale independence, kinetics, and controlled anisotropy.
4. **Experimental feasibility:** DCT sequence, curation/label construction, and stable single-window preliminary results.
5. **Aim 1 design and output:** multi-window partitions, variability sources, and multilevel reliability matrix.
6. **Aim 2 design and output:** paired \(S\)-\(\hat{S}\) and \(E\)-\(\hat{E}\) designs with pair-specific fidelity results.
7. **Aim 3 evidence ladder:** model response, physical attribution, candidate mechanism, and positive/null outcome decision tree.
8. **Execution map:** August 2026-May 2027 Gantt chart aligned with the seven dissertation chapters.

## Core tables

1. Multiscale validation metrics and allowable claim levels.
2. Completed-foundation evidence: neighborhood study, 3D-PRIMME, and experimental preliminary work.
3. Current experimental-manuscript evidence versus Aim 1 extension.
4. Aim 1 perturbations, diagnostics, acceptance criteria, and domain-of-applicability rule.
5. Aim 2 pair-specific fidelity metrics and uncertainty terms.
6. Aim 3 testability and evidence matrix.
7. Risk, detection, mitigation, and fallback register.
8. Core versus optional scope, shared resources, and schedule-protection rules.

---

# Author Inputs Required During Drafting and Before Finalization

The outline is complete enough to support drafting. The following inputs can be resolved during drafting; final claim thresholds must be completed before submission or defense:

1. Proposal format, page limit, and required headings.
2. Preferred title and application emphasis.
3. Final figure panels permitted for reuse from completed manuscripts.
4. Number, placement, and current quality of additional experimental windows.
5. Aim 1 train/test partition across windows and time pairs.
6. Compute budget for replicate models.
7. Final Aim 2 simulation and experimental reference trajectories and replicate policy; any supplemental metrics may be added later.
8. Final Aim 3 figure selection, experimental descriptor availability, and exact independent-validation tolerances.
9. Exact dissertation, manuscript, committee, and defense deadlines before May 2027.
10. Prospective quantitative success thresholds.

---

# Stage 4 Revision Check

- The neighborhood study is treated as completed prior work and not a future aim.
- 3D-PRIMME is treated as completed prior work under review.
- All current experimental-manuscript results are treated as stable preliminary evidence.
- Multi-window analysis is identified as ongoing work in Aim 1.
- Generalization and uncertainty are integrated into Aim 1.
- Aim 2 uses the locked pairing: \(S\) versus \(\hat{S}\), and \(E\) versus \(\hat{E}\).
- Aim 3 incorporates the supplied multiscale input-side and Jacobian/output-side studies as simulation-domain preliminary evidence.
- Aim 1 is separated into core empirical reliability work and optional probabilistic/external extensions.
- Aim 2 no longer requires a common experimental \(T_0\) or a direct \(S\)-versus-\(E\) trajectory comparison.
- Aim 3 transfers the audited interpretation methods to reliable experiment-trained models and records explicit evidence gates.
- The chapter plan is consolidated from eight to seven chapters.
- The current prose draft includes nine source-derived figures from the three manuscripts plus four original synthesis or preliminary-result figures, including the two Aim 3 interpretation figures.
- Schedule drop rules protect the May 2027 completion target.
- The causal sequence is explicit throughout.
- The schedule is backward-planned to May 2027.
- The outline and full prose draft now use the same 15-section structure.
