# Python framework

The Python tree contains the shared software scaffold plus the first conventional physics solver: the Module 4 reduced two-harmonic shear-Alfvén benchmark. It supplies:

- a typed shared state container;
- a module registry with declared dependencies and products;
- one package directory per project module;
- a nominal backbone demonstration;
- contract tests that protect the architecture while physics implementations are added;
- Module 4 profile, continuum, finite-volume eigenvalue, convergence, and output utilities.

Run without installation:

```bash
python -m unittest discover -s tests -v
python cases/run_backbone_demo.py
```

Run the Module 4 benchmark with `python cases/reduced_ae_benchmark/run_case.py`. The matrix solver remains the reference for the later eigenvalue PINN.
