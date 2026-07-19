classdef ScaffoldModule
    %SCAFFOLDMODULE Nonphysical placeholder used to test project wiring only.

    properties
        moduleId = ''
        requiredProducts = {}
        producedMarker = ''
    end

    methods
        function obj = ScaffoldModule(moduleId, requiredProducts, producedMarker)
            if nargin >= 1
                obj.moduleId = char(moduleId);
            end
            if nargin >= 2
                obj.requiredProducts = requiredProducts;
            end
            if nargin >= 3
                obj.producedMarker = char(producedMarker);
            end
        end

        function state = run(obj, state)
            if ~isa(state, 'kinetic_mhd_pinn.common.CoupledState')
                error('kinetic_mhd_pinn:InvalidState', ...
                    'state must be a kinetic_mhd_pinn.common.CoupledState object.');
            end
            state.require(obj.requiredProducts);
            marker = obj.producedMarker;
            if isempty(marker)
                marker = [obj.moduleId '_scaffold_complete'];
            end
            state.publish(obj.moduleId, marker, true);
        end
    end
end
