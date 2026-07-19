function output = convergence_study(caseData, grids)
%CONVERGENCE_STUDY Evaluate eigenfrequency convergence against the finest grid.
if nargin < 2
    grids = double(caseData.numerics.convergence_grids);
end
grids = double(grids(:).');
results = cell(size(grids));
for i = 1:numel(grids)
    localCase = caseData;
    localCase.numerics.radial_points = grids(i);
    results{i} = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.solve_benchmark(localCase);
end
reference = results{end}.frequency_hz;
k = numel(reference);
rows = zeros(numel(grids), 1 + 2*k);
rows(:,1) = grids(:);
for i = 1:numel(grids)
    frequency = results{i}.frequency_hz;
    for j = 1:k
        rows(i, 2*j) = frequency(j);
        rows(i, 2*j+1) = abs(frequency(j) - reference(j)) / reference(j);
    end
end
names = {'radial_points'};
for j = 1:k
    names{end+1} = sprintf('mode_%d_frequency_hz', j); %#ok<AGROW>
    names{end+1} = sprintf('mode_%d_relative_error_to_finest', j); %#ok<AGROW>
end
output = array2table(rows, 'VariableNames', names);
end
