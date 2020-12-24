# THIS IS IN BETA!!1
from __future__ import unicode_literals
from os import system
try:
    import youtube_dl
except:
    system('pip install youtube_dl')
    import youtubedl
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

songs = ['GENOCIDE', 'drink my piss you nasty slut yeah yeah', 'banana pie', 'rap music']

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
    playlistBool = False
    doyouwantplaylist = input("Do you want a playlist? [y/n] \n ");
    if (doyouwantplaylist.strip().lower() == 'y'):
        playlistBool = True
        playlist = []
        songAmount = int(input("Enter the amount of songs you want in this playlist. (MAX IS 5)"));
        if (songAmount == 2):
            song1 = input("Enter a song: ")
            song2 = input("Enter your second song: ")
            print("Starting playlist in...")
            sleep(1)
            print(3)
            sleep(1)
            print(2)
            sleep(1)
            print(1)
            sleep(1)
            print("Playlist started.")
            print("Loop enabled")
            while (playlistBool == True):
                if (song1 == 'GENOCIDE') or (song1 == songs[1]) or (song1 == songs[2]) or (song1 == songs[3]):
                    for _ in range(int(1)):
                        alert(text='Sorry, we cannot continue this program, the dev got lazy and is going to bet C:')
                        quit()
        elif (songAmount == 3):
            song1 = input("Enter a song: ")
            song2 = input("Enter your second song: ")
            song3 = input("Enter your third song: ")
        elif (songAmount == 4):
            song1 = input("Enter a song: ")
            song2 = input("Enter your second song: ")
            song3 = input("Enter your third song: ")
            song4 = input("Enter your forth song: ")
        elif (songAmount == 5):
            song1 = input("Enter a song: ")
            song2 = input("Enter your second song: ")
            song3 = input("Enter your third song: ")
            song4 = input("Enter your forth song: ")
            song5 = input("Enter your fifth song: ")



    else:
        print("Understood.")


    if (songChoice.get() == "GENOCIDE"):
        print("Playing on loop.")
        sleep(3)
        while(True):
            try:
                playsound("/home/mekhib2008/Downloads/y2mate.com - Lil Darkie - GENOCIDE (Prod. Wendigo, Lil Cubensis & Solsa).mp3")
            except:
                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(['https://www.youtube.com/watch?v=00nom6dSQGQ'])
                x = 'Lil Darkie - GENOCIDE (Prod. Wendigo, Lil Cubensis & Solsa)-00nom6dSQGQ.webm'
                playsound(x)
if __name__ == "__main__":
    MainWin().mainloop()
