import tkinter as tk
from tkinter import *
import tkinter.filedialog

import os
import shutil

import datetime


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #Creates buttom for selecting files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #Creates entry for source directory selection!
        self.source_dir = Entry(width=75)
        #Positions the entry in GUI using tkinter grid()
        self.source_dir.grid(row=0, column=1, padx=(20,10), pady=(30,0))

        #Creates Button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command = self.destDir)
        #Position Destination button in GUI
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width = 75)
        #Positions entry in GUI using tkinder grid
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))


        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width = 20, command = self.transferFiles)
        #Positions transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #creates exit button
        self.exit_btn = Button(text="Exit", width = 20, command = self.exit_program)
        #Positions exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))


    #Creating function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()

        #.delete(0, END) will clear the content that is inserted in entry widget,
        #this allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)

        #.insert method will insert the user selection to the source_dir entry
        self.source_dir.insert(0, selectSourceDir)


    #Creating function to select Destination directory.
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()

        #.delete(0, END) will clear the content that is inserted in entry widget,
        #this allows the path to be inserted into the entry widget properly
        self.destination_dir.delete(0, END)

        #.insert method will insert the user selection to the destination_dir entry
        self.destination_dir.insert(0, selectDestDir)


    #Creating a function to transfer files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()

        #gets destination directory
        destination = self.destination_dir.get()

        #gets current time
        current_time = datetime.datetime.now()

        #gets list of files in source directory
        source_files = os.listdir(source)

        #Runs through each file in the source directory
        for i  in source_files:
            #gets the file path of the file
            file_path = os.path.join(source, i)

            #gets the modification time of the file
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            #calculates the difference between current time and the modified time of the file
            time_difference = current_time - modified_time

            #checks if the file was modified wihtin the last 24 hours
            if time_difference < datetime.timedelta(hours=24):
                #moves the file from the source to the destination
                shutil.move(file_path, destination)
                print(i + ' was successfuly transferred.')
            

    #creates function to exit program:
    def exit_program(self):
        root.destroy()
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
