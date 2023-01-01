import librosa
import soundfile
import numpy as np
import math



def main():


    audio, sr = librosa.core.load("mt.wav", sr=44100)
    fir, sr = librosa.core.load("clap.wav", sr=44100)
    for i in range(len(fir)):
        fir[i]=fir[i]

    processed = []



    processed = np.convolve(audio, fir)

    soundfile.write('reverbclap.wav', processed, 44100)


if __name__ == "__main__" :
    main()
   