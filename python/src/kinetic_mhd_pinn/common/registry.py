from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModuleSpec:
    id: str
    number: int
    name: str
    package: str
    dependencies: tuple[str, ...]
    status: str


MODULE_SPECS: tuple[ModuleSpec, ...] = (
    ModuleSpec(id='module_1', number=1, name='Stellarator Equilibrium and Magnetic Geometry', package='module1_stellarator_equilibrium_geometry', dependencies=(), status='scaffold'),
    ModuleSpec(id='module_2', number=2, name='Energetic-Particle Sources and Distribution Functions', package='module2_energetic_particle_sources', dependencies=('module_1',), status='scaffold'),
    ModuleSpec(id='module_3', number=3, name='Guiding-Center Orbits, Confinement, and Wall Losses', package='module3_guiding_center_orbits_wall_losses', dependencies=('module_1', 'module_2'), status='scaffold'),
    ModuleSpec(id='module_4', number=4, name='Alfvén Continuum and Fluid-MHD Eigenmodes', package='module4_alfven_continuum_eigenmodes', dependencies=('module_1', 'module_7'), status='reduced-benchmark'),
    ModuleSpec(id='module_5', number=5, name='Kinetic Energetic-Particle Drive and Damping', package='module5_kinetic_energetic_particle_drive', dependencies=('module_2', 'module_3', 'module_4'), status='scaffold'),
    ModuleSpec(id='module_6', number=6, name='Alfvén-Eigenmode-Induced Fast-Ion Transport', package='module6_ae_induced_fast_ion_transport', dependencies=('module_2', 'module_4', 'module_5'), status='scaffold'),
    ModuleSpec(id='module_7', number=7, name='Alpha Heating and Thermal-Profile Evolution', package='module7_alpha_heating_profile_evolution', dependencies=('module_2', 'module_3', 'module_6'), status='scaffold'),
    ModuleSpec(id='module_8', number=8, name='Coupled Kinetic-MHD Multiphysics Integration', package='module8_coupled_multiphysics_integration', dependencies=('module_1', 'module_2', 'module_3', 'module_4', 'module_5', 'module_6', 'module_7'), status='scaffold'),
    ModuleSpec(id='module_9', number=9, name='PINN and Neural-Operator Surrogates', package='module9_pinn_neural_operator_surrogates', dependencies=('module_8',), status='scaffold'),
    ModuleSpec(id='module_10', number=10, name='Synthetic Diagnostics and Physics-Informed Inverse Modeling', package='module10_synthetic_diagnostics_inverse_modeling', dependencies=('module_3', 'module_4', 'module_5', 'module_6', 'module_7', 'module_8'), status='scaffold'),
    ModuleSpec(id='module_11', number=11, name='GNN Physical Dependency Discovery and Coupling Optimization', package='module11_gnn_dependency_coupling_optimization', dependencies=('module_8',), status='scaffold'),
)


def nominal_startup_order() -> tuple[str, ...]:
    """Return the architecture's nominal initialization order.

    The eventual coupled time integrator may iterate feedback groups in a different
    order; this function only defines deterministic startup and smoke-test order.
    """
    return tuple(spec.id for spec in sorted(MODULE_SPECS, key=lambda item: item.number))


def validate_registry() -> None:
    ids = [spec.id for spec in MODULE_SPECS]
    if len(ids) != len(set(ids)):
        raise ValueError("Module IDs must be unique")
    known = set(ids)
    for spec in MODULE_SPECS:
        unknown = set(spec.dependencies) - known
        if unknown:
            raise ValueError(f"{spec.id} has unknown dependencies: {sorted(unknown)}")
