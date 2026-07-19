from __future__ import annotations

from dataclasses import dataclass

from kinetic_mhd_pinn.common.scaffold import ScaffoldModule
from kinetic_mhd_pinn.common.state import CoupledState


@dataclass
class AeInducedFastIonTransportModule(ScaffoldModule):
    """Architecture placeholder for Module 6: Alfvén-Eigenmode-Induced Fast-Ion Transport.

    This class validates wiring only and performs no physical calculation.
    """

    module_id: str = "module_6"
    required_products: tuple[str, ...] = ()
    produced_marker: str | None = "module_6_contract_ready"

    def run(self, state: CoupledState) -> CoupledState:
        return super().run(state)
