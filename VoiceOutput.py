import pyttsx3
import sys

#TTS variables
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('rate', tts.getProperty('rate') - 50)
#tts.setProperty('voice', voices[1])

#print available voices
def printVoices():
    for voice in voices:
        print (voice.id)

def speak(words):
        tts.say(words)
        tts.runAndWait()

speak(sys.argv[1])
