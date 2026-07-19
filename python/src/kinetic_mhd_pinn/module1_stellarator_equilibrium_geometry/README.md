# Module 1: Stellarator Equilibrium and Magnetic Geometry

**Status:** scaffold only.

**Purpose:** Represent the magnetic configuration, flux surfaces, rotational transform, pressure profile, and equilibrium quantities required by every downstream module.

**Inputs:** coil or boundary parameters, pressure profile $p(\psi)$, current profile, and equilibrium controls.

**Outputs:** $\mathbf B(\mathbf x)$, $\psi(\mathbf x)$, $\iota(\psi)$, metric/Jacobian data, and flux-surface geometry.

Expand the physics note and implementation note before replacing `solver.py` with a numerical method.
