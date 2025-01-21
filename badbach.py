import random
import mingus.core.intervals as intervals
from mingus.containers import Track, Composition, Note
from mingus.midi import midi_file_out

allowed_intervals = [
    "minor third",
    "major third",
    "perfect fifth",
    "minor sixth",
    "major sixth",
    "major unison",
]


def next_note(cpprev, mprev, mcur):
    candidates = [
        Note("A"),
        Note("B"),
        Note("C"),
        Note("D"),
        Note("E"),
        Note("F"),
        Note("G"),
    ]

    # Rule 1: No harmonic invervals are consonances.
    candidates = filter(
        lambda x: intervals.determine(cpprev.name, x.name) not in allowed_intervals,
        candidates,
    )

    cpcur = random.choice(list(candidates))

    return cpcur


def create_counterpoint(melody):
    # A melody is made up of bars, and each note object is a list whose third element is the name.
    cp = Track()
    prev = melody[0][0][2]
    cp.add_notes(prev)
    for bar_i in range(len(melody)):
        for note_i in range(len(melody[bar_i])):
            if bar_i == 0 and note_i == 0:
                continue
            cp.add_notes(
                next_note(Note(cp[-1][-1][2][0]), prev, melody[bar_i][note_i][2])
            )
            prev = melody[bar_i][note_i][2]

    return cp


def create_melody():
    melody = ["C", "D", "E", "F", "G", "F", "E", "D", "C"]
    t = Track()
    for n in melody:
        t.add_notes(n)
    return t


def tracks_to_composition(lst):
    c = Composition()
    for l in lst:
        c.add_track(l)
    return c


def main():
    melody = create_melody()
    cp = create_counterpoint(melody)
    c = tracks_to_composition([melody, cp])
    print(c)
    midi_file_out.write_Composition("test.mid", c)


if __name__ == "__main__":
    main()
