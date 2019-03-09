# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:37:43 2019

@author: JAYAPRAKASH
"""

import speech_recognition as sr
AUDIO_FILE=("sample_audio.wav")
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)

try:
    print("audio contains " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("google speech recognition cannot understand audio")
except sr.RequestError:
    print("could not get results")
    
    
    