from time import time
from click import help_option
import matplotlib
import numpy as np 
import librosa
import matplotlib.pyplot as plt
import seaborn as sns 
import parselmouth


y, sr = librosa.load('public/Bodequita.wav')

hop_length= 512
x_time = librosa.effects.time_stretch()

