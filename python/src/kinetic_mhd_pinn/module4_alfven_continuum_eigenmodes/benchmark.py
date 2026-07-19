from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

from .model import BenchmarkCase, BenchmarkResult, MU0, RadialProfiles


def _iota_to_s(case: BenchmarkCase, iota_value: float) -> float:
    p = case.profiles
    fraction = (iota_value - p.iota_axis) / (p.iota_edge - p.iota_axis)
    fraction = float(np.clip(fraction, 0.0, 1.0))
    return fraction ** (1.0 / p.iota_exponent)


def build_profiles(case: BenchmarkCase) -> RadialProfiles:
    n_points = case.numerics.radial_points
    if n_points < 8:
        raise ValueError("radial_points must be at least 8")
    if case.geometry.major_radius_m <= 0.0 or case.geometry.magnetic_field_t <= 0.0:
        raise ValueError("major radius and magnetic field must be positive")
    if case.profiles.mass_density_axis_kg_m3 <= 0.0:
        raise ValueError("mass density must be positive")
    if not 0.0 < case.profiles.mass_density_edge_fraction <= 1.0:
        raise ValueError("mass_density_edge_fraction must be in (0, 1]")
    if case.mode.poloidal_harmonics[1] != case.mode.poloidal_harmonics[0] + 1:
        raise ValueError("the baseline benchmark requires adjacent harmonics m and m+1")
    if not 0.0 <= case.mode.coupling_fraction < 1.0:
        raise ValueError("coupling_fraction must be in [0, 1) to preserve local positive definiteness")

    h = 1.0 / n_points
    s = (np.arange(n_points, dtype=float) + 0.5) * h
    p = case.profiles
    rho = p.mass_density_axis_kg_m3 * (
        1.0 - (1.0 - p.mass_density_edge_fraction) * s**p.mass_density_exponent
    )
    iota = p.iota_axis + (p.iota_edge - p.iota_axis) * s**p.iota_exponent
    v_a = case.geometry.magnetic_field_t / np.sqrt(MU0 * rho)

    mode = case.mode
    n_tor = mode.toroidal_number
    m, mp1 = mode.poloidal_harmonics
    omega_scale = v_a / case.geometry.major_radius_m
    omega_m = np.abs(n_tor - m * iota) * omega_scale
    omega_mp1 = np.abs(n_tor - mp1 * iota) * omega_scale

    crossing_iota = 2.0 * n_tor / (2.0 * m + 1.0)
    crossing_s = _iota_to_s(case, crossing_iota)
    crossing_index = int(np.argmin(np.abs(s - crossing_s)))
    coupling = (
        mode.coupling_fraction
        * omega_m
        * omega_mp1
        * np.exp(-((s - crossing_s) / mode.coupling_width) ** 2)
    )

    average = 0.5 * (omega_m**2 + omega_mp1**2)
    split = np.sqrt((0.5 * (omega_m**2 - omega_mp1**2)) ** 2 + coupling**2)
    local_lower = np.sqrt(np.maximum(average - split, 0.0))
    local_upper = np.sqrt(np.maximum(average + split, 0.0))

    idx = crossing_index
    return RadialProfiles(
        s=s,
        h=h,
        mass_density_kg_m3=rho,
        iota=iota,
        alfven_speed_m_s=v_a,
        omega_m_rad_s=omega_m,
        omega_mp1_rad_s=omega_mp1,
        coupling_omega2_s2=coupling,
        local_lower_rad_s=local_lower,
        local_upper_rad_s=local_upper,
        crossing_iota=crossing_iota,
        crossing_s=crossing_s,
        crossing_index=crossing_index,
        gap_lower_rad_s=float(local_lower[idx]),
        gap_upper_rad_s=float(local_upper[idx]),
    )


def radial_stiffness_matrix(case: BenchmarkCase, profiles: RadialProfiles) -> sparse.csr_matrix:
    """Finite-volume matrix for -d/ds[D(s) du/ds].

    Cell centers are used. The left boundary has zero flux (Neumann), and the
    right boundary has a zero face value (Dirichlet). This construction is
    symmetric under the ordinary Euclidean inner product.
    """

    n = profiles.s.size
    h2 = profiles.h**2
    omega_scale2 = (profiles.alfven_speed_m_s / case.geometry.major_radius_m) ** 2
    d_center = case.mode.radial_stiffness_fraction * omega_scale2
    d_face = 0.5 * (d_center[:-1] + d_center[1:])
    d_edge = case.mode.radial_stiffness_fraction * (
        case.geometry.magnetic_field_t
        / np.sqrt(
            MU0
            * case.profiles.mass_density_axis_kg_m3
            * case.profiles.mass_density_edge_fraction
        )
        / case.geometry.major_radius_m
    ) ** 2

    diagonal = np.zeros(n)
    lower = np.zeros(n - 1)
    upper = np.zeros(n - 1)

    diagonal[0] += d_face[0] / h2
    upper[0] = -d_face[0] / h2
    for i in range(1, n - 1):
        diagonal[i] += (d_face[i - 1] + d_face[i]) / h2
        lower[i - 1] = -d_face[i - 1] / h2
        upper[i] = -d_face[i] / h2
    diagonal[-1] += (d_face[-1] + 2.0 * d_edge) / h2
    lower[-1] = -d_face[-1] / h2

    return sparse.diags((lower, diagonal, upper), offsets=(-1, 0, 1), format="csr")


def assemble_operator(case: BenchmarkCase, profiles: RadialProfiles) -> sparse.csr_matrix:
    radial = radial_stiffness_matrix(case, profiles)
    a_m = radial + sparse.diags(profiles.omega_m_rad_s**2, format="csr")
    a_mp1 = radial + sparse.diags(profiles.omega_mp1_rad_s**2, format="csr")
    coupling = sparse.diags(profiles.coupling_omega2_s2, format="csr")
    return sparse.bmat([[a_m, coupling], [coupling, a_mp1]], format="csr")


