function K = radial_stiffness_matrix(caseData, profiles)
%RADIAL_STIFFNESS_MATRIX Symmetric finite-volume radial operator.
% The operator approximates -d/ds[D(s) du/ds] on cell centers, with zero
% left-boundary flux and a zero right-boundary face value.
mu0 = 4.0e-7 * pi;
N = numel(profiles.s);
h2 = profiles.h^2;
omegaScale2 = (profiles.alfven_speed_m_s ./ caseData.geometry.major_radius_m).^2;
dCenter = caseData.mode.radial_stiffness_fraction .* omegaScale2;
dFace = 0.5 .* (dCenter(1:end-1) + dCenter(2:end));
dEdge = caseData.mode.radial_stiffness_fraction .* ( ...
    caseData.geometry.magnetic_field_t / sqrt(mu0 * caseData.profiles.mass_density_axis_kg_m3 * caseData.profiles.mass_density_edge_fraction) ...
    / caseData.geometry.major_radius_m)^2;

K = sparse(N, N);
K(1,1) = K(1,1) + dFace(1) / h2;
K(1,2) = -dFace(1) / h2;
for i = 2:N-1
    K(i,i) = K(i,i) + (dFace(i-1) + dFace(i)) / h2;
    K(i,i-1) = -dFace(i-1) / h2;
    K(i,i+1) = -dFace(i) / h2;
end
K(N,N) = K(N,N) + (dFace(end) + 2.0 * dEdge) / h2;
K(N,N-1) = -dFace(end) / h2;
end
