#python
import datetime
import time
from framework import mappings
from tkinter import *
import tkinter.scrolledtext as tkst
from idlelib.ToolTip import *

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
        
        self.gui_deadList = {}
        for i in range(1,16):
            self.gui_deadList[i] = {'role':0, 'rolename':None, 'name':None, 'lw':None, 'dn':None, 'killers':None}
        
        self.time = StringVar()
        self.time.set("Day")
        
        self.day = IntVar()
        self.day.set(0)
        
        self.timeLeft = IntVar()
        self.timeLeft.set(30)
        
        self.chatBox = StringVar()
        self.chatBox.set("")
    
    #Actually creates all GUI elements
    def createWidgets(self):
        #Dead Frame
        deadFrame = LabelFrame(self, text="Dead List")
        deadFrame.grid(row=50, column=0)
        for i in range(1,16):
            #Generate role variables
            temp = IntVar()
            temp.set(0)
            self.gui_deadList[i]['role'] = temp
            #Display Role Numbers
            role = Label(deadFrame, textvariable=self.gui_deadList[i]['role'])
            role.grid(row=i, column=0, sticky=W)
            
            #Generate role name variables
            temp = StringVar()
            temp.set("Unknown")
            self.gui_deadList[i]['rolename'] = temp
            #Display Role Names
            roleName = Label(deadFrame, textvariable=self.gui_deadList[i]['rolename'])
            roleName.grid(row=i, column=1, sticky=W)
            
            #Generate Name variables
            temp = StringVar()
            temp.set("playerName")
            self.gui_deadList[i]['name'] = temp
            #Display Name Labels
            name = Label(deadFrame, textvariable=self.gui_deadList[i]['name'])
            name.grid(row=i, column=2, sticky=W)
            
            #Generate LW variables
            temp = StringVar()
            temp.set("")
            self.gui_deadList[i]['lw'] = temp
            #Display LW Buttons
            LW = Button(deadFrame, text='LW')
            LW.grid(row=i, column=3, sticky=W)
            
            #Generate DN variables
            temp = StringVar()
            temp.set("")
            self.gui_deadList[i]['dn'] = temp
            #Display DN Buttons
            DN = Button(deadFrame, text='DN')
            DN.grid(row=i, column=4, sticky=W)
            
            #Generate Tooltip variables
            temp = StringVar()
            temp.set("")
            self.gui_deadList[i]['killers'] = temp
            #Enable Tooltip on player's name
            Tooltip = ListboxToolTip(name, ["Hello"])
        
        #Chat Frame
        chatFrame = LabelFrame(self, text="Chat")
        chatFrame.grid(row=50, column=25)
        if True:
            self.chat = tkst.ScrolledText(chatFrame, wrap=WORD, width=30, height=23)
            self.chat.config(state=DISABLED)
            self.chat.grid(row=1, column=0, sticky=W)
            
            chatEntry = Entry(chatFrame, width=40, textvariable = self.chatBox)
            chatEntry.grid(row=10, column=0, sticky=W)
        
        #Time Frame
        timeFrame = LabelFrame(self, text="Time")
        timeFrame.grid(row=0, column=50)
        if True:
            time = Label(timeFrame, textvariable = self.time)
            time.grid(row=0, column=1, sticky=W)
            
            day = Label(timeFrame, textvariable = self.day)
            day.grid(row=0, column=2, sticky=W)
            
            spacer = Label(timeFrame, text=" | ")
            spacer.grid(row=0, column=3, sticky=W)
            
            timer = Label(timeFrame, textvariable = self.timeLeft)
            timer.grid(row=0, column=4, sticky=W)
        
        #Playerlist Frame
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
    
    #Shows the action buttons for those alive
    def enable_buttons(self):
        for i in range(1,16):
            if self.gui_playerList[i]['alive']:
                self.gui_playerList[i]['choose'].set("X")
    
    #Adds a chat message to the chat box
    def add_to_chat(self, message):
        self.chat.config(state=NORMAL)
        self.chat.insert(END, message)
        if True:
            self.chat.see(END)
        self.chat.config(state=DISABLED)
    
    # Handles Killing a player
    def kill_player(self, player, role, lw="", dn=""):
        if self.gui_playerList[player]['alive'] is True:
            self.gui_playerList[player]['alive'] = False
            self.gui_playerList[player]['choose'].set("")
            self.gui_playerList[player]['name'].set("**" + self.gui_playerList[player]['name'].get() + "**")
            self.gui_playerList[player]['role'].set(mappings.role_mapping[role])
            #Also update deadplayers here.