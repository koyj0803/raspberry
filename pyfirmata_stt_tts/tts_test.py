# pip3 install gtts playsound 

import speech_recognition as sr 
from gtts import gTTS 
import os 
import time 
import playsound 
import pygame

pygame.mixer.init()

def speak_save(text):
    tts = gTTS(lang='ko', text=text ) #ko')
    filename='/home/pi/Desktop/vsc_ws/raspberry/pyfirmata_stt_tts/voice.mp3'
    tts.save(filename) 
    #playsound.playsound(filename) 

def speaker_out():
    pygame.mixer.music.load("/home/pi/Desktop/vsc_ws/raspberry/pyfirmata_stt_tts/voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

speak_save("안녕하세요 저는 지금 파이썬 공부를 하고 있습니다.")
speaker_out()

"""
speech to text   stt   text to speech tts
"""