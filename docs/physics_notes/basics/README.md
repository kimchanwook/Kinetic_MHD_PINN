# Basics physics-note curriculum

This directory contains the 100-note prerequisite curriculum for `Kinetic_MHD_PINN`.

**Current status:** thirty notes are substantive standalone textbook drafts, version 1.0. Batch 1 contains Basics 01, 02, 03, 05, 06, 07, 11, 12, 13, 17. Batch 2 contains Basics 18, 19, 21, 22, 24, 25, 26, 29, 31, 32. Batch 3 contains Basics 34, 35, 36, 37, 39, 40, 41, 42, 44, and 48. The remaining seventy notes remain curriculum scaffolds. Each draft is maintained as its own `.tex` and `.pdf`; this repository does not assemble the basics notes into a combined volume.

The authoritative machine-readable course map is `curriculum_manifest.json`. The compiled navigation document is `basics_index.pdf`.

Status markers:

- **[DRAFT v1]** substantive standalone textbook draft
- **[SCAFFOLD]** reserved scope and course architecture only

## I - Mathematical and computational foundations

- **[DRAFT v1]** `basics_01_units_dimensions_and_normalization.tex` - Units, Dimensions, and Normalization
- **[DRAFT v1]** `basics_02_vectors_fields_and_coordinate_systems.tex` - Vectors, Fields, and Coordinate Systems
- **[DRAFT v1]** `basics_03_vector_calculus_for_plasma_physics.tex` - Vector Calculus for Plasma Physics
- **[SCAFFOLD]** `basics_04_ordinary_differential_equations.tex` - Ordinary Differential Equations
- **[DRAFT v1]** `basics_05_partial_differential_equations.tex` - Partial Differential Equations
- **[DRAFT v1]** `basics_06_linear_algebra_and_eigenvalue_problems.tex` - Linear Algebra and Eigenvalue Problems
- **[DRAFT v1]** `basics_07_fourier_analysis_and_normal_modes.tex` - Fourier Analysis and Normal Modes
- **[SCAFFOLD]** `basics_08_complex_numbers_phasors_and_wave_notation.tex` - Complex Numbers, Phasors, and Wave Notation
- **[SCAFFOLD]** `basics_09_variational_principles_and_energy_methods.tex` - Variational Principles and Energy Methods
- **[SCAFFOLD]** `basics_10_probability_statistics_and_monte_carlo.tex` - Probability, Statistics, and Monte Carlo

## II - Electromagnetism foundations

- **[DRAFT v1]** `basics_11_electric_and_magnetic_fields.tex` - Electric and Magnetic Fields
- **[DRAFT v1]** `basics_12_maxwell_equations.tex` - Maxwell Equations
- **[DRAFT v1]** `basics_13_lorentz_force_and_charged_particle_motion.tex` - Lorentz Force and Charged-Particle Motion
- **[SCAFFOLD]** `basics_14_electromagnetic_energy_and_poynting_theorem.tex` - Electromagnetic Energy and Poynting Theorem
- **[SCAFFOLD]** `basics_15_magnetic_pressure_tension_and_flux.tex` - Magnetic Pressure, Tension, and Flux
- **[SCAFFOLD]** `basics_16_gauge_fields_and_electromagnetic_potentials.tex` - Gauge Fields and Electromagnetic Potentials

## III - Elementary plasma physics

- **[DRAFT v1]** `basics_17_what_is_a_plasma.tex` - What Is a Plasma?
- **[DRAFT v1]** `basics_18_debye_shielding_and_plasma_frequency.tex` - Debye Shielding and Plasma Frequency
- **[DRAFT v1]** `basics_19_plasma_distributions_and_temperature.tex` - Plasma Distributions and Temperature
- **[SCAFFOLD]** `basics_20_collisions_in_plasmas.tex` - Collisions in Plasmas
- **[DRAFT v1]** `basics_21_single_fluid_and_multifluid_descriptions.tex` - Single-Fluid and Multifluid Descriptions
- **[DRAFT v1]** `basics_22_moments_of_the_kinetic_equation.tex` - Moments of the Kinetic Equation
- **[SCAFFOLD]** `basics_23_plasma_beta_and_dimensionless_parameters.tex` - Plasma Beta and Dimensionless Parameters

## IV - Magnetohydrodynamics

- **[DRAFT v1]** `basics_24_derivation_of_ideal_magnetohydrodynamics.tex` - Derivation of Ideal Magnetohydrodynamics
- **[DRAFT v1]** `basics_25_conservation_laws_in_mhd.tex` - Conservation Laws in MHD
- **[DRAFT v1]** `basics_26_ideal_ohms_law_and_flux_freezing.tex` - Ideal Ohm's Law and Flux Freezing
- **[SCAFFOLD]** `basics_27_resistive_and_nonideal_mhd.tex` - Resistive and Nonideal MHD
- **[SCAFFOLD]** `basics_28_mhd_force_balance_and_equilibrium.tex` - MHD Force Balance and Equilibrium
- **[DRAFT v1]** `basics_29_linearization_of_mhd_equations.tex` - Linearization of MHD Equations
- **[SCAFFOLD]** `basics_30_mhd_energy_principle_and_stability.tex` - MHD Energy Principle and Stability

