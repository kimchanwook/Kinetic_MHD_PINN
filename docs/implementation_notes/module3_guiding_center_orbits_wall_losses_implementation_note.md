# Module 3: Guiding-Center Orbits, Confinement, and Wall Losses - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Follow energetic-particle guiding centers in three-dimensional fields, classify orbits, estimate prompt and delayed losses, and map lost-particle energy to the wall.

## Upstream dependencies

Modules 1 and 2.

## Input contract

$\mathbf B(\mathbf x)$, electric field if retained, particle birth coordinates, energy, pitch, and collision model.

## Output contract

orbit histories, confinement fraction, loss time, loss phase space, and $q_{\mathrm{wall}}(\theta,\phi,t)$.

## Mathematical anchor

```text
\dot{\mathbf R}=v_{\parallel}\mathbf b+\mathbf v_E+\mathbf v_{\nabla B}+\mathbf v_c,\qquad \dot v_{\parallel}=-\frac{\mu}{m}\mathbf b\cdot\nabla B+\frac{q}{m}E_{\parallel}
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
