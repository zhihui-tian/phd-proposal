# Proposal Source Analysis

## Scope, evidence convention, and work-status rules

This document completes Stage 1 only. It analyzes the three supplied manuscripts as a sequential research program:

**neighborhood-controlled simulation physics -> simulation-trained 3D surrogate -> experimentally trained surrogate -> interpretation**

Evidence is cited by manuscript, section, PDF page, and figure or table where relevant. "PDF page" means the page number in the supplied PDF file, not always the printed manuscript page. Claims about the ongoing experimental study are preliminary even when the draft uses definitive language.

Status labels used below:

- `[AUTHOR INPUT REQUIRED]`: a proposal decision or factual detail that the manuscripts do not establish.
- `[PROPOSED FUTURE WORK]`: an extension not demonstrated in the manuscripts.
- `[NEEDS LITERATURE SUPPORT]`: a background statement that requires literature beyond the three supplied manuscripts.
- `[NEEDS QUANTITATIVE CRITERION]`: a validation threshold that must be defined prospectively.

### Work-status note

The three studies are treated according to the author's clarified research status:

- The neighborhood study is **completed prior work**.
- 3D-PRIMME is **completed prior work** and is currently under review.
- The experimental surrogate is **ongoing work**. All results reported in the current manuscript are stable and may be used as preliminary results already obtained.
- Interpretation/mechanism work is temporarily outside the present Stage 1 assessment because additional material will be supplied by the author later.

---

# Manuscript 1: *Neighborhood-Driven Anisotropy and Lattice Pinning in Stochastic Grain-Growth Models*

## 1. Research status

**Completed prior work**, used as a physical and methodological foundation rather than as a future aim.

The manuscript argues that sampling-neighborhood geometry, together with algorithmic stochasticity, governs lattice pinning and inclination-dependent anisotropy in stochastic grain-growth models. [Source: Neighborhood manuscript, Abstract and Introduction, PDF pp. 3-4]

## 2. Scientific problem

Pixel- and voxel-based stochastic grain-growth models can inherit artificial directional preferences from their local update rules. In the conventional Monte Carlo Potts (MCP) model, this appears as lattice pinning, distorted grain-boundary inclination distributions, and departures from ideal curvature-driven morphology. Prior remedies such as increasing pseudo-temperature, changing the lattice, or enlarging/weighting the neighborhood can reduce the problem, but the manuscript identifies a missing internal explanation: why these remedies work and which part of the update rule generates the anisotropy. [Source: Neighborhood manuscript, §1, PDF pp. 3-4]

The manuscript narrows the problem to a testable question: **Does the sampling neighborhood, rather than the underlying site lattice alone, determine the effective inclination-dependent interfacial energy and the resulting pinning?** [Source: Neighborhood manuscript, §§3.2-3.3 and §4.1.5, PDF pp. 6-9]

## 3. Motivation

The physical fidelity of simulated grain growth depends not only on matching aggregate coarsening statistics but also on avoiding artificial boundary alignment and nonphysical triple-junction geometries. These artifacts can distort growth rates, morphology, and texture evolution. A computationally inexpensive way to prescribe or remove inclination dependence would therefore improve control over the physical content of stochastic simulation data. [Source: Neighborhood manuscript, §1, PDF pp. 3-4]

For the PhD narrative, the most important motivation is downstream: a learned surrogate can reproduce the rules in its training data, so the local rules of a simulator must be understood before that simulator is used as a source of supervision. The manuscript itself does not test surrogate training on datasets generated with different neighborhoods; the causal connection is therefore a cross-manuscript synthesis supported by method continuity, rather than a direct surrogate-comparison result.

## 4. Data source

The evidence is simulation-based:

- Two-dimensional domains of \(2400 \times 2400\) pixels.
- A common initial Voronoi tessellation containing 20,000 grains.
- Comparisons made at matched grain counts because neighborhood choice changes the rate of evolution.
- Mode-filter (MF) runs with Gaussian, reshaped-Gaussian, uniform square, and star-shaped neighborhoods.
- MCP and neighborhood-driven MCP (N-MCP) runs, including MCP pseudo-temperatures \(T=0\) and \(kT=0.66\).
- The standard MCP comparison is implemented in SPPARKS.

[Source: Neighborhood manuscript, §4 and §4.1, PDF pp. 7-9]

The manuscript reports MF simulations for 2,000 or 4,000 unitless steps depending on neighborhood and MCP/N-MCP simulations for 1,600 unitless steps. [Source: Neighborhood manuscript, §4, PDF pp. 7-8]

## 5. Model or simulation method

### Conventional MCP

MCP evaluates a local Hamiltonian in a fixed \(3 \times 3\) Moore neighborhood, proposes a grain-ID change from a sampled neighbor, and accepts or rejects the change according to the energy change and pseudo-temperature. [Source: Neighborhood manuscript, §2.1, Eqs. 1-2, PDF p. 4]

### Mode filter

MF treats a positive symmetric kernel as both a spatial energy weighting and a sampling distribution. It samples multiple local sites and assigns the most frequent grain in the sampled neighborhood. The manuscript relates this construction to a convolutional Hamiltonian and threshold-dynamics lineage. [Source: Neighborhood manuscript, §2.2, Eqs. 3-7, PDF p. 5]

### Neighborhood-driven MCP

N-MCP replaces the fixed Moore neighborhood with sites sampled from an arbitrary probability mass function \(K(x,y)\), while retaining the MCP energy-based acceptance rule. This isolates neighborhood shape as an experimental variable without replacing the rest of the MCP logic. [Source: Neighborhood manuscript, §3.1, Eq. 8, PDF p. 6]

### Analytical and diagnostic framework

