"""New Window """
from tkinter import Tk, ttk, StringVar


def increaseFirstText(num):
    """ dşlfklşskdf """
    global firstText
    value = int(firstText.get())
    value += num
    firstText.set(value)


def CreateWindow():
    """Creating Window."""
    newWindow = Tk()

    ttk.Label(newWindow, text="Label 1: ").grid(row=0, column=0)
    global firstText
    firstText = StringVar(newWindow)
    firstText.set("0")
    ttk.Label(newWindow, textvariable=firstText).grid(row=0, column=1)
    ttk.Button(newWindow, text="Show Type", command=lambda: print(
        type(firstText))).grid(row=0, column=2)

    newWindow.geometry("200x100")
    newWindow.mainloop()
