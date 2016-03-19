#python
import datetime
import time
from tkinter import *

# 
class App(Frame):
    instance = None
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.prepare_variables()
        self.createWidgets()
    
    def apply_config(self):
        self.master.title("Town of Dallas")
        self.master.maxsize(800, 500)
        self.master.minsize(800, 500)
    
    def prepare_variables(self):
        App.instance = self
        self.gui_playerList = {1: ["Player 1",  None, None],
                               2: ["Player 2",  None, None],
                               3: ["Player 3",  None, None],
                               4: ["Player 4",  None, None],
                               5: ["Player 5",  None, None],
                               6: ["Player 6",  None, None],
                               7: ["Player 7",  None, None],
                               8: ["Player 8",  None, None],
                               9: ["Player 9",  None, None],
                               10:["Player 10", None, None],
                               11:["Player 11", None, None],
                               12:["Player 12", None, None],
                               13:["Player 13", None, None],
                               14:["Player 14", None, None],
                               15:["Player 15", None, None] }
        self.status = StringVar()
        self.status.set("hello")
    
    def createWidgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "PM"
        self.hi_there["command"] = self.remove_buttons
        self.hi_there.grid(row=0, column=0)
        
        l = Label(self, textvariable = self.status)
        l.grid(row=0, column=51, sticky=W)
        
        for i in range(15):
            #Using 1-indexed for this.
            i = i+1
            #Player Numbers
            num = Label(self, text=i)
            num.grid(row=i+50, column=50, sticky=W)
            #Player Name button
            btn = Button(self, text=self.gui_playerList.get(i, "error")[0] )
            btn.config(width=20)
            btn.grid(row=i+50, column=51, sticky=W)
            self.gui_playerList[i][1] = btn
            #Action Button
            actn = Button(self, text=" X " )
            actn.grid(row=i+50, column=52)
            self.gui_playerList[i][2] = actn
    
    def remove_buttons(self):
        for i in range(15):
            i = i+1
            self.gui_playerList[i][2].config(text="    ")
