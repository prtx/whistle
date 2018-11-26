import os
import pyaudio
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io.wavfile as wavfile
import IPython

from whistle.note import (
    freq_to_note,
    compute_freq_domain,
    compute_notes,
    strongest_note,
)
from whistle.chord import compute_chord


class Music:
    def __init__(self, name, frame_rate, amplitude):
        self.name = name
        self.amplitude = amplitude
        if isinstance(self.amplitude[0], np.ndarray):
            self.amplitude = (self.amplitude[:, 0] + self.amplitude[:, 1]) / 2
        self.frame_rate = frame_rate

    def __repr__(self):
        return "Name: {}\nFrame Rate: {}Hz".format(self.name, self.frame_rate)

    def compute_freq_domain(self):
        return compute_freq_domain(self.amplitude, self.frame_rate)

    def waveform(self):
        time = np.arange(0, len(self.amplitude)) / self.frame_rate

        plt.clf()
        plt.plot(time, self.amplitude)
        plt.title(self.name)
        plt.xlabel("Time (sec)")
        plt.ylabel("Amplitude")
        plt.show()

    def frequency_domain(self):
        freqs, spectre = self.compute_freq_domain()

        plt.clf()
        plt.plot(freqs, spectre)
        plt.title(self.name)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.show()

    def spectogram(self):
        plt.specgram(self.amplitude, Fs=self.frame_rate)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()

    def ipyplay(self):
        IPython.display.Audio(data=self.amplitude, rate=self.frame_rate)

    def notes(self):
        freqs, spectre = self.compute_freq_domain()
        return compute_notes(freqs)

    def strongest_note(self):
        freqs, spectre = self.compute_freq_domain()
        return strongest_note(freqs, spectre)

    def chord(self):
        freqs, spectre = self.compute_freq_domain()
        return compute_chord(freqs, spectre)


class MusicFile(Music):
    def __init__(self, file_path, name=None):
        self.file_name = os.path.basename(file_path)
        frame_rate, amplitude = wavfile.read(file_path)
        super().__init__(name or self.file_name.split(".")[0], frame_rate, amplitude)

    def __repr__(self):
        return (
            "Name: {}\n"
            "File name: {}\n"
            "Frame Rate: {}Hz".format(self.name, self.file_name, self.frame_rate)
        )
