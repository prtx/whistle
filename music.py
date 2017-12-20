import scipy.io.wavfile as wav
import numpy as np


class Music():

    def __init__(self, file_name):
        self.file_name = file_name
        self.frame_rate, self.amplitude = wav.read(self.file_name)
        
        if type(self.amplitude[0]) == np.ndarray:
            self.amplitude = (self.amplitude[:,0] + self.amplitude[:,1])/2
   
    def __str__(self):
        info = (self.file_name, self.frame_rate, str(self.amplitude))
        return "Filename : %s\nFrame Rate : %d\nAmplitudes : %s" % info
