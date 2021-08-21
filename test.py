import speech_recognition as sr
print(sr.__version__)



test = sr.Recognizer()

harvard = sr.AudioFile('precolumbia.mp3')
with harvard as source:
    audio = test.record(source)

print(test.recognize_google(audio))