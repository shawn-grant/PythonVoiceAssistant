import os
import pyttsx3
import openpyxl

if not os.path.exists("Data"):
    os.makedirs("Data")

#TTS variables
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1])

#print available voices
def PrintVoices():
    for voice in voices:
        print (voice.id)

#Files
userFile = open("Data/user.dat", "w+")

if str(userFile.read()) == "":
    name = input("Name: ")
    userFile.write(name)

tts.say('Welcome '+ name)
tts.runAndWait()