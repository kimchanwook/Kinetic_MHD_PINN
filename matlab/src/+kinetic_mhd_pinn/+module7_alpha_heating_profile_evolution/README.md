# Module 7: Alpha Heating and Thermal-Profile Evolution

**Status:** scaffold only.

**Purpose:** Convert confined energetic-particle power into electron/ion heating and evolve reduced density, temperature, pressure, and Alfvén-speed profiles.

**Inputs:** deposited alpha/NBI power, loss power, transport coefficients, radiation losses, and initial profiles.

**Outputs:** $T_i(\psi,t)$, $T_e(\psi,t)$, $p(\psi,t)$, $\rho(\psi,t)$, $v_A(\psi,t)$, and fusion-source updates.

Expand the physics note and implementation note before replacing `solver.m` with a numerical method.


**Parallel contract:** keep governing equations, normalizations, state-product names, and verification cases synchronized with the corresponding Python module while maintaining an independent MATLAB implementation.
