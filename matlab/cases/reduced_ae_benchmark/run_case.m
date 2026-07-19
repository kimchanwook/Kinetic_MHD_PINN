function result = run_case(outputDir)
%RUN_CASE Execute the MATLAB reduced two-harmonic Alfven benchmark.
caseDir = fileparts(mfilename('fullpath'));
matlabRoot = fileparts(fileparts(caseDir));
repoRoot = fileparts(matlabRoot);
addpath(fullfile(matlabRoot, 'src'));
if nargin < 1
    outputDir = fullfile(matlabRoot, 'outputs', 'reduced_ae_benchmark');
end
casePath = fullfile(caseDir, 'case.json');
caseData = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.load_case(string(casePath));
result = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.solve_benchmark(caseData);
convergence = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.convergence_study(caseData);
kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.write_outputs(result, string(outputDir), convergence);

p = result.profiles;
harmonics = double(result.case_data.mode.poloidal_harmonics);
figure('Visible','off');
plot(p.s, p.omega_m_rad_s/(2*pi*1e3), p.s, p.omega_mp1_rad_s/(2*pi*1e3), ...
    p.s, p.local_lower_rad_s/(2*pi*1e3), '--', p.s, p.local_upper_rad_s/(2*pi*1e3), '--');
xline(p.crossing_s, ':');
xlabel('Normalized radial coordinate, s'); ylabel('Frequency (kHz)');
title('Reduced two-harmonic shear-Alfven continuum');
legend(sprintf('uncoupled m=%d', harmonics(1)), sprintf('uncoupled m=%d', harmonics(2)), ...
    'coupled local lower', 'coupled local upper', 'predicted crossing', 'Location', 'best');
grid on;
exportgraphics(gcf, fullfile(outputDir, 'continuum.png'), 'Resolution', 180);
close(gcf);

fprintf('case: %s\n', result.case_data.case_name);
fprintf('crossing: iota=%.6f, s=%.6f\n', p.crossing_iota, p.crossing_s);
fprintf('local gap at crossing: %.3f-%.3f kHz\n', p.gap_lower_rad_s/(2*pi*1e3), p.gap_upper_rad_s/(2*pi*1e3));
for j = 1:numel(result.frequency_khz)
    fprintf('mode %2d: %12.6f kHz, relative residual=%.3e\n', j, result.frequency_khz(j), result.residual_norms(j));
end
fprintf('outputs: %s\n', outputDir);
end
