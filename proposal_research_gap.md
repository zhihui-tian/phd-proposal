# Proposal Research Gap

## Purpose and status

This document completes Stage 2. It defines the research gap, central hypothesis, connected sub-gaps, and provisional future aims. It does not draft the proposal.

Evidence convention:

- Claims about the neighborhood and 3D-PRIMME studies are treated as completed prior work; 3D-PRIMME is currently under review.
- Claims reported in the experimental surrogate manuscript are stable preliminary results from ongoing work.
- Work not demonstrated in the manuscripts is marked `[PROPOSED FUTURE WORK]`.
- Prospective success thresholds that require author or committee agreement are marked `[NEEDS QUANTITATIVE CRITERION]`.

---

# Executive formulation of the gap

## Overarching research gap

There is not yet a validated framework that connects four necessary steps:

1. controlling the physical content and artifacts of simulation-generated local update rules;
2. learning those rules with a scalable three-dimensional surrogate;
3. learning robustly from sparse, imperfect 4D experimental observations and knowing when that learned operator generalizes;
4. converting model sensitivity into reproducible physical attribution and, only after controlled testing, mechanism-level claims.

The completed studies establish the first two steps. The ongoing experimental study provides preliminary feasibility for the third. Interpretation remains a formal fourth step, and its existing supporting work will be incorporated after the author supplies the additional material.

This gap is more precise than "grain-growth prediction is difficult." The unresolved problem is:

> **How can local, physics-guided machine learning move from physically controlled simulation supervision to sparse experimental supervision while preserving label fidelity, quantifying when predictions can be trusted, and producing testable physical attributions rather than post hoc explanations?**

The gap follows directly from the manuscripts:

- local neighborhood geometry changes the inclination-dependent behavior encoded in stochastic simulation data; [Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17]
- 3D-PRIMME can learn and scale the resulting local simulation rule; [Source: 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15]
- but the simulation-trained model is bounded by the assumptions of the MF teacher; [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2]
- direct experimental training is preliminarily feasible but currently limited to one material, one window, and one training interval, with unresolved late-time kinetics and topology; [Source: Experimental surrogate manuscript, §§4-5, PDF pp. 9-17]
- interpretation-related evidence exists outside the three manuscripts and has not yet been assessed in this document.

## Three connected sub-gaps

### Sub-gap 1: Reliable and generalizable learning from sparse 4D experiments

Sparse 4D experiments cannot be used as direct voxel-level supervision until rigid motion, residual distortion, identity linkage, surface clipping, detection limits, and segmentation effects are separated from boundary motion. The preliminary curation pipeline addresses one dataset and predominantly rigid motion, but its robustness to alternative registration choices, windows, intervals, and data sources is not known. The model has been tested on later states within one curated window, but not across spatial regions, datasets, materials, temporal sampling intervals, or acquisition systems. Training-replicate spread is reported, but it is not a calibrated uncertainty model for measurement or distribution shift. These are parts of one scientific problem: establishing when an experiment-trained surrogate is reliable. [Source: Experimental surrogate manuscript, §§2-5, PDF pp. 3-17]

### Sub-gap 2: Domain-specific validation of simulation-trained and experiment-trained surrogates

The completed studies show separately that 3D-PRIMME can learn controlled MF dynamics and that direct experimental training is feasible. What remains unknown under one explicit framework is how faithfully the simulation-trained model reproduces its simulation reference and how faithfully the experiment-trained model reproduces its experimental reference. The four data products therefore form two paired comparisons—\(S\) versus \(\hat{S}\), and \(E\) versus \(\hat{E}\)—rather than one direct simulation-versus-experiment trajectory comparison. The experimental manuscript explicitly identifies the matched simulation-trained assessment as unperformed. [Source: 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15; Experimental surrogate manuscript, §§1 and 5, PDF pp. 3 and 16-17]

### Sub-gap 3: Physical attribution and mechanism testing

Accurate rollout statistics do not identify why a boundary moves. The current experimental model sees local geometry but not explicit misorientation, energy, mobility, or resolved porosity; it can therefore learn only a geometry-conditioned effective response. No supplied manuscript tests whether model sensitivities align with curvature, topology, inclination, triple-junction structure, or crystallography in a reproducible and transferable way. [Source: Experimental surrogate manuscript, §5, PDF pp. 15-17; 3D-PRIMME manuscript, §4, PDF p. 14]

