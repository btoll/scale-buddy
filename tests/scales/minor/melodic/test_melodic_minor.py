import functools
import unittest

from scale-buddy import scales


melodic_minor_scale = functools.partial(scales.get_scale, scale_type="melodic_minor")


class TestMelodicMinorScale(unittest.TestCase):
    def test_C(self):
        self.assertEqual(
            melodic_minor_scale(tonic="C"),
            ["C", "D", "E♭", "F", "G", "A", "B"]
        )

    def test_C_flat(self):
        self.assertEqual(
            melodic_minor_scale(tonic="C", accidental=1),
            ["C♭", "D♭", "E♭♭", "F♭", "G♭", "A♭", "B♭"]
        )

    def test_C_sharp(self):
        self.assertEqual(
            melodic_minor_scale(tonic="C", accidental=3),
            ["C♯", "D♯", "E", "F♯", "G♯", "A♯", "B♯"]
        )

    def test_D(self):
        self.assertEqual(
            melodic_minor_scale(tonic="D"),
            ["D", "E", "F", "G", "A", "B", "C♯"]
        )

    def test_D_flat(self):
        self.assertEqual(
            melodic_minor_scale(tonic="D", accidental=1),
            ["D♭", "E♭", "F♭", "G♭", "A♭", "B♭", "C"]
        )

    def test_E(self):
        self.assertEqual(
            melodic_minor_scale(tonic="E"),
            ["E", "F♯", "G", "A", "B", "C♯", "D♯"]
        )

    def test_E_flat(self):
        self.assertEqual(
            melodic_minor_scale(tonic="E", accidental=1),
            ["E♭", "F", "G♭", "A♭", "B♭", "C", "D"]
        )

    def test_F(self):
        self.assertEqual(
            melodic_minor_scale(tonic="F"),
            ["F", "G", "A♭", "B♭", "C", "D", "E"]
        )

    def test_F_sharp(self):
        self.assertEqual(
            melodic_minor_scale(tonic="F", accidental=3),
            ["F♯", "G♯", "A", "B", "C♯", "D♯", "E♯"]
        )

    def test_G(self):
        self.assertEqual(
            melodic_minor_scale(tonic="G"),
            ["G", "A", "B♭", "C", "D", "E", "F♯"]
        )

    def test_G_flat(self):
        self.assertEqual(
            melodic_minor_scale(tonic="G", accidental=1),
            ["G♭", "A♭", "B♭♭", "C♭", "D♭", "E♭", "F"]
        )

    def test_A(self):
        self.assertEqual(
            melodic_minor_scale(tonic="A"),
            ["A", "B", "C", "D", "E", "F♯", "G♯"]
        )

    def test_A_flat(self):
        self.assertEqual(
            melodic_minor_scale(tonic="A", accidental=1),
            ["A♭", "B♭", "C♭", "D♭", "E♭", "F", "G"]
        )

    def test_B(self):
        self.assertEqual(
            melodic_minor_scale(tonic="B"),
            ["B", "C♯", "D", "E", "F♯", "G♯", "A♯"]
        )

    def test_B_flat(self):
        self.assertEqual(
            melodic_minor_scale(tonic="B", accidental=1),
            ["B♭", "C", "D♭", "E♭", "F", "G", "A"]
        )


if __name__ == "__main__":
    unittest.main()

