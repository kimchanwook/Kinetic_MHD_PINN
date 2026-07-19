# Module 7: Alpha Heating and Thermal-Profile Evolution - Implementation Note

## Status

Scaffold only. No validated numerical solver is implemented in the baseline.

## Purpose

Convert confined energetic-particle power into electron/ion heating and evolve reduced density, temperature, pressure, and Alfvén-speed profiles.

## Upstream dependencies

Modules 2, 3, and 6.

## Input contract

deposited alpha/NBI power, loss power, transport coefficients, radiation losses, and initial profiles.

## Output contract

$T_i(\psi,t)$, $T_e(\psi,t)$, $p(\psi,t)$, $\rho(\psi,t)$, $v_A(\psi,t)$, and fusion-source updates.

## Mathematical anchor

```text
\frac{3}{2}\frac{\partial(n_sT_s)}{\partial t}=-\frac{1}{V\prime}\frac{\partial}{\partial\psi}\left(V\prime Q_s\right)+P_{\alpha\rightarrow s}+P_{\mathrm{NBI}\rightarrow s}-P_{\mathrm{loss},s}
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