The sub-gaps are sequential:

**Aim 1 establishes whether experimental learning is trustworthy; Aim 2 validates the simulation-trained and experiment-trained surrogates against their respective reference domains; Aim 3 interprets only the learned relationships that pass the relevant paired validation.**

---

# Central hypothesis

## Refined central hypothesis

**Local grain-growth evolution is sufficiently encoded in carefully curated neighborhood observations to support reliable three-dimensional prediction across held-out experimental conditions; explicit uncertainty assessment will identify the domain in which those predictions are trustworthy, while paired validation of simulation-trained predictions against simulation and experiment-trained predictions against experiment will establish which learned relationships are reliable enough for subsequent physical interpretation.**

This formulation deliberately separates three levels:

- **prediction:** reproduce measured evolution under predefined metrics;
- **paired domain validation:** determine how faithfully each learned operator reproduces its own supervision source;
- **physical interpretation:** analyze reliable learned dependencies after the interpretation-related preliminary material is incorporated.

The central hypothesis will be rejected or narrowed if:

- performance depends on a particular window or registration choice;
- uncertainty does not rise when inputs move outside the supported data regime;
- experiment-trained responses do not provide reproducible information beyond appropriate simulation and empirical baselines;
- either surrogate fails to reproduce its own reference domain under prespecified criteria;
- interpretation-stage findings are not reproducible after the additional supporting work is incorporated.

---

# Ten research-gap questions

## 1. Why does the quality of simulation data matter for surrogate learning?

A supervised surrogate is constrained by its labels. In 3D-PRIMME, the target at each site is derived from the next MF state, so the network learns which local grain-ID update the MF simulator produced. If the simulator contains artificial inclination dependence, pinning, or oversimplified physics, those effects become part of the learnable rule. [Source: 3D-PRIMME manuscript, §§2.1-2.2, Eqs. 1-7, PDF pp. 2-5]

The neighborhood study demonstrates why this is not an abstract concern. Its theoretical construction ties the sampling kernel to effective interfacial energy and inclination distribution, while its simulations show that square-like neighborhoods produce directional preferences and that Gaussian sampling reduces them. [Source: Neighborhood manuscript, §§3.2-3.3 and §§5.1-6.2, PDF pp. 6-7 and 10-15]

Therefore, training-data quality means more than high resolution or large quantity. It includes:

- whether the simulator's local neighborhood encodes the intended isotropy or anisotropy;
- whether stochastic sampling introduces excessive kinetic scatter;
- whether the update rule preserves relevant statistical relations;
- whether the simulated mechanisms correspond to the scientific question.

The supplied studies support the first three items within idealized stochastic grain growth. Agreement with a real material remains unestablished.

## 2. What did the neighborhood-driven work establish?

It established that:

- local neighborhood geometry is a primary control on inclination-dependent anisotropy in MCP/MF-type stochastic models;
- circular Gaussian neighborhoods can suppress strong lattice-aligned inclination preferences;
- reshaped, square, and star-like neighborhoods can introduce progressively stronger designed anisotropy;
- rotating the neighborhood rotates the inclination distribution even though the grid orientation is unchanged;
- the update and sampling policy affect statistical scatter separately from neighborhood shape.

[Source: Neighborhood manuscript, §§5.1-6.3, Figs. 2-7, PDF pp. 10-16; Supplementary Figs. 8-9 and Table 1, PDF pp. 19-21]

For the proposal, the defensible conclusion is:

> Local neighborhood design provides a physics-based control and diagnostic for the simulation labels used in surrogate training.

It did not establish that a Gaussian MF simulator contains all relevant grain-growth physics, nor did it compare surrogate performance across different training neighborhoods.

## 3. What did 3D-PRIMME establish?

3D-PRIMME established that a local voxel-level neural operator can learn important features of three-dimensional MF evolution from very limited temporal supervision:

- approximately linear squared-radius coarsening;
- comparable average face-count evolution;
- consistent normalized radius distributions;
- synthetic inclination-dependent behavior;
- spatial application from \(100^3\) training domains to domains as large as \(1024^3\), without retraining;
- stable statistical rollouts for 100 tested steps;
- modest variability across repeated trainings.

[Source: 3D-PRIMME manuscript, §§3.1-3.5, Figs. 2-8, PDF pp. 6-13]

