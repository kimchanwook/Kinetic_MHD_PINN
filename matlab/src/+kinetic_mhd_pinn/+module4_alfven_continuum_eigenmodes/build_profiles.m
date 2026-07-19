function profiles = build_profiles(caseData)
%BUILD_PROFILES Construct density, iota, Alfven-speed, and continuum profiles.
mu0 = 4.0e-7 * pi;
N = double(caseData.numerics.radial_points);
if N < 8
    error('KineticMHD:Module4:Grid', 'radial_points must be at least 8.');
end
if caseData.geometry.major_radius_m <= 0 || caseData.geometry.magnetic_field_t <= 0
    error('KineticMHD:Module4:Geometry', 'Major radius and magnetic field must be positive.');
end
if caseData.profiles.mass_density_axis_kg_m3 <= 0
    error('KineticMHD:Module4:Density', 'Mass density must be positive.');
end
if caseData.profiles.mass_density_edge_fraction <= 0 || caseData.profiles.mass_density_edge_fraction > 1
    error('KineticMHD:Module4:Density', 'mass_density_edge_fraction must be in (0,1].');
end
harmonics = double(caseData.mode.poloidal_harmonics);
if harmonics(2) ~= harmonics(1) + 1
    error('KineticMHD:Module4:Harmonics', 'The baseline benchmark requires adjacent m and m+1 harmonics.');
end
if caseData.mode.coupling_fraction < 0 || caseData.mode.coupling_fraction >= 1
    error('KineticMHD:Module4:Coupling', 'coupling_fraction must be in [0,1) to preserve local positive definiteness.');
end

h = 1.0 / N;
s = ((0:N-1).' + 0.5) * h;
p = caseData.profiles;
rho = p.mass_density_axis_kg_m3 .* (1.0 - (1.0 - p.mass_density_edge_fraction) .* s.^p.mass_density_exponent);
iota = p.iota_axis + (p.iota_edge - p.iota_axis) .* s.^p.iota_exponent;
vA = caseData.geometry.magnetic_field_t ./ sqrt(mu0 .* rho);

nTor = double(caseData.mode.toroidal_number);
m = harmonics(1);
mp1 = harmonics(2);
omegaScale = vA ./ caseData.geometry.major_radius_m;
omegaM = abs(nTor - m .* iota) .* omegaScale;
omegaMp1 = abs(nTor - mp1 .* iota) .* omegaScale;

crossingIota = 2.0 * nTor / (2.0 * m + 1.0);
fraction = (crossingIota - p.iota_axis) / (p.iota_edge - p.iota_axis);
fraction = min(max(fraction, 0.0), 1.0);
crossingS = fraction^(1.0 / p.iota_exponent);
[~, crossingIndex] = min(abs(s - crossingS));
coupling = caseData.mode.coupling_fraction .* omegaM .* omegaMp1 .* exp(-((s - crossingS) ./ caseData.mode.coupling_width).^2);
average = 0.5 .* (omegaM.^2 + omegaMp1.^2);
split = sqrt((0.5 .* (omegaM.^2 - omegaMp1.^2)).^2 + coupling.^2);
localLower = sqrt(max(average - split, 0.0));
localUpper = sqrt(max(average + split, 0.0));

profiles = struct( ...
    's', s, ...
    'h', h, ...
    'mass_density_kg_m3', rho, ...
    'iota', iota, ...
    'alfven_speed_m_s', vA, ...
    'omega_m_rad_s', omegaM, ...
    'omega_mp1_rad_s', omegaMp1, ...
    'coupling_omega2_s2', coupling, ...
    'local_lower_rad_s', localLower, ...
    'local_upper_rad_s', localUpper, ...
    'crossing_iota', crossingIota, ...
    'crossing_s', crossingS, ...
    'crossing_index', crossingIndex, ...
    'gap_lower_rad_s', localLower(crossingIndex), ...
    'gap_upper_rad_s', localUpper(crossingIndex));
end
