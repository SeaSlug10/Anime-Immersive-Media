import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio(threshold):
    r = sr.Recognizer()
    r.energy_threshold = threshold
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)
        said = ""
        try:
            print("recognizing")
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


if __name__ == "__main__":
    text = get_audio(4000)