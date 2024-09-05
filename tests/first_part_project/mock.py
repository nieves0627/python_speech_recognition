import unittest
import pyaudio
from unittest.mock import patch, MagicMock
from first_part_project.record_mic import record_audio, save_audio


class TestAudioFunctions(unittest.TestCase):
    def setUp(self):
        self.pyaudio_mock = MagicMock(spec=pyaudio.PyAudio)
        self.stream_mock = MagicMock()
        self.pyaudio_mock.open.return_value = self.stream_mock

    def test_record_audio(self):
        rate = 44100
        channels = 1
        format = pyaudio.paInt16
        frames_per_buffer = 3200
        seconds = 2

        with patch('pyaudio.PyAudio', return_value=self.pyaudio_mock):
            frames = record_audio(self.pyaudio_mock,
                                  rate,
                                  channels,
                                  format,
                                  frames_per_buffer,
                                  seconds)

        self.pyaudio_mock.open.assert_called_once_with(
            format=format,
            channels=channels,
            rate=rate,
            input=True,
            frames_per_buffer=frames_per_buffer
        )
        self.stream_mock.read.assert_called()
        self.stream_mock.stop_stream.assert_called_once()
        self.stream_mock.close.assert_called_once()
        self.pyaudio_mock.terminate.assert_called_once()
        self.assertIsInstance(frames, list)

    def test_save_audio(self):
        frames = [b'frame1', b'frame2', b'frame3']
        channels = 1
        rate = 44100

        with patch('wave.open', create=True) as wave_mock:
            obj_mock = wave_mock.return_value
            obj = save_audio(frames, channels, self.pyaudio_mock, rate)

        wave_mock.assert_called_once_with('output.wav', 'wb')
        obj_mock.setnchannels.assert_called_once_with(channels)
        obj_mock.setsampwidth.assert_called_once()
        obj_mock.setframerate.assert_called_once_with(rate)
        obj_mock.writeframes.assert_called_once_with(b'frame1frame2frame3')
        obj_mock.close.assert_called_once()
        self.assertEqual(obj, obj_mock)


if __name__ == '__main__':
    unittest.main()
