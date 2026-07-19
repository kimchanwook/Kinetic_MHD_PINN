from __future__ import annotations

from dataclasses import dataclass

from .state import CoupledState


@dataclass
class ScaffoldModule:
    """Nonphysical placeholder used to test project wiring only."""

    module_id: str
    required_products: tuple[str, ...] = ()
    produced_marker: str | None = None

    def run(self, state: CoupledState) -> CoupledState:
        state.require(*self.required_products)
        marker = self.produced_marker or f"{self.module_id}_scaffold_complete"
        state.publish(self.module_id, **{marker: True})
        return state