## V - Plasma waves and Alfvén physics

- **[DRAFT v1]** `basics_31_introduction_to_waves_in_plasmas.tex` - Introduction to Waves in Plasmas
- **[DRAFT v1]** `basics_32_alfven_waves_from_first_principles.tex` - Alfvén Waves from First Principles
- **[SCAFFOLD]** `basics_33_fast_and_slow_magnetosonic_waves.tex` - Fast and Slow Magnetosonic Waves
- **[DRAFT v1]** `basics_34_parallel_wave_number_and_field_line_propagation.tex` - Parallel Wave Number and Field-Line Propagation
- **[DRAFT v1]** `basics_35_alfven_continuum.tex` - Alfvén Continuum
- **[DRAFT v1]** `basics_36_coupled_harmonics_and_avoided_crossings.tex` - Coupled Harmonics and Avoided Crossings
- **[DRAFT v1]** `basics_37_toroidal_alfven_eigenmodes.tex` - Toroidal Alfvén Eigenmodes
- **[SCAFFOLD]** `basics_38_stellarator_alfven_eigenmodes.tex` - Stellarator Alfvén Eigenmodes
- **[DRAFT v1]** `basics_39_wave_particle_resonance.tex` - Wave-Particle Resonance
- **[DRAFT v1]** `basics_40_growth_damping_and_complex_frequency.tex` - Growth, Damping, and Complex Frequency

## VI - Kinetic theory and energetic particles

- **[DRAFT v1]** `basics_41_phase_space_and_distribution_functions.tex` - Phase Space and Distribution Functions
- **[DRAFT v1]** `basics_42_vlasov_equation.tex` - Vlasov Equation
- **[SCAFFOLD]** `basics_43_boltzmann_and_fokker_planck_equations.tex` - Boltzmann and Fokker-Planck Equations
- **[DRAFT v1]** `basics_44_guiding_center_theory.tex` - Guiding-Center Theory
- **[SCAFFOLD]** `basics_45_particle_drifts_in_nonuniform_fields.tex` - Particle Drifts in Nonuniform Fields
- **[SCAFFOLD]** `basics_46_trapped_passing_and_banana_orbits.tex` - Trapped, Passing, and Banana Orbits
- **[SCAFFOLD]** `basics_47_canonical_momentum_and_orbit_invariants.tex` - Canonical Momentum and Orbit Invariants
- **[DRAFT v1]** `basics_48_energetic_particle_distributions.tex` - Energetic-Particle Distributions
- **[SCAFFOLD]** `basics_49_kinetic_mhd_and_hybrid_models.tex` - Kinetic MHD and Hybrid Models
- **[SCAFFOLD]** `basics_50_delta_f_particle_methods.tex` - Delta-f Particle Methods
- **[SCAFFOLD]** `basics_51_quasilinear_transport.tex` - Quasilinear Transport

## VII - Fusion and burning-plasma foundations

- **[SCAFFOLD]** `basics_52_nuclear_fusion_reactions.tex` - Nuclear Fusion Reactions
- **[SCAFFOLD]** `basics_53_fusion_reactivity_and_reaction_rates.tex` - Fusion Reactivity and Reaction Rates
- **[SCAFFOLD]** `basics_54_alpha_particle_birth_and_slowing_down.tex` - Alpha-Particle Birth and Slowing Down
- **[SCAFFOLD]** `basics_55_alpha_heating_and_burning_plasma_feedback.tex` - Alpha Heating and Burning-Plasma Feedback
- **[SCAFFOLD]** `basics_56_lawson_criterion_and_fusion_power_balance.tex` - Lawson Criterion and Fusion Power Balance
- **[SCAFFOLD]** `basics_57_neutral_beam_injection.tex` - Neutral Beam Injection
- **[SCAFFOLD]** `basics_58_fast_ion_losses_and_wall_heat_loads.tex` - Fast-Ion Losses and Wall Heat Loads

## VIII - Stellarator and magnetic-confinement foundations

- **[SCAFFOLD]** `basics_59_magnetic_confinement_concepts.tex` - Magnetic-Confinement Concepts
- **[SCAFFOLD]** `basics_60_tokamaks_and_stellarators.tex` - Tokamaks and Stellarators
- **[SCAFFOLD]** `basics_61_toroidal_coordinates_and_magnetic_surfaces.tex` - Toroidal Coordinates and Magnetic Surfaces
- **[SCAFFOLD]** `basics_62_rotational_transform_magnetic_shear_and_resonances.tex` - Rotational Transform, Magnetic Shear, and Resonances
- **[SCAFFOLD]** `basics_63_stellarator_symmetry_and_fourier_geometry.tex` - Stellarator Symmetry and Fourier Geometry
- **[SCAFFOLD]** `basics_64_quasisymmetry_and_neoclassical_confinement.tex` - Quasisymmetry and Neoclassical Confinement
- **[SCAFFOLD]** `basics_65_magnetic_field_coils_and_biot_savart_law.tex` - Magnetic-Field Coils and the Biot-Savart Law
- **[SCAFFOLD]** `basics_66_mhd_equilibrium_codes_and_vmec_concepts.tex` - MHD Equilibrium Codes and VMEC Concepts

