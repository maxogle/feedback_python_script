import parselmouth 

import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 


sns.set()
plt.rcParams['figure.dpi'] = 400
snd = parselmouth.Sound('public/BowlingGreen.wav')
plt.figure()
plt.plot(snd.xs(), snd.values.T)
plt.xlim([snd.xmin, snd.xmax])
plt.xlabel('time[s]')
plt.ylabel("amplitude")
plt.savefig('chart-6.png')
# plt.show()