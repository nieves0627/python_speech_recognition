import wave
import sys


filename = sys.argv[1]


# los parametros adicionales de esta funcion se deben obtener en la funcion definida en el archivo plot_audio e importarce aqui de ser necesario
def get_audio_params(filename):

    obj = wave.open(filename, "rb")

    print("Number of channels", obj.getnchannels())
    print("Sample width", obj.getsampwidth())
    print("Frame rate", obj.getframerate())
    print("Number of frames", obj.getnframes())
    print("Parameters", obj.getparams())

    time_audio = obj.getnframes() / obj.getframerate()
    print(time_audio)

    return obj


# se elimina
def set_audio_params(obj):
    frames = obj.readframes(-1)
    print(type(frames), type(frames[0]))
    print(len(frames))

    # Usar context manager
    obj_new = wave.open("new_audio_file.wav", "wb")

    obj_new.setnchannels(1)
    obj_new.setsampwidth(2)
    obj_new.setframerate(44100.0)

    obj_new.writeframes(frames)

    obj_new.close()

    return obj_new


obj = get_audio_params(filename)
set_audio_params(obj)
