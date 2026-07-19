function tests = test_module4_reduced_ae
tests = functiontests(localfunctions);
end

function setupOnce(testCase)
matlabRoot = fileparts(fileparts(mfilename('fullpath')));
repoRoot = fileparts(matlabRoot);
addpath(fullfile(matlabRoot, 'src'));
casePath = fullfile(matlabRoot, 'cases', 'reduced_ae_benchmark', 'case.json');
testCase.TestData.matlabRoot = matlabRoot;
testCase.TestData.repoRoot = repoRoot;
testCase.TestData.casePath = casePath;
testCase.TestData.caseData = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.load_case(string(casePath));
testCase.TestData.result = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.solve_benchmark(testCase.TestData.caseData);
end

function testCaseFilesMatch(testCase)
pythonCase = fullfile(testCase.TestData.repoRoot, 'python', 'cases', 'reduced_ae_benchmark', 'case.json');
verifyEqual(testCase, fileread(testCase.TestData.casePath), fileread(pythonCase));
end

function testOperatorSymmetryAndResidual(testCase)
result = testCase.TestData.result;
asymmetry = norm(result.operator - result.operator.', 'fro') / norm(result.operator, 'fro');
verifyLessThan(testCase, asymmetry, result.case_data.verification.matrix_symmetry_tolerance);
verifyGreaterThan(testCase, min(result.omega2_s2), 0.0);
verifyLessThan(testCase, max(result.residual_norms), result.case_data.verification.eigen_residual_tolerance);
end

function testNormalization(testCase)
result = testCase.TestData.result;
for j = 1:size(result.eigenvectors, 2)
    value = result.profiles.h * (result.eigenvectors(:,j).' * result.eigenvectors(:,j));
    verifyEqual(testCase, value, 1.0, 'AbsTol', 1.0e-10);
end
end

function testAlfvenScalings(testCase)
baseCase = testCase.TestData.caseData;
baseResult = testCase.TestData.result;
fieldCase = baseCase;
fieldCase.geometry.magnetic_field_t = 2.0 * baseCase.geometry.magnetic_field_t;
fieldResult = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.solve_benchmark(fieldCase);
verifyEqual(testCase, fieldResult.frequency_hz ./ baseResult.frequency_hz, 2.0*ones(size(baseResult.frequency_hz)), 'RelTol', 1.0e-8);
densityCase = baseCase;
densityCase.profiles.mass_density_axis_kg_m3 = 4.0 * baseCase.profiles.mass_density_axis_kg_m3;
densityResult = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.solve_benchmark(densityCase);
verifyEqual(testCase, densityResult.frequency_hz ./ baseResult.frequency_hz, 0.5*ones(size(baseResult.frequency_hz)), 'RelTol', 1.0e-8);
end

function testPythonReferenceEigenfrequencies(testCase)
referencePath = fullfile(testCase.TestData.repoRoot, 'data', 'reference', 'reduced_ae_benchmark', 'eigenvalues.csv');
reference = readtable(referencePath);
relative = abs(testCase.TestData.result.frequency_hz - reference.frequency_hz) ./ reference.frequency_hz;
verifyLessThan(testCase, max(relative), testCase.TestData.caseData.verification.python_matlab_eigenfrequency_relative_tolerance);
end

function testGridConvergence(testCase)
convergence = kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes.convergence_study(testCase.TestData.caseData);
errors = convergence.mode_1_relative_error_to_finest(1:end-1);
verifyGreaterThan(testCase, errors(1), errors(2));
verifyGreaterThan(testCase, errors(2), errors(3));
verifyLessThan(testCase, errors(3), 1.0e-4);
end
