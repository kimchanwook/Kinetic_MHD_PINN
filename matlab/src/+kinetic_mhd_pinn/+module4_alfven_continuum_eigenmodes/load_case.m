function caseData = load_case(path)
%LOAD_CASE Read and validate the shared reduced-AE JSON configuration.
arguments
    path (1,1) string
end
caseData = jsondecode(fileread(path));
caseData.mode.poloidal_harmonics = double(caseData.mode.poloidal_harmonics(:).');
caseData.numerics.convergence_grids = double(caseData.numerics.convergence_grids(:).');
end
