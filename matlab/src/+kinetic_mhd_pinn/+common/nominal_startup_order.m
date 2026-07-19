function order = nominal_startup_order()
%NOMINAL_STARTUP_ORDER Return deterministic startup and smoke-test order.
%
% The eventual coupled time integrator may iterate feedback groups in a
% different order; this function does not prescribe the physical coupling
% sequence.

specs = kinetic_mhd_pinn.common.registry();
[~, indices] = sort([specs.number]);
order = {specs(indices).id};
end
