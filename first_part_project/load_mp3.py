from pydub import AudioSegment
import os
import os.path
import pydub


def getting_filename(input_path):
    filename = os.path.basename(input_path).split('/')[-1]
    print(f"filename: {filename} {os.path.isfile(filename)}")

    filename_without_extension = filename.split(".")[0]
    return filename_without_extension


# Documente la funcion utilizando los docstrings de google guidelines


def to_mp3(filename_without_extension, input_path, save_path, ffmpeg_path=None):
    print(f"input_path: {input_path} {os.path.isfile(input_path)}")
    if ffmpeg_path is not None:
        pydub.AudioSegment.converter = ffmpeg_path

    audio = AudioSegment.from_wav(input_path)

    audio_name = filename_without_extension + ".mp3"

    completePath = os.path.join(save_path, audio_name)
    print(f"completePath: {completePath} {os.path.isfile(completePath)}")
    audio.export(completePath, format="mp3")
    print("Audio saved!")


