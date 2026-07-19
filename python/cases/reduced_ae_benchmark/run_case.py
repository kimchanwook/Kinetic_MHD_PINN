from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

CASE_DIR = Path(__file__).resolve().parent
PYTHON_ROOT = CASE_DIR.parents[1]
REPOSITORY_ROOT = PYTHON_ROOT.parent
SRC = PYTHON_ROOT / "src"
sys.path.insert(0, str(SRC))

from kinetic_mhd_pinn.module4_alfven_continuum_eigenmodes import (  # noqa: E402
    convergence_study,
    load_case,
    solve_benchmark,
    write_outputs,
)


def make_plots(result, output_dir: Path, figure_dir: Path | None = None) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    if figure_dir is not None:
        figure_dir.mkdir(parents=True, exist_ok=True)
    p = result.profiles
    m, mp1 = result.case.mode.poloidal_harmonics

    fig = plt.figure(figsize=(8.0, 5.2))
    plt.plot(p.s, p.omega_m_rad_s / (2.0 * np.pi * 1.0e3), label=fr"uncoupled $m={m}$")
    plt.plot(p.s, p.omega_mp1_rad_s / (2.0 * np.pi * 1.0e3), label=fr"uncoupled $m={mp1}$")
    plt.plot(p.s, p.local_lower_rad_s / (2.0 * np.pi * 1.0e3), linestyle="--", label="coupled local lower")
    plt.plot(p.s, p.local_upper_rad_s / (2.0 * np.pi * 1.0e3), linestyle="--", label="coupled local upper")
    plt.axvline(p.crossing_s, linewidth=1.0, linestyle=":", label="predicted crossing")
    plt.xlabel("Normalized radial coordinate, s")
    plt.ylabel("Frequency (kHz)")
    plt.title("Reduced two-harmonic shear-Alfven continuum")
    plt.grid(True, alpha=0.3)
    plt.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "continuum.png", dpi=180)
    fig.savefig(output_dir / "continuum.pdf")
    if figure_dir is not None:
        fig.savefig(figure_dir / "module4_reduced_ae_continuum.pdf")
    plt.close(fig)

    component_m, component_mp1 = result.harmonic_components
    selected = int(np.argmin(np.abs(result.frequency_hz - 0.5 * (p.gap_lower_rad_s + p.gap_upper_rad_s) / (2.0 * np.pi))))
    fig = plt.figure(figsize=(8.0, 5.2))
    plt.plot(p.s, component_m[:, selected], label=fr"$\xi_{{m={m}}}$")
    plt.plot(p.s, component_mp1[:, selected], label=fr"$\xi_{{m={mp1}}}$")
    plt.xlabel("Normalized radial coordinate, s")
    plt.ylabel("Normalized eigenfunction component")
    plt.title(f"Representative coupled eigenmode {selected + 1}: {result.frequency_khz[selected]:.2f} kHz")
    plt.grid(True, alpha=0.3)
    plt.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "representative_eigenmode.png", dpi=180)
    fig.savefig(output_dir / "representative_eigenmode.pdf")
    if figure_dir is not None:
        fig.savefig(figure_dir / "module4_reduced_ae_eigenmode.pdf")
    plt.close(fig)

    grids = np.array([64, 128, 256, 512])
    convergence = convergence_study(result.case, grids)
    errors = np.array([row["mode_1_relative_error_to_finest"] for row in convergence])
    fig = plt.figure(figsize=(8.0, 5.2))
    plt.loglog(grids[:-1], errors[:-1], marker="o")
    plt.xlabel("Radial cells")
    plt.ylabel("Mode 1 relative error to 512-cell result")
    plt.title("Grid-convergence diagnostic")
    plt.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_dir / "convergence.png", dpi=180)
    fig.savefig(output_dir / "convergence.pdf")
    if figure_dir is not None:
        fig.savefig(figure_dir / "module4_reduced_ae_convergence.pdf")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the reduced two-harmonic Alfven-eigenmode benchmark.")
    parser.add_argument("--case", type=Path, default=CASE_DIR / "case.json")
    parser.add_argument("--output", type=Path, default=REPOSITORY_ROOT / "data" / "reference" / "reduced_ae_benchmark")
    parser.add_argument("--doc-figures", action="store_true", help="also refresh Module 4 documentation figures")
    args = parser.parse_args()

    case = load_case(args.case)
    result = solve_benchmark(case)
    convergence = convergence_study(case)
    write_outputs(result, args.output, convergence)
    figure_dir = REPOSITORY_ROOT / "docs" / "physics_notes" / "figures" if args.doc_figures else None
    make_plots(result, args.output, figure_dir)

    print(f"case: {case.case_name}")
    print(f"crossing: iota={result.profiles.crossing_iota:.6f}, s={result.profiles.crossing_s:.6f}")
    print(
        "local gap at crossing: "
        f"{result.profiles.gap_lower_rad_s / (2*np.pi*1e3):.3f}-"
        f"{result.profiles.gap_upper_rad_s / (2*np.pi*1e3):.3f} kHz"
    )
    for index, (frequency, residual) in enumerate(zip(result.frequency_khz, result.residual_norms, strict=True), start=1):
        print(f"mode {index:2d}: {frequency:12.6f} kHz, relative residual={residual:.3e}")
    print(f"outputs: {args.output}")


if __name__ == "__main__":
    main()
