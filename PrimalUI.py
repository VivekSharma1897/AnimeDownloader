import tkinter as tk
import DownloadLatest as dl
import DownloadEpisode as de

def downloadLatest(AnimeName):
    dl.DownloadLatest(AnimeName)

def download(AnimeName, EpNo):
    de.Download(AnimeName, EpNo)
    
screen = tk.Tk()
screen.geometry("500x500")
screen.title("Download Anime")

nameVar = tk.StringVar(screen)
epVar = tk.StringVar(screen)

NameLabel = tk.Label(screen, text="Anime Name: ", font=("arial", 12, "bold"))
NameLabel.place(x=100, y=100)

NameEntry = tk.Entry(screen, bd=1, textvariable=nameVar)
NameEntry.place(x=250, y=100, width=150)

EpLabel = tk.Label(screen, text="Episode No: ", font=("arial", 12, "bold"))
EpLabel.place(x=100, y=200)

EpEntry = tk.Entry(screen, bd=1, textvariable=epVar)
EpEntry.place(x=250, y=200, width=50)

LatestBtn = tk.Button(screen, text="Download Latest Episode", command=lambda: downloadLatest(nameVar.get()))
LatestBtn.place(x=150, y=250, width=200, height=50)

EpisodeBtn = tk.Button(screen, text="Download Episode", command= lambda: download(nameVar.get(), epVar.get()))
EpisodeBtn.place(x=150, y=320, width=200, height=50)
