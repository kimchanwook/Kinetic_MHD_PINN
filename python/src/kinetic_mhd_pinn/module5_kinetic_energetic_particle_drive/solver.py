from __future__ import annotations

from dataclasses import dataclass

from kinetic_mhd_pinn.common.scaffold import ScaffoldModule
from kinetic_mhd_pinn.common.state import CoupledState


@dataclass
class KineticEnergeticParticleDriveModule(ScaffoldModule):
    """Architecture placeholder for Module 5: Kinetic Energetic-Particle Drive and Damping.

    This class validates wiring only and performs no physical calculation.
    """

    module_id: str = "module_5"
    required_products: tuple[str, ...] = ()
    produced_marker: str | None = "module_5_contract_ready"

    def run(self, state: CoupledState) -> CoupledState:
        return super().run(state)
