from __future__ import annotations

from dataclasses import dataclass

from kinetic_mhd_pinn.common.scaffold import ScaffoldModule
from kinetic_mhd_pinn.common.state import CoupledState


@dataclass
class StellaratorEquilibriumGeometryModule(ScaffoldModule):
    """Architecture placeholder for Module 1: Stellarator Equilibrium and Magnetic Geometry.

    This class validates wiring only and performs no physical calculation.
    """

    module_id: str = "module_1"
    required_products: tuple[str, ...] = ()
    produced_marker: str | None = "module_1_contract_ready"

    def run(self, state: CoupledState) -> CoupledState:
        return super().run(state)
