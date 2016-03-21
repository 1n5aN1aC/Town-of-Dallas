#python
import datetime
import time
from framework import mappings
from tkinter import *

# 
class App(Frame):
    instance = None
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.prepare_variables()
        self.createWidgets()
    
    #Apply tkinter-specific options
    def apply_config(self):
        self.master.title("Town of Dallas")
        self.master.maxsize(800, 500)
        self.master.minsize(800, 500)
    
    #Prepare all GUI variables
    def prepare_variables(self):
        App.instance = self
        
        self.gui_playerList = {}
        for i in range(1,16):
            self.gui_playerList[i] = {'name':"Player " + str(i), 'votes':None, 'choose':None, 'role':None, 'alive':True}
        
        self.status = StringVar()
        self.status.set("hello")
    
    #Actually creates all GUI elements
    def createWidgets(self):
        self.hi_there = Button(self, text="Disable")
        self.hi_there["command"] = self.remove_buttons
        self.hi_there.grid(row=0, column=0)
        
        self.test2 = Button(self, text="Enable")
        self.test2["command"] = self.enable_buttons
        self.test2.grid(row=1, column=0)
        
        
        l = Label(self, textvariable = self.status)
        l.grid(row=10, column=0, sticky=W)
        
        playerlist = LabelFrame(self, text="Player List")
        playerlist.grid(row=50, column=50)
        for i in range(1,16):
            #Display Player Number
            num = Label(playerlist, text=i)
            num.grid(row=i+50, column=50, sticky=W)
            
            #Generate Name Variables
            temp = StringVar()
            temp.set("Player " + str(i) )
            self.gui_playerList[i]['name'] = temp
            #Display Player Name Buttons
            nameBtn = Button(playerlist, textvariable = self.gui_playerList[i]['name'])
            nameBtn.config(width=20)
            nameBtn.grid(row=i+50, column=51, sticky=W)
            
            #Generate Vote Variables
            temp = IntVar()
            temp.set(0)
            self.gui_playerList[i]['votes'] = temp
            #Display Vote Counts
            voteZone = Label(playerlist, textvariable=self.gui_playerList[i]['votes'])
            voteZone.config(width=3)
            voteZone.grid(row=i+50, column=52, sticky=W)
            
            #Generate Action Variable
            temp = StringVar()
            temp.set("X")
            self.gui_playerList[i]['choose'] = temp
            #Display Action Button
            actn = Button(playerlist, textvariable=self.gui_playerList[i]['choose'])
            actn.config(width=2)
            actn.grid(row=i+50, column=53)
            
            #Generate Role Variable
            temp = StringVar()
            temp.set("??")
            self.gui_playerList[i]['role'] = temp
            #Display Role / edit field.
            roleZone = Label(playerlist, textvariable=self.gui_playerList[i]['role'])
            roleZone.config(width=13)
            roleZone.grid(row=i+50, column=54, sticky=W)
            
    #Changes action buttons to be blank
    def remove_buttons(self):
        for i in range(1,16):
            self.gui_playerList[i]['choose'].set("")
    
    #
    def enable_buttons(self):
        for i in range(1,16):
            if self.gui_playerList[i]['alive']:
                self.gui_playerList[i]['choose'].set("X")
    
    #
    def kill_player(self, player, role, lw="", dn=""):
        self.gui_playerList[player]['alive'] = False
        self.gui_playerList[player]['choose'].set("")
        self.gui_playerList[player]['name'].set("**" + self.gui_playerList[player]['name'].get() + "**")
        self.gui_playerList[player]['role'].set(mappings.role_mapping[role])
        #Also update deadplayers here.