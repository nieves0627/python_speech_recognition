import pyaudio
import wave


def record_audio(
    pyaudio_object: pyaudio.PyAudio,
    rate: int,
    channels: int,
    format: int,
    frames_per_buffer: int,
    seconds: int) -> pyaudio.PyAudio:

    # Usar contextmanager
    stream = pyaudio_object.open(
        format=format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=frames_per_buffer,
    )

    print("Start recording")

    frames = []
    for i in range(0, int(rate / frames_per_buffer * seconds)):
        data = stream.read(frames_per_buffer)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    pyaudio_object.terminate()

    return frames


def save_audio(frames, channels, pyaudio_object, rate):
    obj = wave.open("output.wav", "wb")
    obj.setnchannels(channels)
    obj.setsampwidth(pyaudio_object.get_sample_size(format))
    obj.setframerate(rate)
    obj.writeframes(b"".join(frames))
    obj.close()

    return obj


frames_per_buffer = 3200
format = pyaudio.paInt16
channels = 1
rate = 44100  # We can use 16000 for a change
seconds = 6
pyaudio_object = (
            pyaudio.PyAudio()
        )

frames = record_audio(pyaudio_object, rate,
                      channels,
                      format,
                      frames_per_buffer,
                      seconds)
save_audio(frames, channels, pyaudio_object, rate)
