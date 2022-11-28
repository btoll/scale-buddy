import functools
import unittest

from scale_buddy import scales


minor_pentatonic_scale = functools.partial(scales.get_scale, scale_type="minor_pentatonic")


class TestMinorPentatonicScale(unittest.TestCase):
    def test_C(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="C"),
            ["C", "E♭", "F", "G", "B♭"]
        )

    def test_C_flat(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="C", accidental=1),
            ["C♭", "E♭♭", "F♭", "G♭", "B♭♭"]
        )

    def test_C_sharp(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="C", accidental=3),
            ["C♯", "E", "F♯", "G♯", "B"]
        )

    def test_D(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="D"),
            ["D", "F", "G", "A", "C"]
        )

    def test_D_flat(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="D", accidental=1),
            ["D♭", "F♭", "G♭", "A♭", "C♭"]
        )

    def test_E(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="E"),
            ["E", "G", "A", "B", "D"]
        )

    def test_E_flat(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="E", accidental=1),
            ["E♭", "G♭", "A♭", "B♭", "D♭"]
        )

    def test_F(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="F"),
            ["F", "A♭", "B♭", "C", "E♭"]
        )

    def test_F_sharp(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="F", accidental=3),
            ["F♯", "A", "B", "C♯", "E"]
        )

    def test_G(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="G"),
            ["G", "B♭", "C", "D", "F"]
        )

    def test_G_flat(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="G", accidental=1),
            ["G♭", "B♭♭", "C♭", "D♭", "F♭"]
        )

    def test_A(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="A"),
            ["A", "C", "D", "E", "G"]
        )

    def test_A_flat(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="A", accidental=1),
            ["A♭",  "C♭", "D♭", "E♭", "G♭"]
        )

    def test_B(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="B"),
            ["B",  "D", "E", "F♯",  "A"]
        )

    def test_B_flat(self):
        self.assertEqual(
            minor_pentatonic_scale(tonic="B", accidental=1),
            ["B♭",  "D♭", "E♭", "F",  "A♭"]
        )


if __name__ == "__main__":
    unittest.main()

