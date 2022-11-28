# https://en.wikipedia.org/wiki/Jazz_scale#Modes_of_the_melodic_minor_scale
# https://en.wikipedia.org/wiki/Minor_scale#Modes_of_harmonic_minor_scale
# https://en.wikipedia.org/wiki/Jazz_minor_scale
# https://www.jazzguitar.be/blog/melodic-minor-modes/
import argparse

import scale_buddy.scales as scales


parser = argparse.ArgumentParser()
parser.add_argument("tonic", help="The tonic note of the scale", type=str)
parser.add_argument("-f", "--flat", help="Flat", action="store_true")
parser.add_argument("-s", "--sharp", help="Sharp", action="store_true")
parser.add_argument("-d", "--delimiter", help="The symbol that separates the notes", type=str, default="  ")
parser.add_argument("--with-minor", help="Include minor scales", action="store_true")
parser.add_argument("--with-pentatonic", help="Include pentatonic scales", action="store_true")
parser.add_argument("-v", "--verbose", help="Add extra information", action="store_true")
args = parser.parse_args()


has_accidental = args.flat or args.sharp


def get_accidental():
    if args.flat:
        return scales.flat
    elif args.sharp:
        return scales.sharp
    else:
        return ""


#def display_key_string():
#    if not args.flat and not args.sharp:
#        return ""
#    else:
#        return get_accidental()


def main():
    try:
        tonic = args.tonic.upper()

#        print(scales.get_modes(tonic, "major"))
#        print()
#        print(scales.get_modes(tonic, "melodic_minor"))

        if args.sharp:
            accidental = 3
        elif args.flat:
            accidental = 1
        else:
            accidental = 2

#        print(scales.get_tritone(tonic, accidental))
#        whole_half_scale = scales.get_whole_half_scale(tonic, accidental)
#        print("".join([tonic, get_accidental(), " whole-half:"]))
#        print(args.delimiter.join(whole_half_scale))

        major_scale = scales.get_scale("major", tonic, accidental)
        print("".join([tonic, get_accidental(), " major:"]))
        print(args.delimiter.join(major_scale))

#        blues_scale = scales.get_scale("blues", tonic, accidental)
#        print("".join([tonic, get_accidental(), " blues:"]))
#        print(args.delimiter.join(blues_scale))

#        altered_dominant_scale = get_scale("altered_dominant", args.tonic, accidental)
#        print("".join(["\n", tonic, get_accidental(), " altered dominant:"]))
#        print(args.delimiter.join(altered_dominant_scale))

#        dorian_scale = scales.get_scale("dorian", tonic, accidental)
#        print("".join([tonic, get_accidental(), " dorian:"]))
#        print(args.delimiter.join(dorian_scale))

        if args.with_minor:
            s = "".join(["\n", tonic, get_accidental()])

            natural_minor_scale = scales.get_scale("natural_minor", tonic, accidental)
            print("".join([s, " natural minor (Aeolian):"]))
            print(args.delimiter.join(natural_minor_scale))

            harmonic_minor_scale = scales.get_scale("harmonic_minor", tonic, accidental)
            print("".join([s, " harmonic minor:"]))
            print(args.delimiter.join(harmonic_minor_scale))

            melodic_minor_scale = scales.get_scale("melodic_minor", tonic, accidental)
            print("".join([s, " melodic minor (jazz minor):"]))
            print(args.delimiter.join(melodic_minor_scale))

        if args.with_pentatonic:
            s = "".join(["\n", tonic, get_accidental()])

            major_pentatonic_scale = scales.get_scale("major_pentatonic", tonic, accidental)
            print("".join([s, " major pentatonic:"]))
            print("    ".join(major_pentatonic_scale))

            minor_pentatonic_scale = scales.get_scale("minor_pentatonic", tonic, accidental)
            print("".join([s, " minor pentatonic scale:"]))
            print("    ".join(minor_pentatonic_scale))

    except ValueError as err:
        print("[ERROR] The tonic note must be in the range A..G")


if __name__ == "__main__":
    main()

