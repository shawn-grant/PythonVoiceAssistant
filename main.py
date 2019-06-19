import os
import openpyxl
import threading
from subprocess import call
import VoiceRecognizer
import FaceRecognizer

if not os.path.exists("Data"):
    os.makedirs("Data")

#RUN FACE DETECTION AND VOICE RECOGNITION SIMULTANEOUSLY
try:
    vr = threading.Thread(target=VoiceRecognizer.startListening)
    vr.start()

    fd = threading.Thread(target=FaceRecognizer.startRecognition)
    fd.start()
except:
   print ("Error: unable to start one or more threads")

call(["python", "VoiceOutput.py", "Welcome, what can I help you with?"])
