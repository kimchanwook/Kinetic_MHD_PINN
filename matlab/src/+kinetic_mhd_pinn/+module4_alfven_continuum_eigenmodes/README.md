# Module 4 - Alfvén continuum and fluid-MHD eigenmodes

## Implemented milestone

This package now contains the first conventional physics solver in the repository: a self-adjoint, two-harmonic reduced shear-Alfvén eigenvalue benchmark. It computes prescribed density and rotational-transform profiles, uncoupled continuum branches, a localized avoided crossing, finite-volume radial coupling, and the lowest coupled eigenpairs.

The model is a verification and software-integration benchmark. It is **not** a predictive VMEC-based stellarator Alfvén-eigenmode calculation. Its purpose is to establish equations, normalization, boundary conditions, output contracts, convergence behavior, and independent Python/MATLAB implementations before kinetic drive and PINN work begins.

The public entry point is `solver.m`. With no input it returns the architecture scaffold used by the backbone test; with a JSON path or decoded case struct it runs the benchmark.
