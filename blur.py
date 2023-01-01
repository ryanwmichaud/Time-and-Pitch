import librosa
import soundfile
import numpy as np
import math


def gaussian(x, a, b, c): #peak height, position of the peak, standard deviation
    
    exp_n = (x-b)**2
    exp_d = 2*(c**2)
    exp = -(exp_n/exp_d)
    return (a*math.e)**exp

def gaussian2(x, mu, sigma): #x value of mean, standard deviation
    n = (x-mu)**2
    d = (sigma**2)
    exp = 1/2  * (n/d)
    b= 1/(sigma * math.sqrt(2*math.pi))
    return b**exp

def main():

    audio, sr = librosa.core.load("mt.wav", sr=44100)
    processed = []
    l = []

    print("window length (samples): ",end='')
    len = int(input())
    print("standard deviation: ",end='')
    sd = int(input())

    for i in range(len):
        l.append(gaussian2(i,len/2,sd))
    print(l)

    sum = np.sum(l)
    print(sum)

    for i in range(len):
        l[i] = l[i]/sum
    print(l)

    sum = np.sum(l)
    print(sum)

    processed = np.convolve(audio, l)

    soundfile.write('gaussian.wav', processed, 44100)


if __name__ == "__main__" :
    main()
   