It also established that the observation-window size materially affects the learned kinetics, reinforcing the scientific role of local context. [Source: 3D-PRIMME manuscript, §3.1, Fig. 2, PDF pp. 6-7]

The work demonstrates scalable learning of the simulator's evolution rule. It does not prove that the learned rule is unique, universal, or experimentally complete.

## 4. What is the ceiling of simulation-trained surrogate learning?

The ceiling is the physical content of the simulation teacher. A simulation-trained surrogate may approximate its trainer extremely well and still omit material behavior the trainer does not contain. 3D-PRIMME explicitly motivates experiment-facing learning by noting the idealized assumptions and simplified material descriptions of physics-based models. [Source: 3D-PRIMME manuscript, §1, PDF p. 1]

The current 3D-PRIMME inputs also omit explicit misorientation and other boundary-character variables, and its anisotropic test is generated by a prescribed MF covariance. [Source: 3D-PRIMME manuscript, §§2.1, 3.5, and 4, PDF pp. 3, 10-14]

Thus simulation training can establish:

- computational feasibility;
- whether the learning architecture can recover known local rules;
- controlled tests of isotropy, anisotropy, and scale extrapolation.

It cannot by itself determine whether experimentally absent correlations, heterogeneous mobilities, crystallographic effects, or acquisition-specific phenomena are represented correctly.

## 5. Why is direct experimental training scientifically necessary?

Direct experimental training removes the simulator as the sole source of supervision. The labels then reflect measured changes in a real microstructure, including the combined influence of mechanisms that may be missing or oversimplified in an idealized simulator. [Source: Experimental surrogate manuscript, §§1 and 5, PDF pp. 1-3 and 15-17]

This does not guarantee that all measured changes are physical. It changes the core scientific problem from "Can the model reproduce a prescribed rule?" to:

> "Can the model extract a reproducible evolution rule from measurements while separating physical boundary motion from measurement and curation artifacts?"

That distinction is the reason direct experimental training is scientifically necessary and technically harder.

## 6. What makes experimental training technically difficult?

The experimental manuscript identifies the following coupled difficulties:

- few temporal states;
- rigid translation and rotation between scans;
- sub-voxel residual misalignment;
- spatially varying distortion;
- surface recession and clipping;
- cross-frame grain-identity linkage;
- unlinked voxels and all-zero training labels;
- detection limits for small grains;
- segmentation churn and reconstruction errors;
- circular padding applied to a non-periodic analysis box;
- unresolved porosity;
- acquisition and indexing artifacts;
- a fixed scan interval rather than continuous time.

[Source: Experimental surrogate manuscript, §§1-3 and §5, PDF pp. 3-9 and 15-17]

The difficulty is amplified by the voxel-level target: even a coherent one-voxel displacement can become a large field of incorrect training labels. Aggregate loss or size statistics may remain plausible, so directional diagnostics such as residual label displacement and rollout drift are required. [Source: Experimental surrogate manuscript, §1, Fig. 1, and Table 1, PDF pp. 3-4 and 15]

## 7. What preliminary progress has been made?



The experimental draft reports:

- use of a five-state 4D lab-DCT alumina dataset;
- residual-driven window selection;
- integer, interpolation-free registration;
- in-place trimming to a common interior field of view;
- overlap-based grain linkage;
- direct training on T0 -> T1 grain-ID maps;
- 797,712 local training samples from one scan pair;
- three independent training replicates;
- validation against held-out T2-T4 states;
- early grain-count and squared-radius agreement;
- matched-grain-count comparisons of normalized radius distributions;
- sensitivity to the approximately 20 micrometer confidence limit;
- directional rollout-drift diagnostics;
- topology and individual-grain kinetic checks.

[Source: Experimental surrogate manuscript, §§2-4, Figs. 1-6 and Table 1, PDF pp. 3-15]

The preliminary evidence is intentionally mixed:

- positive: direct training is feasible; rollouts are coherent; early kinetics and resolvable size statistics are promising;
- negative: late slowdown is not captured; held-out face-count topology is not reproduced at matched steps; individual-grain change magnitudes are underpredicted; some intervals do not support identity-based validation.

[Source: Experimental surrogate manuscript, §4, Figs. 3-6, PDF pp. 9-14]

