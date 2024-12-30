package scales_test

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("MajorScale", func() {
	var scale []string

	It("is correct for C Major", func() {
		scale = []string{"C", "D", "E", "F", "G", "A", "B"}
		Expect(major("C")).To(Equal(scale))
	})

	It("is correct for C Flat Major", func() {
		scale = []string{"C♭", "D♭", "E♭", "F♭", "G♭", "A♭", "B♭"}
		Expect(majorFlat("C")).To(Equal(scale))
	})

	It("is correct for C Sharp Major", func() {
		scale = []string{"C♯", "D♯", "E♯", "F♯", "G♯", "A♯", "B♯"}
		Expect(majorSharp("C")).To(Equal(scale))
	})

	It("is correct for D Major", func() {
		scale = []string{"D", "E", "F♯", "G", "A", "B", "C♯"}
		Expect(major("D")).To(Equal(scale))
	})

	It("is correct for D Flat Major", func() {
		scale = []string{"D♭", "E♭", "F", "G♭", "A♭", "B♭", "C"}
		Expect(majorFlat("D")).To(Equal(scale))
	})

	It("is correct for E Major", func() {
		scale = []string{"E", "F♯", "G♯", "A", "B", "C♯", "D♯"}
		Expect(major("E")).To(Equal(scale))
	})

	It("is correct for E Flat Major", func() {
		scale = []string{"E♭", "F", "G", "A♭", "B♭", "C", "D"}
		Expect(majorFlat("E")).To(Equal(scale))
	})

	It("is correct for F Major", func() {
		scale = []string{"F", "G", "A", "B♭", "C", "D", "E"}
		Expect(major("F")).To(Equal(scale))
	})

	It("is correct for F Sharp Major", func() {
		scale = []string{"F♯", "G♯", "A♯", "B", "C♯", "D♯", "E♯"}
		Expect(majorSharp("F")).To(Equal(scale))
	})

	It("is correct for G Major", func() {
		scale = []string{"G", "A", "B", "C", "D", "E", "F♯"}
		Expect(major("G")).To(Equal(scale))
	})

	It("is correct for G Flat Major", func() {
		scale = []string{"G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F"}
		Expect(majorFlat("G")).To(Equal(scale))
	})

	It("is correct for A Major", func() {
		scale = []string{"A", "B", "C♯", "D", "E", "F♯", "G♯"}
		Expect(major("A")).To(Equal(scale))
	})

	It("is correct for A Flat Major", func() {
		scale = []string{"A♭", "B♭", "C", "D♭", "E♭", "F", "G"}
		Expect(majorFlat("A")).To(Equal(scale))
	})

	It("is correct for B Major", func() {
		scale = []string{"B", "C♯", "D♯", "E", "F♯", "G♯", "A♯"}
		Expect(major("B")).To(Equal(scale))
	})

	It("is correct for B Flat Major", func() {
		scale = []string{"B♭", "C", "D", "E♭", "F", "G", "A"}
		Expect(majorFlat("B")).To(Equal(scale))
	})
})
