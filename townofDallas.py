#python
import datetime
import time
from framework import listener_thread
from framework import gui
from tkinter import *

def update_tacos(gui_instance):
    gui_instance.gui_playerList[2][1].config(text = str(datetime.datetime.now()) )
    gui_instance.status.set("2")
    gui_instance.after(1000, update_tacos, gui_instance)

# create the application
ToD = gui.App()
ToD.apply_config()
# start the program
#ToD.after(10000, update_tacos, ToD)

listen = listener_thread.thread_listen(ToD)

print ("GUI Loop Running")
ToD.mainloop()
