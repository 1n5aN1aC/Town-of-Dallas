#python

from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Town of Dallas")
myapp.master.maxsize(1000, 400)
myapp.master.minsize(1000, 400)

# start the program
myapp.mainloop()