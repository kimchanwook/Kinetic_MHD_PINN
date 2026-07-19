# Module 3: Guiding-Center Orbits, Confinement, and Wall Losses

**Status:** scaffold only.

**Purpose:** Follow energetic-particle guiding centers in three-dimensional fields, classify orbits, estimate prompt and delayed losses, and map lost-particle energy to the wall.

**Inputs:** $\mathbf B(\mathbf x)$, electric field if retained, particle birth coordinates, energy, pitch, and collision model.

**Outputs:** orbit histories, confinement fraction, loss time, loss phase space, and $q_{\mathrm{wall}}(\theta,\phi,t)$.

Expand the physics note and implementation note before replacing `solver.m` with a numerical method.


**Parallel contract:** keep governing equations, normalizations, state-product names, and verification cases synchronized with the corresponding Python module while maintaining an independent MATLAB implementation.
