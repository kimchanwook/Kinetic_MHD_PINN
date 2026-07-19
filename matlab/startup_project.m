function startup_project()
%STARTUP_PROJECT Add the MATLAB project source and case directories to the path.

matlabRoot = fileparts(mfilename('fullpath'));
addpath(fullfile(matlabRoot, 'src'));
addpath(fullfile(matlabRoot, 'cases'));
fprintf('Kinetic MHD-PINN MATLAB paths added from %s\n', matlabRoot);
end