The manuscript connects the first absolute moment of the kernel to an inclination-dependent interfacial energy \(\gamma(\theta)\), uses a Wulff construction to predict equilibrium shape, and derives a corresponding inclination distribution. A discrete form is introduced for a pixel lattice. It then evaluates simulated inclination distributions, an aggregate anisotropy magnitude, and the two-dimensional von Neumann-Mullins area-change relation. [Source: Neighborhood manuscript, §§2.3, 3.2-3.3, 6.1, and 6.3, Eqs. 9-12 and 22-23, PDF pp. 5-7 and 13-15]

## 6. Main hypothesis

**Reconstructed hypothesis:** The effective inclination anisotropy of a stochastic grain-growth model is governed primarily by the geometry and sampling of its local neighborhood; circularly symmetric sampling should suppress directional pinning, deliberately shaped neighborhoods should prescribe anisotropy, and algorithmic stochasticity should soften the realized response relative to its deterministic theoretical limit.

This hypothesis is not presented as a single formal sentence in the manuscript, but it is supported by the Abstract, the neighborhood-dependent interfacial-energy construction, the rotated-neighborhood test, and the comparative results. [Source: Neighborhood manuscript, Abstract, PDF p. 3; §§3.2-3.3 and §4.1.5, PDF pp. 6-9; §§5.1-6.2, PDF pp. 10-15]

## 7. Major results

1. **MCP pinning is reduced when the neighborhood is changed.** Conventional MCP at \(T=0\) shows strong directional boundary populations near the diagonal directions; raising the pseudo-temperature softens the distribution. N-MCP with Gaussian sampling is reported to yield an approximately circular inclination distribution at both tested temperatures. [Source: Neighborhood manuscript, §5.1, Fig. 2, PDF pp. 10-11]

2. **Neighborhood shape tunes anisotropy in a graded way.** For N-MCP, the reported progression from Gaussian to reshaped Gaussian, square, and star neighborhoods increases directional preference, while random sampling softens the realized inclination distributions relative to theoretical shapes. [Source: Neighborhood manuscript, §5.2, Fig. 3, PDF pp. 11-12]

3. **MF exhibits the same qualitative dependence on neighborhood shape.** The Gaussian case is reported as nearly isotropic; progressively non-circular neighborhoods create stronger directional inclination distributions. [Source: Neighborhood manuscript, §5.3, Fig. 4, PDF pp. 12-13]

4. **Rotating the neighborhood rotates the anisotropy.** For reshaped-Gaussian and uniform MF neighborhoods, rotating the sampling distribution by 0, 30, and 60 degrees produces a corresponding rotation of the inclination distribution. This is the clearest test separating neighborhood orientation from fixed grid orientation. [Source: Neighborhood manuscript, §6.2, Fig. 6, PDF pp. 14-15]

5. **Neighborhood shape and update stochasticity affect different observables.** The manuscript reports that Gaussian MF has low anisotropy magnitude, whereas square-like neighborhoods increase it. In the von Neumann-Mullins assessment, MF has much less scatter than MCP and N-MCP, but changing N-MCP neighborhood shape does not itself eliminate the scatter. [Source: Neighborhood manuscript, §§6.1 and 6.3, Figs. 5 and 7, PDF pp. 13-16]

6. **Sampling count affects statistical stability.** Supplementary results report that MF agreement with the von Neumann-Mullins trend improves as the number of sampled points increases, consistent with reduced sampling variability. [Source: Neighborhood manuscript, Supplementary materials, Eq. 24 and Figs. 8-9, PDF pp. 19-21]

## 8. Physical meaning

The local neighborhood is not merely a numerical stencil. In these stochastic models it defines, or approximates, an effective interfacial-energy landscape. Consequently:

- a non-circular neighborhood can imprint an artificial directional preference;
- a circularly symmetric neighborhood can reduce that artifact;
- a deliberately anisotropic neighborhood can create a controlled direction-dependent response;
- the sampling and update policy determine how sharply the theoretical response is expressed.

[Source: Neighborhood manuscript, §§3.2-3.3 and §§5.1-6.3, PDF pp. 6-7 and 10-16]

For the proposal, this establishes a **training-data governance principle**: the simulator's local neighborhood is part of the physics encoded in the labels. It supports describing Gaussian MF data as more controlled with respect to lattice pinning than standard Moore-neighborhood MCP data. It does **not** establish that one simulator is universally more faithful to every experimental material or mechanism.

## 9. Limitations

- The demonstrated neighborhood study is two-dimensional, while the downstream surrogate is three-dimensional. The theory is said to extend to higher dimensions, but the supplied neighborhood results do not directly validate three-dimensional pinning removal. [Source: Neighborhood manuscript, §2, PDF p. 4; §4, PDF pp. 7-8]
- The simulations concern idealized stochastic grain growth; no experimental comparison is provided. [Source: Neighborhood manuscript, §§4-7, PDF pp. 7-17]
- Inclination control does not by itself ensure low variance in individual-grain von Neumann-Mullins behavior; N-MCP reduces pinning but retains high scatter. [Source: Neighborhood manuscript, §6.3 and Supplementary Table 1, PDF pp. 15-16 and 19]
- The selected metrics primarily assess inclination distribution, aggregate anisotropy, and two-dimensional topological kinetics. They do not establish correct grain-boundary mobility, misorientation dependence, or material-specific energetics.
- Runtime comparisons show N-MCP is substantially slower than MCP and MF for the reported setup; computational cost is therefore part of the neighborhood-design tradeoff. [Source: Neighborhood manuscript, Supplementary Table 1, PDF p. 19]

## 10. Open questions

