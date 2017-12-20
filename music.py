import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt


class Music():

    def __init__(self, file_name):
        self.file_name = file_name
        self.frame_rate, self.amplitude = wav.read(self.file_name)
        
        if type(self.amplitude[0]) == np.ndarray:
            self.amplitude = (self.amplitude[:,0] + self.amplitude[:,1])/2
   

    def __str__(self):
        info = (self.file_name, self.frame_rate, str(self.amplitude))
        return "Filename : %s\nFrame Rate : %d\nAmplitudes : %s" % info
    

    def plot(self):
        plt.clf()
        plt.plot(np.arange(0, len(self.amplitude))/self.frame_rate, self.amplitude)

        plt.title(self.file_name)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        
        plt.show()



if __name__ == '__main__':
    music = Music('G.wav')
    print(music)
    music.plot()
