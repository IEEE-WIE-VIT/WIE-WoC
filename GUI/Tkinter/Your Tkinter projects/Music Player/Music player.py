from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music player")
root.geometry('320x568')
root.configure(bg="#00457C")
root.resizable(False,False)

mixer.init()

songs = []
i=0

def open_folder():
    file = filedialog.askopenfilename(initialdir="C:/")
    title = file.split('/')
    name.config(text=title[-1])
    songs.append(file)

def play_song():
        mixer.music.load(songs[0])
        mixer.music.play()

def pause_song():
    global i
    if (i==0):
        i=1
        mixer.music.pause()
    elif (i==1):
        i=0
        mixer.music.unpause()


name = Label(root, text="music", font=("Montserrat",12), background="#00457C", foreground="#FFFFFF" )
name.pack(ipadx=10, ipady=10)

photo = tk.PhotoImage(file='../img/music.png')
image_label = ttk.Label(
    root,
    image=photo,
    padding=15,
background="#00457C"
)
image_label.pack()

pause = PhotoImage(file="../img/pause.png")
Button(root,image=pause,bd=0,background="#00457C", command=pause_song).place(x=0,y=334)

play = PhotoImage(file="../img/play.png")
Button(root,image=play,bd=0,background="#00457C", command=play_song).place(x=110,y=334)

stop = PhotoImage(file="../img/stop.png")
Button(root,image=stop,bd=0,background="#00457C",command=mixer.music.stop).place(x=220,y=334)

add = PhotoImage(file="../img/add.png")
Button(root,image=add,bd=0,background="#00457C", command=open_folder).place(x=110,y=450)

root.mainloop()