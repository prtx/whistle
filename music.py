import scipy.io.wavfile as wav
import numpy as np


def read_music(file_name):
    frame_rate, amplitude = wav.read(file_name)
    if type(amplitude[0]) == 'numpy.ndarray':
        amplitude = amplitude[:,0] + amplitude[:,1]

    print(frame_rate)
    print(amplitude)
