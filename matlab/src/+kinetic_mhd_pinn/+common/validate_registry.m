function validate_registry()
%VALIDATE_REGISTRY Validate module IDs and dependency references.

specs = kinetic_mhd_pinn.common.registry();
ids = {specs.id};
if numel(unique(ids)) ~= numel(ids)
    error('kinetic_mhd_pinn:DuplicateModuleId', ...
        'Module IDs must be unique.');
end

known = ids;
for i = 1:numel(specs)
    dependencies = specs(i).dependencies;
    unknown = setdiff(dependencies, known);
    if ~isempty(unknown)
        error('kinetic_mhd_pinn:UnknownDependency', ...
            '%s has unknown dependencies: %s', specs(i).id, strjoin(unknown, ', '));
    end
end
end
