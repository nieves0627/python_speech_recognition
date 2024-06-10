from pydub import AudioSegment
import sys
import os
import os.path


input_path = sys.argv[1]
save_path = "C:\\Users\\andre\\OneDrive\\Escritorio\\Juliana\\Programacion\\python_speech_recognition\\app\\output\\"


def getting_filename(input_path):
    filename = os.path.basename(input_path).split('/')[-1]
    return filename


# Ingrese como parametro la ruta del archivo de salida y que el nombre del archivo de salida sea el mismo del de entrada exceptuando la extension
# Los datos de subir volumen y repetir el clip tambien deben ser parametros que se pasen a la funcion con un default en el cual no se hagan cambios
# Documente la funcion utilizando los docstrings de google guidelines


def to_mp3(filename, input_path=input_path, save_path=save_path):
    audio = AudioSegment.from_wav(input_path)

    audio_name = filename + ".mp3"
    audio.export(audio_name, format="mp3")

    completePath = os.path.join(save_path, audio_name)

    file1 = open(completePath, "w")

    file1.write(audio_name)

    file1.close()

    print("Audio saved!")


filename = getting_filename(input_path)
to_mp3(filename, input_path=input_path, save_path=save_path)
