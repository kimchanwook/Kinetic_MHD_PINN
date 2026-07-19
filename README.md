# Kinetic MHD-PINN

This repository is the project backbone for a **Stellarator Energetic-Particle Alfvén Eigenmode Digital Twin**. It is organized to mirror the maintained architecture of `RadiationEffects_proj2`: a top-level living roadmap, shared LaTeX styling, module-by-module physics notes, implementation notes, modular source code, cases, tests, outputs, and explicit coupling interfaces.

`This work was conducted with the assistance of a large language model (LLM)`.

## Current status

The repository architecture is established, the 100-note educational prerequisite curriculum is in progress, and **Modules 1 and 4 now contain completed textbook physics notes**. Module 1 is a 58-page version-1.0 chapter on stellarator equilibrium and magnetic geometry. Module 4 is a 77-page version-2.0 chapter deriving shear-Alfvén waves from ideal MHD, the Alfvén continuum, geometric harmonic coupling, spectral gaps, global eigenmodes, the reduced variational model, finite-volume discretization, sparse eigensolution, and verification. Both long chapters use modular section files for maintainability. **Module 4 remains the first conventional numerical physics milestone**: a reduced, self-adjoint, two-harmonic continuum/eigenmode benchmark implemented independently in Python and MATLAB. The new textbook audit preserves its frozen outputs and states a stricter interpretation: the baseline verifies coupled-harmonic numerics and a TAE-like avoided crossing, but it does not yet establish a strongly crossing-localized or predictive stellarator TAE. Python reference generation and tests pass. MATLAB source and tests are complete but have not been executed in the build environment because MATLAB is unavailable. No validated three-dimensional equilibrium, kinetic-drive, orbit-following, transport, or PINN solver is claimed yet.

## Maintained architecture documents

- `README.md` - repository entry point and current status
- `project_plan.tex/.pdf` - single living roadmap for objectives, modules, data exchange, coupling loops, fidelity stages, and implementation order
- `docs/shared/project_style.tex` - shared LaTeX style copied from the Radiation Effects project and renamed for this project
- `docs/physics_notes/` - advanced module physics notes
- `docs/physics_notes/basics/` - 100-note prerequisite curriculum, master index, and machine-readable manifest; thirty standalone textbook drafts and seventy scaffolds
- `docs/implementation_notes/` - implementation contracts and coding plans; Module 4 is maintained in LaTeX/PDF

## High-level code structure

- `python/` - Python simulation, coupling, and machine-learning framework
- `matlab/` - MATLAB implementation developed in parallel with the Python framework
- `python/src/kinetic_mhd_pinn/` and `matlab/src/+kinetic_mhd_pinn/` - language-specific packages organized by the same physical modules
- `python/cases/` and `matlab/cases/` - executable benchmark and demonstration cases
- `python/tests/` and `matlab/tests/` - contract, verification, and later regression tests
- `python/outputs/` and `matlab/outputs/` - generated run products; intentionally empty in the baseline
- `data/` - raw, processed, and reference data products
- `configs/` - version-controlled run configurations

## Parallel Python/MATLAB development policy

The two implementations share module numbering, governing equations, normalization conventions, configuration inputs, state-product names, verification cases, and output definitions. They remain independent numerical implementations rather than line-by-line translations. Agreement between them is evidence for verification, not proof of correctness; both must also pass analytic limits, conservation checks, and external benchmarks.

## Module architecture

- Module 1 - Stellarator Equilibrium and Magnetic Geometry
- Module 2 - Energetic-Particle Sources and Distribution Functions
- Module 3 - Guiding-Center Orbits, Confinement, and Wall Losses
- Module 4 - Alfvén Continuum and Fluid-MHD Eigenmodes
- Module 5 - Kinetic Energetic-Particle Drive and Damping
- Module 6 - Alfvén-Eigenmode-Induced Fast-Ion Transport
- Module 7 - Alpha Heating and Thermal-Profile Evolution
- Module 8 - Coupled Kinetic-MHD Multiphysics Integration
- Module 9 - PINN and Neural-Operator Surrogates
- Module 10 - Synthetic Diagnostics and Physics-Informed Inverse Modeling
- Module 11 - GNN Physical Dependency Discovery and Coupling Optimization


## Nominal physical workflow

1. Define an analytic or imported stellarator equilibrium.
2. Generate alpha-particle and/or neutral-beam source distributions.
3. Follow energetic-particle guiding-center trajectories and identify wall losses.
4. Compute the Alfvén continuum and reduced fluid-MHD eigenmodes.
5. Add energetic-particle kinetic drive and damping to obtain net mode growth rates.
6. Convert unstable modes into reduced fast-ion redistribution and loss enhancement.
7. Update alpha heating, thermal profiles, pressure, density, and Alfvén speed.
8. Iterate the coupled feedback loops with conservation and convergence diagnostics.
9. Train PINN/neural-operator surrogates only after benchmark solvers exist.
10. Generate synthetic diagnostics and solve selected inverse problems.
11. Use graph learning to study dependency strength and candidate coupling sequences under physical admissibility constraints.

## First numerical milestone

Module 4 implements the reduced two-harmonic Alfvén-eigenmode benchmark. The frozen Python reference outputs are in `data/reference/reduced_ae_benchmark/`; both language trees use byte-identical `case.json` files. The 77-page textbook note is modularized under `docs/physics_notes/module4_sections/` and now documents the full derivation, numerical method, verification hierarchy, and the limits of interpreting the baseline as a TAE. The next planned milestone is an eigenvalue PINN validated against this conventional solver.

## Educational curriculum

The `docs/physics_notes/basics/` directory reserves stable filenames for 100 textbook-style prerequisite notes. Thirty notes are now substantive standalone textbook drafts, version 1.0. Batch 1 contains Basics 01, 02, 03, 05, 06, 07, 11, 12, 13, and 17; Batch 2 contains Basics 18, 19, 21, 22, 24, 25, 26, 29, 31, and 32; Batch 3 contains Basics 34, 35, 36, 37, 39, 40, 41, 42, 44, and 48. The other seventy notes remain scaffolds. Every note is maintained as a separate `.tex` and `.pdf`, and no combined basics volume is produced. `basics_index.pdf` provides the course map, while `curriculum_manifest.json` records numbering, scope, module connections, batch, and status. Module 1 and Module 4 include explicit prerequisite tables linking their advanced material to stable basics-note filenames. Module 1 is deliberately self-contained even where its stellarator-specific Basics 59--66 companions remain scaffolds.

## Documentation build

From the repository root:

```bash
bash scripts/build_docs.sh
```

## Python scaffold smoke test

```bash
cd python
python -m unittest discover -s tests -v
python cases/run_backbone_demo.py
```

## MATLAB scaffold smoke test

```matlab
cd matlab
addpath('src')
results = runtests('tests');
assert(all([results.Passed]));
addpath('cases')
run_backbone_demo
```

The repository-level `scripts/run_tests.sh` always runs Python tests and runs MATLAB tests automatically when a `matlab` executable is available.

## Reduced-AE benchmark

```bash
python python/cases/reduced_ae_benchmark/run_case.py --doc-figures
```

The case writes profiles, continuum branches, eigenvalues, eigenmodes, convergence data, metadata, and figures. MATLAB produces the same output contract under `matlab/outputs/reduced_ae_benchmark/`.
