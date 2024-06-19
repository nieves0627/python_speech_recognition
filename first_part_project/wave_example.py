import wave

# los parametros adicionales de esta funcion se deben obtener en la funcion definida en el archivo plot_audio e importarce aqui de ser necesario
def get_audio_params(input_path):

    obj = wave.open(input_path, "rb")

    nchannels = obj.getnchannels()
    samplewidth =  obj.getsampwidth()
    framerate =  obj.getframerate()
    nframes = obj.getnframes()

    time_audio = nframes / framerate
    print(f"Frame rate: {framerate}, Number of channels: {nchannels}, Sample width: {samplewidth}, Time audio: {time_audio}")

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

