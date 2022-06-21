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

# mfcc_delta = librosa.feature.delta(mfcc)

maxima = librosa.feature.spectral_contrast(y=y, sr=sr, linear='true')

# beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]), beat_frames)

chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

# beat_chroma = librosa.util.sync(chromagram, beat_frames, aggregate=np.median)

time_stamps = librosa.samples_to_time(maxima, sr=sr)

formatted_time_stamp = np.round(time_stamps, 2)
# beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

print(sr)
avg = abs(maxima.mean()) 

# print(beat_features)
print(avg)







"{:.2f}"
        # Michael function using pysoundfile set data to and array and set a buffer of +- 10_000 and create a clip from that value
            # for i, d in enumerate(data):
            #     for sfx in d:
            #         if sfx >= 0.4:
            #             print(f'HIGH VOL: {sfx} at {i}')
for i in maxima:
    for amp in i:
        
        if amp >= (avg * 10):
            print('event!', [float(ts) for ts in time_stamps[0]])
        # elif amp <= (avg * 0.5):
            # print('quiet event!', formatted_time_stamp)