- Does the neighborhood-to-anisotropy relationship transfer quantitatively from the two-dimensional tests to three-dimensional voxel lattices? `[PROPOSED FUTURE WORK]`
- Which neighborhood produces simulation data that best match a particular experiment rather than merely suppressing grid artifacts? `[PROPOSED FUTURE WORK]`
- How do neighborhood geometry, sampling count, pseudo-temperature, and update rule interact in determining both anisotropy and individual-boundary kinetics? `[PROPOSED FUTURE WORK]`
- Would surrogates trained on different neighborhood-generated datasets reproduce the corresponding macroscopic anisotropy and pinning, and how sensitively? `[PROPOSED FUTURE WORK]`
- What criterion defines "physically reliable simulation data" for the proposal: isotropic inclination distribution, von Neumann-Mullins statistics, agreement with experiment, or a combination? `[NEEDS QUANTITATIVE CRITERION]`

## 11. Role in the PhD narrative

This study should be presented as **Foundation 1: physics-informed generation and assessment of stochastic grain-growth simulation data**.

Its proposal function is to establish that local-update design controls the physical content of simulation labels. That result is a prerequisite for interpreting a simulation-trained surrogate: before asking whether a neural network learned the training dynamics, one must know which dynamics the simulator supplied and which lattice artifacts it introduced.

The study should not be framed as an independent future aim, and it should not be claimed to have explained the experiment-trained surrogate.

## 12. Relationship to the next manuscript

3D-PRIMME uses three-dimensional MF data and explicitly cites three reasons for selecting MF: stochastic fluctuations, control of kinetics and inclination dependence through the neighborhood kernel, and computational efficiency. Its isotropic data use a covariance \(\Sigma=aI\), while anisotropic data use an off-diagonal covariance that biases sampling along [111]. [Source: 3D-PRIMME manuscript, §2.1, PDF pp. 2-3]

This is a direct method-level connection: the neighborhood study explains why MF kernel design matters, and 3D-PRIMME uses that controllable simulator as its teacher. However, the manuscripts do not show a controlled comparison in which 3D-PRIMME is trained on "poor" versus "improved" neighborhood data. The strongest defensible proposal language is therefore:

> The neighborhood study provides the physical basis for selecting and diagnosing the simulation rules used to generate surrogate training data; 3D-PRIMME then tests whether a local neural operator can learn and scale those controlled rules.

Do not write that the neighborhood paper directly compared or proved improved surrogate performance; its role is to establish the physical basis for selecting and diagnosing the simulation teacher.

---

# Manuscript 2: *A Physics-Regulated Neural Framework for Learning 3D Grain Growth Dynamics* (3D-PRIMME)

## 1. Research status

**Completed prior work**, currently under review, and used as a feasibility foundation rather than as a future aim.

The manuscript presents the model, simulation data, sensitivity analysis, scalability tests, data-efficiency tests, anisotropic tests, limitations, and conclusions. [Source: 3D-PRIMME manuscript, PDF pp. 1-16]

## 2. Scientific problem

Three-dimensional microstructure evolution is expensive to simulate over spatial domains and time horizons large enough to obtain stable statistics. Many machine-learning approaches operate on global fields or latent encodings, which creates large memory costs and can tie the trained model to a specific domain size. The scientific and computational question is whether a local evolution operator can reproduce the simulator's kinetic, topological, and anisotropic behavior while scaling to much larger three-dimensional domains and long autoregressive rollouts. [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2]

## 3. Motivation

Grain growth is largely governed by local interactions near grain boundaries. If the relevant update rule can be learned from fixed-size neighborhoods rather than a global field, one small three-dimensional training volume may contain many reusable local examples. This offers a path to spatial scalability, temporal extrapolation, and data efficiency. The manuscript also motivates eventual learning from experiment because physics-based models contain idealized assumptions and simplified material descriptions. [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2]

## 4. Data source

The training and evaluation data come entirely from the three-dimensional MF simulator:

- 200 isotropic sequences and a parallel set of 200 inclination-dependent sequences.
- Each sequence begins from a different 512-grain Voronoi structure on a \(100^3\)-voxel domain.
- Each simulation evolves for 100 steps.
- Training sets sample \(M\) sequences and two consecutive time states.
- The anisotropic dataset uses covariance \(a=25\), \(b=20\), biasing growth along the [111] direction.

[Source: 3D-PRIMME manuscript, §2.1, Eqs. 1-4, PDF pp. 2-3]

No experimental microstructure is used for training or quantitative validation in this manuscript.

## 5. Model or simulation method

3D-PRIMME learns voxel updates from local grain-boundary geometry:

1. Grain IDs are transformed into an interface-site representation that counts unlike neighbors in an observation window.
2. Boundary-centered local patches are extracted using an action window.
3. A neural network maps the local representation to candidate grain-state update scores.
4. Local predictions are assembled into the next global microstructure.
5. The learned operator is applied autoregressively.

[Source: 3D-PRIMME manuscript, §2.2, Fig. 1, Table 1, and Eqs. 5-7, PDF pp. 3-5]

The observation window and action window are distinct. The observation window controls the structural context used to build the interface-site representation; the action window controls the neural-network input/output neighborhood. Unlike the earlier two-dimensional PRIMME, 3D-PRIMME removes an explicit boundary-site regularization term and instead relies on the local representation and windows as an implicit constraint. [Source: 3D-PRIMME manuscript, §2.2, PDF p. 5]

Validation uses:

- linear evolution of squared mean grain radius \(\langle r\rangle^2\);
- average number of grain faces;
- the relation between topology and \(\langle r\rangle^2\);
- voxel-wise accuracy;
- visual morphology and inclination distributions.

[Source: 3D-PRIMME manuscript, §2.3, Eq. 8, PDF p. 5]

