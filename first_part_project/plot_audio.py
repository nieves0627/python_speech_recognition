import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("audio_file_one_channel_44100.wav", "rb")

sample_freq = obj.getframerate()  # Muestras por segundos(44100)
n_samples = obj.getnframes()  # Numero de muestras en total (382693)
signal_wave = obj.readframes(-1)  # Lee las muestras 

obj.close()

time_audio = n_samples / sample_freq  # Tiempo de audio (8.6 seg)
print(time_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)  # Eje y. Cada muestra es de 2 bytes (en total hay 765386 bytes en todo el audio/765 kilobytes)

times = np.linspace(0, time_audio, num=n_samples)  # Eje x

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, time_audio)
plt.show()
