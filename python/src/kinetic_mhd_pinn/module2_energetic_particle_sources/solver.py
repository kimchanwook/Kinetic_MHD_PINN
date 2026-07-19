from __future__ import annotations

from dataclasses import dataclass

from kinetic_mhd_pinn.common.scaffold import ScaffoldModule
from kinetic_mhd_pinn.common.state import CoupledState


@dataclass
class EnergeticParticleSourcesModule(ScaffoldModule):
    """Architecture placeholder for Module 2: Energetic-Particle Sources and Distribution Functions.

    This class validates wiring only and performs no physical calculation.
    """

    module_id: str = "module_2"
    required_products: tuple[str, ...] = ()
    produced_marker: str | None = "module_2_contract_ready"

    def run(self, state: CoupledState) -> CoupledState:
        return super().run(state)
