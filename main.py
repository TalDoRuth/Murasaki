# our main file


# criar reconhecedor
import speech_recognition as sr # importa a lib de reconhecimento de voz


r = sr.Recognizer() # cria um reconhecedor


with sr.Microphone() as source: # reconhece o microfone como fonte de audio
    while True:
        r.adjust_for_ambient_noise(source) # ajusta a sensibilidade do dispositivo de audio para diminuir o som ambiente
        audio = r.listen(source) # define o microfone como a fonte do audio 
        print(r.recognize_google(audio, language='pt'))
