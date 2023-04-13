import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Create a label and entry widget for user input
        self.lbl = Label(self.master, text="Enter custom text:")
        self.lbl.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        self.txt = Entry(self.master, width=50)
        self.txt.grid(row=0, column=1, padx=(10, 10), pady=(10, 0))

        # Create a button to generate custom HTML page
        self.btn_custom = Button(self.master, text="Custom HTML Page", width=15, height=1, command=self.customHTML)
        self.btn_custom.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        # Create the original button for generating default HTML page
        self.btn_default = Button(self.master, text="Default HTML Page", width=15, height=1, command=self.defaultHTML)
        self.btn_default.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

        # Button for exiting the program
        self.btnExit = Button(self.master, text="Exit", width=15, height=1, command=self.master.destroy)
        self.btnExit.grid(row=1, column=2, padx=(10,0), pady=(10,10))


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        userText = self.txt.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<p>" + userText + "</p>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
