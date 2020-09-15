import numpy as np
import matplotlib.pyplot as plt
import sckits.audiolab as al

file_path = "~/Downloads/ダウンロード.wav"
wr = wave.open(wavf, "r")
data, sampling_rate, fmt = al.wavread(file_path)


#フーリエ変換のための準備
# 周波数成分にわける（短時間フーリエ変換）


nfft = 1024
#FFTの時のサイズ
overlap =nfft // 2
#オーバーラップする範囲
frame_length = data.shape[0]

time_song = float(frame_length) / fs
time_unit = 1.0 / float(fs)

start = (nfft // 2) * time_unit
stop = time_song
step = (nfft - overlap) * time_unit
time_ruler = np.arange(start, stop, step)


window = np.hamming(nfft)
spec = np.zeros([len(time_ruler), int(nfft)], dtype=np.complex)
pos = 0

#フーリエ変換の実行
for fft_index in range(len(time_ruler)):
    frame = data[pos:pos+nfft]
    if len(frame) == nfft:
        #windowed = window * frame
        windowed = frame 
        #窓関数をかけるとうまく書き戻せないのでかけないことにした
        fft_result = np.fft.fft(windowed)
        for i in range(len(spec[fft_index])):
            spec[fft_index][i] = fft_result[i]
        pos += int(nfft - overlap)

N = 100
#適当なフレームを選択
x = np.arange(0, fs, fs/len(spec[N]))
y = np.abs(spec[N])
plt.plot(x, y)
plt.show()