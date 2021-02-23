# our main file

'''
import speech_recognition as sr # importa a lib de reconhecimento de voz


r = sr.Recognizer() # cria um reconhecedor


with sr.Microphone() as source: # reconhece o microfone como fonte de audio
    r.adjust_for_ambient_noise(source) # ajusta a sensibilidade do dispositivo de audio para diminuir o som ambiente
    audio = r.listen(source) # define o microfone como a fonte do audio 
    print(r.recognize_google(audio, language='pt'))
'''




import json
import pyttsx3
#sintese de fala
engine = pyttsx3.init()



def speak(text): 
    engine.say(text)
    engine.runAndWait()


from vosk import Model, KaldiRecognizer
import os

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

import pyaudio

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            speak(text)
