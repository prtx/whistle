import os
import pyaudio
import pylab
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpack


class Music:
    def __init__(self, frame_rate, amplitude):
        self.amplitude = amplitude
        if isinstance(self.amplitude[0], np.ndarray):
            self.amplitude = (self.amplitude[:,0] + self.amplitude[:,1])/2
        self.frame_rate = frame_rate


    def __repr__(self):
        return "Frame Rate: {}Hz".format(self.frame_rate)


    def waveform(self):
        plt.clf()
        time = np.arange(0, len(self.amplitude))/self.frame_rate
        plt.plot(time, self.amplitude)

        plt.title(self.file_name)
        plt.xlabel("Time (sec)")
        plt.ylabel("Amplitude")
        
        plt.show()


class MusicFile(Music):
    def __init__(self, file_path):
        self.file_name = os.path.basename(file_path)
        frame_rate, amplitude = wavfile.read(file_path)
        super().__init__(frame_rate, amplitude)


    def __repr__(self):
        return (
            "File name: {}\n"
            "Frame Rate: {}Hz"
            .format(self.file_name, self.frame_rate)
        )