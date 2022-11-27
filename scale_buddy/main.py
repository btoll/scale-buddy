# https://en.wikipedia.org/wiki/Jazz_scale#Modes_of_the_melodic_minor_scale
# https://en.wikipedia.org/wiki/Minor_scale#Modes_of_harmonic_minor_scale
# https://en.wikipedia.org/wiki/Jazz_minor_scale
# https://www.jazzguitar.be/blog/melodic-minor-modes/
import argparse
import ipdb


parser = argparse.ArgumentParser()
parser.add_argument("tonic", help="The tonic note of the scale", type=str)
parser.add_argument("-f", "--flat", help="Flat", action="store_true")
parser.add_argument("-s", "--sharp", help="Sharp", action="store_true")
parser.add_argument("-d", "--delimiter", help="The symbol that separates the notes", type=str, default="  ")
parser.add_argument("--with-minor", help="Include minor scales", action="store_true")
parser.add_argument("--with-pentatonic", help="Include pentatonic scales", action="store_true")
parser.add_argument("-v", "--verbose", help="Add extra information", action="store_true")
args = parser.parse_args()


natural = b"\xe3\x99\xae".decode()
flat = b"\xe2\x99\xad".decode()
doubleflat = flat * 2
sharp = b"\xe2\x99\xaf".decode()
doublesharp = sharp * 2
accidentals = [ doubleflat, flat, "", sharp, doublesharp]


has_accidental = args.flat or args.sharp


# This is mutated each time as the scale is built, so a copy must always be made.
interval_table = {
    "C": 2,
    "D": 2,
    "E": 1,
    "F": 2,
    "G": 2,
    "A": 2,
    "B": 1,
}


diatonic_notes = ( "C", "D", "E", "F", "G", "A", "B" )
scale_intervals = {
    "major": ( 2, 2, 1, 2, 2, 2, 1 ),
    "harmonic_minor": ( 2, 1, 2, 2, 1, 3, 1 ),
    "melodic_minor": ( 2, 1, 2, 2, 2, 2, 1 ), # jazz minor
    "natural_minor": ( 2, 1, 2, 2, 1, 2, 2 ), # aeolian
    "altered_dominant": ( 1, 2, 1, 2, 2, 2, 2 ),
}


# These are zero-based.
secondary_scales = {
    "blues": ( 0, 2, 3, "{flat}4", 4, 6 ),
    "major_pentatonic": ( 0, 1, 2, 4, 5 ), # 1, 2, 3, 5, 6 of major scale
    "minor_pentatonic": ( 0, 2, 3, 4, 6 ), # 1, b3, 4, 5, b7 of aeolian (natural minor) scale
}


modes = {
    "major": (
        "Ionian",
        "Dorian",
        "Phrygian",
        "Lydian",
        "Mixolydian",
        "Aeolian",
        "Locrian"
    ),
    "melodic_minor": (
        "Melodic minor",
        f"Dorian {flat}2 / Phrygian {sharp}6",
        f"Lydian augmented / Lydian {sharp}5",
        f"Lydian dominant / Lydian {flat}7",
        f"Mixolydian {flat}6",
        f"Locrian {sharp}2 / Aeolian {flat}5",
        "Super Locrian / altered dominant / altered",
    ),
}


#def display_key_string():
#    if not args.flat and not args.sharp:
#        return ""
#    else:
#        return get_accidental()


def get_accidental():
    if args.flat:
        return flat
    elif args.sharp:
        return sharp
    else:
        return ""


#def get_blues_scale(major_scale):
#    # 1, 3, 4, flat 5, 5, 7
#    minor_tonic, minor_scale = get_relative_minor_scale(major_scale)
#    return minor_tonic, minor_scale[:1] + minor_scale[2:5] + minor_scale[6:7]


#def get_relative_minor_scale(tonic):
#    relative_minor_tonic = diatonic_notes[ ( diatonic_notes.index(tonic) + 2 ) % len(diatonic_notes) ]
#    _, major_scale = get_scale(relative_minor_tonic, intervals["major"])
#    front = major_scale[-3:]
#    back = major_scale[1:-3]
#    return front[0], front + back + front[:1]

