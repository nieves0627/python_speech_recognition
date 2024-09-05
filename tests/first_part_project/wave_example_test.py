import unittest
from first_part_project.wave_example import get_audio_params, set_audio_params


class TestWaveExample(unittest.TestCase):

    def test_get_audio_params(self): 
        input_path_from_terminal = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\audio_files\\output.wav"
        save_path_output = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\Python\\python_speech_recognition\\app\\output\\"  # Ruta relativa

        obj = get_audio_params(input_path_from_terminal)
        set_audio_params(obj)