## 6. Main hypothesis

**Reconstructed hypothesis:** A fixed local representation of grain-boundary geometry contains sufficient information for a neural operator to learn the MF simulator's three-dimensional update rule, and repeated local application of that rule will preserve the simulator's kinetics and statistics across larger spatial domains and longer temporal rollouts.

The manuscript does not label this as a formal hypothesis, but the question is tested through window sensitivity, replicate training, spatial scaling, training-data sufficiency, and inclination-dependent growth. [Source: 3D-PRIMME manuscript, §§2.4 and 3.1-3.5, PDF pp. 5-13]

## 7. Major results

1. **Window sensitivity establishes a finite local context.** All tested window settings recover approximately linear coarsening, but the observation window has a stronger effect on growth rate than the action window. \(N_o=9\), \(N_a=9\) gives the smallest reported relative kinetic error, 2.85%, and is used as the default. [Source: 3D-PRIMME manuscript, §3.1, Fig. 2, PDF pp. 6-7]

2. **Replicate training gives similar statistical trajectories.** Ten models trained on the same single two-state sequence with different initialization and shuffling show small spread in \(\langle r\rangle^2\), average face count, topology-size relation, and voxel accuracy, though uncertainty increases with rollout time. [Source: 3D-PRIMME manuscript, §3.2, Fig. 3, PDF pp. 7-8]

3. **The local operator scales far beyond the training volume.** A model trained on \(100^3\) voxels with 512 grains is applied without retraining to \(256^3\), \(512^3\), and \(1024^3\) domains containing approximately 8,600, 68,700, and 550,000 initial grains. The three sizes exhibit nearly identical coarsening kinetics, similar topological evolution, and overlapping normalized radius distributions at matched coarsening states. [Source: 3D-PRIMME manuscript, §3.3, Figs. 4-5, PDF pp. 7-10]

4. **Long rollouts remain statistically stable in the tested simulation setting.** The manuscript reports stable prediction for 100 evolution steps on the \(1024^3\) case, with 41,674 grains, or 7.6% of the initial grain count, remaining. [Source: 3D-PRIMME manuscript, §3.3, PDF p. 8]

5. **Minimal supervision can reproduce major simulator statistics.** Models trained on 1, 10, or 50 sequences of two states all preserve approximately linear coarsening and similar face-count behavior. Ten sequences give the highest voxel accuracy in the reported comparison; 50 sequences produce slower growth and larger variability under a fixed number of optimizer updates. The manuscript treats redundancy and additional stochastic variability as a possible explanation, not a settled mechanism. [Source: 3D-PRIMME manuscript, §3.4, Fig. 6, PDF pp. 8-11]

6. **Inclination-dependent MF behavior can be learned without explicit inclination input.** The anisotropically trained model qualitatively reproduces direction-dependent morphology and remains close to MF inclination distributions in the XY, XZ, and YZ projections through the tested rollout. [Source: 3D-PRIMME manuscript, §3.5, Figs. 7-8, PDF pp. 10-13]

## 8. Physical meaning

The main physical inference is limited but useful: a compact local representation can carry enough information to reproduce the **simulator's** kinetic, topological, and inclination-dependent statistics over scales much larger than those seen during training. The observation-window sensitivity also shows that "local" is not synonymous with arbitrary: the neighborhood must be large enough to capture relevant boundary context but not so large that it adds unhelpful complexity. [Source: 3D-PRIMME manuscript, §3.1 and §4, PDF pp. 6-7 and 13-14]

The work does **not** show that the network learned universal grain-growth physics. It shows that the network learned a transferable local rule within the distribution of MF-generated behavior. The manuscript itself notes that simulation models contain idealizations and uses that limitation to motivate eventual experimental learning. [Source: 3D-PRIMME manuscript, §1, PDF p. 1; §4 and §5, PDF pp. 13-15]

## 9. Limitations

- The model is trained and evaluated on MF simulations; the physical content is bounded by that simulator. [Source: 3D-PRIMME manuscript, §§2.1 and 3, PDF pp. 2-13]
- Voxel-wise trajectory accuracy decreases with rollout time even when aggregate statistics remain plausible; statistical fidelity and realization-level predictability are distinct. [Source: 3D-PRIMME manuscript, §3.1, Fig. 2d, PDF pp. 6-7]
- The input is based on grain-boundary geometry and does not explicitly include crystallographic misorientation, boundary energy, or mobility. The manuscript identifies explicit misorientation as a future extension. [Source: 3D-PRIMME manuscript, §4, PDF p. 14]
- Window sizes are fixed in the demonstrated model and may depend on microstructural length scale; adaptive windows are suggested as future work. [Source: 3D-PRIMME manuscript, §4, PDF p. 14]
- The inclination-dependent test is generated by a prescribed anisotropic MF kernel. It demonstrates recovery of known synthetic anisotropy, not discovery of an unknown experimental mechanism. [Source: 3D-PRIMME manuscript, §§2.1 and 3.5, PDF pp. 3 and 10-13]
- The manuscript's uncertainty study addresses variability from initialization and shuffling. It does not provide calibrated predictive uncertainty for unseen materials, experiments, registration error, or measurement noise. [Source: 3D-PRIMME manuscript, §3.2 and §4, PDF pp. 7-8 and 14]

## 10. Open questions

- Can the same local-learning framework be trained directly from a measured three-dimensional time series?
- How should experimental rigid motion, distortion, linkage failure, clipping, and detection limits be prevented from becoming learned "physics"?
- How faithfully does each model reproduce its own reference domain: simulation-trained versus simulation and experiment-trained versus experiment?
- Can geometry-only local features represent material-specific effects, or are crystallographic and energetic inputs required?
- How should uncertainty be decomposed into training variability, measurement uncertainty, registration uncertainty, and rollout uncertainty?
- What model interrogation can connect learned update behavior to measurable physical variables?

