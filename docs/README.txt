Kinetic MHD-PINN documentation structure

shared/
  Shared LaTeX style inherited from RadiationEffects_proj2.

physics_notes/
  Derivation-oriented LaTeX/PDF notes for each physical or machine-learning module. Modules 1 and 4 are completed textbook chapters; the other advanced notes remain scaffolds unless stated otherwise.

implementation_notes/
  Solver contracts, data interfaces, verification plans, and coding notes for the parallel Python and MATLAB implementations. These are Markdown because they are operational documents rather than derivation-focused physics notes.

The top-level project_plan.tex/.pdf remains the single living architecture roadmap.

Module 4 is the first completed numerical milestone. Its 77-page textbook physics note, version 2.0, is modularized under physics_notes/module4_sections/, while its implementation note remains a separate LaTeX/PDF software contract.
