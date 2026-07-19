# Module 10: Synthetic Diagnostics and Physics-Informed Inverse Modeling - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Generate diagnostic signals from simulated states and reconstruct energetic-particle distributions, mode amplitudes, or profile changes from incomplete observations.

## Upstream dependencies

Modules 3--8.

## Input contract

coupled plasma state, diagnostic geometry, response functions, noise model, and observation cadence.

## Output contract

synthetic magnetic, neutron, fast-ion-loss, and heat-load signals plus reconstructed latent states and uncertainties.

## Mathematical anchor

```text
y_k(t)=\mathcal H_k[\mathbf U(t)]+\epsilon_k(t)
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
