# pip install SpeechRecognition
# Pip install PyAudio
# Used Google API, limitted to 50 times a day.

import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Listening')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='en-US')
    print(text)
except sr.UnknownValueError:
    print("Hard to understand")
except sr.RequestError as e:
    print("Error: {0}".format(e))