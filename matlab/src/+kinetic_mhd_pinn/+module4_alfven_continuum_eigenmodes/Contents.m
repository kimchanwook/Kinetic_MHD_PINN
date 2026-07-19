% Module 4 - Alfven continuum and fluid-MHD eigenmodes.
%   solver                  - Public scaffold/physics entry point.
%   load_case               - Read benchmark JSON.
%   build_profiles          - Build density, iota, Alfven speed, and continua.
%   radial_stiffness_matrix - Symmetric finite-volume radial operator.
%   assemble_operator       - Assemble the two-harmonic block operator.
%   solve_benchmark         - Compute eigenfrequencies and eigenfunctions.
%   convergence_study       - Grid-refinement diagnostic.
%   write_outputs           - Write common CSV/JSON products.