These limitations strengthen rather than weaken the proposed research gap because they identify concrete failure modes for future aims.

## 8. What scientific questions remain unanswered?

The major unanswered questions are:

1. **Robustness:** Does the curation/training pipeline work beyond the selected quiet window?
2. **Temporal representation:** Can the model handle multiple intervals, unequal sampling, or a rate-aware/continuous-time formulation?
3. **Generalization:** Does it transfer across regions, datasets, materials, or conditions?
4. **Comparative value:** Is direct experimental training more predictive than simulation-only training on matched experimental tests?
5. **Four-way comparison:** Can simulation, experiment, simulation-trained predictions, and experiment-trained predictions separate data-source differences from surrogate-model error?
6. **Uncertainty:** Can the model identify when registration uncertainty, detection limits, or distribution shift make a prediction unreliable?
7. **Multiscale fidelity:** Can field morphology, aggregate kinetics, topology, individual-grain changes, and boundary motion be predicted consistently?
8. **Feature completeness:** Which geometric, topological, crystallographic, and energetic inputs are necessary?
9. **Interpretation:** Which model dependencies are stable and physically measurable?
10. **Mechanism testing:** Do those dependencies reproduce in controlled tests and independent datasets?

All are `[PROPOSED FUTURE WORK]`.

## 9. Why does accurate experimental prediction not automatically imply physical understanding?

Multiple local rules can produce similar aggregate coarsening curves or normalized size distributions. The experimental draft explicitly calls the normalized size distribution a weak discriminant because the measured distribution is nearly self-similar over the examined window. It also shows that favorable size-distribution agreement can coexist with incorrect held-out topology and missed late-time slowdown. [Source: Experimental surrogate manuscript, §4, PDF pp. 10-13]

Furthermore, the current model input includes geometry but not explicit misorientation, energy, mobility, or resolved porosity. A prediction can therefore reflect correlations in geometry without identifying which omitted physical factor caused the observed motion. [Source: Experimental surrogate manuscript, §5, PDF pp. 15-17]

Consequently:

- **prediction** asks whether outputs match observations;
- **model interpretation** asks how inputs influence outputs;
- **physical attribution** asks whether those influences correspond to measured material variables;
- **mechanism discovery** asks whether the relationship is reproducible, transferable, and confirmed by controlled tests.

Success at one level does not imply success at the next.

## 10. What experiments or analyses are needed to support physical interpretation?

This question will be answered in detail after the author's existing interpretation-related work is reviewed. At minimum, Aim 3 will need to distinguish:

1. model-level interpretation of how local inputs affect predictions;
2. attribution of those responses to measurable microstructural variables;
3. independent tests that determine whether a reproducible attribution supports a physical-mechanism claim.

The specific perturbations, physical variables, datasets, and quantitative criteria remain `[AUTHOR INPUT REQUIRED]` at this stage.

---

# Provisional future-aim structure

The aims below are organized by scientific dependency, not by manuscript count.

## Proposed Aim 1: Establish reliable and generalizable learning of 3D grain-growth evolution from sparse 4D experiments

### Scientific question

Under what curation, registration, linkage, temporal-supervision, and validation conditions can a local surrogate learn from sparse 4D experiments and remain trustworthy beyond its exact training pair?

### Hypothesis

**If voxel-level labels are curated with direction-sensitive registration checks and the model is evaluated across independent spatial and temporal partitions, then experiment-trained local operators will reproduce held-out evolution at field, population, topology, and individual-grain levels; uncertainty generated from model, curation, and data variability will increase with realized prediction error and identify unsupported conditions.**

### Rationale

The experimental draft shows that uncurated labels produce large coherent rollout drift, while integer registration and window selection reduce it. It also shows that early kinetics and resolvable size distributions can be promising even when topology remains incorrect. The three reported training replicates characterize initialization variability in one window, but not measurement uncertainty or distribution shift. Reliability, generalization, and uncertainty must therefore be evaluated together rather than separated into a model-building aim and a model-assessment aim. [Source: Experimental surrogate manuscript, Fig. 1, Figs. 3-6, Table 1, and §5, PDF pp. 4 and 10-17]

### Completed preliminary evidence

