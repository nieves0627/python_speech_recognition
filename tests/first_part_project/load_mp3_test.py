import unittest
from first_part_project.load_mp3 import getting_filename, to_mp3
import os

class TestLoadMP3Methods(unittest.TestCase):

    def test_to_mp3(self):
        completePath_expected = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\Python\\python_speech_recognition\\app\\output\\output.mp3"
        
        ffmpeg_path = "C:\\Users\\Juli\\Documents\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"

        input_path_from_terminal = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\audio_files\\output.wav"
        save_path_output = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\Python\\python_speech_recognition\\app\\output\\"  # Ruta relativa

        filename_without_extension = getting_filename(input_path_from_terminal)
        to_mp3(filename_without_extension, input_path_from_terminal, save_path_output, ffmpeg_path)
        self.assertTrue(os.path.isfile(completePath_expected))


    def test_getting_filename(self):
        input_path_from_terminal = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\audio_files\\output.wav"

        filename_without_extension_expected = "output"

        filename_without_extension =  getting_filename(input_path_from_terminal)
        self.assertTrue(filename_without_extension == filename_without_extension_expected)
        
if __name__ == '__main__':
    unittest.main()