import soundfile as sf
import numpy as np

soundfile = "public/BowlingGreen.wav"

data, samplerate = sf.read(soundfile)

root_mean_square = [np.sqrt(np.mean(block**2))for block in sf.blocks(soundfile, blocksize=1024, overlap=512)]

avg = sum(root_mean_square) / len(root_mean_square)

clipnum = 1
clipnum2 = 1

for i in root_mean_square:
    if i >= (avg * 19):
        start = i - 10_000
        end = i + 10_000
        clipname = f"{soundfile}loud{clipnum}.wav"
        # sf.write(clipname, [start, end], 44100, 'PCM_24')
        clipnum = clipnum+1
        print(f"event! {i}")
    elif i <= (avg * 0.001):
        start = i - 10_000
        end = i + 10_000
        clipname = f"{soundfile}quiet{clipnum2}.wav"
        # sf.write(clipname, [start, end], 44100, 'PCM_24')
        clipnum2 = clipnum2+1
        print(f"quiet event! {i}")
