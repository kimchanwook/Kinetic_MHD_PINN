# Module 5: Kinetic Energetic-Particle Drive and Damping

**Status:** scaffold only.

**Purpose:** Evaluate resonant energetic-particle drive and reduced damping contributions to determine whether each Alfvén eigenmode grows or decays.

**Inputs:** mode structure, mode frequency, equilibrium, orbit frequencies, and $f_f$.

**Outputs:** $\gamma_{\mathrm{EP}}$, damping terms, net $\gamma_j$, resonance maps, and stability labels.

Expand the physics note and implementation note before replacing `solver.m` with a numerical method.


**Parallel contract:** keep governing equations, normalizations, state-product names, and verification cases synchronized with the corresponding Python module while maintaining an independent MATLAB implementation.
