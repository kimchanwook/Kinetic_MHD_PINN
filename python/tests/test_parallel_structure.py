from __future__ import annotations

import sys
import unittest
from pathlib import Path

PYTHON_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PYTHON_ROOT.parent
SRC = PYTHON_ROOT / "src"
sys.path.insert(0, str(SRC))

from kinetic_mhd_pinn import MODULE_SPECS


class ParallelStructureTests(unittest.TestCase):
    def test_top_level_language_trees_match(self) -> None:
        for language in ("python", "matlab"):
            root = REPOSITORY_ROOT / language
            self.assertTrue(root.is_dir(), language)
            for directory in ("cases", "outputs", "src", "tests"):
                self.assertTrue((root / directory).is_dir(), f"{language}/{directory}")

    def test_every_python_module_has_matlab_mirror(self) -> None:
        matlab_package = REPOSITORY_ROOT / "matlab" / "src" / "+kinetic_mhd_pinn"
        for spec in MODULE_SPECS:
            python_module = SRC / "kinetic_mhd_pinn" / spec.package
            matlab_module = matlab_package / f"+{spec.package}"
            self.assertTrue((python_module / "solver.py").is_file(), spec.package)
            self.assertTrue((python_module / "README.md").is_file(), spec.package)
            self.assertTrue((matlab_module / "solver.m").is_file(), spec.package)
            self.assertTrue((matlab_module / "README.md").is_file(), spec.package)
            solver_text = (matlab_module / "solver.m").read_text(encoding="utf-8")
            self.assertIn(spec.id, solver_text)


if __name__ == "__main__":
    unittest.main()
