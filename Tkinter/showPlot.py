from tkinter import *
import matplotlib as plt
from matplotlib.figure import (Figure)
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

mainScreen = Tk()
mainScreen.title("Show PLOT on screen")
mainScreen.geometry("500x500")
mainScreen.resizable(0, 0)


def updateFigure():

quitButton = Button(mainScreen, text="Quit", command=mainScreen.destroy)
quitButton.pack()

updateButton = Button(mainScreen, text="Update", command=updateFigure)
updateButton.pack()

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
fig.legend()
fig.xlabel = 'X axis'
fig.ylabel = 'Y axis'

figCanvas = FigureCanvasTkAgg(fig, master=mainScreen)
figCanvas.draw()
figCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

mainScreen.mainloop()
