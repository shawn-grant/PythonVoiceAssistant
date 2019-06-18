import os
import pyttsx3
import openpyxl
import speech_recognition as sr

if not os.path.exists("Data"):
    os.makedirs("Data")

#TTS variables
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1])
#Voice Recognition
rec = sr.Recognizer()

#print available voices
def printVoices():
    for voice in voices:
        print (voice.id)

printVoices()

def listenToUser():
    tts.say("I'm listening")
    tts.runAndWait()

    with sr.Microphone() as source:
        audio = rec.listen(source)

        try:
            print("recognizing text ....")
            text = rec.recognize_google(audio, language = "en-US")
            return text
        except:
            print("CANT UNDERSTAND YOU")
            tts.say("Sorry I couldn't catch that, please repeat")
            tts.runAndWait()
            listenToUser()

#Files
userFile = open("Data/user.dat", "w+")

'''if str(userFile.read()) == "":
    name = input("Name: ")
    userFile.write(name)

tts.say('Welcome '+ name)
tts.runAndWait()'''

response = listenToUser()
tts.say("you said, " + response)
tts.runAndWait()