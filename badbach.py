import random
import mingus.core.intervals as intervals
from mingus.containers import Track, Composition, Note
from mingus.midi import midi_file_out

perfect_intervals = [
    "perfect fifth",
    "major unison",
]

allowed_intervals = [
    "minor third",
    "major third",
    "minor sixth",
    "major sixth",
] + perfect_intervals

weight_delta = 10


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
    weights = [100 // len(candidates)] * len(candidates)

    for i in range(len(candidates)):
        # Rule 1: No harmonic invervals are consonances.
        if (
            intervals.determine(cpprev.name, candidates[i].name)
            not in allowed_intervals
        ):
            weights[i] += weight_delta
        # Rule 2: Parallel perfect intervals are forbidden.
        if intervals.determine(mprev.name, mcur.name) in perfect_intervals:
            weights[i] += weight_delta

    cpcur = random.choices(list(candidates), weights=weights)

    return cpcur


def create_counterpoint(melody):
    # A melody is made up of bars, and each note object is a list whose third element is a list of names.
    cp = Track()
    prev = melody[0][0][2][0]
    cp.add_notes(prev)
    for bar_i in range(len(melody)):
        for note_i in range(len(melody[bar_i])):
            if bar_i == 0 and note_i == 0:
                continue
            cp.add_notes(
                next_note(
                    Note(cp[-1][-1][2][0]),
                    Note(prev),
                    Note(melody[bar_i][note_i][2][0]),
                )
            )
            prev = melody[bar_i][note_i][2][0]

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
