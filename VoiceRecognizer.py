import cv2
import speech_recognition as sr
from subprocess import call

#Voice Recognition
rec = sr.Recognizer()

def Listen():
    with sr.Microphone() as source:
        audio = rec.listen(source)

        try:
            print("recognizing text ....")
            text = rec.recognize_google(audio, language="en-US")
            #send text off to be processed
        except:
            #VoiceOutput.speak("Sorry I couldn't catch that, please repeat")
            call(["python", "VoiceOutput.py", "Sorry I couldn't catch that, please repeat"])
        