The first two questions are addressed preliminarily by the experimental manuscript; the others remain unresolved.

## 11. Role in the PhD narrative

This study should be presented as **Foundation 2: scalable surrogate learning of three-dimensional simulated grain-growth dynamics**.

It establishes the second necessary condition for the dissertation:

> Once the local rules in simulation data are physically controlled and diagnosed, a local neural operator can learn those rules and reuse them over much larger spatial and temporal domains.

Its strongest feasibility contributions are three-dimensional locality, minimal temporal supervision, autoregressive stability at the statistical level, and scalability without retraining. It should occupy enough proposal space to establish feasibility, but not more space than the unresolved experimental and interpretive program.

## 12. Relationship to the next manuscript

3D-PRIMME supplies the architecture and training logic used by the experimental study. The experimental manuscript states that it uses the published 3D-PRIMME architecture without modification, keeps architecture and hyperparameters unchanged, and replaces only the training signal with curated experimental grain-ID maps. [Source: Experimental surrogate manuscript, §3, PDF pp. 8-9]

The causal transition is:

1. 3D-PRIMME shows that a local operator can learn simulated three-dimensional update rules from very limited temporal supervision.
2. But simulation supervision cannot contain mechanisms absent from its simulator.
3. Therefore, the next scientific test is whether measured 4D grain-ID maps can provide viable direct supervision.

This transition is explicitly supported by the introductions of both manuscripts. [Source: 3D-PRIMME manuscript, §1, PDF pp. 1-2; Experimental surrogate manuscript, §1, PDF pp. 1-3]

---

# Manuscript 3: *Training a Voxel-Level Grain-Growth Surrogate Directly on a 4D Experiment*

## 1. Research status

**Ongoing work and preliminary evidence for the proposed research.**

The supplied Letter draft reports a substantially developed experimental training and evaluation pipeline, but its results must be presented as preliminary until the author confirms final analyses. The Data availability section still includes `[TO CONFIRM: repository URL]`. [Source: Experimental surrogate manuscript, Data availability, PDF p. 17]

## 2. Scientific problem

A simulation-trained surrogate cannot learn effects that are absent from its labels. Direct experimental supervision could lift this ceiling, but a measured frame is not automatically a trustworthy voxel-level training label. Inter-scan motion, residual distortion, grain-identity errors, clipping, resolution limits, and reconstruction artifacts can be learned as if they were physical boundary motion. Aggregate loss and grain statistics may fail to reveal this corruption. [Source: Experimental surrogate manuscript, §1, PDF pp. 1-3]

The scientific problem is therefore twofold:

1. Can sparse four-dimensional experimental grain-ID maps be curated into label-faithful training pairs?
2. Can a local 3D surrogate trained on those pairs reproduce held-out experimental evolution without absorbing coherent acquisition artifacts?

## 3. Motivation

The manuscript argues that idealized curvature-driven simulators do not fully reproduce measured grain-boundary kinetics and that material-specific boundary energy and mobility are difficult to prescribe comprehensively. These literature-based motivations are cited within the manuscript but should be independently checked if used prominently in the proposal. `[NEEDS LITERATURE SUPPORT]` [Source: Experimental surrogate manuscript, §1, PDF p. 2]

At the practical level, 4D diffraction imaging produces the same kind of voxelized grain-ID map that PRIMME consumes. Although a dataset may contain only a few temporal states, each three-dimensional state contains many local boundary voxels and therefore many spatial training samples. [Source: Experimental surrogate manuscript, §§1 and 3, PDF pp. 2-3 and 8]

## 4. Data source

The draft uses a five-state laboratory DCT annealing series of undoped, untextured alumina:

- Full reconstruction: \(549 \times 149 \times 211\) voxels.
- Voxel size: 5 micrometers.
- States T0-T4 after cumulative holds of 8, 10, 12, 14, and 16 hours at 1800 degrees C following sintering.
- Full-volume indexed grain count decreases from about 20,000 to about 13,600; mean grain size grows from 45.1 to 49.3 micrometers under the data providers' convention.
- The selected \(100^3\) candidate window is ultimately trimmed in place to \(100 \times 95 \times 84\) voxels so all five registered frames remain interior.
- In that analysis window, grain count decreases from 1,757 to 1,345 and mean radius grows by about 10% over four intervals.
- Grains below about 20 micrometers equivalent diameter are treated as below a working confidence limit for sensitivity analysis.

 [Source: Experimental surrogate manuscript, §2, PDF pp. 3 and 5-7; Fig. 1, PDF p. 4]

Training uses T0 -> T1; T2-T4 are held out from fitting, although all five frames are used to define the common field of view. [Source: Experimental surrogate manuscript, §§2-3, PDF pp. 7-9]

## 5. Model or experimental method

### Experimental curation

The proposed curation pipeline includes:

1. **Residual-driven window selection:** a coarse and refined grid search over candidate \(100^3\) windows, ranked by post-registration residual and displacement-gradient amplitude rather than raw inter-frame agreement. [Source: Experimental surrogate manuscript, §2(i), Fig. 1a, PDF pp. 4 and 6]
2. **Integer affine registration:** a rounded affine displacement field copies whole grain-ID labels without interpolation or requantization. [Source: Experimental surrogate manuscript, §2(ii), Fig. 1b-c, PDF pp. 4 and 6]
3. **In-place surface trimming:** the common registered volume is cropped to keep all states within the material as the specimen surface recedes. [Source: Experimental surrogate manuscript, §2(ii), PDF pp. 6-7]
4. **Cross-frame grain linkage:** greedy one-to-one maximum-overlap matching is performed on full volumes before registration; unmatched grains receive new identities. [Source: Experimental surrogate manuscript, §2, PDF p. 7]
5. **Directional label-quality checks:** residual label displacement and rollout rigid drift are used to detect coherent errors that aggregate metrics may miss. [Source: Experimental surrogate manuscript, §2 and Table 1, PDF pp. 7 and 15]

