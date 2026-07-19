classdef CoupledState < handle
    %COUPLEDSTATE Shared cross-module state container.
    %
    % Physics modules exchange named, unit-documented products through this
    % object. The baseline intentionally uses generic structures; concrete
    % typed arrays should be introduced only when the first numerical module
    % is selected.

    properties
        fields = struct()
        metadata = struct()
        history = {}
    end

    methods
        function obj = CoupledState(metadata)
            if nargin >= 1
                if ~isstruct(metadata)
                    error('kinetic_mhd_pinn:InvalidMetadata', ...
                        'metadata must be a structure.');
                end
                obj.metadata = metadata;
            end
        end

        function require(obj, varargin)
            names = varargin;
            if numel(names) == 1 && iscell(names{1})
                names = names{1};
            end
            missing = {};
            for i = 1:numel(names)
                name = char(names{i});
                if ~isfield(obj.fields, name)
                    missing{end + 1} = name; %#ok<AGROW>
                end
            end
            if ~isempty(missing)
                error('kinetic_mhd_pinn:MissingProducts', ...
                    'Missing required state products: %s', strjoin(missing, ', '));
            end
        end

        function publish(obj, moduleId, varargin)
            if mod(numel(varargin), 2) ~= 0
                error('kinetic_mhd_pinn:InvalidPublishArguments', ...
                    'Products must be supplied as name-value pairs.');
            end

            productNames = cell(1, numel(varargin) / 2);
            for i = 1:2:numel(varargin)
                name = char(varargin{i});
                if ~isvarname(name)
                    error('kinetic_mhd_pinn:InvalidProductName', ...
                        'Invalid MATLAB product name: %s', name);
                end
                obj.fields.(name) = varargin{i + 1};
                productNames{(i + 1) / 2} = name;
            end

            record = struct('module', char(moduleId), ...
                'products', {productNames});
            obj.history{end + 1} = record;
        end
    end
end
