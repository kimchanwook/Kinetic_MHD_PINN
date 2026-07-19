from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from kinetic_mhd_pinn.common.scaffold import ScaffoldModule
from kinetic_mhd_pinn.common.state import CoupledState

from .benchmark import solve_benchmark
from .model import BenchmarkCase, BenchmarkResult, load_case


@dataclass
class AlfvenContinuumEigenmodesModule(ScaffoldModule):
    """Module 4 interface plus the first validated reduced benchmark.

    The shared-state ``run`` method preserves the architecture smoke test. The
    actual physics milestone is exposed through ``solve_case`` and implements a
    self-adjoint two-harmonic reduced shear-Alfven eigenvalue model.
    """

    module_id: str = "module_4"
    required_products: tuple[str, ...] = ()
    produced_marker: str | None = "module_4_contract_ready"

    def run(self, state: CoupledState) -> CoupledState:
        return super().run(state)

    @staticmethod
    def solve_case(case: BenchmarkCase | str | Path) -> BenchmarkResult:
        resolved = load_case(case) if isinstance(case, (str, Path)) else case
        return solve_benchmark(resolved)
