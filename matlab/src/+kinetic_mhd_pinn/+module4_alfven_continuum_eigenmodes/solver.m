function output = solver(caseInput)
%SOLVER Module 4 public entry point.
% With no input, returns the architecture contract for module_4. With a JSON
% path or decoded case struct, solves the reduced two-harmonic benchmark.
if nargin == 0
    output = kinetic_mhd_pinn.common.ScaffoldModule( ...
        'module_4', {}, 'module_4_contract_ready');
else
    output = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.solve_benchmark(caseInput);
end
end
