import unittest

from scale_buddy import scales


class TestMinorPentatonicScale(unittest.TestCase):
    def test_C(self):
        scale = scales.get_scale("C", 2, "minor_pentatonic")
        self.assertEqual(scale, ["C", "E♭", "F", "G", "B♭"])

    def test_C_flat(self):
        scale = scales.get_scale("C", 1, "minor_pentatonic")
        self.assertEqual(scale, ["C♭", "E♭♭", "F♭", "G♭", "B♭♭"])

    def test_C_sharp(self):
        scale = scales.get_scale("C", 3, "minor_pentatonic")
        self.assertEqual(scale, ["C♯", "E", "F♯", "G♯", "B"])

    def test_D(self):
        scale = scales.get_scale("D", 2, "minor_pentatonic")
        self.assertEqual(scale, ["D", "F", "G", "A", "C"])

    def test_D_flat(self):
        scale = scales.get_scale("D", 1, "minor_pentatonic")
        self.assertEqual(scale, ["D♭", "F♭", "G♭", "A♭", "C♭"])

    def test_E(self):
        scale = scales.get_scale("E", 2, "minor_pentatonic")
        self.assertEqual(scale, ["E", "G", "A", "B", "D"])

    def test_E_flat(self):
        scale = scales.get_scale("E", 1, "minor_pentatonic")
        self.assertEqual(scale, ["E♭", "G♭", "A♭", "B♭", "D♭"])

    def test_F(self):
        scale = scales.get_scale("F", 2, "minor_pentatonic")
        self.assertEqual(scale, ["F", "A♭", "B♭", "C", "E♭"])

    def test_F_sharp(self):
        scale = scales.get_scale("F", 3, "minor_pentatonic")
        self.assertEqual(scale, ["F♯", "A", "B", "C♯", "E"])

    def test_G(self):
        scale = scales.get_scale("G", 2, "minor_pentatonic")
        self.assertEqual(scale, ["G", "B♭", "C", "D", "F"])

    def test_G_flat(self):
        scale = scales.get_scale("G", 1, "minor_pentatonic")
        self.assertEqual(scale, ["G♭", "B♭♭", "C♭", "D♭", "F♭"])

    def test_A(self):
        scale = scales.get_scale("A", 2, "minor_pentatonic")
        self.assertEqual(scale, ["A", "C", "D", "E", "G"])

    def test_A_flat(self):
        scale = scales.get_scale("A", 1, "minor_pentatonic")
        self.assertEqual(scale, ["A♭",  "C♭", "D♭", "E♭", "G♭"])

    def test_B(self):
        scale = scales.get_scale("B", 2, "minor_pentatonic")
        self.assertEqual(scale, ["B",  "D", "E", "F♯",  "A"])

    def test_B_flat(self):
        scale = scales.get_scale("B", 1, "minor_pentatonic")
        self.assertEqual(scale, ["B♭",  "D♭", "E♭", "F",  "A♭"])


if __name__ == "__main__":
    unittest.main()