## IX - Computational physics methods

- **[SCAFFOLD]** `basics_67_discretization_and_numerical_error.tex` - Discretization and Numerical Error
- **[SCAFFOLD]** `basics_68_finite_difference_methods.tex` - Finite-Difference Methods
- **[SCAFFOLD]** `basics_69_finite_volume_methods.tex` - Finite-Volume Methods
- **[SCAFFOLD]** `basics_70_finite_element_methods.tex` - Finite-Element Methods
- **[SCAFFOLD]** `basics_71_spectral_and_fourier_methods.tex` - Spectral and Fourier Methods
- **[SCAFFOLD]** `basics_72_time_integration_methods.tex` - Time-Integration Methods
- **[SCAFFOLD]** `basics_73_numerical_eigenvalue_solvers.tex` - Numerical Eigenvalue Solvers
- **[SCAFFOLD]** `basics_74_particle_pushers.tex` - Particle Pushers
- **[SCAFFOLD]** `basics_75_particle_in_cell_methods.tex` - Particle-in-Cell Methods
- **[SCAFFOLD]** `basics_76_interpolation_and_conservative_remapping.tex` - Interpolation and Conservative Remapping
- **[SCAFFOLD]** `basics_77_verification_validation_and_benchmarking.tex` - Verification, Validation, and Benchmarking
- **[SCAFFOLD]** `basics_78_uncertainty_quantification.tex` - Uncertainty Quantification
- **[SCAFFOLD]** `basics_79_high_performance_computing_for_simulation.tex` - High-Performance Computing for Simulation

## X - Multiphysics coupling

- **[SCAFFOLD]** `basics_80_multiphysics_modeling.tex` - Multiphysics Modeling
- **[SCAFFOLD]** `basics_81_explicit_implicit_and_partitioned_coupling.tex` - Explicit, Implicit, and Partitioned Coupling
- **[SCAFFOLD]** `basics_82_fixed_point_and_newton_coupling_methods.tex` - Fixed-Point and Newton Coupling Methods
- **[SCAFFOLD]** `basics_83_multirate_and_multiscale_time_integration.tex` - Multirate and Multiscale Time Integration
- **[SCAFFOLD]** `basics_84_conservation_across_module_interfaces.tex` - Conservation Across Module Interfaces
- **[SCAFFOLD]** `basics_85_dependency_graphs_and_coupling_sequence.tex` - Dependency Graphs and Coupling Sequence
- **[SCAFFOLD]** `basics_86_digital_twins_for_physical_systems.tex` - Digital Twins for Physical Systems

## XI - Physics-informed machine learning

- **[SCAFFOLD]** `basics_87_neural_networks_from_first_principles.tex` - Neural Networks from First Principles
- **[SCAFFOLD]** `basics_88_automatic_differentiation.tex` - Automatic Differentiation
- **[SCAFFOLD]** `basics_89_physics_informed_neural_networks.tex` - Physics-Informed Neural Networks
- **[SCAFFOLD]** `basics_90_pinn_loss_design_and_training_pathologies.tex` - PINN Loss Design and Training Pathologies
- **[SCAFFOLD]** `basics_91_eigenvalue_pinns.tex` - Eigenvalue PINNs
- **[SCAFFOLD]** `basics_92_operator_learning.tex` - Operator Learning
- **[SCAFFOLD]** `basics_93_hamiltonian_and_symplectic_neural_networks.tex` - Hamiltonian and Symplectic Neural Networks
- **[SCAFFOLD]** `basics_94_surrogate_models_for_plasma_simulation.tex` - Surrogate Models for Plasma Simulation
- **[SCAFFOLD]** `basics_95_inverse_problems_and_data_assimilation.tex` - Inverse Problems and Data Assimilation

## XII - Graph neural networks and scientific graphs

- **[SCAFFOLD]** `basics_96_graph_theory_for_physical_systems.tex` - Graph Theory for Physical Systems
- **[SCAFFOLD]** `basics_97_graph_neural_networks.tex` - Graph Neural Networks
- **[SCAFFOLD]** `basics_98_physical_dependency_graph_learning.tex` - Physical Dependency-Graph Learning
- **[SCAFFOLD]** `basics_99_gnns_for_multiphysics_coupling.tex` - GNNs for Multiphysics Coupling
- **[SCAFFOLD]** `basics_100_interpretable_and_physics_constrained_graph_learning.tex` - Interpretable and Physics-Constrained Graph Learning
