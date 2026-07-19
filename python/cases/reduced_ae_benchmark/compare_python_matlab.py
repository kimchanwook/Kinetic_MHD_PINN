from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def read_csv(path: Path) -> np.ndarray:
    return np.genfromtxt(path, delimiter=",", names=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare independent Python and MATLAB reduced-AE benchmark outputs.")
    parser.add_argument("python_output", type=Path)
    parser.add_argument("matlab_output", type=Path)
    parser.add_argument("--relative-tolerance", type=float, default=1.0e-5)
    args = parser.parse_args()

    py_values = read_csv(args.python_output / "eigenvalues.csv")
    ml_values = read_csv(args.matlab_output / "eigenvalues.csv")
    if py_values.size != ml_values.size:
        raise SystemExit("eigenvalue files contain different numbers of modes")
    relative = np.abs(py_values["frequency_hz"] - ml_values["frequency_hz"]) / np.abs(py_values["frequency_hz"])
    maximum = float(np.max(relative))
    print(f"maximum eigenfrequency relative difference: {maximum:.6e}")

    py_modes = read_csv(args.python_output / "eigenmodes.csv")
    ml_modes = read_csv(args.matlab_output / "eigenmodes.csv")
    if py_modes.dtype.names != ml_modes.dtype.names:
        raise SystemExit("eigenmode files have different columns")
    correlations = []
    for name in py_modes.dtype.names[1:]:
        a = np.asarray(py_modes[name], dtype=float)
        b = np.asarray(ml_modes[name], dtype=float)
        correlations.append(abs(float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))))
    minimum_correlation = min(correlations)
    print(f"minimum sign-invariant component correlation: {minimum_correlation:.9f}")

    if maximum > args.relative_tolerance:
        raise SystemExit(f"FAIL: eigenfrequency tolerance {args.relative_tolerance:.3e} exceeded")
    if minimum_correlation < 0.999:
        raise SystemExit("FAIL: an eigenmode component correlation is below 0.999")
    print("PASS: Python/MATLAB parity criteria satisfied")


if __name__ == "__main__":
    main()
