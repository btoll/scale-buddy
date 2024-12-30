package scales_test

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("MinorScale", func() {
	var scale []string

	Describe("Natural Minor", func() {
		It("is correct for C Natural Minor", func() {
			scale = []string{"C", "D", "E♭", "F", "G", "A♭", "B♭"}
			Expect(naturalMinor("C")).To(Equal(scale))
		})

		It("is correct for C Flat Natural Minor", func() {
			scale = []string{"C♭", "D♭", "E♭♭", "F♭", "G♭", "A♭♭", "B♭♭"}
			Expect(naturalMinorFlat("C")).To(Equal(scale))
		})

		It("is correct for C Sharp Natural Minor", func() {
			scale = []string{"C♯", "D♯", "E", "F♯", "G♯", "A", "B"}
			Expect(naturalMinorSharp("C")).To(Equal(scale))
		})

		It("is correct for D Natural Minor", func() {
			scale = []string{"D", "E", "F", "G", "A", "B♭", "C"}
			Expect(naturalMinor("D")).To(Equal(scale))
		})

		It("is correct for D Flat Natural Minor", func() {
			scale = []string{"D♭", "E♭", "F♭", "G♭", "A♭", "B♭♭", "C♭"}
			Expect(naturalMinorFlat("D")).To(Equal(scale))
		})

		It("is correct for E Natural Minor", func() {
			scale = []string{"E", "F♯", "G", "A", "B", "C", "D"}
			Expect(naturalMinor("E")).To(Equal(scale))
		})

		It("is correct for E Flat Natural Minor", func() {
			scale = []string{"E♭", "F", "G♭", "A♭", "B♭", "C♭", "D♭"}
			Expect(naturalMinorFlat("E")).To(Equal(scale))
		})

		It("is correct for F Natural Minor", func() {
			scale = []string{"F", "G", "A♭", "B♭", "C", "D♭", "E♭"}
			Expect(naturalMinor("F")).To(Equal(scale))
		})

		It("is correct for F Sharp Natural Minor", func() {
			scale = []string{"F♯", "G♯", "A", "B", "C♯", "D", "E"}
			Expect(naturalMinorSharp("F")).To(Equal(scale))
		})

		It("is correct for G Natural Minor", func() {
			scale = []string{"G", "A", "B♭", "C", "D", "E♭", "F"}
			Expect(naturalMinor("G")).To(Equal(scale))
		})

		It("is correct for G Flat Natural Minor", func() {
			scale = []string{"G♭", "A♭", "B♭♭", "C♭", "D♭", "E♭♭", "F♭"}
			Expect(naturalMinorFlat("G")).To(Equal(scale))
		})

		It("is correct for A Natural Minor", func() {
			scale = []string{"A", "B", "C", "D", "E", "F", "G"}
			Expect(naturalMinor("A")).To(Equal(scale))
		})

		It("is correct for A Flat Natural Minor", func() {
			scale = []string{"A♭", "B♭", "C♭", "D♭", "E♭", "F♭", "G♭"}
			Expect(naturalMinorFlat("A")).To(Equal(scale))
		})

		It("is correct for B Natural Minor", func() {
			scale = []string{"B", "C♯", "D", "E", "F♯", "G", "A"}
			Expect(naturalMinor("B")).To(Equal(scale))
		})

		It("is correct for B Flat Natural Minor", func() {
			scale = []string{"B♭", "C", "D♭", "E♭", "F", "G♭", "A♭"}
			Expect(naturalMinorFlat("B")).To(Equal(scale))
		})
	})

	Describe("Harmonic Minor", func() {
		It("is correct for C Harmonic Minor", func() {
			scale = []string{"C", "D", "E♭", "F", "G", "A♭", "B"}
			Expect(harmonicMinor("C")).To(Equal(scale))
		})

		It("is correct for C Flat Harmonic Minor", func() {
			scale = []string{"C♭", "D♭", "E♭♭", "F♭", "G♭", "A♭♭", "B♭"}
			Expect(harmonicMinorFlat("C")).To(Equal(scale))
		})

		It("is correct for C Sharp Harmonic Minor", func() {
			scale = []string{"C♯", "D♯", "E", "F♯", "G♯", "A", "B♯"}
			Expect(harmonicMinorSharp("C")).To(Equal(scale))
		})

		It("is correct for D Harmonic Minor", func() {
			scale = []string{"D", "E", "F", "G", "A", "B♭", "C♯"}
			Expect(harmonicMinor("D")).To(Equal(scale))
		})

		It("is correct for D Flat Harmonic Minor", func() {
			scale = []string{"D♭", "E♭", "F♭", "G♭", "A♭", "B♭♭", "C"}
			Expect(harmonicMinorFlat("D")).To(Equal(scale))
		})

		It("is correct for E Harmonic Minor", func() {
			scale = []string{"E", "F♯", "G", "A", "B", "C", "D♯"}
			Expect(harmonicMinor("E")).To(Equal(scale))
		})

		It("is correct for E Flat Harmonic Minor", func() {
			scale = []string{"E♭", "F", "G♭", "A♭", "B♭", "C♭", "D"}
			Expect(harmonicMinorFlat("E")).To(Equal(scale))
		})

		It("is correct for F Harmonic Minor", func() {
			scale = []string{"F", "G", "A♭", "B♭", "C", "D♭", "E"}
			Expect(harmonicMinor("F")).To(Equal(scale))
		})

		It("is correct for F Sharp Harmonic Minor", func() {
			scale = []string{"F♯", "G♯", "A", "B", "C♯", "D", "E♯"}
			Expect(harmonicMinorSharp("F")).To(Equal(scale))
		})

		It("is correct for G Harmonic Minor", func() {
			scale = []string{"G", "A", "B♭", "C", "D", "E♭", "F♯"}
			Expect(harmonicMinor("G")).To(Equal(scale))
		})

		It("is correct for G Flat Harmonic Minor", func() {
			scale = []string{"G♭", "A♭", "B♭♭", "C♭", "D♭", "E♭♭", "F"}
			Expect(harmonicMinorFlat("G")).To(Equal(scale))
		})

		It("is correct for A Harmonic Minor", func() {
			scale = []string{"A", "B", "C", "D", "E", "F", "G♯"}
			Expect(harmonicMinor("A")).To(Equal(scale))
		})

		It("is correct for A Flat Harmonic Minor", func() {
			scale = []string{"A♭", "B♭", "C♭", "D♭", "E♭", "F♭", "G"}
			Expect(harmonicMinorFlat("A")).To(Equal(scale))
		})

		It("is correct for B Harmonic Minor", func() {
			scale = []string{"B", "C♯", "D", "E", "F♯", "G", "A♯"}
			Expect(harmonicMinor("B")).To(Equal(scale))
		})

		It("is correct for B Flat Harmonic Minor", func() {
			scale = []string{"B♭", "C", "D♭", "E♭", "F", "G♭", "A"}
			Expect(harmonicMinorFlat("B")).To(Equal(scale))
		})
	})

	Describe("Melodic Minor", func() {
		It("is correct for C Melodic Minor", func() {
			scale = []string{"C", "D", "E♭", "F", "G", "A", "B"}
			Expect(melodicMinor("C")).To(Equal(scale))
		})

		It("is correct for C Flat Melodic Minor", func() {
			scale = []string{"C♭", "D♭", "E♭♭", "F♭", "G♭", "A♭", "B♭"}
			Expect(melodicMinorFlat("C")).To(Equal(scale))
		})

		It("is correct for C Sharp Melodic Minor", func() {
			scale = []string{"C♯", "D♯", "E", "F♯", "G♯", "A♯", "B♯"}
			Expect(melodicMinorSharp("C")).To(Equal(scale))
		})

		It("is correct for D Melodic Minor", func() {
			scale = []string{"D", "E", "F", "G", "A", "B", "C♯"}
			Expect(melodicMinor("D")).To(Equal(scale))
		})

		It("is correct for D Flat Melodic Minor", func() {
			scale = []string{"D♭", "E♭", "F♭", "G♭", "A♭", "B♭", "C"}
			Expect(melodicMinorFlat("D")).To(Equal(scale))
		})

		It("is correct for E Melodic Minor", func() {
			scale = []string{"E", "F♯", "G", "A", "B", "C♯", "D♯"}
			Expect(melodicMinor("E")).To(Equal(scale))
		})

		It("is correct for E Flat Melodic Minor", func() {
			scale = []string{"E♭", "F", "G♭", "A♭", "B♭", "C", "D"}
			Expect(melodicMinorFlat("E")).To(Equal(scale))
		})

		It("is correct for F Melodic Minor", func() {
			scale = []string{"F", "G", "A♭", "B♭", "C", "D", "E"}
			Expect(melodicMinor("F")).To(Equal(scale))
		})

		It("is correct for F Sharp Melodic Minor", func() {
			scale = []string{"F♯", "G♯", "A", "B", "C♯", "D♯", "E♯"}
			Expect(melodicMinorSharp("F")).To(Equal(scale))
		})

		It("is correct for G Melodic Minor", func() {
			scale = []string{"G", "A", "B♭", "C", "D", "E", "F♯"}
			Expect(melodicMinor("G")).To(Equal(scale))
		})

		It("is correct for G Flat Melodic Minor", func() {
			scale = []string{"G♭", "A♭", "B♭♭", "C♭", "D♭", "E♭", "F"}
			Expect(melodicMinorFlat("G")).To(Equal(scale))
		})

		It("is correct for A Melodic Minor", func() {
			scale = []string{"A", "B", "C", "D", "E", "F♯", "G♯"}
			Expect(melodicMinor("A")).To(Equal(scale))
		})

		It("is correct for A Flat Melodic Minor", func() {
			scale = []string{"A♭", "B♭", "C♭", "D♭", "E♭", "F", "G"}
			Expect(melodicMinorFlat("A")).To(Equal(scale))
		})

		It("is correct for B Melodic Minor", func() {
			scale = []string{"B", "C♯", "D", "E", "F♯", "G♯", "A♯"}
			Expect(melodicMinor("B")).To(Equal(scale))
		})

		It("is correct for B Flat Melodic Minor", func() {
			scale = []string{"B♭", "C", "D♭", "E♭", "F", "G", "A"}
			Expect(melodicMinorFlat("B")).To(Equal(scale))
		})
	})
})
