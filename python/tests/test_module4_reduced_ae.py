from __future__ import annotations

import csv
import sys
import unittest
from pathlib import Path

import numpy as np

PYTHON_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PYTHON_ROOT.parent
SRC = PYTHON_ROOT / "src"
sys.path.insert(0, str(SRC))

from kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes import (  # noqa: E402
    assemble_operator,
    build_profiles,
    convergence_study,
    load_case,
    solve_benchmark,
)


class ReducedAEBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.case_path = PYTHON_ROOT / "cases" / "reduced_ae_benchmark" / "case.json"
        cls.case = load_case(cls.case_path)
        cls.result = solve_benchmark(cls.case)

    def test_case_files_are_identical_across_languages(self) -> None:
        matlab_case = REPOSITORY_ROOT / "matlab" / "cases" / "reduced_ae_benchmark" / "case.json"
        self.assertEqual(self.case_path.read_bytes(), matlab_case.read_bytes())

    def test_profiles_are_physical_and_crossing_is_resolved(self) -> None:
        p = self.result.profiles
        self.assertTrue(np.all(p.mass_density_kg_m3 > 0.0))
        self.assertTrue(np.all(p.alfven_speed_m_s > 0.0))
        self.assertGreater(p.crossing_s, 0.0)
        self.assertLess(p.crossing_s, 1.0)
        self.assertLess(p.gap_lower_rad_s, p.gap_upper_rad_s)
        self.assertTrue(np.all(p.local_lower_rad_s > 0.0))
        self.assertLess(p.gap_lower_rad_s / (2.0 * np.pi), self.result.frequency_hz[1])
        self.assertLess(self.result.frequency_hz[1], p.gap_upper_rad_s / (2.0 * np.pi))

    def test_operator_is_symmetric_and_positive(self) -> None:
        a = self.result.operator
        asymmetry = np.linalg.norm((a - a.T).toarray()) / np.linalg.norm(a.toarray())
        self.assertLess(asymmetry, self.case.verification.matrix_symmetry_tolerance)
        self.assertTrue(np.all(self.result.omega2_s2 > 0.0))

    def test_eigenvectors_are_normalized_and_residuals_are_small(self) -> None:
        h = self.result.profiles.h
        for index in range(self.result.eigenvectors.shape[1]):
            norm = h * np.dot(self.result.eigenvectors[:, index], self.result.eigenvectors[:, index])
            self.assertAlmostEqual(float(norm), 1.0, places=11)
        self.assertLess(float(np.max(self.result.residual_norms)), self.case.verification.eigen_residual_tolerance)

    def test_expected_alfven_scalings(self) -> None:
        doubled_b = solve_benchmark(
            self.case.with_updates(magnetic_field_t=2.0 * self.case.geometry.magnetic_field_t)
        )
        density_x4 = solve_benchmark(self.case.with_updates(density_scale=4.0))
        np.testing.assert_allclose(doubled_b.frequency_hz / self.result.frequency_hz, 2.0, rtol=2.0e-10, atol=0.0)
        np.testing.assert_allclose(density_x4.frequency_hz / self.result.frequency_hz, 0.5, rtol=2.0e-10, atol=0.0)

    def test_decoupled_limit_closes_avoided_crossing(self) -> None:
        decoupled = self.case.with_updates(coupling_fraction=0.0)
        profiles = build_profiles(decoupled)
        np.testing.assert_allclose(
            profiles.local_lower_rad_s,
            np.minimum(profiles.omega_m_rad_s, profiles.omega_mp1_rad_s),
            rtol=0.0,
            atol=1.0e-6,
        )
        np.testing.assert_allclose(
            profiles.local_upper_rad_s,
            np.maximum(profiles.omega_m_rad_s, profiles.omega_mp1_rad_s),
            rtol=0.0,
            atol=1.0e-6,
        )
        operator = assemble_operator(decoupled, profiles)
        n = profiles.s.size
        self.assertEqual(operator[:n, n:].nnz, 0)
        self.assertEqual(operator[n:, :n].nnz, 0)

    def test_grid_convergence_improves(self) -> None:
        rows = convergence_study(self.case)
        errors = [row["mode_1_relative_error_to_finest"] for row in rows[:-1]]
        self.assertGreater(errors[0], errors[1])
        self.assertGreater(errors[1], errors[2])
        self.assertLess(errors[2], 1.0e-4)

    def test_reference_regression(self) -> None:
        path = REPOSITORY_ROOT / "data" / "reference" / "reduced_ae_benchmark" / "eigenvalues.csv"
        with path.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        reference = np.array([float(row["frequency_hz"]) for row in rows])
        np.testing.assert_allclose(
            self.result.frequency_hz,
            reference,
            rtol=self.case.verification.regression_eigenfrequency_relative_tolerance,
            atol=0.0,
        )

    def test_language_neutral_output_contract_is_complete(self) -> None:
        output = REPOSITORY_ROOT / "data" / "reference" / "reduced_ae_benchmark"
        required = {
            "profiles_and_continuum.csv",
            "eigenvalues.csv",
            "eigenmodes.csv",
            "convergence.csv",
            "metadata.json",
            "continuum.png",
            "continuum.pdf",
            "representative_eigenmode.png",
            "representative_eigenmode.pdf",
            "convergence.png",
            "convergence.pdf",
        }
        self.assertTrue(required.issubset({path.name for path in output.iterdir()}))


if __name__ == "__main__":
    unittest.main()