### Surrogate training

The unmodified 3D-PRIMME architecture uses:

- a \(9^3\) boundary-geometry observation;
- a \(9^3\) action neighborhood, flattened to 729 features/scores;
- a four-layer perceptron with sigmoid outputs;
- binary maps indicating which neighboring T0 grain ID becomes the observed T1 ID;
- mean-squared error training and arg-max voxel updates;
- one T0 -> T1 training pair with 797,712 boundary-centered samples;
- a random 80/20 split that monitors fit, not spatial generalization;
- three independently initialized training replicates.

 [Source: Experimental surrogate manuscript, §3, PDF pp. 8-9]

## 6. Main hypothesis

**Reconstructed preliminary hypothesis:** If coherent scan artifacts are removed without interpolating grain labels, then the local 3D-PRIMME operator can learn a repeatable effective grain-growth rule from one experimental scan interval and reproduce selected statistics of later experimental states.

This is a feasibility hypothesis, not yet a mechanism-discovery hypothesis. The current geometry-only model estimates a geometry-conditioned average of unresolved crystallographic and material effects. [Source: Experimental surrogate manuscript, §5, PDF pp. 15-16]

## 7. Stable preliminary results and future extensions

### A. Preliminary results reported as already obtained

All results in this subsection are stable preliminary results from the ongoing experimental study.

1. **Experimental data curation and window selection:** the selected window ranks 15th of 831 candidates under the residual-driven objective, while the raw-agreement baseline ranks last. [Source: Experimental surrogate manuscript, §2(i), Fig. 1a, PDF pp. 4 and 6]

2. **Integer registration reduces boundary mismatch and residual motion without interpolation:** the draft reports unmatched boundary fractions falling from 0.54-0.73 to 0.19-0.21 on three visible faces and residual displacement no larger than 0.05 voxel per axis. [Source: Experimental surrogate manuscript, Fig. 1b-c, PDF p. 4; §2, PDF p. 7]

3. **Rigid motion, residual distortion, and surface clipping are explicitly handled:** the manuscript reports removal of 87% of the dominant rotation-induced ramp and trimming to a fully interior common field of view. It also discloses rounding seams and the use of T2-T4 in defining that common field. [Source: Experimental surrogate manuscript, §2(ii), PDF pp. 6-7]

4. **Grain linkage is sufficient for the training pair:** 90.4% of T1 grains and 97.4% of T1 voxels inherit T0 identities; the 2.6% unlinked T1 voxels contribute all-zero label maps. [Source: Experimental surrogate manuscript, §§2-3, PDF pp. 7-8]

5. **Direct training from experimental grain-ID maps is demonstrated:** one T0 -> T1 pair supplies 797,712 local samples and supports three independent replicate trainings with closely grouped validation losses. [Source: Experimental surrogate manuscript, §3, PDF pp. 8-9]

6. **Rollouts remain visually coherent and largely drift-free over the experimental window:** Fig. 2 reports qualitative large-grain growth, small-grain disappearance, and boundary flattening, with a short-lived single-voxel speckle artifact. [Source: Experimental surrogate manuscript, §4, Fig. 2, PDF pp. 9-10]

7. **Early aggregate coarsening is reproduced, but late slowdown is not:** after one rollout step the representative comparison retains 1,624 grains versus 1,609 experimentally, then diverges as the experiment slows between T3 and T4 while the model maintains a steadier rate. One model step represents the trained two-hour transition; continuous-time calibration is not established. [Source: Experimental surrogate manuscript, §4, Fig. 3, PDF pp. 9-11]

8. **Held-out normalized grain-size distributions are similar at matched grain count:** across three held-out states and three replicates, reported KS values are 0.071-0.095; restricting to grains above the approximately 20 micrometer confidence limit gives 0.025-0.059. All held-out frames pair with rollout step 2 because the experiment slows. The test establishes distribution-shape consistency, not uniqueness of the learned rule. [Source: Experimental surrogate manuscript, §4, Fig. 4, PDF pp. 10-12]

9. **Topology exposes a present failure:** at steps paired to held-out states, rollout face counts remain above the experimental band; topology is not reproduced at those matched steps. The draft associates this with an arg-max speckle transient and small-grain sensitivity. [Source: Experimental surrogate manuscript, §4, Fig. 5, PDF pp. 11-13]

10. **Individual-grain validation is partially feasible:** sign accuracy is reported as 72-73% on the training interval and 62-63% on the usable held-out T2 -> T3 interval, with regression slopes below unity (0.78 and 0.57). Other intervals lack sufficient identity consistency for the same test. [Source: Experimental surrogate manuscript, §4, Fig. 6, PDF pp. 13-14]

11. **Curation prevents artificial rollout drift:** the three-replicate mean per-step drift is reported as approximately \((-0.02,+0.13,-0.09)\) voxels along \((x,y,z)\), compared with about 3.5 voxels per step for uncurated labels. The residual direction is consistent with the known rotational shear. [Source: Experimental surrogate manuscript, §4, Table 1 and Fig. 1d, PDF pp. 4 and 15]

12. **Numerical stability beyond the experiment is observed, not experimentally validated:** one rollout decreases monotonically to 38 grains over 100 steps without instability, but no experimental ground truth or quantitative self-similarity test exists there. [Source: Experimental surrogate manuscript, §4, PDF p. 15]