def _canonicalize_eigenvectors(vectors: np.ndarray, h: float) -> np.ndarray:
    output = vectors.copy()
    for j in range(output.shape[1]):
        norm = np.sqrt(h * np.dot(output[:, j], output[:, j]))
        if norm == 0.0:
            raise RuntimeError("zero eigenvector returned by eigensolver")
        output[:, j] /= norm
        dominant = int(np.argmax(np.abs(output[:, j])))
        if output[dominant, j] < 0.0:
            output[:, j] *= -1.0
    return output


def solve_benchmark(case: BenchmarkCase) -> BenchmarkResult:
    profiles = build_profiles(case)
    operator = assemble_operator(case, profiles)
    k = case.numerics.number_of_eigenpairs
    if not 1 <= k < operator.shape[0] - 1:
        raise ValueError("number_of_eigenpairs is inconsistent with matrix size")
    values, vectors = eigsh(operator, k=k, which="SM", tol=1.0e-12, maxiter=200000)
    order = np.argsort(values)
    values = np.asarray(values[order], dtype=float)
    vectors = _canonicalize_eigenvectors(np.asarray(vectors[:, order], dtype=float), profiles.h)
    if np.any(values <= 0.0):
        raise RuntimeError("non-positive omega^2 encountered")
    residuals = np.empty(k)
    for j in range(k):
        residual = operator @ vectors[:, j] - values[j] * vectors[:, j]
        denominator = max(np.linalg.norm(operator @ vectors[:, j]), np.finfo(float).tiny)
        residuals[j] = np.linalg.norm(residual) / denominator
    return BenchmarkResult(
        case=case,
        profiles=profiles,
        operator=operator,
        omega2_s2=values,
        eigenvectors=vectors,
        residual_norms=residuals,
    )


def convergence_study(case: BenchmarkCase, grids: Iterable[int] | None = None) -> list[dict[str, float]]:
    grid_list = tuple(grids if grids is not None else case.numerics.convergence_grids)
    results: list[BenchmarkResult] = [solve_benchmark(case.with_updates(radial_points=n)) for n in grid_list]
    reference = results[-1].frequency_hz
    rows: list[dict[str, float]] = []
    for n, result in zip(grid_list, results, strict=True):
        row: dict[str, float] = {"radial_points": float(n)}
        for j, frequency in enumerate(result.frequency_hz, start=1):
            row[f"mode_{j}_frequency_hz"] = float(frequency)
            row[f"mode_{j}_relative_error_to_finest"] = float(
                abs(frequency - reference[j - 1]) / reference[j - 1]
            )
        rows.append(row)
    return rows


def write_outputs(result: BenchmarkResult, output_dir: str | Path, convergence: list[dict[str, float]]) -> None:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    p = result.profiles
    m, mp1 = result.case.mode.poloidal_harmonics

    profiles_header = [
        "s",
        "mass_density_kg_m3",
        "iota",
        "alfven_speed_m_s",
        f"omega_m{m}_rad_s",
        f"omega_m{mp1}_rad_s",
        "coupling_omega2_s2",
        "local_lower_rad_s",
        "local_upper_rad_s",
    ]
    profiles_data = np.column_stack(
        [
            p.s,
            p.mass_density_kg_m3,
            p.iota,
            p.alfven_speed_m_s,
            p.omega_m_rad_s,
            p.omega_mp1_rad_s,
            p.coupling_omega2_s2,
            p.local_lower_rad_s,
            p.local_upper_rad_s,
        ]
    )
    np.savetxt(output / "profiles_and_continuum.csv", profiles_data, delimiter=",", header=",".join(profiles_header), comments="")

    with (output / "eigenvalues.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["mode_index", "omega2_s2", "omega_rad_s", "frequency_hz", "frequency_khz", "relative_residual"])
        for j in range(result.omega2_s2.size):
            writer.writerow(
                [
                    j + 1,
                    f"{result.omega2_s2[j]:.16e}",
                    f"{result.omega_rad_s[j]:.16e}",
                    f"{result.frequency_hz[j]:.16e}",
                    f"{result.frequency_khz[j]:.16e}",
                    f"{result.residual_norms[j]:.16e}",
                ]
            )

    component_m, component_mp1 = result.harmonic_components
    columns = [p.s]
    header = ["s"]
    for j in range(result.omega2_s2.size):
        columns.extend([component_m[:, j], component_mp1[:, j]])
        header.extend([f"mode_{j+1}_m{m}", f"mode_{j+1}_m{mp1}"])
    np.savetxt(output / "eigenmodes.csv", np.column_stack(columns), delimiter=",", header=",".join(header), comments="")

    if convergence:
        fieldnames = list(convergence[0].keys())
        with (output / "convergence.csv").open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(convergence)

    metadata = {
        "case_name": result.case.case_name,
        "model_status": result.case.model["fidelity"],
        "crossing_iota": p.crossing_iota,
        "crossing_s": p.crossing_s,
        "crossing_cell_s": float(p.s[p.crossing_index]),
        "gap_lower_frequency_khz": p.gap_lower_rad_s / (2.0 * np.pi * 1.0e3),
        "gap_upper_frequency_khz": p.gap_upper_rad_s / (2.0 * np.pi * 1.0e3),
        "axis_boundary_condition": "zero radial flux (homogeneous Neumann)",
        "edge_boundary_condition": "zero face value (homogeneous Dirichlet)",
        "normalization": "integral_0^1 (xi_m^2 + xi_mplus1^2) ds = 1",
        "python_solver": "scipy.sparse.linalg.eigsh, smallest algebraic eigenpairs",
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
