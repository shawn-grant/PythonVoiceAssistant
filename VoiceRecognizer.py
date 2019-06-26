import cv2
import speech_recognition as sr
from subprocess import call

#Voice Recognition
rec = sr.Recognizer()

#calibrate
with sr.Microphone() as source:  
   print("Please wait. Calibrating microphone...")
   r.adjust_for_ambient_noise(source, duration=5) 
   print("Speech input ready!") 

def Listen():
    with sr.Microphone() as source:
        audio = rec.listen(source)

        try:
            print("recognizing text ....")
            text = rec.recognize_sphinx(audio, language="en-US")
            #send text off to be processed
            call(["python", "VoiceOutput.py", "You said " + text])
        except:
            #VoiceOutput.speak("Sorry I couldn't catch that, please repeat")
            call(["python", "VoiceOutput.py", "Sorry I couldn't catch that, please repeat"])
        