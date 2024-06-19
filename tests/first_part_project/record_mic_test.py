import unittest
import pyaudio
import wave
from first_part_project.record_mic import record_audio, save_audio


class TestRecordMic(unittest.TestCase):

    def test_record_mic(self):
        frames_per_buffer = 3200
        format = pyaudio.paInt16
        channels = 1
        rate = 44100  # We can use 16000 for a change
        seconds = 6
        pyaudio_object = (
            pyaudio.PyAudio()
        )  # the pyaudio_object is an instance of the PyAudio class

        frames = record_audio(pyaudio_object, rate, channels, format, frames_per_buffer, seconds)
        save_audio(frames, channels, pyaudio_object, rate)
        

    def save_audio(self):
        pass