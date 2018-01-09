from whistle.note import NOTES, compute_notes


CHORD_DICTIONARY = {
    "maj": [0, 4, 7],
    "m": [0, 3, 7],
    "7": [0, 4, 7, 10],
    "maj7": [0, 4, 7, 11],
    "m7": [0, 3, 7, 10],
    "9": [0, 2, 4, 7, 9],
    "dim": [0, 3, 6],
    "sus": [0, 5, 7],
    # ["smthng remaining here", [0, 5, 7]],
    "add9": [0, 2, 4, 6],
}


class Chord:
    def __init__(self, note, chord_type):
        if note not in NOTES:
            raise NoteException("{} is not a notation.".format(note))
        if chord_type not in CHORD_DICTIONARY:
            raise NoteException("{} is not a chord.".format(chord_type))
        self._note = note
        self._chord_type = chord_type

    @property
    def note(self):
        return self._note

    @property
    def chord_type(self):
        return self._chord_type

    def __repr__(self):
        return "{}{}".format(self._note, self._chord_type)


def note_combination(note, chord_type):
    note_index = NOTES.index(note)
    chord_notes = []
    for key in CHORD_DICTIONARY[chord_type]:
        chord_notes.append(NOTES[(note_index + key) % 12])
    return chord_notes


def compute_chord(freqs, spectre):
    chord_strength = {}
    notes = compute_notes(freqs)

    for note in NOTES:
        for chord_type, chord_keys in CHORD_DICTIONARY.items():
            chord_notes = note_combination(note, chord_type)
            n = len(chord_keys)

            chord_magnitude = 0.0
            for note_obj, magnitude in zip(notes, spectre):
                if note_obj.note in chord_notes:
                    chord_magnitude += magnitude
            chord_strength[Chord(note, chord_type)] = chord_magnitude / n

    return max(chord_strength, key=chord_strength.get)
