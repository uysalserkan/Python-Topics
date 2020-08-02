"""
Public Module Test1
"""
from tkinter import Tk, ttk
from NewWindow import CreateWindow, increaseFirstText


Screen1 = Tk()
Screen1.title("Test1 Main  Screen")
Screen1.geometry("400x400")
Screen1.resizable(0, 0)

mainGrid = ttk.Frame(Screen1)
mainGrid.pack()
ttk.Button(mainGrid, text="Pencereyi Aç", command=CreateWindow).grid(
    row=0, column=1, ipadx=32)
ttk.Button(mainGrid, text="Arttır", command=lambda: increaseFirstText(2)).grid(
    row=1, column=1, ipadx=32)
ttk.Button(mainGrid, text="Azalt").grid(row=3, column=1, ipadx=32)

Screen1.mainloop()
