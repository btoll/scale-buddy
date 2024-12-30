package scales_test

import (
	"testing"

	"github.com/btoll/scale-buddy/scales"
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func getScale(scaleType string) func(int) func(string) []string {
	return func(accidental int) func(string) []string {
		return func(tonic string) []string {
			return scales.GetScale(scaleType, tonic, accidental)
		}
	}
}

var getMajorScale = getScale("major")
var getMajorNaturalScale = getMajorScale(scales.NaturalAccidental)
var getMajorFlatScale = getMajorScale(scales.FlatAccidental)
var getMajorSharpScale = getMajorScale(scales.SharpAccidental)

func major(tonic string) []string      { return getMajorNaturalScale(tonic) }
func majorFlat(tonic string) []string  { return getMajorFlatScale(tonic) }
func majorSharp(tonic string) []string { return getMajorSharpScale(tonic) }

var getNaturalMinorScale = getScale("naturalMinor")
var getNaturalMinorNaturalScale = getNaturalMinorScale(scales.NaturalAccidental)
var getNaturalMinorFlatScale = getNaturalMinorScale(scales.FlatAccidental)
var getNaturalMinorSharpScale = getNaturalMinorScale(scales.SharpAccidental)

func naturalMinor(tonic string) []string      { return getNaturalMinorNaturalScale(tonic) }
func naturalMinorFlat(tonic string) []string  { return getNaturalMinorFlatScale(tonic) }
func naturalMinorSharp(tonic string) []string { return getNaturalMinorSharpScale(tonic) }

var getHarmonicMinorScale = getScale("harmonicMinor")
var getHarmonicMinorNaturalScale = getHarmonicMinorScale(scales.NaturalAccidental)
var getHarmonicMinorFlatScale = getHarmonicMinorScale(scales.FlatAccidental)
var getHarmonicMinorSharpScale = getHarmonicMinorScale(scales.SharpAccidental)

func harmonicMinor(tonic string) []string      { return getHarmonicMinorNaturalScale(tonic) }
func harmonicMinorFlat(tonic string) []string  { return getHarmonicMinorFlatScale(tonic) }
func harmonicMinorSharp(tonic string) []string { return getHarmonicMinorSharpScale(tonic) }

var getMelodicMinorScale = getScale("melodicMinor")
var getMelodicMinorNaturalScale = getMelodicMinorScale(scales.NaturalAccidental)
var getMelodicMinorFlatScale = getMelodicMinorScale(scales.FlatAccidental)
var getMelodicMinorSharpScale = getMelodicMinorScale(scales.SharpAccidental)

func melodicMinor(tonic string) []string      { return getMelodicMinorNaturalScale(tonic) }
func melodicMinorFlat(tonic string) []string  { return getMelodicMinorFlatScale(tonic) }
func melodicMinorSharp(tonic string) []string { return getMelodicMinorSharpScale(tonic) }

var getMajorPentatonicScale = getScale("majorPentatonic")
var getMajorPentatonicNaturalScale = getMajorPentatonicScale(scales.NaturalAccidental)
var getMajorPentatonicFlatScale = getMajorPentatonicScale(scales.FlatAccidental)
var getMajorPentatonicSharpScale = getMajorPentatonicScale(scales.SharpAccidental)

func majorPentatonic(tonic string) []string      { return getMajorPentatonicNaturalScale(tonic) }
func majorPentatonicFlat(tonic string) []string  { return getMajorPentatonicFlatScale(tonic) }
func majorPentatonicSharp(tonic string) []string { return getMajorPentatonicSharpScale(tonic) }

var getMinorPentatonicScale = getScale("minorPentatonic")
var getMinorPentatonicNaturalScale = getMinorPentatonicScale(scales.NaturalAccidental)
var getMinorPentatonicFlatScale = getMinorPentatonicScale(scales.FlatAccidental)
var getMinorPentatonicSharpScale = getMinorPentatonicScale(scales.SharpAccidental)

func minorPentatonic(tonic string) []string      { return getMinorPentatonicNaturalScale(tonic) }
func minorPentatonicFlat(tonic string) []string  { return getMinorPentatonicFlatScale(tonic) }
func minorPentatonicSharp(tonic string) []string { return getMinorPentatonicSharpScale(tonic) }

func TestScales(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Scales Suite")
}
