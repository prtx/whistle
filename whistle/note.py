import math


NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class NoteException(Exception):
    pass


class Note:
    def __init__(self, note, octave):
        if note not in NOTES:
            raise NoteException("{} is not a notation.".format(note))
        if not isinstance(octave, int):
            raise NoteException("Octace should be an integer.")

        self._note = note
        self._octave = octave
    

    @property
    def note(self):
        return self._note


    @property
    def octave(self):
        return self._octave


    def __repr__(self):
        return "{}{}".format(self._note, self._octave)


A4 = 440
C0 = A4 * math.pow(2, -4.75)
def freq_to_note(freq):
    half_steps = round(12 * math.log2(freq/C0))
    octave = half_steps // 12
    return Note(NOTES[half_steps % 12], octave)


def strongest_note(freqs, spectre):
    d = dict()
    for f, m in zip(freqs, spectre):
        note = freq_to_note(f)
        if note not in d:
            d[note] = float()
        d[note] += m
    return max(d, key=d.get)
