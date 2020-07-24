# ---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
from tkinter import ttk, BOTH
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
# from matplotlib import style
import random
# ---------End of imports


plt.rcParams['toolbar'] = 'toolbar2'


class Scope(object):
    def __init__(self, ax, maxt=5, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,


def emitter(p=0.03):
    'return a random value with probability p, else 0'
    while True:
        v = np.random.rand(1)
        if v > p:
            yield 0.
        else:
            yield np.random.rand(1)


np.random.seed()


fig, ax = plt.subplots()
ax.set_ylabel('Value')
ax.set_xlabel('Time (ms)')
scope = Scope(ax)


root = Tk.Tk()


# label = Tk.Label(root, text="SHM Simulation").grid(
#     column=0, row=0,padx=3)
ttk.Button(root, text="EXIT", command=root.quit, width=105).pack()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=5,
                              blit=True)


Tk.mainloop()

# pass a generator in "emitter" to produce data for the update func

# ---------


# Fixing random state for reproducibility
