import re
import numpy as np
from scipy.signal import square

notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
octaves = ["3", "4", "5", "6", "7"]
duration = re.compile("^(\d+(?:\.\d+)?)")
pitch = re.compile("[{}|p]+[\d]*".format("|".join(notes))) 


def play_melody(melody, sample_freq=10.e3, bpm=50, amplitude=1):
    measure_duration = 4 * 60. / bpm #usually it's 4/4 measures
    output = np.zeros((0,))

    for note in melody:
        # regexp matching
        duration_match = duration.findall(note)
        pitch_match = pitch.findall(note)
        
        # duration 
        if len(duration_match) == 0:
            t_max = 1/4.
        else:
            t_max = 1/float(duration_match[0])
        if "." in pitch_match[0]:
            t_max *= 1.5
            pitch_match[0] = "".join(pitch_match[0].split("."))
        t_max = t_max * measure_duration

        # pitch
        if pitch_match[0] == 'p':
            freq = 0
        else:
            if pitch_match[0][-1] in octaves: # octave is known
                octave = octaves.index(pitch_match[0][-1]) + 4 
                note = pitch_match[0][:-1]
            else: # octave is not known
                octave = 5
                note = pitch_match[0]
            freq = 261.626 * 2 ** ((notes.index(note) / 12. + octave - 7))  
            
        # generate sound
        t = np.arange(0, t_max, 1/sample_freq)
        wave = amplitude * square(2 * np.pi * freq * t)
        
        # append to output
        output = np.hstack((output, wave))

    return output
