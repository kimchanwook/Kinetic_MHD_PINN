# MATLAB framework

The MATLAB tree is the parallel implementation scaffold for the Kinetic MHD-PINN project. It mirrors the logical architecture of `python/` while using MATLAB package conventions:

- `cases/` - executable benchmark and demonstration drivers;
- `outputs/` - generated run products;
- `src/+kinetic_mhd_pinn/` - package source organized by physical module;
- `tests/` - contract and later regression tests.

The leading `+` on MATLAB package directories is required by MATLAB and is the language-specific equivalent of the Python package hierarchy. Every physical module has the same module number, responsibility, declared dependencies, README contract, and scaffold completion marker in both languages.

This tree contains the runnable scaffold plus an independent MATLAB implementation of the Module 4 reduced two-harmonic shear-Alfvén benchmark. It supplies:

- a shared handle-class state container;
- a module registry with declared dependencies and products;
- one MATLAB package directory per project module;
- a nominal backbone demonstration;
- contract tests protecting the architecture while physics implementations are added;
- Module 4 profile, continuum, finite-volume eigenvalue, convergence, and output functions.

From MATLAB, run:

```matlab
cd matlab
addpath('src')
results = runtests('tests');
assert(all([results.Passed]));
addpath('cases')
run_backbone_demo
```

Run Module 4 with `addpath('cases/reduced_ae_benchmark'); run_case`. The implementation reads the same JSON case and is tested against the frozen Python reference, but agreement between languages is not a substitute for physical validation.
