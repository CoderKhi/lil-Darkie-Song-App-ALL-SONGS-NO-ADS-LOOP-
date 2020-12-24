# PLEASE REMEMBER THIS IS CURRENTLY A BETA! THIS IS A TEST!!!
from os import system
try:
    import youtube_dl
    from __future__ import unicode_literals
except:
    system('pip install youtube_dl')
    import youtubedl
    from __future__ import unicode_literals
try:
    import tkinter as tk
except:
    system('pip install python3-tk')
    import tkinter as tk
try:
    from playsound import playsound
except:
    system('pip install playsound')
    from playsound import playsound
from time import sleep
try:
    from pyautogui import alert
except:
    system('pip install pyautogui')
    from pyautogui import alert


title = 'Lil Darkie Song App'
res = '620x480'

songs = ['GENOCIDE']

class MainWin(tk.Tk):
    def __init__(self):
        global songChoice
        super().__init__()
        self.title(title)
        self.geometry(res)


        songChoice = tk.Entry(self);
        songChoice.pack(side=tk.TOP);
        songChoiceLab = tk.Label(self, text="Enter the song you want to play -> \n(from lil darkie) ");
        songChoiceLab.place(x=0, y=0);
        playSong = tk.Button(self, text="PLAY SONG!", command=songCheck).pack(side=tk.LEFT)

def songCheck():
    if (songChoice.get() == "GENOCIDE"):
        print("Playing on loop.")
        sleep(3)
        while(True):
            try:
                playsound("/home/mekhib2008/Downloads/y2mate.com - Lil Darkie - GENOCIDE (Prod. Wendigo, Lil Cubensis & Solsa).mp3")
            except:
                from __future__ import unicode_literals
                import youtube_dl

                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(['https://www.youtube.com/watch?v=00nom6dSQGQ'])
                x = input('Enter the file path of the current download (it\'s inside of the folder where this py file is! :D')
                playsound(x)
if __name__ == "__main__":
    MainWin().mainloop()
