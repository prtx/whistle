import math
from whistle.constants import NOTES


A4 = 440
C0 = A4 * math.pow(2, -4.75)
def freq_to_note(freq):
    half_steps = round(12 * math.log2(freq/C0))
    octave = half_steps // 12
    return NOTES[half_steps % 12] + str(octave)
