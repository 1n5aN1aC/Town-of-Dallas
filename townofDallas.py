#python
import datetime
import time
from framework import listener_thread
from framework import gui
from tkinter import *

def update_tacos(gui_instance):
    gui_instance.gui_playerList[2]['name'].set( str(datetime.datetime.now()) )
    gui_instance.kill_player(2, 4)
    gui_instance.status.set("2")
    #gui_instance.after(1000, update_tacos, gui_instance)

# Create the application
ToD = gui.App()
ToD.apply_config()

ToD.after(3000, update_tacos, ToD)

listen = listener_thread.thread_listen(ToD)

print ("GUI Loop Running")
ToD.mainloop()
