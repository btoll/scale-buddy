package scales_test

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("PentatonicScale", func() {
	var scale []string

	Describe("Major Pentatonic", func() {
		It("is correct for C Natural Major Pentatonic", func() {
			scale = []string{"C", "D", "E", "G", "A"}
			Expect(majorPentatonic("C")).To(Equal(scale))
		})

		It("is correct for C Flat Natural Major Pentatonic", func() {
			scale = []string{"C♭", "D♭", "E♭", "G♭", "A♭"}
			Expect(majorPentatonicFlat("C")).To(Equal(scale))
		})

		It("is correct for C Sharp Natural Major Pentatonic", func() {
			scale = []string{"C♯", "D♯", "E♯", "G♯", "A♯"}
			Expect(majorPentatonicSharp("C")).To(Equal(scale))
		})

		It("is correct for D Natural Major Pentatonic", func() {
			scale = []string{"D", "E", "F♯", "A", "B"}
			Expect(majorPentatonic("D")).To(Equal(scale))
		})

		It("is correct for D Flat Natural Major Pentatonic", func() {
			scale = []string{"D♭", "E♭", "F", "A♭", "B♭"}
			Expect(majorPentatonicFlat("D")).To(Equal(scale))
		})

		It("is correct for E Natural Major Pentatonic", func() {
			scale = []string{"E", "F♯", "G♯", "B", "C♯"}
			Expect(majorPentatonic("E")).To(Equal(scale))
		})

		It("is correct for E Flat Natural Major Pentatonic", func() {
			scale = []string{"E♭", "F", "G", "B♭", "C"}
			Expect(majorPentatonicFlat("E")).To(Equal(scale))
		})

		It("is correct for F Natural Major Pentatonic", func() {
			scale = []string{"F", "G", "A", "C", "D"}
			Expect(majorPentatonic("F")).To(Equal(scale))
		})

		It("is correct for F Sharp Natural Major Pentatonic", func() {
			scale = []string{"F♯", "G♯", "A♯", "C♯", "D♯"}
			Expect(majorPentatonicSharp("F")).To(Equal(scale))
		})

		It("is correct for G Natural Major Pentatonic", func() {
			scale = []string{"G", "A", "B", "D", "E"}
			Expect(majorPentatonic("G")).To(Equal(scale))
		})

		It("is correct for G Flat Natural Major Pentatonic", func() {
			scale = []string{"G♭", "A♭", "B♭", "D♭", "E♭"}
			Expect(majorPentatonicFlat("G")).To(Equal(scale))
		})

		It("is correct for A Natural Major Pentatonic", func() {
			scale = []string{"A", "B", "C♯", "E", "F♯"}
			Expect(majorPentatonic("A")).To(Equal(scale))
		})

		It("is correct for A Flat Natural Major Pentatonic", func() {
			scale = []string{"A♭", "B♭", "C", "E♭", "F"}
			Expect(majorPentatonicFlat("A")).To(Equal(scale))
		})

		It("is correct for B Natural Major Pentatonic", func() {
			scale = []string{"B", "C♯", "D♯", "F♯", "G♯"}
			Expect(majorPentatonic("B")).To(Equal(scale))
		})

		It("is correct for B Flat Natural Major Pentatonic", func() {
			scale = []string{"B♭", "C", "D", "F", "G"}
			Expect(majorPentatonicFlat("B")).To(Equal(scale))
		})
	})

	Describe("Minor Pentatonic", func() {
		It("is correct for C Natural Minor Pentatonic", func() {
			scale = []string{"C", "E♭", "F", "G", "B♭"}
			Expect(minorPentatonic("C")).To(Equal(scale))
		})

		It("is correct for C Flat Natural Minor Pentatonic", func() {
			scale = []string{"C♭", "E♭♭", "F♭", "G♭", "B♭♭"}
			Expect(minorPentatonicFlat("C")).To(Equal(scale))
		})

		It("is correct for C Sharp Natural Minor Pentatonic", func() {
			scale = []string{"C♯", "E", "F♯", "G♯", "B"}
			Expect(minorPentatonicSharp("C")).To(Equal(scale))
		})

		It("is correct for D Natural Minor Pentatonic", func() {
			scale = []string{"D", "F", "G", "A", "C"}
			Expect(minorPentatonic("D")).To(Equal(scale))
		})

		It("is correct for D Flat Natural Minor Pentatonic", func() {
			scale = []string{"D♭", "F♭", "G♭", "A♭", "C♭"}
			Expect(minorPentatonicFlat("D")).To(Equal(scale))
		})

		It("is correct for E Natural Minor Pentatonic", func() {
			scale = []string{"E", "G", "A", "B", "D"}
			Expect(minorPentatonic("E")).To(Equal(scale))
		})

		It("is correct for E Flat Natural Minor Pentatonic", func() {
			scale = []string{"E♭", "G♭", "A♭", "B♭", "D♭"}
			Expect(minorPentatonicFlat("E")).To(Equal(scale))
		})

		It("is correct for F Natural Minor Pentatonic", func() {
			scale = []string{"F", "A♭", "B♭", "C", "E♭"}
			Expect(minorPentatonic("F")).To(Equal(scale))
		})

		It("is correct for F Sharp Natural Minor Pentatonic", func() {
			scale = []string{"F♯", "A", "B", "C♯", "E"}
			Expect(minorPentatonicSharp("F")).To(Equal(scale))
		})

		It("is correct for G Natural Minor Pentatonic", func() {
			scale = []string{"G", "B♭", "C", "D", "F"}
			Expect(minorPentatonic("G")).To(Equal(scale))
		})

		It("is correct for G Flat Natural Minor Pentatonic", func() {
			scale = []string{"G♭", "B♭♭", "C♭", "D♭", "F♭"}
			Expect(minorPentatonicFlat("G")).To(Equal(scale))
		})

		It("is correct for A Natural Minor Pentatonic", func() {
			scale = []string{"A", "C", "D", "E", "G"}
			Expect(minorPentatonic("A")).To(Equal(scale))
		})

		It("is correct for A Flat Natural Minor Pentatonic", func() {
			scale = []string{"A♭", "C♭", "D♭", "E♭", "G♭"}
			Expect(minorPentatonicFlat("A")).To(Equal(scale))
		})

		It("is correct for B Natural Minor Pentatonic", func() {
			scale = []string{"B", "D", "E", "F♯", "A"}
			Expect(minorPentatonic("B")).To(Equal(scale))
		})

		It("is correct for B Flat Natural Minor Pentatonic", func() {
			scale = []string{"B♭", "D♭", "E♭", "F", "A♭"}
			Expect(minorPentatonicFlat("B")).To(Equal(scale))
		})
	})
})
