import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

#harvard = sr.AudioFile("F:\\2021_2_lecture\\control2\\pyfirmata_stt_tts\\harvard.wav")
harvard = sr.AudioFile("/home/pi/Desktop/vsc_ws/raspberry/pyfirmata_stt_tts/harvard.wav")
# sr.AudioFile()에 들어가는 파일 path는 전체 파일 패스를 넣어야 함
# 또한 윈도우의 경우 \\를 사용하던지 아니면 /를 사용해야 함
with harvard as source:
    audio = r.record(source)
    out_text = r.recognize_google(audio)

print(out_text)