- 4D lab-DCT grain-ID data have been curated and linked.
- An interpolation-free integer registration protocol has been implemented.
- Direct training on one scan pair has been demonstrated.
- Three replicate trainings and held-out temporal tests have been performed.
- Rigid-drift, grain-size, topology, and grain-level metrics have been evaluated.
- Simulation-trained 3D-PRIMME has shown low replicate variability and spatial scaling within the MF domain, providing a reference for distinguishing in-domain repeatability from experimental generalization.

 [Source: Experimental surrogate manuscript, §§2-4, PDF pp. 3-15; 3D-PRIMME manuscript, §§3.2-3.3, PDF pp. 7-10]

### Proposed methodology

1. Freeze and document the preliminary curation pipeline, including all decision points.
2. Extend the pipeline across alternative admissible experimental windows; this multi-window analysis is ongoing and is not part of the completed preliminary evidence.
3. Perturb registration parameters and linkage rules within justified ranges to measure label sensitivity.
4. Compare uncurated, rigid-only, integer-affine, and any justified alternative curation levels without interpolating labels unless explicitly treated as an ablation.
5. Compare the inherited voxel arg-max readout with a topology-preserving or grain-pooled alternative.
6. Train replicate models for every condition using fixed evaluation splits.
7. Validate at voxel/boundary, individual-grain, network-topology, and population-statistics levels.
8. If multiple temporal intervals are available, test interval conditioning or multi-interval training.
9. Decompose uncertainty arising from initialization, finite training regions, registration/linkage choices, detection limits, and temporal or spatial distribution shift.
10. Calibrate uncertainty against realized held-out errors and define an abstention or domain-of-applicability rule.

### Required data

- Current five-state lab-DCT alumina series and full metadata.
- Registered and raw grain-ID maps.
- Grain orientation information if available, although Aim 1 can proceed geometry-only.
- Additional experimental windows from the current volume as the ongoing multi-window study develops.
- No independent external dataset is assumed in the core Aim 1 scope.

### Quantitative validation criteria

Preliminary metrics to retain:

- mean residual label displacement by axis;
- rollout rigid drift by axis;
- voxel/boundary transition accuracy;
- grain count and \(\langle R\rangle^2\) trajectory error;
- KS or another prespecified distance between normalized size distributions above and below the detection limit;
- face-count/topology error;
- per-grain sign accuracy and magnitude calibration;
- replicate variability;
- prediction-interval coverage and calibration error;
- association between predicted uncertainty and realized error;
- accuracy retained after excluding high-uncertainty predictions.

Success should require:

- coherent drift statistically indistinguishable from the curated-label residual or below a preregistered fraction of uncurated drift;
- consistent improvement over uncurated and persistence/size-rule baselines;
- no metric accepted solely because a detection-limit filter removes the discrepancy;
- performance reproduced across prespecified replicates and held-out spatial/temporal partitions;
- higher uncertainty corresponding to higher realized error, with abstention improving retained prediction accuracy.

Numerical thresholds beyond the preliminary registration gate of no more than 0.05 voxel per axis must be set before final analysis. `[NEEDS QUANTITATIVE CRITERION]` [Source for preliminary gate: Experimental surrogate manuscript, §2, PDF p. 7]

### Expected outcome

A validated, artifact-aware protocol defining when sparse 4D grain-ID maps can serve as direct supervision, plus an experiment-trained surrogate with calibrated limits of applicability.

### Risks

- Too few independent intervals for robust training/testing.
- Registration error is not predominantly rigid in other regions.
- Grain linkage failure biases labels.
- Detection limits dominate the apparent error.
- Readout changes improve one metric while degrading another.
- Ensembles capture optimization variability but miss systematic measurement bias.

### Alternative strategies

- use cross-window rather than cross-dataset validation if only one dataset is available;
- mask low-confidence labels or use uncertainty-weighted loss rather than imputing labels;
- train only on high-confidence boundary regions;
- formulate interval-specific operators if rate conditioning is underdetermined;
- use identity-agnostic boundary-motion metrics when grain linkage is insufficient;
- retain the integer registration as the primary method and treat interpolated warps only as explicit sensitivity analyses;
- bootstrap at the grain, boundary, or spatial-block level rather than treating overlapping voxels as independent;
- report a domain-of-applicability score rather than a full predictive probability if uncertainty calibration is underdetermined.

### Deliverables

