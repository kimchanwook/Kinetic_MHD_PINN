# Module 11: GNN Physical Dependency Discovery and Coupling Optimization - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Infer directed physical-variable dependencies, feedback groups, state-dependent coupling strengths, and candidate numerical exchange sequences from synthetic interventions.

## Upstream dependencies

Module 8 trajectories and controlled synthetic interventions.

## Input contract

multimodule trajectories, intervention labels, mechanism switches, time lags, and candidate graph priors.

## Output contract

directed typed graphs, edge strengths and lags, strongly connected feedback groups, and ranked coupling strategies.

## Mathematical anchor

```text
\widehat G=\arg\min_G\left(\mathcal L_{\mathrm{trajectory}}+\lambda_{\mathrm{phys}}\mathcal L_{\mathrm{admissibility}}+\lambda_{\mathrm{sparse}}\lVert G\rVert_1\right)
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
