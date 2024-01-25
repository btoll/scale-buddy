import functools
import unittest

from scale-buddy import scales


major_pentatonic_scale = functools.partial(scales.get_scale, scale_type="major_pentatonic")


class TestMajorPentatonicScale(unittest.TestCase):
    def test_C(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="C"),
            ["C", "D", "E", "G", "A"]
        )

    def test_C_flat(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="C", accidental=1),
            ["C♭", "D♭", "E♭", "G♭", "A♭"]
        )

    def test_C_sharp(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="C", accidental=3),
            ["C♯", "D♯", "E♯", "G♯", "A♯"]
        )

    def test_D(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="D"),
            ["D", "E", "F♯", "A", "B"]
        )

    def test_D_flat(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="D", accidental=1),
            ["D♭", "E♭", "F", "A♭", "B♭"]
        )

    def test_E(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="E"),
            ["E", "F♯", "G♯", "B", "C♯"]
        )

    def test_E_flat(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="E", accidental=1),
            ["E♭", "F", "G", "B♭", "C"]
        )

    def test_F(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="F"),
            ["F", "G", "A", "C", "D"]
        )

    def test_F_sharp(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="F", accidental=3),
            ["F♯", "G♯", "A♯", "C♯", "D♯"]
        )

    def test_G(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="G"),
            ["G", "A", "B", "D", "E"]
        )

    def test_G_flat(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="G", accidental=1),
            ["G♭", "A♭", "B♭", "D♭", "E♭"]
        )

    def test_A(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="A"),
            ["A", "B", "C♯", "E", "F♯"]
        )

    def test_A_flat(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="A", accidental=1),
            ["A♭", "B♭", "C", "E♭", "F"]
        )

    def test_B(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="B"),
            ["B", "C♯", "D♯", "F♯", "G♯"]
        )

    def test_B_flat(self):
        self.assertEqual(
            major_pentatonic_scale(tonic="B", accidental=1),
            ["B♭", "C", "D", "F", "G"]
        )


if __name__ == "__main__":
    unittest.main()