- reproducible curation and linkage protocol;
- robustness map over windows, registration choices, thresholds, and readouts;
- validated experiment-trained model(s);
- multilevel benchmark dataset and evaluation report;
- uncertainty decomposition, calibration, and trust criterion;
- manuscript on robust experimental surrogate learning.

---

## Proposed Aim 2: Validate simulation-trained and experiment-trained surrogates against their respective references

### Scientific question

How faithfully does the simulation-trained model reproduce simulation reference evolution, and how faithfully does the experiment-trained model reproduce experimental reference evolution?

### Hypothesis

**The simulation-trained model will reproduce the supported kinetics, statistics, topology, and local update behavior of its simulation reference, while the experiment-trained model will reproduce the corresponding supported behavior of the curated experimental reference within the reliability domain established by Aim 1.**

### Rationale

The neighborhood study shows that local simulation rules can be controlled through neighborhood design, and 3D-PRIMME shows that those rules can be learned and scaled. The experimental manuscript demonstrates direct experimental learning but does not provide one unified paired assessment of simulation-reference fidelity and experiment-reference fidelity. Comparing the two surrogate predictions directly would conflate supervision-source differences with approximation error. Aim 2 therefore evaluates \(S\) against \(\hat{S}\) and \(E\) against \(\hat{E}\). [Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17; 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15; Experimental surrogate manuscript, §§1 and 5, PDF pp. 3 and 16]

The initial metric policy is fixed by the author:

- \(S\)-versus-\(\hat{S}\) uses the metrics already reported in the 3D-PRIMME manuscript, including coarsening kinetics, topology/face-count behavior, normalized radius distributions, voxel accuracy, morphology, and applicable inclination distributions.
- \(E\)-versus-\(\hat{E}\) uses the metrics already reported in the experimental manuscript, including grain-count and size/coarsening trajectories, normalized grain-size distributions, topology, linked individual-grain evolution, morphology, drift, detection-limit sensitivity, and replicate variability.
- additional metrics may be supplied later; they are not required to define Aim 2 now.

[Source: 3D-PRIMME manuscript, §§2.3 and 3.1-3.5, PDF pp. 5-13; Experimental surrogate manuscript, §4, PDF pp. 9-15]

### Completed preliminary evidence

- Neighborhood design provides controlled isotropic and inclination-dependent MF training data.
- Simulation-trained 3D-PRIMME learns major MF kinetics, topology, scaling, and prescribed anisotropy.
- The same 3D-PRIMME architecture has been trained directly on one curated experimental interval.
- Field, kinetic, grain-size, topology, and grain-level evaluation concepts are available.
- The unified paired comparison is future work and has not yet been performed.

[Source: Neighborhood manuscript, §§4-6, PDF pp. 7-16; 3D-PRIMME manuscript, §§2-3, PDF pp. 2-13; Experimental surrogate manuscript, §§3-5, PDF pp. 8-17]

### Proposed methodology

1. Select MF reference trajectories \(S\) and corresponding simulation-trained rollouts \(\hat{S}\).
2. Select curated experimental reference trajectories \(E\) from Aim 1 and corresponding experiment-trained rollouts \(\hat{E}\).
3. Reuse the metrics and definitions already reported in the corresponding manuscript; document any later additions separately.
4. Quantify simulation-domain fidelity through \(d(S,\hat{S})\).
5. Quantify experimental-domain fidelity through \(d(E,\hat{E})\).
6. Evaluate field morphology, kinetics, grain-size distribution, topology, individual-grain change, local update behavior, and uncertainty where each pair supports the metric.
7. Repeat the simulation comparison across relevant simulation/model replicates and the experimental comparison across model replicates and available Aim 1 windows.
8. Compare fidelity patterns across the two pairs only where the manuscript metrics are already commensurate; keep pair-specific measurements separate.
9. Treat any direct \(S\)-versus-\(E\) physical comparison as a distinct follow-on analysis, not a required Aim 2 result.

### Required data

- validated experimental reference data and reliability framework from Aim 1;
- MF simulation reference trajectories with controlled neighborhood physics;
- simulation-trained and experiment-trained replicate rollouts;
- manuscript-defined metrics plus pair-specific thresholds and uncertainty estimates;
- additional experimental windows from Aim 1 when available.

### Quantitative validation criteria

