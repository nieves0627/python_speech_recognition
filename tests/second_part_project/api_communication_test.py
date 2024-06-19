import unittest
from second_part_project.api_secrets import API_KEY_ASSEMBLYAI
from second_part_project.api_communication import upload, transcribe, poll, get_transcription_result_url, save_transcript

class TestAPIcommunication(unittest.TestCase):

    def test_api_communication(self):
        input_path_from_terminal = "C:\\Users\\Juli\\Desktop\\Juliana\\Progranmacion\\audio_files\\output.wav"
        upload_endpoint = "https://api.assemblyai.com/v2/upload"
        transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
        headers = {'authorization': API_KEY_ASSEMBLYAI}

        audio_url = upload(input_path_from_terminal, upload_endpoint, headers)
        save_transcript(audio_url, input_path_from_terminal)