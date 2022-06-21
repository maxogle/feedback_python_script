from time import time
from click import help_option
import matplotlib
import numpy as np 
import librosa
import matplotlib.pyplot as plt
import seaborn as sns 
import parselmouth


y, sr = librosa.load('public/BowlingGreen.wav')

hop_length = 512 
y_harmonic, y_percussive = librosa.effects.hpss(y)

tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time")
print(beat_frames)
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)

maxima = librosa.feature.spectral_contrast(y=y, sr=sr, linear='true')


time_stamps = librosa.samples_to_time(maxima, sr=22050)

avg = abs(maxima.mean())

for i in maxima:
    for amp in i:
        if amp >= (avg * 10):
            print('event!', time_stamps)




