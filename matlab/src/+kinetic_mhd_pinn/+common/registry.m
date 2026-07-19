function specs = registry()
%REGISTRY Return the project module registry.

specs = repmat(struct('id', '', 'number', 0, 'name', '', 'package', '', ...
    'dependencies', {{}}, 'status', ''), 1, 11);
    specs(1) = makeSpec('module_1', 1, 'Stellarator Equilibrium and Magnetic Geometry', 'module1_stellarator_equilibrium_geometry', {}, 'scaffold');
    specs(2) = makeSpec('module_2', 2, 'Energetic-Particle Sources and Distribution Functions', 'module2_energetic_particle_sources', {'module_1'}, 'scaffold');
    specs(3) = makeSpec('module_3', 3, 'Guiding-Center Orbits, Confinement, and Wall Losses', 'module3_guiding_center_orbits_wall_losses', {'module_1', 'module_2'}, 'scaffold');
    specs(4) = makeSpec('module_4', 4, 'Alfven Continuum and Fluid-MHD Eigenmodes', 'module4_alfven_continuum_eigenmodes', {'module_1', 'module_7'}, 'reduced-benchmark');
    specs(5) = makeSpec('module_5', 5, 'Kinetic Energetic-Particle Drive and Damping', 'module5_kinetic_energetic_particle_drive', {'module_2', 'module_3', 'module_4'}, 'scaffold');
    specs(6) = makeSpec('module_6', 6, 'Alfven-Eigenmode-Induced Fast-Ion Transport', 'module6_ae_induced_fast_ion_transport', {'module_2', 'module_4', 'module_5'}, 'scaffold');
    specs(7) = makeSpec('module_7', 7, 'Alpha Heating and Thermal-Profile Evolution', 'module7_alpha_heating_profile_evolution', {'module_2', 'module_3', 'module_6'}, 'scaffold');
    specs(8) = makeSpec('module_8', 8, 'Coupled Kinetic-MHD Multiphysics Integration', 'module8_coupled_multiphysics_integration', {'module_1', 'module_2', 'module_3', 'module_4', 'module_5', 'module_6', 'module_7'}, 'scaffold');
    specs(9) = makeSpec('module_9', 9, 'PINN and Neural-Operator Surrogates', 'module9_pinn_neural_operator_surrogates', {'module_8'}, 'scaffold');
    specs(10) = makeSpec('module_10', 10, 'Synthetic Diagnostics and Physics-Informed Inverse Modeling', 'module10_synthetic_diagnostics_inverse_modeling', {'module_3', 'module_4', 'module_5', 'module_6', 'module_7', 'module_8'}, 'scaffold');
    specs(11) = makeSpec('module_11', 11, 'GNN Physical Dependency Discovery and Coupling Optimization', 'module11_gnn_dependency_coupling_optimization', {'module_8'}, 'scaffold');
end

function spec = makeSpec(id, number, name, package, dependencies, status)
spec = struct('id', id, 'number', number, 'name', name, ...
    'package', package, 'dependencies', {dependencies}, 'status', status);
end
