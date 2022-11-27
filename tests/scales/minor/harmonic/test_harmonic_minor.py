import unittest

from scale_buddy import scales


class TestHarmonicMinorScale(unittest.TestCase):
    def test_C(self):
        scale = scales.get_scale("C", 2, "harmonic_minor")
        self.assertEqual(scale, ["C", "D", "E♭", "F", "G", "A♭", "B"])

    def test_C_flat(self):
        scale = scales.get_scale("C", 1, "harmonic_minor")
        self.assertEqual(scale, ["C♭", "D♭", "E♭♭", "F♭", "G♭", "A♭♭", "B♭"])

    def test_C_sharp(self):
        scale = scales.get_scale("C", 3, "harmonic_minor")
        self.assertEqual(scale, ["C♯", "D♯", "E", "F♯", "G♯", "A", "B♯"])

    def test_D(self):
        scale = scales.get_scale("D", 2, "harmonic_minor")
        self.assertEqual(scale, ["D", "E", "F", "G", "A", "B♭", "C♯"])

    def test_D_flat(self):
        scale = scales.get_scale("D", 1, "harmonic_minor")
        self.assertEqual(scale, ["D♭", "E♭", "F♭", "G♭", "A♭", "B♭♭", "C"])

    def test_E(self):
        scale = scales.get_scale("E", 2, "harmonic_minor")
        self.assertEqual(scale, ["E", "F♯", "G", "A", "B", "C", "D♯"])

    def test_E_flat(self):
        scale = scales.get_scale("E", 1, "harmonic_minor")
        self.assertEqual(scale, ["E♭", "F", "G♭", "A♭", "B♭", "C♭", "D"])

    def test_F(self):
        scale = scales.get_scale("F", 2, "harmonic_minor")
        self.assertEqual(scale, ["F", "G", "A♭", "B♭", "C", "D♭", "E"])

    def test_F_sharp(self):
        scale = scales.get_scale("F", 3, "harmonic_minor")
        self.assertEqual(scale, ["F♯", "G♯", "A", "B", "C♯", "D", "E♯"])

    def test_G(self):
        scale = scales.get_scale("G", 2, "harmonic_minor")
        self.assertEqual(scale, ["G", "A", "B♭", "C", "D", "E♭", "F♯"])

    def test_G_flat(self):
        scale = scales.get_scale("G", 1, "harmonic_minor")
        self.assertEqual(scale, ["G♭", "A♭", "B♭♭", "C♭", "D♭", "E♭♭", "F"])

    def test_A(self):
        scale = scales.get_scale("A", 2, "harmonic_minor")
        self.assertEqual(scale, ["A", "B", "C", "D", "E", "F", "G♯"])

    def test_A_flat(self):
        scale = scales.get_scale("A", 1, "harmonic_minor")
        self.assertEqual(scale, ["A♭", "B♭", "C♭", "D♭", "E♭", "F♭", "G"])

    def test_B(self):
        scale = scales.get_scale("B", 2, "harmonic_minor")
        self.assertEqual(scale, ["B", "C♯", "D", "E", "F♯", "G", "A♯"])

    def test_B_flat(self):
        scale = scales.get_scale("B", 1, "harmonic_minor")
        self.assertEqual(scale, ["B♭", "C", "D♭", "E♭", "F", "G♭", "A"])


if __name__ == "__main__":
    unittest.main()

