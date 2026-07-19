#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"
latexmk -pdf -interaction=nonstopmode -halt-on-error project_plan.tex

cd "$ROOT/docs/physics_notes"
for tex in module*.tex; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$tex"
done

cd "$ROOT/docs/physics_notes/basics"
# Compile completed standalone basics notes, the still-scaffolded prerequisites linked
# from Module 4, and the course index. Every note remains a separate PDF.
completed_basics=(
  basics_01_units_dimensions_and_normalization.tex
  basics_02_vectors_fields_and_coordinate_systems.tex
  basics_03_vector_calculus_for_plasma_physics.tex
  basics_05_partial_differential_equations.tex
  basics_06_linear_algebra_and_eigenvalue_problems.tex
  basics_07_fourier_analysis_and_normal_modes.tex
  basics_11_electric_and_magnetic_fields.tex
  basics_12_maxwell_equations.tex
  basics_13_lorentz_force_and_charged_particle_motion.tex
  basics_17_what_is_a_plasma.tex
  basics_18_debye_shielding_and_plasma_frequency.tex
  basics_19_plasma_distributions_and_temperature.tex
  basics_21_single_fluid_and_multifluid_descriptions.tex
  basics_22_moments_of_the_kinetic_equation.tex
  basics_24_derivation_of_ideal_magnetohydrodynamics.tex
  basics_25_conservation_laws_in_mhd.tex
  basics_26_ideal_ohms_law_and_flux_freezing.tex
  basics_29_linearization_of_mhd_equations.tex
  basics_31_introduction_to_waves_in_plasmas.tex
  basics_32_alfven_waves_from_first_principles.tex
  basics_34_parallel_wave_number_and_field_line_propagation.tex
  basics_35_alfven_continuum.tex
  basics_36_coupled_harmonics_and_avoided_crossings.tex
  basics_37_toroidal_alfven_eigenmodes.tex
  basics_39_wave_particle_resonance.tex
  basics_40_growth_damping_and_complex_frequency.tex
  basics_41_phase_space_and_distribution_functions.tex
  basics_42_vlasov_equation.tex
  basics_44_guiding_center_theory.tex
  basics_48_energetic_particle_distributions.tex
)
module4_remaining_prerequisites=(
  basics_69_finite_volume_methods.tex
  basics_73_numerical_eigenvalue_solvers.tex
)
for tex in "${completed_basics[@]}" "${module4_remaining_prerequisites[@]}" basics_index.tex; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$tex"
done

if [[ "${BUILD_ALL_BASICS:-0}" == "1" ]]; then
  for tex in basics_[0-9]*.tex; do
    latexmk -pdf -interaction=nonstopmode -halt-on-error "$tex"
  done
fi

cd "$ROOT/docs/implementation_notes"
for tex in module*.tex; do
  [[ -e "$tex" ]] || continue
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$tex"
done

# Remove auxiliary files while retaining sources and PDFs.
find "$ROOT" -type f \( -name '*.aux' -o -name '*.fdb_latexmk' -o -name '*.fls' -o -name '*.log' -o -name '*.out' -o -name '*.toc' -o -name '*.synctex.gz' \) -delete
