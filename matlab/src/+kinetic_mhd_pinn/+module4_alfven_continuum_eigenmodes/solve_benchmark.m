function result = solve_benchmark(caseInput)
%SOLVE_BENCHMARK Solve the reduced two-harmonic shear-Alfven eigenproblem.
% module_4 physics implementation milestone.
if ischar(caseInput) || isstring(caseInput)
    caseData = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.load_case(string(caseInput));
else
    caseData = caseInput;
end
profiles = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.build_profiles(caseData);
A = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.assemble_operator(caseData, profiles);
k = double(caseData.numerics.number_of_eigenpairs);
opts = struct('tol', 1.0e-12, 'maxit', 200000, 'issym', true, 'isreal', true, 'disp', 0);
[V, D] = eigs(A, k, 'smallestreal', opts);
values = real(diag(D));
[values, order] = sort(values, 'ascend');
V = real(V(:, order));
if any(values <= 0)
    error('KineticMHD:Module4:Eigenvalue', 'Non-positive omega^2 encountered.');
end
for j = 1:k
    normValue = sqrt(profiles.h * (V(:,j).' * V(:,j)));
    if normValue == 0
        error('KineticMHD:Module4:Eigenvector', 'Zero eigenvector returned.');
    end
    V(:,j) = V(:,j) / normValue;
    [~, dominant] = max(abs(V(:,j)));
    if V(dominant,j) < 0
        V(:,j) = -V(:,j);
    end
end
residuals = zeros(k,1);
for j = 1:k
    residual = A * V(:,j) - values(j) * V(:,j);
    denominator = max(norm(A * V(:,j)), realmin);
    residuals(j) = norm(residual) / denominator;
end
result = struct( ...
    'case_data', caseData, ...
    'profiles', profiles, ...
    'operator', A, ...
    'omega2_s2', values, ...
    'omega_rad_s', sqrt(values), ...
    'frequency_hz', sqrt(values) / (2.0*pi), ...
    'frequency_khz', sqrt(values) / (2.0*pi*1.0e3), ...
    'eigenvectors', V, ...
    'residual_norms', residuals);
end
