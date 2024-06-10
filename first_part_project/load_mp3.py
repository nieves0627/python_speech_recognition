from pydub import AudioSegment
import sys
import os
import os.path
import pydub

ffmpeg_path = "C:\\Users\\Juli\\Documents\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"

pydub.AudioSegment.converter = ffmpeg_path

print(f"ffmpeg: {ffmpeg_path} {os.path.isfile(ffmpeg_path)}")


input_path = sys.argv[1]
save_path = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\Python\\python_speech_recognition\\app\\output\\"  # Ruta relativa


def getting_filename(input_path):
    filename = os.path.basename(input_path).split('/')[-1]
    print(f"filename: {filename} {os.path.isfile(filename)}")

    return filename


# Ingrese como parametro la ruta del archivo de salida y que el nombre del archivo de salida sea el mismo del de entrada exceptuando la extension
# Los datos de subir volumen y repetir el clip tambien deben ser parametros que se pasen a la funcion con un default en el cual no se hagan cambios
# Documente la funcion utilizando los docstrings de google guidelines


def to_mp3(filename, input_path=input_path, save_path=save_path):
    print(f"input_path: {input_path} {os.path.isfile(input_path)}")

    audio = AudioSegment.from_wav(input_path)

    audio_name = filename + ".mp3"

    completePath = os.path.join(save_path, audio_name)
    print(f"completePath: {completePath} {os.path.isfile(completePath)}")
    audio.export(completePath, format="mp3")

    print("Audio saved!")


filename = getting_filename(input_path)
to_mp3(filename, input_path=input_path, save_path=save_path)