- simulation-trained prediction error relative to simulation reference;
- experiment-trained prediction error relative to experimental reference;
- confidence intervals across model replicates and available trajectories/windows;
- sensitivity to pair-specific thresholds and evaluation definitions;
- explicit pass/fail results for each prespecified metric within each pair.

Success is assessed independently: \(\hat{S}\) must satisfy criteria against \(S\), and \(\hat{E}\) must satisfy criteria against \(E\). Performance in one pair cannot compensate for failure in the other. Exact thresholds must be set prospectively. `[NEEDS QUANTITATIVE CRITERION]`

### Expected outcome

A paired fidelity map identifying which simulated behaviors are reproduced by the simulation-trained surrogate and which measured behaviors are reproduced by the experiment-trained surrogate, together with pair-specific errors and limits of applicability.

### Risks

- The experimental series is too small for precise \(E\)-versus-\(\hat{E}\) uncertainty estimates.
- The two manuscript-specific metric sets are not identical.
- Aggregate statistics hide local failures within either pair.
- Pair-specific thresholds make a single combined summary inappropriate.

### Alternative strategies

- use only naturally commensurate manuscript metrics for optional cross-pair synthesis;
- use identity-agnostic experimental metrics when grain linkage is inadequate;
- retain pair-specific conclusions when cross-pair metrics are not commensurate;
- vary controlled simulation assumptions only as a limited sensitivity study;
- limit generalization claims to the available material and windows.

### Deliverables

- simulation-reference versus simulation-trained benchmark;
- experimental-reference versus experiment-trained benchmark;
- pair-specific fidelity, uncertainty, and failure-mode analysis;
- manuscript on domain-specific validation of learned grain-growth operators.

---

## Proposed Aim 3: Interpret learned experimental evolution rules and test candidate physical mechanisms

### Current status

Aim 3 remains a formal and necessary part of the dissertation. The author has indicated that relevant work already exists and will be shared separately. The present document therefore fixes Aim 3's scientific role and dependency but does not yet prescribe its detailed methods, datasets, or validation thresholds.

### Scientific question

Which physically meaningful factors are represented in experimentally learned local evolution rules, and how can those relationships be distinguished from model- or dataset-specific correlations?

### Provisional hypothesis

**Reliable differences and dependencies identified in the experimentally trained operator can be related to measurable microstructural factors and tested as candidate explanations for experimentally observed grain-growth dynamics.**

### Rationale

Aim 1 establishes a trustworthy experimental operator. Aim 2 determines which simulation-trained and experiment-trained responses are reliable relative to their respective references. Aim 3 uses only those validated relationships as the basis for physical interpretation. The neighborhood study provides a methodological precedent that local rule changes can generate measurable macroscopic responses, while 3D-PRIMME shows that a learned operator can recover prescribed anisotropy. [Source: Neighborhood manuscript, §§5.2-6.2, Figs. 3-6, PDF pp. 11-15; 3D-PRIMME manuscript, §3.5, Figs. 7-8, PDF pp. 10-13]

### Completed preliminary evidence

- The three current manuscripts establish the simulation-physics, scalable-learning, and experimental-learning foundations.
- Additional interpretation-related preliminary evidence will be incorporated after it is supplied by the author. `[AUTHOR INPUT REQUIRED]`

### Proposed methodology

`[AUTHOR INPUT REQUIRED]` To be specified after the interpretation-related work is reviewed. The final methodology must distinguish model interpretation, physical attribution, and mechanism testing.

### Required data

Validated outputs from Aims 1-2 plus the additional interpretation-related data and analyses to be provided by the author. `[AUTHOR INPUT REQUIRED]`

### Quantitative validation criteria

`[NEEDS QUANTITATIVE CRITERION]` To be defined after the existing Aim 3 evidence and available validation data are reviewed.

### Expected outcome

A defensible physical interpretation of experimentally learned evolution rules and a set of testable candidate explanations for observed grain-growth behavior.

### Risks

`[AUTHOR INPUT REQUIRED]` To be refined after the existing work is incorporated.

### Alternative strategies

`[AUTHOR INPUT REQUIRED]` To be refined after the existing work is incorporated.

### Deliverables

- validated interpretation framework;
- physically grounded analysis of learned experimental evolution rules;
- dissertation chapter/manuscript on interpretable experimental grain-growth learning.

---

# Integration and dependency of the aims

The aims are not parallel:

