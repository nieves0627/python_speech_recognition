import unittest
from first_part_project.plot_audio import get_audio_params, audio_plot

class TestPlotAudio(unittest.TestCase):
    
    def test_get_audio_params(self):
        input_path_from_terminal = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\audio_files\\output.wav"
        
        n_samples_expected = 262400
        
        time_audio_expected = 5.950113378684807

        n_samples, _, time_audio = get_audio_params(input_path_from_terminal)
        
        self.assertTrue(n_samples==n_samples_expected)
        self.assertTrue(time_audio==time_audio_expected)
    
    
    def test_audio_plot(self):
        input_path_from_terminal = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\audio_files\\output.wav"
        
        n_samples, signal_wave, time_audio = get_audio_params(input_path_from_terminal)
        graphic = audio_plot(n_samples, signal_wave, time_audio)
        
        self.assertTrue(graphic is None)
     
    

