from __future__ import annotations

from dataclasses import dataclass, replace
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy import sparse

MU0 = 4.0e-7 * np.pi


@dataclass(frozen=True)
class GeometryConfig:
    major_radius_m: float
    minor_radius_m: float
    magnetic_field_t: float


@dataclass(frozen=True)
class ProfileConfig:
    mass_density_axis_kg_m3: float
    mass_density_edge_fraction: float
    mass_density_exponent: float
    iota_axis: float
    iota_edge: float
    iota_exponent: float


@dataclass(frozen=True)
class ModeConfig:
    toroidal_number: int
    poloidal_harmonics: tuple[int, int]
    coupling_fraction: float
    coupling_width: float
    radial_stiffness_fraction: float


@dataclass(frozen=True)
class NumericsConfig:
    radial_points: int
    number_of_eigenpairs: int
    convergence_grids: tuple[int, ...]


@dataclass(frozen=True)
class VerificationConfig:
    python_matlab_eigenfrequency_relative_tolerance: float
    regression_eigenfrequency_relative_tolerance: float
    matrix_symmetry_tolerance: float
    eigen_residual_tolerance: float


@dataclass(frozen=True)
class BenchmarkCase:
    case_name: str
    geometry: GeometryConfig
    profiles: ProfileConfig
    mode: ModeConfig
    numerics: NumericsConfig
    verification: VerificationConfig
    model: dict[str, Any]

    def with_updates(
        self,
        *,
        magnetic_field_t: float | None = None,
        density_scale: float = 1.0,
        radial_points: int | None = None,
        coupling_fraction: float | None = None,
    ) -> "BenchmarkCase":
        geometry = self.geometry
        if magnetic_field_t is not None:
            geometry = replace(geometry, magnetic_field_t=float(magnetic_field_t))
        profiles = replace(
            self.profiles,
            mass_density_axis_kg_m3=self.profiles.mass_density_axis_kg_m3 * float(density_scale),
        )
        numerics = self.numerics
        if radial_points is not None:
            numerics = replace(numerics, radial_points=int(radial_points))
        mode = self.mode
        if coupling_fraction is not None:
            mode = replace(mode, coupling_fraction=float(coupling_fraction))
        return replace(self, geometry=geometry, profiles=profiles, numerics=numerics, mode=mode)


@dataclass(frozen=True)
class RadialProfiles:
    s: np.ndarray
    h: float
    mass_density_kg_m3: np.ndarray
    iota: np.ndarray
    alfven_speed_m_s: np.ndarray
    omega_m_rad_s: np.ndarray
    omega_mp1_rad_s: np.ndarray
    coupling_omega2_s2: np.ndarray
    local_lower_rad_s: np.ndarray
    local_upper_rad_s: np.ndarray
    crossing_iota: float
    crossing_s: float
    crossing_index: int
    gap_lower_rad_s: float
    gap_upper_rad_s: float


@dataclass(frozen=True)
class BenchmarkResult:
    case: BenchmarkCase
    profiles: RadialProfiles
    operator: sparse.csr_matrix
    omega2_s2: np.ndarray
    eigenvectors: np.ndarray
    residual_norms: np.ndarray

    @property
    def omega_rad_s(self) -> np.ndarray:
        return np.sqrt(self.omega2_s2)

    @property
    def frequency_hz(self) -> np.ndarray:
        return self.omega_rad_s / (2.0 * np.pi)

    @property
    def frequency_khz(self) -> np.ndarray:
        return self.frequency_hz / 1.0e3

    @property
    def harmonic_components(self) -> tuple[np.ndarray, np.ndarray]:
        n = self.profiles.s.size
        return self.eigenvectors[:n, :], self.eigenvectors[n:, :]


def load_case(path: str | Path) -> BenchmarkCase:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return BenchmarkCase(
        case_name=payload["case_name"],
        geometry=GeometryConfig(**payload["geometry"]),
        profiles=ProfileConfig(**payload["profiles"]),
        mode=ModeConfig(
            toroidal_number=int(payload["mode"]["toroidal_number"]),
            poloidal_harmonics=tuple(int(v) for v in payload["mode"]["poloidal_harmonics"]),
            coupling_fraction=float(payload["mode"]["coupling_fraction"]),
            coupling_width=float(payload["mode"]["coupling_width"]),
            radial_stiffness_fraction=float(payload["mode"]["radial_stiffness_fraction"]),
        ),
        numerics=NumericsConfig(
            radial_points=int(payload["numerics"]["radial_points"]),
            number_of_eigenpairs=int(payload["numerics"]["number_of_eigenpairs"]),
            convergence_grids=tuple(int(v) for v in payload["numerics"]["convergence_grids"]),
        ),
        verification=VerificationConfig(**payload["verification"]),
        model=dict(payload["model"]),
    )
