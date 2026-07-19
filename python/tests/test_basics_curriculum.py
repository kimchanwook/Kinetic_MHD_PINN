from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

PYTHON_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PYTHON_ROOT.parent
BASICS_ROOT = REPOSITORY_ROOT / "docs" / "physics_notes" / "basics"
MODULE4 = REPOSITORY_ROOT / "docs" / "physics_notes" / "module4_alfven_continuum_eigenmodes.tex"
MODULE5 = REPOSITORY_ROOT / "docs" / "physics_notes" / "module5_kinetic_energetic_particle_drive.tex"
DRAFTS = {1, 2, 3, 5, 6, 7, 11, 12, 13, 17, 18, 19, 21, 22, 24, 25, 26, 29, 31, 32, 34, 35, 36, 37, 39, 40, 41, 42, 44, 48}
SECOND_BATCH = {18, 19, 21, 22, 24, 25, 26, 29, 31, 32}
THIRD_BATCH = {34, 35, 36, 37, 39, 40, 41, 42, 44, 48}


class BasicsCurriculumTests(unittest.TestCase):
    def test_exactly_one_hundred_numbered_sources_exist(self) -> None:
        pattern = re.compile(r"basics_(\d{2,3})_[a-z0-9_]+\.tex$")
        numbered = []
        for path in BASICS_ROOT.glob("basics_*.tex"):
            match = pattern.fullmatch(path.name)
            if match:
                numbered.append((int(match.group(1)), path))
        self.assertEqual([n for n, _ in sorted(numbered)], list(range(1, 101)))
        self.assertEqual(len(numbered), 100)

    def test_manifest_matches_three_ten_note_batches(self) -> None:
        manifest = json.loads((BASICS_ROOT / "curriculum_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "mixed_curriculum_textbook_drafts_and_scaffolds")
        self.assertEqual(manifest["count"], 100)
        self.assertEqual(manifest["textbook_draft_count"], 30)
        self.assertEqual(set(manifest["textbook_draft_numbers"]), DRAFTS)
        self.assertEqual(manifest["scaffold_count"], 70)
        self.assertEqual(manifest["completed_batches"][1]["numbers"], sorted(SECOND_BATCH))
        self.assertEqual(manifest["completed_batches"][2]["numbers"], sorted(THIRD_BATCH))
        self.assertEqual(len(manifest["notes"]), 100)
        for note in manifest["notes"]:
            source = BASICS_ROOT / f"{note['filename']}.tex"
            self.assertTrue(source.is_file(), source)
            text = source.read_text(encoding="utf-8")
            self.assertIn("../../shared/project_style.tex", text)
            if note["number"] in DRAFTS:
                self.assertEqual(note["status"], "textbook_draft_v1")
                self.assertEqual(note["version"], "1.0")
                self.assertIn("Textbook draft, version 1.0", text)
                self.assertIn(r"\section{Learning objectives}", text)
                self.assertIn(r"\section{Computational laboratory}", text)
                self.assertIn(r"\section{Exercises}", text)
                self.assertIn(r"\section{References}", text)
                self.assertGreater(len(text), 6500)
            else:
                self.assertEqual(note["status"], "curriculum_scaffold")
                self.assertIn("Curriculum scaffold - not yet a completed textbook chapter", text)

    def test_second_batch_has_expected_subject_chain(self) -> None:
        required_sections = {
            18: ["Debye", "plasma frequency"],
            19: ["Distribution function", "Maxwellian"],
            21: ["Species fluid equations", "generalized Ohm"],
            22: ["Zeroth moment", "First moment", "Second moment"],
            24: ["Target ideal-MHD system", "Induction equation"],
            25: ["Mass conservation", "Total energy"],
            26: ["Ideal Ohm", "Flux-freezing theorem"],
            29: ["Equilibrium and perturbation", "Lagrangian displacement"],
            31: ["Dispersion relations", "Complex frequency"],
            32: ["magnetic tension", "Alfvén speed"],
        }
        manifest = json.loads((BASICS_ROOT / "curriculum_manifest.json").read_text(encoding="utf-8"))
        by_number = {note["number"]: note for note in manifest["notes"]}
        for number, phrases in required_sections.items():
            text = (BASICS_ROOT / f"{by_number[number]['filename']}.tex").read_text(encoding="utf-8")
            for phrase in phrases:
                self.assertIn(phrase, text)

        debye = (BASICS_ROOT / f"{by_number[18]['filename']}.tex").read_text(encoding="utf-8")
        self.assertIn(r"E=\frac{en_0}{\epsilon_0}\xi", debye)
        self.assertIn(r"m_e\ddot\xi=-eE=-\frac{n_0e^2}{\epsilon_0}\xi", debye)
        moments = (BASICS_ROOT / f"{by_number[22]['filename']}.tex").read_text(encoding="utf-8")
        self.assertNotIn(r"\mathbf F_v", moments)


    def test_third_batch_has_expected_subject_chain(self) -> None:
        required_sections = {
            34: ["Parallel derivative", "Rational surfaces"],
            35: ["Local surface frequency", "Continuum damping"],
            36: ["Coupled matrix", "avoided"],
            37: ["TAE gap", "Energetic-particle resonance"],
            39: ["phase synchronism", "Action-angle"],
            40: ["Complex frequency", "Power balance"],
            41: ["Phase-space continuity", "Marker particles"],
            42: ["Vlasov equation", "Characteristic interpretation"],
            44: ["Magnetic moment", "Guiding-center drifts"],
            48: ["Classical slowing-down", "Neutral-beam distributions"],
        }
        manifest = json.loads((BASICS_ROOT / "curriculum_manifest.json").read_text(encoding="utf-8"))
        by_number = {note["number"]: note for note in manifest["notes"]}
        for number, phrases in required_sections.items():
            text = (BASICS_ROOT / f"{by_number[number]['filename']}.tex").read_text(encoding="utf-8")
            for phrase in phrases:
                self.assertIn(phrase, text)

        slowing = (BASICS_ROOT / f"{by_number[48]['filename']}.tex").read_text(encoding="utf-8")
        self.assertIn(r"\frac{3n_f}{4\pi", slowing)
        guiding = (BASICS_ROOT / f"{by_number[44]['filename']}.tex").read_text(encoding="utf-8")
        self.assertIn(r"\mu=\frac{mv_\perp^2}{2B}", guiding)

    def test_basics_are_not_combined_into_a_volume(self) -> None:
        forbidden_names = {
            "core_foundations_volume.tex", "core_foundations_volume.pdf",
            "combined_basics.tex", "combined_basics.pdf",
        }
        present = {path.name for path in BASICS_ROOT.iterdir()} & forbidden_names
        self.assertEqual(present, set())
        build = (REPOSITORY_ROOT / "scripts" / "build_docs.sh").read_text(encoding="utf-8").lower()
        self.assertNotIn("includepdf", build)
        self.assertNotIn("core_foundations_volume", build)

    def test_module4_declares_required_prerequisites(self) -> None:
        text = MODULE4.read_text(encoding="utf-8")
        required = {
            29: "basics_29_linearization_of_mhd_equations.pdf",
            32: "basics_32_alfven_waves_from_first_principles.pdf",
            34: "basics_34_parallel_wave_number_and_field_line_propagation.pdf",
            35: "basics_35_alfven_continuum.pdf",
            36: "basics_36_coupled_harmonics_and_avoided_crossings.pdf",
            37: "basics_37_toroidal_alfven_eigenmodes.pdf",
            69: "basics_69_finite_volume_methods.pdf",
            73: "basics_73_numerical_eigenvalue_solvers.pdf",
        }
        self.assertIn("Prerequisite basics notes", text)
        for number, filename in required.items():
            self.assertIn(f"Basics {number}", text)
            self.assertIn(filename, text)


    def test_module5_declares_kinetic_prerequisites(self) -> None:
        text = MODULE5.read_text(encoding="utf-8")
        required = [32, 34, 35, 37, 39, 40, 41, 42, 44, 48]
        self.assertIn("Prerequisite basics notes", text)
        for number in required:
            self.assertIn(f"Basics {number}", text)

    def test_build_script_compiles_completed_notes_separately(self) -> None:
        text = (REPOSITORY_ROOT / "scripts" / "build_docs.sh").read_text(encoding="utf-8")
        self.assertIn("BUILD_ALL_BASICS", text)
        self.assertIn("basics_index.tex", text)
        manifest = json.loads((BASICS_ROOT / "curriculum_manifest.json").read_text(encoding="utf-8"))
        by_number = {note["number"]: note for note in manifest["notes"]}
        for number in DRAFTS:
            self.assertIn(f"{by_number[number]['filename']}.tex", text)


if __name__ == "__main__":
    unittest.main()
