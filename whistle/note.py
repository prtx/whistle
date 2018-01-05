import math


NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class Note:
    def __init__(self, note, octave):
        self.note = note
        self.octave = octave
    

    def __repr__(self):
        return "{}{}".format(self.note, self.octave)


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