### B. Additional stable analyses reported in the current manuscript

- Sensitivity to the approximately 20 micrometer experimental confidence limit and to the inherited greater-than-8-voxel pipeline threshold. [Source: Experimental surrogate manuscript, §§2 and 4, PDF pp. 5 and 10-12]
- Boundary-padding sensitivity obtained by excluding face-touching grains. This tests size statistics only, not faces per grain, drift, or training-label effects. [Source: Experimental surrogate manuscript, §3, PDF p. 8]
- Grain-pooled readout as an alternative to single-voxel arg-max. The caption reports improved KS, but the main model remains unmodified and the supplementary evidence was not supplied separately. [Source: Experimental surrogate manuscript, Fig. 4 caption, PDF p. 12]
- Segmentation-churn analysis and per-pair linkage diagnostics, referenced to supplementary notes not included as separate files. [Source: Experimental surrogate manuscript, §§2 and 4, PDF pp. 7, 10, and 13]
- Repository and data-access details. `[AUTHOR INPUT REQUIRED]` [Source: Experimental surrogate manuscript, Data availability, PDF p. 17]

The author has confirmed that all results reported in the current experimental manuscript are stable. They remain preliminary because the overall research program is ongoing, not because the reported analyses are unverified.

### C. Extensions proposed for the remainder of the PhD

- Extend the analysis to multiple experimental windows in the current volume. **ONGOING WORK**
- Evaluate additional datasets, materials, or annealing conditions if they become available. `[PROPOSED FUTURE WORK]`
- Quantify sensitivity to registration model, residual rotation/shear, window selection, linkage policy, and detection limit. `[PROPOSED FUTURE WORK]`
- Compare simulation reference evolution with simulation-trained predictions. `[PROPOSED FUTURE WORK]`
- Compare experimental reference evolution with experiment-trained predictions. `[PROPOSED FUTURE WORK]`
- Treat any direct cross-domain or same-initial-state simulation-versus-experiment comparison as a separate follow-on study rather than the core Aim 2 design. `[PROPOSED FUTURE WORK]`
- Incorporate crystallographic orientation/misorientation or boundary-character features where the experimental data support them. `[PROPOSED FUTURE WORK]`
- Replace or regularize the voxel arg-max readout and validate topology at individual-grain and grain-boundary levels. `[PROPOSED FUTURE WORK]`
- Develop calibrated uncertainty that includes replicate variation, measurement limits, registration uncertainty, and rollout divergence. `[PROPOSED FUTURE WORK]`
- Interrogate the learned operator with controlled perturbations and physical covariates to determine which local dependencies are reproducible. `[PROPOSED FUTURE WORK]`

## 8. Physical meaning

The draft establishes preliminary feasibility for learning an **effective** local update rule directly from measured evolution. The word "effective" is essential:

- the model input contains local boundary geometry but not explicit crystallographic misorientation, grain-boundary energy, mobility, or resolved porosity;
- unresolved effects can influence the measured labels and therefore enter only through their geometry-conditioned average;
- agreement in grain count or normalized size distribution does not demonstrate that the correct physical mechanism has been learned.

[Source: Experimental surrogate manuscript, §5, PDF pp. 15-17]

The current work therefore supports the transition from simulator-prescribed rules to measurement-conditioned rules. It does not yet support physical mechanism discovery.

## 9. Limitations

The manuscript explicitly identifies:

- one material and one analysis window;
- one training interval;
- a fixed two-hour transition operator with no continuous-time calibration;
- failure to capture late experimental slowdown;
- no simulation-trained baseline evaluated on the same experimental data;
- geometry-only inputs and no explicit misorientation dependence;
- incomplete grain linkage and all-zero labels for unlinked voxels;
- circular padding on a non-periodic box;
- porosity mostly below reconstruction resolution;
- single-voxel arg-max speckle and failed held-out topology;
- detection-limit sensitivity;
- no isolation of individual noise sources;
- only predominantly rigid registration conditions tested.

[Source: Experimental surrogate manuscript, §§3-5, PDF pp. 8, 10-17]

## 10. Open questions

- Does performance transfer beyond one quiet window of one alumina dataset?
- How much apparent learning is specific to registration, trimming, detection thresholds, or segmentation churn?
- How faithfully does the experiment-trained model reproduce the experimental reference, and how faithfully does the simulation-trained model reproduce the simulation reference?
- Can the model handle different time intervals or learn a continuous-time/rate-aware operator?
- Which uncertainties dominate: acquisition, reconstruction, registration, linkage, finite training coverage, initialization, or autoregressive rollout?
- Can topology, individual-grain kinetics, and boundary-level motion be predicted simultaneously?
- What additional physical features are required to move from a geometry-conditioned average to boundary-character-sensitive learning?
- Which local model dependencies are reproducible across datasets and controlled physical tests?

## 11. Role in the PhD narrative

This manuscript is the **bridge from completed foundations to the proposed dissertation research**.

It provides preliminary evidence for **Proposed Aim 1: robust learning directly from sparse 4D experiments** by showing that:

- voxelized DCT grain-ID maps can be converted into local supervision;
- curation and registration are integral to the learning problem;
- a single scan pair can supply many local examples;
- held-out experimental states can be used for evaluation;
- replicate training and directional drift checks are feasible.

It also reveals why further experimental-learning work is necessary:

- one dataset/window does not establish generalization;
- replicate spread is not calibrated predictive uncertainty;
- size-distribution agreement coexists with topology and rate failures;

## 12. Relationship to the next stage: interpretation

The author has indicated that interpretation-related work already exists but will be shared separately. It is therefore **deferred rather than evaluated as unsupported** in the present Stage 1 analysis.

