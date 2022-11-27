import unittest

from scale_buddy import scales


class TestMajorPentatonicScale(unittest.TestCase):
    def test_C(self):
        scale = scales.get_scale("C", 2, "major_pentatonic")
        self.assertEqual(scale, ["C", "D", "E", "G", "A"])

    def test_C_flat(self):
        scale = scales.get_scale("C", 1, "major_pentatonic")
        self.assertEqual(scale, ["C♭", "D♭", "E♭", "G♭", "A♭"])

    def test_C_sharp(self):
        scale = scales.get_scale("C", 3, "major_pentatonic")
        self.assertEqual(scale, ["C♯", "D♯", "E♯", "G♯", "A♯"])

    def test_D(self):
        scale = scales.get_scale("D", 2, "major_pentatonic")
        self.assertEqual(scale, ["D", "E", "F♯", "A", "B"])

    def test_D_flat(self):
        scale = scales.get_scale("D", 1, "major_pentatonic")
        self.assertEqual(scale, ["D♭", "E♭", "F", "A♭", "B♭"])

    def test_E(self):
        scale = scales.get_scale("E", 2, "major_pentatonic")
        self.assertEqual(scale, ["E", "F♯", "G♯", "B", "C♯"])

    def test_E_flat(self):
        scale = scales.get_scale("E", 1, "major_pentatonic")
        self.assertEqual(scale, ["E♭", "F", "G", "B♭", "C"])

    def test_F(self):
        scale = scales.get_scale("F", 2, "major_pentatonic")
        self.assertEqual(scale, ["F", "G", "A", "C", "D"])

    def test_F_sharp(self):
        scale = scales.get_scale("F", 3, "major_pentatonic")
        self.assertEqual(scale, ["F♯", "G♯", "A♯", "C♯", "D♯"])

    def test_G(self):
        scale = scales.get_scale("G", 2, "major_pentatonic")
        self.assertEqual(scale, ["G", "A", "B", "D", "E"])

    def test_G_flat(self):
        scale = scales.get_scale("G", 1, "major_pentatonic")
        self.assertEqual(scale, ["G♭", "A♭", "B♭", "D♭", "E♭"])

    def test_A(self):
        scale = scales.get_scale("A", 2, "major_pentatonic")
        self.assertEqual(scale, ["A", "B", "C♯", "E", "F♯"])

    def test_A_flat(self):
        scale = scales.get_scale("A", 1, "major_pentatonic")
        self.assertEqual(scale, ["A♭", "B♭", "C", "E♭", "F"])

    def test_B(self):
        scale = scales.get_scale("B", 2, "major_pentatonic")
        self.assertEqual(scale, ["B", "C♯", "D♯", "F♯", "G♯"])

    def test_B_flat(self):
        scale = scales.get_scale("B", 1, "major_pentatonic")
        self.assertEqual(scale, ["B♭", "C", "D", "F", "G"])


if __name__ == "__main__":
    unittest.main()

