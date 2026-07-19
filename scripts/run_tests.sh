#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT/python"
python -m unittest discover -s tests -v
python cases/run_backbone_demo.py
python cases/reduced_ae_benchmark/run_case.py --output "$ROOT/data/reference/reduced_ae_benchmark"

if command -v matlab >/dev/null 2>&1; then
  matlab -batch "cd('$ROOT/matlab'); addpath('src'); results = runtests('tests'); disp(results); assert(all([results.Passed])); addpath('cases'); run_backbone_demo; addpath('cases/reduced_ae_benchmark'); run_case"
  python "$ROOT/python/cases/reduced_ae_benchmark/compare_python_matlab.py" \
    "$ROOT/data/reference/reduced_ae_benchmark" \
    "$ROOT/matlab/outputs/reduced_ae_benchmark"
else
  echo "MATLAB executable not found; MATLAB source and tests were not executed."
fi
