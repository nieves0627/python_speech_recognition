import wave
import matplotlib.pyplot as plt
import numpy as np

def get_audio_params(input_path):
    # Cambie wave. open a utilizar context managers
    obj = wave.open(input_path, "rb")

    framerate = obj.getframerate()
    nframes = obj.getnframes()
    frames = obj.readframes(-1)

    obj.close()
    #Wave.open

    time_audio = nframes/ framerate

    # Retorne un diccionario con esos datos
    return nframes, frames, time_audio


# Uno de los parametros de la funcion debe ser el output_path donde se guardara la imagen
def audio_plot(nframes, frames, time_audio):
    signal_array = np.frombuffer(frames, dtype=np.int16)  # Axis y. Each sample is 2 bytes long
    times = np.linspace(0, time_audio, num=nframes)  # Axis x.

    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title("Audio signal")
    plt.ylabel("Signal wave")
    plt.xlabel("Time (s)")
    plt.xlim(0, time_audio)
    plt.show()

    

    


