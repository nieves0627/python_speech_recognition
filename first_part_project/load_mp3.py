from pydub import AudioSegment


audio = AudioSegment.from_wav("output.wav")

audio = audio + 6  # this will increase the volume by 6dB
audio = audio * 2  # repeat the clips
audio = audio.fade_in(2000)  # The fade_in method is used to gradually increase the volume of the audio over a specified duration (2000 milliseconds).

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
