# our main file

import speech_recognition as sr

# criar reconhecedor
r = sr.Recognizer()

# Abrir dispositivo de audio para captura 
with sr.Microphone() as source: 
    audio = r.listen(source) # Definir o microfone como fonte de audio

    print(r.recognize_google(audio))