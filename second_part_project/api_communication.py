import requests
# from api_secrets import API_KEY_ASSEMBLYAI
import time


# Upload
def upload(input_path, upload_endpoint, headers):
    def read_file(input_path, chunk_size=5242880):
        with open(input_path, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                                    headers=headers,
                                    data=read_file(input_path))

    audio_url = upload_response.json()["upload_url"]
    return audio_url


# Transcribe
def transcribe(audio_url, transcript_endpoint, headers):
    transcript_request = {"audio_url": audio_url}
    transcript_response = requests.post(transcript_endpoint,
                                        json=transcript_request,
                                        headers=headers)

    transcript_id = transcript_response.json()["id"]
    return transcript_id


# Poll
def poll(transcript_id, transcript_endpoint, headers):
    polling_endpoint = transcript_endpoint + "/" + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data["status"] == "completed":
            return data, None
        elif data["status"] == "error":
            return data, data["error"]

        print("Waiting 30 seconds...")
        time.sleep(30)


# Save transcript

def save_transcript(audio_url, input_path):
    data, error = get_transcription_result_url(audio_url)

    if data:
        text_file_name = input_path + ".txt"
        with open(text_file_name, "w") as f:
            f.write(data["text"])
        print("Transcription saved")
    elif error:
        print("Error", error)
