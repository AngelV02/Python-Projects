import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

import phonebook_gui
import phonebook_main


def center_window (self, w, h): #pass in the tkinter frame(master) refrence and the w and h
    #gets the users screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    
    #calculates x and y coords to paint the app centered on users screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user click on the windows 'X' to ensure they want to close 
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #this closes app
        self.master.destroy()
        os.exit(0)
        
#==================================================================================

def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMERAY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        
        #Commit() to save changes and close the database connection
        conn.commit()
    conn.close()
    first_run(self)
    

def first_run(self):
    data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commitj()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count
