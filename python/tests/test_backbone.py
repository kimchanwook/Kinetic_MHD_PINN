from __future__ import annotations

import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from kinetic_mhd_pinn import CoupledState, MODULE_SPECS, nominal_startup_order
from kinetic_mhd_pinn.common.registry import validate_registry
from kinetic_mhd_pinn.common.scaffold import ScaffoldModule


class BackboneTests(unittest.TestCase):
    def test_registry_is_valid(self) -> None:
        validate_registry()
        self.assertEqual(len(MODULE_SPECS), 11)

    def test_nominal_order_is_numbered(self) -> None:
        self.assertEqual(nominal_startup_order(), tuple(f"module_{i}" for i in range(1, 12)))

    def test_shared_state_contract(self) -> None:
        state = CoupledState()
        module = ScaffoldModule(module_id="module_test", produced_marker="test_product")
        module.run(state)
        self.assertTrue(state.fields["test_product"])
        self.assertEqual(state.history[-1]["module"], "module_test")

    def test_missing_product_fails_loudly(self) -> None:
        state = CoupledState()
        module = ScaffoldModule(module_id="module_test", required_products=("missing",))
        with self.assertRaises(KeyError):
            module.run(state)


if __name__ == "__main__":
    unittest.main()
