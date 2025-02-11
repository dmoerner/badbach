# BadBach

Bad Bach is a crude attempt to produce "bad" first-species counterpoint which
deliberately breaks the counterpoint rules. It uses the library
https://bspaans.github.io/python-mingus.

The rules for First-Species Counterpoint (*Graduate Review of Tonal Theory*, p.
28):

1. All harmonic intervals must be consonances (P8, P5, P1, M3, m3, M6, m6).
2. Parallel perfect intervals are forbidden.
3. Direct fifths and octaves are forbidden except when the soprano voice moves
   by a step.
4. Lower voice must begin on 1, upper voice can be begin on 1, 3, or 5. Both
   voices end on 1.
5. Unisons are allowed only at the beginning and end.
6. In minor keys, raise 6 and 7 only if they immediately precede the cadence.

# Features and Roadmap:

Implemented:

- Non-deterministic music generation which prefers counterpoint lines which
  violate the first five rules of first species counterpoint. (The sixth rule
  applies to minor keys, which are not
  implemented.)
- Melody composition with `create_melody` function, which takes a list of
  notes, each of which is expressed as a string.

Roadmap, not implemented:

- Support for accidentals and keys other than major C.
- Support for rhythm and higher-species counterpoint.
- UI for composing or importing melodies.

# Demo

https://moerner.com/awful-twinkle.html
