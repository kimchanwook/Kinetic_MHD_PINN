# Module 2: Energetic-Particle Sources and Distribution Functions - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Construct alpha-particle and neutral-beam source terms and reduced energetic-particle distributions in energy, pitch, radius, and time.

## Upstream dependencies

Module 1 and prescribed thermal-plasma profiles.

## Input contract

equilibrium geometry, $n_D$, $n_T$, $T_i$, beam parameters, and source normalization.

## Output contract

$S_f(\psi,E,\lambda,t)$, $f_f(\psi,E,\lambda,t)$, birth power, and moments of the fast-ion population.

## Mathematical anchor

```text
\frac{\partial f_f}{\partial t}+\dot{\mathbf Z}\cdot\nabla_{\mathbf Z}f_f=C[f_f]+S_f-L_f
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
