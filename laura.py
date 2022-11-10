#Main Programming of Laura
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time
import comandos as CM


def assistente():
    os.remove("hello.mp3")


    def inicializacao():
        fraseResposta = "Olá meu senhor, comandos inicializados com sucesso. O que você deseja?"
        cria_audio(fraseResposta)
        time.sleep(1)
        os.remove("hello1.mp3")
        ouvir_microfone()


    def cria_audio(audio):
            tts = gTTS(audio,lang='pt-br')
            #Salva o arquivo de audio
            tts.save('hello2.mp3')
            #Da play ao audio
            playsound('hello2.mp3')
            os.remove("hello2.mp3")

    #Função para ouvir e reconhecer a fala
    def ouvir_microfone():
        #Habilita o microfone do usuário
        microfone = sr.Recognizer()
        
        #usando o microfone
        with sr.Microphone() as source:
            
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            print("Diga alguma coisa: ")
            
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
            
        try:
            
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            
            #Retorna a frase pronunciada
            print("Você disse: " + frase)
            
        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            time.sleep(2)
            print("Repita por favor")

        if frase == "Laura Iniciar comandos":
            inicializacao()

        elif frase == "Laura encerrar":
            cria_audio("Ok meu senhor, qualquer coisa é só me chamar.")
            time.sleep(2)
            os.remove("hello.mp3")
            print("Execução_Laura Encerrada com sucesso")

        elif frase == "escutar música":
            CM.escutarMusic()
        
        else:
            ouvir_microfone()


    ouvir_microfone()



microfone = sr.Recognizer()
        
#usando o microfone
with sr.Microphone() as source:
    
    #Chama um algoritmo de reducao de ruidos no som
    microfone.adjust_for_ambient_noise(source)
    
    #Frase para o usuario dizer algo
    print("Diga alguma coisa: ")
    
    #Armazena o que foi dito numa variavel
    audio = microfone.listen(source)
    
try:
    
    #Passa a variável para o algoritmo reconhecedor de padroes
    frase = microfone.recognize_google(audio,language='pt-BR')
    
    #Retorna a frase pronunciada
    print("Você disse: " + frase)
    
#Se nao reconheceu o padrao de fala, exibe a mensagem
except sr.UnknownValueError:
    time.sleep(2)
    print("Repita por favor")


def cria_audio2(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    #Da play ao audio
    playsound('hello.mp3')
    assistente()

if frase == "Laura":
    boasvindas = "Olá, Pedro! Fico feliz em te ver novamente."
    cria_audio2(boasvindas)
