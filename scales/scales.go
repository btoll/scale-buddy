package scales

import (
	"fmt"
	"slices"
	"strings"
)

var (
	Flat          string   = "♭"
	DoubleFlat    string   = "♭♭"
	Natural       string   = "♮"
	Sharp         string   = "♯"
	DoubleSharp   string   = "♯♯"
	accidentals   []string = []string{DoubleFlat, Flat, "", Sharp, DoubleSharp}
	intervalTable          = map[string]int{
		"C": 2,
		"D": 2,
		"E": 1,
		"F": 2,
		"G": 2,
		"A": 2,
		"B": 1,
	}
)

//type Accidental int

const (
	FlatAccidental int = iota + 1
	NaturalAccidental
	SharpAccidental
)

func flatted(tonic string) string {
	return fmt.Sprintf("%s%s", tonic, Flat)
}

func sharped(tonic string) string {
	return fmt.Sprintf("%s%s", tonic, Sharp)
}

var semitones = map[string][]string{
	"flat": {
		"C",
		flatted("D"),
		"D",
		flatted("E"),
		"E",
		//		flatted("F"),
		"F",
		flatted("G"),
		"G",
		flatted("A"),
		"A",
		flatted("B"),
		"B",
	},
	"sharp": {
		"C",
		sharped("C"),
		"D",
		sharped("D"),
		"E",
		sharped("E"),
		"F",
		sharped("F"),
		"G",
		sharped("G"),
		"A",
		sharped("A"),
		"B",
	},
}

var diatonicNotes = []string{"C", "D", "E", "F", "G", "A", "B"}
var scaleIntervals = map[string][]int{
	"major":           {2, 2, 1, 2, 2, 2, 1},
	"dorian":          {2, 1, 2, 2, 2, 1, 2},
	"phrygian":        {1, 2, 2, 2, 1, 2, 2},
	"lydian":          {2, 2, 2, 1, 2, 2, 1},
	"mixolydian":      {2, 2, 1, 2, 2, 1, 2},
	"locrian":         {1, 2, 2, 1, 2, 2, 2},
	"harmonicMinor":   {2, 1, 2, 2, 1, 3, 1},
	"melodicMinor":    {2, 1, 2, 2, 2, 2, 1}, // jazz minor
	"naturalMinor":    {2, 1, 2, 2, 1, 2, 2}, // Aeolian
	"alteredDominant": {1, 2, 1, 2, 2, 2, 2},
}

//scaleIntervals["ionian"] = scaleIntervals["major"]
//scaleIntervals["aeolian"] = scaleIntervals["natural_minor"]

// These are zero-based and depend on a scale being handed to them.
var secondaryScales = map[string]map[string]interface{}{
	"blues": {
		"dependsOn": "naturalMinor",
		"notes":     []int{0, 2, 3, 4, 4, 6},
	},
	"majorPentatonic": {
		"dependsOn": "major",
		"notes":     []int{0, 1, 2, 4, 5}, // 1, 2, 3, 5, 6 of major scale
	},
	"minorPentatonic": {
		"dependsOn": "naturalMinor",
		"notes":     []int{0, 2, 3, 4, 6}, // 1, b3, 4, 5, b7 of Aeolian (natural minor) scale
	},
}

var modes = map[string][]string{
	"major": {
		"Ionian",
		"Dorian",
		"Phrygian",
		"Lydian",
		"Mixolydian",
		"Aeolian",
		"Locrian",
	},
	"melodicMinor": {
		"Melodic minor",
		fmt.Sprintf("Dorian %s2 / Phrygian %s6", Flat, Sharp),
		fmt.Sprintf("Lydian augmented / Lydian %s5", Sharp),
		fmt.Sprintf("Lydian dominant / Lydian %s7", Flat),
		fmt.Sprintf("Mixolydian %s6", Flat),
		fmt.Sprintf("Locrian %s2 / Aeolian %s5", Sharp, Flat),
		"Super Locrian / altered dominant / altered",
	},
}

func GetModes(scale, tonic string, accidental int) map[string][]string {
	notes := GetScale(scale, tonic, accidental)
	modeNames := modes[scale]
	l := len(notes)

	m := make(map[string][]string, l)
	for i := range l {
		var targetScale []string
		targetScale = append(targetScale, notes[i:l]...)
		targetScale = append(targetScale, notes[0:i]...)
		k := modeNames[i]
		m[k] = targetScale
	}
	return m
	// return { modeNames[i]: notes[i:l] + notes[0:i] for i in range(l) }
}

func GetScale(scaleType, tonic string, accidental int) []string {
	tonic = strings.ToUpper(tonic)
	currentAccidental := accidentals[accidental]
	scale := []string{tonic}
	built := []string{fmt.Sprintf("%s%s", tonic, currentAccidental)}

	var secondaryScale map[string]interface{}
	var hasSecondaryScale bool
	if v, ok := secondaryScales[scaleType]; ok {
		secondaryScale = v
		if v, ok := secondaryScale["dependsOn"]; ok {
			scaleType = v.(string)
		}
		hasSecondaryScale = true
	}

	var intervalScale []int
	if v, ok := scaleIntervals[scaleType]; ok {
		intervalScale = v
	}

	// Don't get the first note because it's pushed onto the stack.
	idx := slices.Index(diatonicNotes, tonic)
	var targetScale []string
	targetScale = append(targetScale, diatonicNotes[idx+1:]...)
	targetScale = append(targetScale, diatonicNotes[:idx]...)

	for i, note := range targetScale {
		diatonicInterval := intervalTable[scale[i]]
		targetInterval := intervalScale[i]

		if targetInterval == diatonicInterval {
			built = append(built, fmt.Sprintf("%s%s", note, currentAccidental))
		} else if diatonicInterval != targetInterval {
			if diatonicInterval > targetInterval {
				accidental = accidental - diatonicInterval + targetInterval
			} else {
				accidental = accidental + targetInterval - diatonicInterval
			}
			currentAccidental = accidentals[accidental]
			built = append(built, fmt.Sprintf("%s%s", note, currentAccidental))
		}

		scale = append(scale, note)
	}

	if v, ok := secondaryScale["notes"]; ok && hasSecondaryScale {
		return getSecondaryScale(v.([]int), built)
	} else {
		return built
	}
}

func getSecondaryScale(notes []int, primaryScale []string) []string {
	s := make([]string, len(notes))
	for i, note := range notes {
		s[i] = primaryScale[note]
	}
	return s
}
