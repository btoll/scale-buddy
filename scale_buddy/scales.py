natural = b"\xe3\x99\xae".decode()
flat = b"\xe2\x99\xad".decode()
doubleflat = flat * 2
sharp = b"\xe2\x99\xaf".decode()
doublesharp = sharp * 2
accidentals = [ doubleflat, flat, "", sharp, doublesharp]


interval_table = {
    "C": 2,
    "D": 2,
    "E": 1,
    "F": 2,
    "G": 2,
    "A": 2,
    "B": 1,
}


semitones = {
    "flat": (
        "C",
        f"D{flat}",
        "D",
        f"E{flat}",
        "E",
#        "F{flat}",
        "F",
        f"G{flat}",
        "G",
        f"A{flat}",
        "A",
        f"B{flat}",
        "B"
    ),
    "sharp": (
        "C",
        f"C{sharp}",
        "D",
        f"D{sharp}",
        "E",
#        "E{sharp}",
        "F",
        f"F{sharp}",
        "G",
        f"G{sharp}",
        "A",
        f"A{sharp}",
        "B"
    )
}


diatonic_notes = ( "C", "D", "E", "F", "G", "A", "B" )
scale_intervals = {
    "major": ( 2, 2, 1, 2, 2, 2, 1 ),
    "dorian": ( 2, 1, 2, 2, 2, 1, 2 ),
    "phrygian": ( 1, 2, 2, 2, 1, 2, 2 ),
    "lydian": ( 2, 2, 2, 1, 2, 2, 1 ),
    "mixolydian": ( 2, 2, 1, 2, 2, 1, 2 ),
    "locrian": ( 1, 2, 2, 1, 2, 2, 2 ),
    "harmonic_minor": ( 2, 1, 2, 2, 1, 3, 1 ),
    "melodic_minor": ( 2, 1, 2, 2, 2, 2, 1 ), # jazz minor
    "natural_minor": ( 2, 1, 2, 2, 1, 2, 2 ), # Aeolian
    "altered_dominant": ( 1, 2, 1, 2, 2, 2, 2 ),
}

scale_intervals["ionian"] = scale_intervals["major"]
scale_intervals["aeolian"] = scale_intervals["natural_minor"]


# These are zero-based and depend on a scale being handed to them.
secondary_scales = {
    "blues": {
        "depends_on": "natural_minor",
        "notes": ( 0, 2, 3, 4, 4, 6 ),
    },
    "major_pentatonic": {
        "depends_on": "major",
        "notes": ( 0, 1, 2, 4, 5 ), # 1, 2, 3, 5, 6 of major scale
    },
    "minor_pentatonic": {
        "depends_on": "natural_minor",
        "notes": ( 0, 2, 3, 4, 6 ), # 1, b3, 4, 5, b7 of Aeolian (natural minor) scale
    }
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


def get_minor_thirds(tonic, accidental):
    if accidental == 3:
        s_tones = semitones["sharp"]
    else:
        s_tones = semitones["flat"]

    idx = s_tones.index(tonic + accidentals[accidental])
    target_scale = s_tones[idx:] + s_tones[:idx]

    return [ target_scale[i] for i in range(0, 12, 3) ]


def get_modes(tonic, scale):
    notes = get_scale(tonic, 2, scale)
    mode_names = modes[scale]
    l = len(notes)

    return { mode_names[i]: notes[i:l] + notes[0:i] for i in range(l) }


def get_scale(tonic, accidental, scale_type):
    tonic = tonic.upper()
    current_accidental = accidentals[accidental]
    idx = diatonic_notes.index(tonic)
    has_secondary_scale = False

    scale = [tonic]
    built = [tonic + current_accidental]

    if scale_type in secondary_scales:
        secondary_scale = secondary_scales[scale_type]
        scale_type = secondary_scale["depends_on"]
        has_secondary_scale = True

    interval_scale = scale_intervals[scale_type]

    # Don't get the first note because it's pushed onto the stack.
    idx = diatonic_notes.index(tonic)
    target_scale = diatonic_notes[idx+1:] + diatonic_notes[:idx]

    for i, note in enumerate(target_scale):
        diatonic_interval = interval_table[scale[i]]
        target_interval = interval_scale[i]

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

    if has_secondary_scale:
        return get_secondary_scale(secondary_scale["notes"], built)
    else:
        return built


def get_secondary_scale(notes, primary_scale):
    return [ primary_scale[note] for note in notes ]


def get_tritone(tonic, accidental):
    if accidental == 3:
        s_tones = semitones["sharp"]
    else:
        s_tones = semitones["flat"]

    idx = s_tones.index(tonic + accidentals[accidental])
    target_scale = s_tones[idx:] + s_tones[:idx]

    return target_scale[6]


def get_whole_half_scale(tonic, accidental):
    dorian_scale = get_scale(tonic, accidental, "dorian")
    tritone = get_tritone(tonic, accidental)

    try:
        tonic, accidental = tritone[0], tritone[1]
        if accidental == flat:
            accidental = 1
        else:
            accidental = 3
    except IndexError:
        tonic = tritone[0]
        accidental = 2

    return dorian_scale[:4] + get_scale(tonic, accidental, "dorian")[:4]


