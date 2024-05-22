import wave

obj = wave.open("audio_file_one_channel_44100.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("Parameters", obj.getparams())

time_audio = obj.getnframes() / obj.getframerate()
print(time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj_new = wave.open("new_audio_file.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)

obj_new.writeframes(frames)

obj_new.close()
