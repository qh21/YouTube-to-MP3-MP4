import tkinter as tk
from tkinter import *
import tkinter.font
from tkinter import filedialog
import yt_dlp
import os

script_dir = os.path.dirname(__file__)



root = Tk()
label= tk.Label()
root.title('YouTube Converter')

root.geometry('500x500')
root.config(bg='#131417')

root.iconbitmap(os.path.join(script_dir, "YTD.ico"))

Desired_font = tkinter.font.Font( family = "Roboto Mono", 
                                 size = 10, 
                                 weight = "bold")


def downloadVideo(link):
    ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'outtmpl': os.path.join(dllocation, '%(title)s.%(ext)s'), 
    'ffmpeg_location': os.path.join(script_dir, 'ffmpeg'), # Edit the path of ffmpeg
    'noplaylist': True,

    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])



def downloadAudio(link):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(dllocation, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': os.path.join(script_dir, 'ffmpeg'),
    'noplaylist': True,
}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def downloadOptions():
    if  format(value_inside2.get())==options_list2[1]:
        downloadVideo(link.get())
        ('\a')    
    elif format(value_inside2.get())==options_list2[0]:
        downloadAudio(link.get())
        ('\a')
    link.delete(0, END)

def clickEnter(event):
    downloadOptions()
    link.delete(0, END)

def ClearDownloadLocation():
    global label3
    label3.destroy()
    ChangeDownloadLocation()

def DisplayDownloadLocation():
    global label3
    global dllocation
    dllocation_file = open(os.path.join(script_dir, "dllocation.txt"),"r+") 
    dllocation = dllocation_file.readline()
    dllocation_file.close() 
    label3 = Label(root, text=f"'{dllocation}'",bg='#131417',fg='#fff',font=Desired_font)
    label3.place(x=145,y=60)

def ChangeDownloadLocation():
    global label3
    global dllocation
    dllocation = filedialog.askdirectory()
    dllocation_file = open(os.path.join(script_dir, "dllocation.txt"),"r+") 
    dllocation_file.truncate(0)
    dllocation_file.writelines(dllocation)
    dllocation_file.close()
    DisplayDownloadLocation()
    
label1 = Label(root, text='Enter Video Link: ',bg='#131417',fg='#fff',font=Desired_font)
label1.place(x=10,y=15)

link = Entry(root,width=50,bg='#222222',fg='#fff')
link.place(x=130,y=10,height=30,width=300)



myButton = Button(root, text='Download',command=lambda:[downloadOptions()],bg='#2474a8',fg='#fff',font=Desired_font)
root.bind('<Return>',clickEnter)

myButton.place(x=530,y=8)

options_list2 = {0:"MP3",1:"MP4"}
value_inside2 = tk.StringVar(root)
value_inside2.set(options_list2[0])
question_menu2 = OptionMenu(root,value_inside2, *options_list2.values())    
question_menu2.place(x=440,y=8)
label2 = Label(root, text='Download Location: ',bg='#131417',fg='#fff',font=Desired_font)
label2.place(x=10,y=60)
DisplayDownloadLocation()
myButton2 = Button(root, text='Change',command=lambda:[ClearDownloadLocation()],bg='#2474a8',fg='#fff',font=Desired_font)
myButton2.place(x=35,y=90)
root.mainloop()
