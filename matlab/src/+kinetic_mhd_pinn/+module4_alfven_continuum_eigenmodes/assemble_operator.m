function A = assemble_operator(caseData, profiles)
%ASSEMBLE_OPERATOR Build the 2N-by-2N self-adjoint coupled-harmonic matrix.
N = numel(profiles.s);
K = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.radial_stiffness_matrix(caseData, profiles);
Am = K + spdiags(profiles.omega_m_rad_s.^2, 0, N, N);
Amp1 = K + spdiags(profiles.omega_mp1_rad_s.^2, 0, N, N);
C = spdiags(profiles.coupling_omega2_s2, 0, N, N);
A = [Am, C; C, Amp1];
end