The current three-manuscript evidence establishes the progression through experimentally grounded surrogate learning. The interpretation stage should be analyzed and integrated only after the additional source material is available. `[AUTHOR INPUT REQUIRED]`

---

# Cross-manuscript synthesis

| Manuscript | Status | Scientific role | Existing contribution | Limitation | How it enables the next stage | Proposal usage |
|---|---|---|---|---|---|---|
| Neighborhood-driven anisotropy and lattice pinning | Completed prior work | Establishes control and diagnosis of the simulation teacher | Connects neighborhood geometry and stochastic sampling to effective interfacial anisotropy, pinning, inclination distributions, and statistical scatter; introduces N-MCP | Two-dimensional, simulation-only, no surrogate comparison | Shows that local simulation labels have designed physical content and motivates Gaussian/controlled neighborhoods for training data | Foundation 1; concise preliminary-work section, not a future aim |
| 3D-PRIMME | Completed prior work; currently under review | Establishes scalable local learning of controlled 3D simulation rules | Learns MF evolution from two states; preserves major kinetics/topology; scales from \(100^3\) to \(1024^3\); learns synthetic anisotropy | Supervision is entirely simulated; geometry-only input; no experimental validation or calibrated out-of-distribution uncertainty | Supplies architecture, data-efficiency rationale, validation metrics, and local-learning feasibility for experimental training | Foundation 2; feasibility evidence, not a claim of universal physics |
| Experimental voxel-level surrogate | Ongoing work; stable preliminary results | Tests direct learning from sparse measured 4D evolution | Curates a five-state lab-DCT series; trains unmodified 3D-PRIMME on T0 -> T1; evaluates held-out states, replicates, drift, size distributions, topology, and grain kinetics | One material/window/pair; no matched simulation baseline; late slowdown and held-out topology not reproduced; geometry-only features; measurement/linkage limits | Defines unresolved robustness, generalization, uncertainty, and feature-completeness questions | Stable preliminary evidence for proposed experimental-learning aims |

---

# Explicit sequence verification

## Step 1: Neighborhood-driven simulation physics

**Supported.** The neighborhood manuscript provides theoretical and simulated evidence that the geometry and stochastic sampling of local neighborhoods control inclination-dependent anisotropy and lattice pinning in MCP/MF-type models. [Source: Neighborhood manuscript, §§3-7, PDF pp. 6-17]

## Step 2: 3D-PRIMME simulation surrogate

**Supported.** 3D-PRIMME is trained on MF data whose isotropic or anisotropic behavior is controlled through the neighborhood kernel. It learns a local evolution rule and applies it over substantially larger domains and longer rollouts. [Source: 3D-PRIMME manuscript, §§2.1-3.5, PDF pp. 2-13]

## Step 3: Experimental surrogate

**Supported as preliminary, ongoing work.** The experimental manuscript transfers the 3D-PRIMME architecture and evaluation pipeline to curated DCT grain-ID maps, trains on one scan pair, and tests later states. [Source: Experimental surrogate manuscript, §§2-4, PDF pp. 3-15]

## Step 4: Interpretation

**Deferred pending additional source material.** The author reports that some interpretation-related work has already been completed, but it is not part of the three manuscripts analyzed here. No conclusion about its maturity or evidentiary strength is made at this stage. `[AUTHOR INPUT REQUIRED]`

## Does the full sequence hold?

**Yes through the experimental-surrogate stage; the interpretation stage remains to be assessed after additional materials are supplied.**

The manuscripts support the following chain:

> Local neighborhood design controls the physical rules present in stochastic simulation data. A local 3D neural operator can learn and scale those simulated rules. Because its knowledge is limited by the simulator, direct experimental supervision is the necessary next test. Preliminary work indicates that such supervision is feasible after careful curation. The interpretation stage will be integrated after its supporting material is reviewed.

The sequence is strongest when phrased as **necessary conditions and progressively removed assumptions**, not as three papers that each prove the next.

## Unsupported or only partially supported links

1. **"The neighborhood study directly proved improved surrogate performance for 3D-PRIMME."** Not shown. The supported connection is that it establishes the physics-based rationale for selecting and diagnosing the Gaussian-kernel MF simulation teacher.
2. **"Gaussian MF is physically faithful to real grain growth."** Not established. The neighborhood study shows reduced lattice anisotropy and better statistical stability for some metrics, not universal experimental fidelity.
3. **"3D-PRIMME learned curvature-driven physics rather than the MF rule."** The results demonstrate statistical agreement with MF. Claims of universal or uniquely identified curvature dynamics would be too strong.
4. **"Experimental training is superior to simulation training."** Explicitly untested in the experimental manuscript. `[PROPOSED FUTURE WORK]` [Source: Experimental surrogate manuscript, §1 and §5, PDF pp. 3 and 16]
5. **"The experimental surrogate generalizes."** Held-out temporal states in one window support limited temporal testing, but not transfer across regions, datasets, materials, instruments, or thermal histories.
---

# Candidate proposal titles

1. **Predictive and Interpretable Machine Learning for Mesoscale Grain Growth**
2. **From Controlled Simulations to 4D Experiments: Local Machine Learning of Grain-Growth Dynamics**
3. **Physics-Guided Local Learning of Simulated and Experimental Grain Growth**
4. **Experimentally Grounded Surrogate Learning and Interpretation of Three-Dimensional Grain Growth**
5. **Learning Mesoscale Grain-Growth Rules Across Simulation and Experiment**

Title 2 most clearly communicates the three-stage causal progression established by the current sources. Titles 1 and 4 remain provisional until the additional interpretation-related material is reviewed.