1. **Aim 1 establishes label fidelity, generalization, uncertainty, and multilevel predictive validity for experimental learning.**
2. **Aim 2 validates \(S\) against \(\hat{S}\) and \(E\) against \(\hat{E}\).**
3. **Aim 3 interprets the reliable learned relationships established by Aims 1-2.**

If Aim 1 finds that topology or grain kinetics cannot be reproduced, those outputs should not be interpreted as physical in Aim 3. If either Aim 2 pair fails its fidelity criteria, the corresponding model output should not be used for physical attribution.

---

# What is completed, ongoing, and proposed

| Research component | Maturity | Evidence |
|---|---|---|
| Diagnose neighborhood-driven pinning and anisotropy in stochastic models | **COMPLETED PRIOR WORK** | Neighborhood manuscript, §§3-7, PDF pp. 6-17 |
| Learn and scale 3D MF evolution with a local surrogate | **COMPLETED PRIOR WORK; UNDER REVIEW** | 3D-PRIMME manuscript, §§2-5, PDF pp. 2-15 |
| Curate one five-state lab-DCT series and train on T0 -> T1 | **ONGOING WORK / PRELIMINARY EVIDENCE** | Experimental surrogate manuscript, §§2-4, PDF pp. 3-15 |
| Validate later states, replicates, size distributions, drift, topology, and grain kinetics | **STABLE PRELIMINARY RESULTS FROM ONGOING WORK** | Experimental surrogate manuscript, Figs. 1-6 and Table 1, PDF pp. 4 and 10-15 |
| Robustness across multiple experimental windows | **ONGOING WORK** | Extension of the current single-window experimental study |
| Paired \(S\)-\(\hat{S}\) and \(E\)-\(\hat{E}\) validation | **PROPOSED FUTURE WORK** | Unified paired analysis is unperformed; experimental manuscript, §§1 and 5, PDF pp. 3 and 16 |
| Calibrated uncertainty under experimental distribution shift | **PROPOSED FUTURE WORK** | Not supplied; distinct from seed variability |
| Model interpretation, physical attribution, and mechanism tests | **PROPOSED AIM; DETAILS DEFERRED** | Additional interpretation-related work will be supplied by the author |

---

# Proposal-ready one-paragraph gap statement

The completed work establishes that the physical content of stochastic grain-growth simulations is controlled by local neighborhood design and that a local neural operator can learn those simulation rules and apply them across much larger three-dimensional domains and longer rollouts. These advances expose a fundamental ceiling: a simulation-trained surrogate can reproduce only the mechanisms and artifacts present in its simulator. Stable preliminary results show that an unmodified 3D-PRIMME model can instead be trained directly on carefully curated 4D laboratory-DCT grain-ID maps, but the present evidence is limited to one material, one window, and one training interval, and favorable early kinetics and grain-size statistics coexist with unresolved late-time slowdown, topology error, linkage limits, and measurement sensitivity. The resulting research gap is to establish when sparse experimental supervision produces a reliable and generalizable local evolution operator, validate the simulation-trained model against simulation and the experiment-trained model against experiment, and then interpret only the learned relationships that pass the relevant paired validation.

---

# Confirmed planning inputs and remaining items before Stage 3

## Confirmed

1. All results reported in the current experimental manuscript are stable preliminary results.
2. Multi-window experimental analysis has not yet been completed and is ongoing work.
3. Aim 2 will use two primary comparisons: simulation reference versus simulation-trained prediction, and experimental reference versus experiment-trained prediction. Each pair initially uses the metrics already reported in its corresponding manuscript; additional metrics can be supplied later.
4. The target for completing the remaining PhD research is **May 2027**.

## Can remain open during initial Stage 3 outlining

1. `[AUTHOR INPUT REQUIRED]` Supply the existing interpretation-related work before Aim 3 is specified in detail.
2. `[NEEDS QUANTITATIVE CRITERION]` Set prospective success thresholds for multilevel prediction, uncertainty calibration, and both Aim 2 paired comparisons.
3. `[NEEDS LITERATURE SUPPORT]` Add external literature for experimental resolution, uncertainty calibration, simulation-experiment comparison, attribution methods, and controlled grain-boundary physics.

The Stage 3 timeline should be constructed backward from May 2027 and should prioritize completion of the ongoing multi-window Aim 1 work before the Aim 2 paired validation and detailed Aim 3 integration.
