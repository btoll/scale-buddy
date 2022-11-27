import ipdb


natural = b"\xe3\x99\xae".decode()
flat = b"\xe2\x99\xad".decode()
doubleflat = flat * 2
sharp = b"\xe2\x99\xaf".decode()
doublesharp = sharp * 2
accidentals = [ doubleflat, flat, "", sharp, doublesharp]


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
    notes = get_scale(args.tonic, scale)
    m = modes[scale]
    l = len(notes)

    print(" ".join(["Modes of", scale, "scale:"]))

    for i in range(l):
        mode = args.delimiter.join(notes[i:l] + notes[0:i])
        print("".join([m[i], "\n", mode, "\n"]))


# If `args.flat` or `args.sharp` do the opposite!
def get_scale(tonic, accidental, scale_type):
    current_accidental = accidentals[accidental]
    tonic = tonic.upper()
    idx = diatonic_notes.index(tonic)

    # Why have two different scale arrays?
    # This is necessary because one is used to lookup the notes in the
    # `scale_intervals` dict, and the other is returned to the program
    # (the `built` array).
    #
    # The latter will have accents, both flats and sharps, and this can't
    tonic = tonic.upper()
    # be used to lookup the intervals since the `interval_table` only has
    # natural notes as its keys.
    scale = [tonic]
    built = [tonic + current_accidental]

    interval_scale = scale_intervals[scale_type]

    # Don't get the first note because it's pushed onto the stack.
    target_scale = diatonic_notes[idx+1:] + diatonic_notes[:idx]

    for i, note in enumerate(target_scale):
        diatonic_interval = interval_table[scale[i]]
        target_interval = interval_scale[i]
#        ipdb.set_trace()

        if target_interval == diatonic_interval:
            built.append(note + current_accidental)
        elif diatonic_interval != target_interval:
            if diatonic_interval > target_interval:
                accidental = accidental - diatonic_interval + target_interval
            else:
                accidental = accidental + target_interval - diatonic_interval

            current_accidental = accidentals[accidental]
            built.append(note + current_accidental)

        scale.append(note)

    return built


def get_secondary_scale(scale_type, primary_scale):
    scale = []

    for note in secondary_scales[scale_type]:
        scale.append(primary_scale[note])

    return scale


