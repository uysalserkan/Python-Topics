"""from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.testVar = Radiobutton(master)
        self.testVar.pack()

        self.testMessage = Message(master,text="Test mesajidir")
        self.testMessage.pack()

        self.myLabel = Label(master, text="Enter your Password:")
        self.myLabel.pack()
        
        self.myButton =Button(master, text="Search")
        self.myButton.pack()
        # self.myCheck = Checkbutton(master, text="Remember Me", variable="v", value=True)
        # self.myCheck.pack()
        self.myEntry = Entry(master, width=30)
        self.myEntry.pack()
        # self.Radiobutton(master, text="Male", variable=v, value=1)
        # self.Radiobutton(master, text="Female", variable=v, value=2)
        self.myOption = OptionMenu(master,  "Select Country", "USA", "UK", "India","Others")
        self.myOption.pack()
        # self.myScroll = Scrollbar(master, orient=VERTICAL, command= text.yview)
        # self.myScroll.pack()
        self.myFrame = Frame(master,relief=RAISED,borderwidth=1)
        self.myFrame.pack(expand=True)


    def greet(self):
        print("Greetings!")

root = Tk()
# root.geometry("250x250")
# root.resizable(0,0)
my_gui = MyFirstGUI(root)


root.mainloop()

"""
#%% Other UI
#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use the pack manager
to position two buttons in the
bottom-right corner of the window.

Author: Jan Bodnar
Website: www.zetcode.com
"""

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style,Label

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=2)
        frame.pack(fill=BOTH, expand=True)

        self.myLabel = Label(self, text="Blue Sky")
        self.myLabel.pack()
        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=7, pady=7)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)


def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()

