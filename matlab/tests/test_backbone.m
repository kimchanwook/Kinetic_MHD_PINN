function tests = test_backbone
%TEST_BACKBONE Contract tests for the MATLAB project scaffold.
tests = functiontests(localfunctions);
end

function setupOnce(testCase)
testsDir = fileparts(mfilename('fullpath'));
matlabRoot = fileparts(testsDir);
sourceDir = fullfile(matlabRoot, 'src');
addpath(sourceDir);
testCase.TestData.sourceDir = sourceDir;
end

function teardownOnce(testCase)
rmpath(testCase.TestData.sourceDir);
end

function testRegistryIsValid(testCase)
kinetic_mhd_pinn.common.validate_registry();
specs = kinetic_mhd_pinn.common.registry();
verifyEqual(testCase, numel(specs), 11);
end

function testNominalOrderIsNumbered(testCase)
actual = kinetic_mhd_pinn.common.nominal_startup_order();
expected = arrayfun(@(i) sprintf('module_%d', i), 1:11, ...
    'UniformOutput', false);
verifyEqual(testCase, actual, expected);
end

function testSharedStateContract(testCase)
state = kinetic_mhd_pinn.common.CoupledState();
module = kinetic_mhd_pinn.common.ScaffoldModule( ...
    'module_test', {}, 'test_product');
module.run(state);
verifyTrue(testCase, state.fields.test_product);
verifyEqual(testCase, state.history{end}.module, 'module_test');
end

function testMissingProductFailsLoudly(testCase)
state = kinetic_mhd_pinn.common.CoupledState();
module = kinetic_mhd_pinn.common.ScaffoldModule( ...
    'module_test', {'missing'}, 'unused');
verifyError(testCase, @() module.run(state), ...
    'kinetic_mhd_pinn:MissingProducts');
end

function testAllModuleScaffoldsAreAddressable(testCase)
specs = kinetic_mhd_pinn.common.registry();
for i = 1:numel(specs)
    factory = str2func(sprintf('kinetic_mhd_pinn.%s.solver', specs(i).package));
    module = factory();
    verifyEqual(testCase, module.moduleId, specs(i).id);
end
end
