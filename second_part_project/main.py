import sys
from api_communication import *


input_path = input_path

audio_url = upload(input_path)
save_transcript(audio_url, input_path)
