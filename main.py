import os
import openpyxl
import threading
import FaceRecognizer

if not os.path.exists("Data"):
    os.makedirs("Data")

#RUN FACE DETECTION
try:
    fd = threading.Thread(target=FaceRecognizer.startRecognition)
    fd.start()
except:
   print ("Error: unable to start one or more threads")

import SpeechUI