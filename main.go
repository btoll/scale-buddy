package main

import (
	"flag"
	"fmt"
	"strings"

	"github.com/btoll/scale-buddy/scales"
)

// https://en.wikipedia.org/wiki/Jazz_scale#Modes_of_the_melodic_minor_scale
// https://en.wikipedia.org/wiki/Minor_scale#Modes_of_harmonic_minor_scale
// https://en.wikipedia.org/wiki/Jazz_minor_scale
// https://www.jazzguitar.be/blog/melodic-minor-modes/

var (
	delimiter      string
	flat           bool
	sharp          bool
	tonic          string
	verbose        bool
	withMinor      bool
	withPentatonic bool
)

// TODO: Me no likey.
func getAccidental() string {
	if flat {
		return scales.Flat
	} else if sharp {
		return scales.Sharp
	} else {
		return ""
	}
}

//#def display_key_string():
//#    if not args.flat and not args.sharp:
//#        return ""
//#    else:
//#        return get_accidental()

func main() {
	flag.StringVar(&delimiter, "delimiter", "", "The symbol that separates the notes")
	flag.BoolVar(&flat, "flat", false, "Flat")
	flag.BoolVar(&sharp, "sharp", false, "Sharp")
	flag.StringVar(&tonic, "tonic", "", "The tonic note of the scale")
	flag.BoolVar(&verbose, "verbose", false, "Add extra information")
	flag.BoolVar(&withMinor, "withMinor", false, "Include minor scales")
	flag.BoolVar(&withPentatonic, "withPentatonic", false, "Include pentatonic scales")
	flag.Parse()

	//	var hasAccidental bool
	//	if flat || sharp {
	//		hasAccidental = true
	//	}

	tonic = strings.ToUpper(tonic)

	var accidental int
	if sharp {
		accidental = scales.SharpAccidental
	} else if flat {
		accidental = scales.FlatAccidental
	} else {
		accidental = scales.NaturalAccidental
	}
	majorScale := scales.GetScale("major", tonic, accidental)
	fmt.Println("majorScale", majorScale)
	for name, mode := range scales.GetModes("major", tonic, accidental) {
		fmt.Printf("%42s: %s\n", name, mode)
	}
	for name, mode := range scales.GetModes("melodicMinor", tonic, accidental) {
		fmt.Printf("%42s: %s\n", name, mode)
	}
	if withMinor {
		s := fmt.Sprintf("\n%s%s", tonic, getAccidental())
		fmt.Print(
			fmt.Sprintf("%s natural minor (Aeolian): %s%s\n",
				s,
				delimiter,
				scales.GetScale("naturalMinor", tonic, accidental)))
		fmt.Print(
			fmt.Sprintf("%s harmonic minor: %s%s\n",
				s,
				delimiter,
				scales.GetScale("harmonicMinor", tonic, accidental)))
		fmt.Print(
			fmt.Sprintf("%s melodic minor (jazz minor): %s%s\n",
				s,
				delimiter,
				scales.GetScale("melodicMinor", tonic, accidental)))
	}
	if withPentatonic {
		s := fmt.Sprintf("\n%s%s", tonic, getAccidental())
		fmt.Print(
			fmt.Sprintf("%s major pentatonic: %s%s\n",
				s,
				delimiter,
				scales.GetScale("majorPentatonic", tonic, accidental)))
		fmt.Print(
			fmt.Sprintf("%s minor pentatonic: %s%s\n",
				s,
				delimiter,
				scales.GetScale("minorPentatonic", tonic, accidental)))
	}
}
