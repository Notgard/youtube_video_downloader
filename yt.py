from __future__ import unicode_literals
from tkinter import ttk
import tkinter as tk
from threading import Timer
import youtube_dl
import time
import tkinter.messagebox
import os

now = time.time()
window = tk.Tk()
window.geometry('520x220')
window.title("Youtube vids downloader V.1.0")
window.iconbitmap('src/ico/favicon.ico')

tkinter.messagebox.showinfo(title="Warning !", message="DO NOT PRESS THE STOP DOWNLOAD BUTTON, also wait like 20 seconds for the program to start")

topFrame = tk.Frame(window)
nameLabel = tk.Label(topFrame, text="Youtube Video URL : ").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
fileLabel = tk.Label(topFrame, text="Download extension : ").pack(side=tk.LEFT)
entFile = tk.Entry(topFrame)
entFile.pack(side=tk.LEFT)
midFrame = tk.Frame(window).pack(side=tk.TOP)

pb = ttk.Progressbar(
    midFrame,
    orient='horizontal',
    mode='determinate',
    length= 420
)

pb.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
bottomFrame = tk.Frame(window)

def update_progress_label():
    return f"Current Progress: {pb['value']}%"

reset = tk.Button(midFrame, text="Reset", command = lambda : resetTimer()).place(relx=0.5, rely=0.3 , anchor=tk.CENTER)
label_value = tk.Label(midFrame, text=update_progress_label())
thumbnail = tk.Button(midFrame, text="Thumbnail ?", command = lambda : getThumb(), bg="yellow").place(relx = 0.35, rely=0.3, anchor=tk.CENTER)
label_value.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
topFrame.pack(side=tk.TOP)
load = tk.Button(bottomFrame, text="Start Download", command=lambda : [switch(), download()], bg="green")
load.pack(side=tk.LEFT)
stopLoad = tk.Button(bottomFrame, text="Stop Download", command=lambda : [switch(), stop()], bg="red", state="disabled")
stopLoad.pack(side=tk.LEFT)
bottomFrame.pack(side=tk.BOTTOM)

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def stop():
    pb.stop()
    label_value['text'] = update_progress_label()


def switch():
    if load["state"] == "normal":
        load["state"] = "disabled"
    if load["state"] == "disabled":
        stopLoad["state"] = "normal"
    if stopLoad["state"] == "normal":
        stopLoad["state"] = "disabled"

def resetTimer():
    pb['value'] = 0
    pb.update_idletasks()
    label_value['text'] = update_progress_label()
    load["state"] = "normal"
    stopLoad["state"] = "normal"    
    os.system("cls")
    print("Reset-ed youtube download programm.", "\n")
    print("Current videos/songs downloaded : ", "\n")
    print("-------------------------------------------------------------------------------")
    for i in os.listdir("src/"):
        if os.path.splitext(i)[1][1:] in {"mp4", "mp3", "mpeg", "webm", "m4a"}:
            print(i)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def getThumb():
    thumbnail["state"] = "disabled"

def isFileUploaded(retrivedSet):
    savedSet = set()
    path = "src/"
    

def yt_download():
    thumb = False
    ydl_opts = {
        'download_archive' : 'downloads.txt',
        'outtmpl': 'src/%(title)s.%(ext)s',
        'videoformat': str(entFile.get()),
        'writethumbnail': thumb,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': 'en',
        'nopart' : True,
        'postprocessors' : [{
            'key' : 'FFmpegVideoConvertor',
            'preferedformat' : str(entFile.get()),
            }
        ],
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if len(str(entName.get())) > 0:
            ydl.download([str(entName.get())])

def download():
#TODO add threading
    print("\n", "Chosen File extension : ", entFile.get(), "\n")
    print("Chosen Video to download : ", entName.get())
    timer = 0.5
    fourchette = 10
    timerino = timer * fourchette
    for i in range(fourchette):
        pb['value'] += 10
        pb.update_idletasks()
        label_value['text'] = update_progress_label()
        time.sleep(timer)
    T = Timer(timerino, lambda : yt_download())
    T.start()
    if T.is_alive() == False:
        print("Download successfull !")
    else:
        print("Fix this for 1.1 !! >_<")
then = time.time()
window.mainloop()