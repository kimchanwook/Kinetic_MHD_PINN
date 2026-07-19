# Module 9: PINN and Neural-Operator Surrogates - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Develop and compare PINNs, causal PINNs, neural operators, and structure-preserving surrogates for selected expensive forward and inverse maps.

## Upstream dependencies

Training products from Modules 1--8.

## Input contract

high-fidelity or reduced-model datasets, governing residuals, boundary conditions, conservation laws, and uncertainty targets.

## Output contract

trained surrogates, error budgets, calibration metrics, speedups, and admissibility diagnostics.

## Mathematical anchor

```text
\mathcal L=\lambda_{\mathrm{data}}\mathcal L_{\mathrm{data}}+\lambda_{\mathrm{PDE}}\mathcal L_{\mathrm{PDE}}+\lambda_{\mathrm{BC}}\mathcal L_{\mathrm{BC}}+\lambda_{\mathrm{cons}}\mathcal L_{\mathrm{cons}}
```

## Implementation decisions to resolve

- coordinate system and normalization
- state-array shapes and units
- discretization and solver algorithm
- boundary and initial conditions
- convergence and failure criteria
- conservative data exchange/remapping
- baseline verification problems
- reference datasets or external-code comparison
- PINN/surrogate training and validation split, if applicable

## Test obligations

1. Unit and sign checks.
2. Analytic or manufactured limiting case.
3. Resolution/convergence study.
4. Interface-contract test with synthetic upstream data.
5. Conservation or invariant diagnostics appropriate to the module.

## Coupling notes

Coupling implementation belongs in Module 8. This module should expose data products through the shared `CoupledState` contract and should not depend directly on another module's private solver objects.
