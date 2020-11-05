import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            sallie_speak(ask)
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            sallie_speak('Sorry, I did not get that')
        except sr.RequestError:
            sallie_speak('Sorry, I cannot process your request at the moment')
        return voice_data


def sallie_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        sallie_speak('My name is Sallie')
        print('My name is Sallie')
    if 'what time is it' in voice_data:
        sallie_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        sallie_speak('Here is what I found for ' + search + '...')
        print('Here is what I found for ' + search + '...')
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        sallie_speak('Here is the location for ' + location)
        print('Here is the location for ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
sallie_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
