# Module 5: Kinetic Energetic-Particle Drive and Damping - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Evaluate resonant energetic-particle drive and reduced damping contributions to determine whether each Alfvén eigenmode grows or decays.

## Upstream dependencies

Modules 2--4.

## Input contract

mode structure, mode frequency, equilibrium, orbit frequencies, and $f_f$.

## Output contract

$\gamma_{\mathrm{EP}}$, damping terms, net $\gamma_j$, resonance maps, and stability labels.

## Mathematical anchor

```text
\gamma_j=\gamma_{\mathrm{EP},j}-\gamma_{\mathrm{cont},j}-\gamma_{\mathrm{Landau},j}-\gamma_{\mathrm{FLR},j}-\gamma_{\mathrm{other},j}
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
