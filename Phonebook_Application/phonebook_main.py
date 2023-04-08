# Python 3.11.2
#
# Author: Angel Dominick Velasco
#
# Purpose: 

from tkinter import *
import tkinter as tk

import phonebook_gui
import phonebook_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #define master frame configuration
        self.master = master
        self.master.minsize(500,300) #height, width
        self.master.maxsize(500,300)
        
        #This CenterWindow method will center the app on the user screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="F0F0F0")
        
        #This protocol method is a tkinter built-in method to catch
        # if the user clicks the upper corner, "X" on windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        
        #loads up the GUI widgets from the separate module,
        #Keeping the code comparmentalized and clutter free
        phonebook_gui.load_gui(self)
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