def get_modes(scale):
    tonic, notes = get_scale(args.tonic, scale)
    m = modes[scale]
    l = len(notes)

    print(" ".join(["Modes of", scale, "scale:"]))

    for i in range(l):
        mode = args.delimiter.join(notes[i:l] + notes[0:i])
        print("".join([m[i], "\n", mode, "\n"]))

# If `args.flat` or `args.sharp` do the opposite!
def get_scale(tonic, scale_type):
    if args.sharp:
        d = 3
    elif args.flat:
        d = 1
    else:
        d = 2

    current_accidental = accidentals[d]
    tonic = tonic.upper()
    idx = diatonic_notes.index(tonic)

    # Why have two different scale arrays?
    # This is necessary because one is used to lookup the notes in the
    # `scale_intervals` dict, and the other is returned to the program
    # (the `built` array).
    #
    # The latter will have accents, both flats and sharps, and this can't
    # be used to lookup the intervals since the `interval_table` only has
    # natural notes as its keys.
    scale = [tonic]
    if has_accidental:
        built = [tonic + get_accidental()]
    else:
        built = [tonic]

    interval_scale = scale_intervals[scale_type]

    # Don't get the first note because it's pushed onto the stack.
    target_scale = diatonic_notes[idx+1:] + diatonic_notes[:idx]

    for i, note in enumerate(target_scale):
        diatonic_interval = interval_table[scale[i]]
        target_interval = interval_scale[i]
#        ipdb.set_trace()

        if target_interval == diatonic_interval:
            built.append(note + current_accidental)
#            if has_accidental:
#                built.append(note + get_accidental())
#            else:
#                built.append(note)

#        elif target_interval - diatonic_interval == 1:
#            built.append(note + get_accidental())
#            if has_accidental:
#                built.append(note)
#            else:
#                built.append(note + get_accidental())

        elif diatonic_interval != target_interval:
            if diatonic_interval > target_interval:
                d -= 1
            else:
                d += 1

            current_accidental = accidentals[d]
            built.append(note + current_accidental)
#            if has_accidental:
#                if args.flat:
#                    built.append(note + doubleflat)
#                else:
#                    built.append(note)
#            else:
#                # This is `flat` and not `get_accidental()` purposefully!
#                built.append(note + flat)

        scale.append(note)

    return tonic, built


def get_secondary_scale(scale_type, primary_scale):
    scale = []

    for note in secondary_scales[scale_type]:
        scale.append(primary_scale[note])

    return scale[0], scale


def main():
    try:
#        get_modes("major")
#        print()
#        get_modes("melodic_minor")

        tonic, major_scale = get_scale(args.tonic, "major")
        print("".join([tonic, get_accidental(), " major:"]))
        print(args.delimiter.join(major_scale))

#        tonic, altered_dominant_scale = get_scale(args.tonic, "altered_dominant")
#        print("".join(["\n", tonic, get_accidental(), " altered dominant:"]))
#        print(args.delimiter.join(altered_dominant_scale))

        if args.with_minor:
            s = "".join(["\n", tonic, get_accidental()])

            tonic, natural_minor_scale = get_scale(args.tonic, "natural_minor")
            print("".join([s, " natural minor (Aeolian):"]))
            print(args.delimiter.join(natural_minor_scale))

            tonic, harmonic_minor_scale = get_scale(args.tonic, "harmonic_minor")
            print("".join([s, " harmonic minor:"]))
            print(args.delimiter.join(harmonic_minor_scale))

            tonic, melodic_minor_scale = get_scale(args.tonic, "melodic_minor")
            print("".join([s, " melodic minor (jazz minor):"]))
            print(args.delimiter.join(melodic_minor_scale))

        if args.with_pentatonic:
            s = "".join(["\n", tonic, get_accidental()])

            tonic, natural_minor_scale = get_scale(args.tonic, "natural_minor")

            _, major_pentatonic_scale = get_secondary_scale("major_pentatonic", major_scale)
            print("".join([s, " major pentatonic:"]))
            print("    ".join(major_pentatonic_scale))

            _, minor_pentatonic_scale = get_secondary_scale("minor_pentatonic", natural_minor_scale)
            print("".join([s, " minor pentatonic scale:"]))
            print("    ".join(minor_pentatonic_scale))

    except ValueError as err:
        print("[ERROR] The tonic note must be in the range A..G")


if __name__ == "__main__":
    main()
