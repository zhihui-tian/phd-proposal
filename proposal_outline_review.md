# Committee-Style Review of the PhD Proposal Outline

## Review scope

This document completes the review component of Stage 4. It evaluates `proposal_outline.md` as a strict PhD committee member would evaluate it before permitting a full proposal draft.

The review asks whether the outline:

1. presents a defensible causal connection from neighborhood physics to 3D-PRIMME;
2. justifies the neighborhood study's role in improving the simulation training source;
3. avoids overstating simulator fidelity;
4. uses 3D-PRIMME to motivate direct experimental learning;
5. presents sufficient stable preliminary experimental evidence;
6. separates future aims from the current experimental manuscript;
7. formulates interpretation as a testable research program;
8. is feasible by May 2027;
9. reads as one dissertation;
10. addresses the five most important weaknesses.

## Overall committee verdict

**Approved to proceed with drafting, with Aim 3 intentionally deferred.**

The outline has a strong dissertation-level causal structure and unusually clear source grounding. The first two completed foundations are appropriately used to justify the transition from controlled simulation labels to experimental supervision. The stable experimental preliminary work is sufficiently developed to support a proposed research program.

Three issues required explicit treatment:

1. **Aim 1 is broader than the remaining time permits unless calibrated uncertainty and extensive sensitivity studies are separated into core and optional work.**
2. **Aim 2 was initially ambiguous about whether it compared simulation directly with experiment or validated each surrogate against its own domain. The author has clarified that the intended comparisons are \(S\) versus \(\hat{S}\) and \(E\) versus \(\hat{E}\).**
3. **Aim 3 remains a placeholder rather than a testable specific aim. The author has chosen to retain its formal position and supply the detailed work later.**

The outline has been revised to narrow Aim 1, formalize Aim 2 as two paired within-domain validations, and record Aim 3 as a deferred section that does not block drafting of the rest of the proposal.

---

# Summary evaluation

| Committee question | Verdict | Main concern | Required response |
|---|---|---|---|
| 1. Does neighborhood work enable 3D-PRIMME? | **Pass with qualification** | Connection is conceptual and methodological, not a direct before/after surrogate test | Retain precise language that it diagnoses the simulation teacher |
| 2. Is improved training-data-source language justified? | **Partial pass** | "Physically reliable" is too broad; only specific lattice/inclination artifacts are controlled | Replace broad fidelity claims with artifact-specific claims |
| 3. Does the outline avoid overstating simulator fidelity? | **Pass after revision** | Direct \(S\)-versus-\(E\) language risked treating residual differences as missing physics | Use \(S\)-versus-\(\hat{S}\) and \(E\)-versus-\(\hat{E}\) as the primary comparisons |
| 4. Does 3D-PRIMME motivate experimental learning? | **Pass** | Transition is strong | Preserve Sections 6.4 and 7 |
| 5. Is experimental preliminary evidence sufficient? | **Pass for feasibility** | One selected window does not support generalization | State explicitly that current evidence supports feasibility only |
| 6. Are future aims distinct from the Scripta work? | **Partial pass** | Aim 1 includes some analyses already in the manuscript; boundary between completed and future tasks is not sharp enough | Add a current-manuscript-versus-Aim-1 task matrix |
| 7. Is interpretation testable? | **Deferred by author** | Aim 3 has no locked methods, data, or success criteria yet | Retain a formal placeholder and complete it before final submission/defense |
| 8. Are aims feasible by May 2027? | **Partial pass** | Aim 1 uncertainty program plus Aim 2 plus Aim 3 is ambitious | Define minimum viable aims and drop rules |
| 9. Does it read as one dissertation? | **Pass with revision** | Eight proposed chapters risk duplicating the current experimental work and Aim 1 | Merge closely related experimental chapters |
| 10. Are five main weaknesses identified? | **Pass in this review** | They must be reflected in the revised outline | Apply revisions listed below |

---

# Detailed review

## 1. Does the neighborhood work clearly enable 3D-PRIMME?

### Committee assessment

**Yes, if the proposal describes enablement at the level of physical control and diagnosis of the simulation teacher.**

The neighborhood study demonstrates that sampling-neighborhood geometry and stochastic policy affect lattice pinning, inclination distributions, and statistical behavior. 3D-PRIMME then uses MF training data whose isotropic and anisotropic behavior is controlled through the kernel. This supports a clear methodological sequence:

> understand the local rules encoded in the simulator -> generate controlled supervision -> test whether a local neural operator can learn and scale those rules.

[Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17; 3D-PRIMME manuscript, §2.1, PDF pp. 2-3]

### Concern

The neighborhood manuscript does not train 3D-PRIMME on alternative "bad" and "good" neighborhoods. Therefore, it does not directly demonstrate that neighborhood correction improves neural-surrogate accuracy.

### Required revision

Retain the current qualification in Outline §§5.4 and 6.2. Use phrases such as:

- "provides the physical basis for selecting and diagnosing the simulation teacher";
- "controls simulation-label anisotropy and lattice artifacts";
- "enables physically controlled surrogate-training experiments."

Avoid:

- "proved that better neighborhoods improve 3D-PRIMME";
- "validated the surrogate's physical fidelity."

## 2. Is it justified to describe the neighborhood study as improving the training-data source?

### Committee assessment

**Only in a narrowly defined sense.**

The work supports improvement with respect to:

- lattice pinning;
- artificial inclination preference;
- controllability of prescribed anisotropy;
- statistical scatter associated with sampling/update policy.

It does not establish material-specific fidelity, correct boundary mobility, misorientation dependence, or agreement with experimental alumina.

### Concern

The phrases "physically reliable simulation data" and "physical quality of simulation labels" may be read as universal validation. That is not supported.

### Required revision

Replace general statements with:

> "simulation data controlled with respect to lattice pinning and inclination-dependent artifacts."

When "physical fidelity" is used, state the metric and domain to which it refers.

## 3. Does the proposal avoid overstating the physical fidelity of the simulator?

### Committee assessment

**Mostly yes.**

The outline repeatedly distinguishes learning the MF rule from learning universal grain-growth physics. Sections 6.4 and 7 correctly treat the simulator as a controlled teacher with a ceiling.

### Concern

The earlier Aim 2 wording implied a direct \(S\)-versus-\(E\) trajectory comparison and risked interpreting cross-domain residuals as missing physics. The author has clarified that Aim 2 instead contains two within-domain comparisons:

- simulation reference \(S\) versus simulation-trained prediction \(\hat{S}\);
- experimental reference \(E\) versus experiment-trained prediction \(\hat{E}\).

### Required revision

Make these two pairings the primary design. Do not require a common \(T_0\), shared time coordinate, or \(d(S,E)\) result. Any later direct simulation-experiment comparison must be described as a separate follow-on analysis with its own alignment assumptions.

## 4. Does 3D-PRIMME logically motivate direct experimental learning?

### Committee assessment

**Yes. This is one of the strongest parts of the outline.**

3D-PRIMME establishes:

- local learning from minimal temporal supervision;
- reuse of the local operator at larger scales;
- stable statistical rollouts;
- recovery of prescribed synthetic anisotropy.

[Source: 3D-PRIMME manuscript, §§3.1-3.5, PDF pp. 6-13]

These results justify testing the same architecture on spatially rich, temporally sparse 4D experimental data. The outline also correctly states that architecture feasibility does not remove label-quality problems.

### Required revision

No structural change. Preserve the transition:

> scale-independent local learning is technically feasible -> experimental labels are scientifically necessary -> label curation becomes the next core problem.

## 5. Is the experimental work sufficiently developed to serve as preliminary evidence?

### Committee assessment

**Yes for feasibility, but not for generalization.**

The stable preliminary results include:

- a defined five-state lab-DCT dataset;
- residual-driven window selection;
- integer registration and trimming;
- cross-frame grain linkage;
- direct T0 -> T1 training;
- held-out T2-T4 evaluation;
- three replicate trainings;
- grain-size, topology, grain-level, and drift results;
- clear negative results, including late-time and topology limitations.

[Source: Experimental surrogate manuscript, §§2-5, PDF pp. 3-17]

This is enough to motivate Aim 1.

### Concern

All results come from one selected window in one material. T2-T4 also participate in defining the common field of view even though they are excluded from fitting. The random voxel-level train/validation split monitors fit rather than spatial generalization.

### Required revision

The proposal must state:

> Current results establish direct-training feasibility and limited held-out temporal evidence within one curated field of view. They do not establish cross-window, cross-specimen, or cross-material generalization.

## 6. Are the future aims distinct from the current Scripta draft?

### Committee assessment

**Aim 2 is clearly distinct; Aim 1 is only partially separated.**

Aim 2's paired \(S\)-\(\hat{S}\) and \(E\)-\(\hat{E}\) validation is explicitly unperformed and therefore clearly future work. Aim 1's multi-window analysis and empirical uncertainty are also future/ongoing extensions. However, some listed Aim 1 tasks already appear in the current manuscript:

- registration sensitivity;
- threshold sensitivity;
- replicate training;
- drift analysis;
- alternative grain-pooled readout;
- padding sensitivity.

### Concern

Without an explicit boundary, the committee may ask whether Aim 1 is simply "finish the current paper."

### Required revision

Add a table that separates:

| Current experimental manuscript | Aim 1 extension |
|---|---|
| One selected window | Multiple windows with prespecified selection and blocked validation |
| Three initialization replicates | Variability across windows, models, and curation choices |
| Detection-limit sensitivity in one window | Cross-window sensitivity and domain-of-applicability |
| Held-out later states in same field of view | Grouped spatial/temporal validation |
| Preliminary drift/topology/grain metrics | Prespecified multilevel acceptance matrix |

Aim 1's new contribution should be framed as **reliability across experimental data partitions**, not additional single-window diagnostics.

## 7. Is interpretation formulated as a testable research program?

### Committee assessment

**Not yet; acceptable as an explicitly deferred section at the current stage.**

The outline properly distinguishes model interpretation, physical attribution, and mechanism testing, but Aim 3 currently contains:

- no selected inputs or physical descriptors;
- no specified intervention/perturbation;
- no independent validation data;
- no success or falsification criterion;
- no fixed deliverable beyond a general interpretation framework.

### Concern

A committee will not accept "interpret the model" as a specific aim. The aim must test a scientific relationship.

### Required later completion

Before the final proposal is submitted or defended, Aim 3 should specify at least:

1. the response to be explained;
2. the physical variables or controlled changes to be tested;
3. the unit of analysis - voxel, boundary, grain, or neighborhood;
4. the comparison or intervention;
5. a reproducibility criterion;
6. an independent physical or held-out test;
7. the strongest claim allowed by the evidence.

Until then, Aim 3 may remain a concise formal placeholder. Drafting of the other sections can proceed.

## 8. Are the aims feasible in the remaining PhD period?

### Committee assessment

**Conditionally feasible by May 2027 if the core scope is narrowed.**

The current schedule is approximately ten months and already includes:

- multi-window curation and training;
- cross-window validation;
- uncertainty decomposition/calibration;
- paired validation of simulation-trained and experiment-trained surrogates against their respective references;
- Aim 3 integration;
- dissertation writing and defense preparation.

### Concern

Full probabilistic uncertainty calibration across multiple measurement-error sources may be infeasible with one experimental series and a small number of windows. Extensive simulator-neighborhood sweeps or external datasets would endanger completion.

### Required revision

Define:

**Core Aim 1**

- multiple windows from the current volume;
- blocked cross-window validation;
- empirical variability/sensitivity;
- multilevel reliability matrix.

**Optional Aim 1**

- fully calibrated predictive intervals;
- external datasets;
- broad material transfer.

**Core Aim 2**

- one documented \(S\)-\(\hat{S}\) comparison;
- one documented \(E\)-\(\hat{E}\) comparison;
- pair-specific metric sets and criteria;
- replicate uncertainty within each pair;
- cross-pair synthesis limited to commensurate metrics.

**Optional Aim 2**

- extensive neighborhood sweeps;
- additional simulators;
- cross-material comparison.

**Core Aim 3**

- must be defined from existing work, not a new open-ended campaign.

## 9. Does the proposal read as one dissertation rather than three papers?

### Committee assessment

**Scientifically yes, structurally almost.**

The causal sequence is strong, and the common concepts of training-source physics, local operators, and multilevel validation unify the work.

### Concern

The eight-chapter plan separates the current experimental manuscript from Aim 1 into two consecutive chapters, which may create repetition:

- Chapter 4: direct learning from 4D experimental data;
- Chapter 5: reliability across windows.

### Required revision

Use a more integrated chapter plan:

1. Introduction and research framework.
2. Neighborhood-controlled simulation physics.
3. Scalable local learning of simulated dynamics.
4. Experimentally grounded learning: curation, direct training, and cross-window reliability.
5. Paired validation of simulation-trained and experiment-trained surrogates against their respective references.
6. Physical interpretation of learned experimental rules.
7. Integrated conclusions.

This structure still permits manuscript-style subchapters without making one paper equal one aim.

## 10. Five most important weaknesses

### Weakness 1 - Aim 3 is not yet a specific aim

**Severity: Deferred; critical before final proposal submission or defense, but not blocking current drafting.**

