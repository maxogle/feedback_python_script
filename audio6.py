import soundfile as sf
import numpy as np

soundfile = "public/BowlingGreen.wav"
print(sf.info(soundfile))
data, samplerate = sf.read(soundfile)

root_mean_square = [np.sqrt(np.mean(block**2))for block in sf.blocks(soundfile, blocksize=1024, overlap=512)]

avg = abs(sum(root_mean_square)) / len(root_mean_square)

clipnum = 1
clipnum2 = 1

current_idx = 0 
for idx, i in enumerate(root_mean_square):
    if idx <= current_idx + 25:
        continue
    elif i >= (avg * 1.5):
        start = float(idx - 50)
        end = idx + 50
        clipname = f"{soundfile}loud{clipnum}.wav"
        sf.write(clipname, [start, end], 44100, 'PCM_16')
        clipnum = clipnum+1
        print(f'event! {(idx, i)}')
        current_idx = idx
    elif i <= (avg * 0.001):
        start = float(idx - 50)
        end = idx + 50
        clipname = f"{soundfile}quiet{clipnum2}.wav"
        sf.write(clipname, [start, end], 44100, 'PCM_16')
        clipnum2 = clipnum2+1
        print(f"quiet event! {(idx, i)}")
        current_idx = idx
