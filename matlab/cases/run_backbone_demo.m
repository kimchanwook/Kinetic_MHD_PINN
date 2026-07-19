function run_backbone_demo()
%RUN_BACKBONE_DEMO Exercise the MATLAB registry and shared-state contract.

casesDir = fileparts(mfilename('fullpath'));
matlabRoot = fileparts(casesDir);
sourceDir = fullfile(matlabRoot, 'src');
addpath(sourceDir);
cleanup = onCleanup(@() rmpath(sourceDir)); %#ok<NASGU>

kinetic_mhd_pinn.common.validate_registry();
specs = kinetic_mhd_pinn.common.registry();
order = kinetic_mhd_pinn.common.nominal_startup_order();
state = kinetic_mhd_pinn.common.CoupledState( ...
    struct('purpose', 'architecture smoke test'));

fprintf('Kinetic MHD-PINN MATLAB backbone\n');
fprintf('Nominal startup order:\n');
for i = 1:numel(order)
    moduleId = order{i};
    index = find(strcmp({specs.id}, moduleId), 1, 'first');
    spec = specs(index);
    fprintf('  %02d. %s [%s]\n', spec.number, spec.name, spec.status);
    state.publish(moduleId, [moduleId '_registered'], true);
end
fprintf('Registered %d module transitions.\n', numel(state.history));
fprintf('No physics solver was executed; this is an interface-only smoke test.\n');
end