The title and scientific role are present, but the aim is not yet testable. Existing Aim 3 work will be supplied and incorporated later.

### Weakness 2 - Aim 2's comparison structure was ambiguous

**Severity: High.**

The earlier four-data-product language did not make the intended pairings explicit and could be read as requiring:

- direct \(S\)-versus-\(E\) comparison;
- common initialization across domains;
- a shared simulation/experiment time coordinate.

The author's clarification resolves this: Aim 2 should compare \(S\) with \(\hat{S}\) and \(E\) with \(\hat{E}\). The initial metrics are those already used in the corresponding 3D-PRIMME and experimental manuscripts; supplemental metrics and final thresholds may be added later.

### Weakness 3 - Aim 1 is over-scoped for ten months

**Severity: High.**

Multi-window learning, readout improvement, registration/linkage sensitivity, uncertainty decomposition, probability calibration, and abstention are too much if all are core deliverables.

### Weakness 4 - "Physical quality" language can overstate the neighborhood result

**Severity: Moderate.**

The completed work controls specific numerical artifacts; it does not establish universal material fidelity.

### Weakness 5 - Current versus proposed experimental work is insufficiently separated

**Severity: Moderate.**

The outline needs a compact matrix showing exactly what the Scripta manuscript has completed and what Aim 1 adds.

---

# Required revisions to the outline

## Revision 1 - Remove the unsupported direct cross-domain claim

Do not make \(d(S,E)\), a common experimental \(T_0\), or simulation-experiment time alignment part of the core Aim 2 design. The aim validates each model against its respective reference rather than claiming that it identifies physics missing from simulation.

## Revision 2 - Formalize the two Aim 2 pairs

The revised outline should specify:

1. simulation reference \(S\) versus simulation-trained prediction \(\hat{S}\);
2. experimental reference \(E\) versus experiment-trained prediction \(\hat{E}\);
3. the metrics already reported in the corresponding manuscript, with supplemental metrics added later if needed;
4. replicate assessment within each pair;
5. cross-pair synthesis only where manuscript metrics are already commensurate.

## Revision 3 - Split core and optional Aim 1 work

Core reliability should emphasize cross-window reproduction and empirical uncertainty. Full probabilistic calibration should be optional unless enough independent windows support it.

## Revision 4 - Add a current-versus-future experimental-work matrix

The proposal should prevent current Scripta results from being presented as future tasks.

## Revision 5 - Record Aim 3 as an intentional deferral

Keep Aim 3's formal position and causal role, but leave its detailed methods, data, and claims as placeholders until the author supplies the existing work. This does not block drafting of the other sections.

## Revision 6 - Consolidate dissertation chapters and visuals

Merge the current experimental and Aim 1 chapters. Reduce the figure architecture from sixteen candidates to approximately eight core figures, with others marked optional.

## Revision 7 - Add schedule drop rules

If work is delayed:

1. protect multi-window Aim 1;
2. protect both core Aim 2 paired validations;
3. remove external datasets and extensive simulation variants;
4. limit uncertainty to empirical sensitivity/domain-of-applicability;
5. scope Aim 3 to existing data and analyses.

---

# Stage 4 decision

The outline may proceed to revision now. After revision:

- Sections 1-9, Aim 1, Aim 2, integration, risk, and timeline can be considered structurally ready.
- Aim 3 remains intentionally incomplete until the author supplies the existing work.
- Drafting may proceed for the rest of the proposal, with Aim 3 clearly labeled as deferred.

## Revision disposition

The Stage 4 revisions have now been applied to `proposal_outline.md`:

| Required revision | Disposition |
|---|---|
| Remove direct cross-domain Aim 2 claims | Applied; \(d(S,E)\) is not a primary outcome |
| Formalize Aim 2 pairings | Applied; \(S\)-\(\hat{S}\) and \(E\)-\(\hat{E}\) are the two primary comparisons |
| Split Aim 1 core and optional work | Applied |
| Separate current manuscript from Aim 1 extension | Applied through a comparison matrix |
| Record Aim 3 deferral | Applied; its formal position and later completion requirements are preserved |
| Consolidate chapters and visuals | Applied; seven chapters and eight core figures |
| Add schedule drop rules | Applied |

**Remaining item before final submission/defense:** provide the existing Aim 3 materials and convert that work into a testable aim. It does not block drafting now. Aim 2 metrics begin with those already reported in the two corresponding manuscripts and can be supplemented later.
