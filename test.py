from bs4 import BeautifulSoup
import requests
from tkinter import *
import webbrowser
from time import sleep
from tkinter import Tk

def rankbot_activation():
    try:
        u = Username.get()
        name = "https://euw.op.gg/summoner/userName=" + u
        source = requests.get(name, "lxml").text
        soup = BeautifulSoup(source, "html.parser")
        lp = soup.find("span", {"class": "LeaguePoints"}).getText()
        rank = soup.find("div", {"class": "TierRank"}).getText()
        print(str(rank).replace("\t", ""), str(lp).replace("\t", ""))
    except:
        print("There is no account of this name or the summoner is unranked")
master = Tk()
Label(master, text="Username").grid(row=0)
Username = Entry(master)
Username.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=1, column=0, sticky=W, pady=4)
Button(master, text='Activate webbot', command=rankbot_activation).grid(row=1, column=1, sticky=W, pady=4)
mainloop()