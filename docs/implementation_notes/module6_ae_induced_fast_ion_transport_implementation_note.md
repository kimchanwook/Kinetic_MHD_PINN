# Module 6: Alfvén-Eigenmode-Induced Fast-Ion Transport - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Translate unstable mode amplitudes and resonance structure into energetic-particle redistribution, radial diffusion, convection, and loss enhancement.

## Upstream dependencies

Modules 2, 4, and 5.

## Input contract

$f_f$, $\omega_j$, $\gamma_j$, mode amplitudes, resonance functions, and transport closure parameters.

## Output contract

$D_{\mathrm{AE}}$, $V_{\mathrm{AE}}$, updated $f_f$, mode saturation histories, and redistributed loss power.

## Mathematical anchor

```text
\frac{\partial f_f}{\partial t}=\frac{1}{V\prime}\frac{\partial}{\partial\psi}\left[V\prime D_{\mathrm{AE}}\frac{\partial f_f}{\partial\psi}-V\prime V_{\mathrm{AE}}f_f\right]+S_f-C[f_f]
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
