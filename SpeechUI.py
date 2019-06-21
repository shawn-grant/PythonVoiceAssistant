import tkinter
import VoiceRecognizer

window = tkinter.Tk()
window.title("VOICE ASSISTANT")
window.geometry("300x400+800+100")

info = tkinter.Label(window, anchor=tkinter.NW)
info.pack()

def btnListen():
    info.config(text = "Listening...")
    VoiceRecognizer.Listen()
    info.config(text = "Processing...")


talkBtn = tkinter.Button ( window, text="LISTEN", fg="white", bg="blue", command=btnListen)
talkBtn.pack(fill="x")

logTxt = tkinter.Label(window, text="Helpl\nBoi\nhvugu\njuu")
logTxt.pack(fill=tkinter.BOTH)

window.mainloop()
