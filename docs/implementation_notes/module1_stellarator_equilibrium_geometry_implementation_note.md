# Module 1: Stellarator Equilibrium and Magnetic Geometry - Implementation Note

## Status

Solver scaffold only. The companion physics note is now a completed textbook chapter, version 1.0, but no validated three-dimensional numerical equilibrium solver is implemented in the baseline.

## Purpose

Represent the magnetic configuration, flux surfaces, rotational transform, pressure profile, and equilibrium quantities required by every downstream module.

## Upstream dependencies

External equilibrium description or analytic reduced geometry.

## Input contract

coil or boundary parameters, pressure profile $p(\psi)$, current profile, and equilibrium controls.

## Output contract

$\mathbf B(\mathbf x)$, $\psi(\mathbf x)$, $\iota(\psi)$, metric/Jacobian data, and flux-surface geometry.

## Mathematical anchor

```text
\nabla p = \mathbf J\times\mathbf B,\qquad \nabla\times\mathbf B=\mu_0\mathbf J,\qquad \nabla\cdot\mathbf B=0
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
