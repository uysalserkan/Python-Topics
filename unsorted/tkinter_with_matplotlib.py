import matplotlib.pyplot as plt
import numpy as np

x_coord = np.linspace(0, 2000, 2000)
print(x_coord)
y_coord = np.linspace(2000, 0, 2000)

# import image
im = plt.imread("baykar_tb2.png")
implot = plt.imshow(im)

# create a color spectrum
y = np.arange(0, 2000)

# plot x and y coords
plt.scatter(x=x_coord, y=y_coord, c=y, s=10, marker="1")
plt.show()

""" import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


def f(x, y):
    return np.sin(x) + np.cos(y)


x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for i in range(60):
    x += np.pi / 15.0
    y += np.pi / 20.0
    im = plt.imshow(f(x, y), animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
 """
#%% ??
""" import matplotlib.pyplot as plt
import time
import random

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

ysample = random.sample(range(-50, 50), 100)

xdata = []
ydata = []

plt.show()

axes = plt.gca()
axes.set_xlim(0, 100)
axes.set_ylim(-50, +50)
arr_img = plt.imread("baykar_tb2.png", format="png")
imagebox = OffsetImage(arr_img, zoom=0.05)
imagebox.image.axes = axes
xy = [0, 0]
ab = AnnotationBbox(
    imagebox,
    xy,
    # xybox=(120.0, -80.0),
    # xycoords="data",
    # # boxcoords="offset points",
    # pad=0.5,
)
(line,) = axes.plot(xdata, ydata, "r-")

for i in range(100):
    xdata.append(i)
    ydata.append(ysample[i])
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    ab.xy = [xdata, ydata]
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.1)

# add this if you don't want the window to disappear at the end
plt.show()
 """
#%% other
""" 
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
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

# from matplotlib import style
import random

# ---------End of imports


plt.rcParams["toolbar"] = "toolbar2"


class Scope(object):
    def __init__(self, ax, maxt=5, dt=0.02):

        arr_img = plt.imread("baykar_tb2.png", format="png")
        imagebox = OffsetImage(arr_img, zoom=0.05)
        imagebox.image.axes = ax
        xy = [0, 0]
        self.ab = AnnotationBbox(
            imagebox,
            xy,
            # xybox=(120.0, -80.0),
            # xycoords="data",
            # # boxcoords="offset points",
            # pad=0.5,
        )

        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-0.1, 1.1)
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
        self.ab.xy = [t, y + 5]
        self.line.set_data(self.tdata, self.ydata)
        return (self.line,)


def emitter(p=0.03):
    "return a random value with probability p, else 0"
    while True:
        v = np.random.rand(1)
        if v > p:
            yield 0.0
        else:
            yield np.random.rand(1)


np.random.seed()


fig, ax = plt.subplots()
ax.set_ylabel("Value")
ax.set_xlabel("Time (ms)")
scope = Scope(ax)


root = Tk.Tk()


# label = Tk.Label(root, text="SHM Simulation").grid(
#     column=0, row=0,padx=3)
ttk.Button(root, text="EXIT", command=root.quit, width=105).pack()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=5, blit=True)


Tk.mainloop()

# pass a generator in "emitter" to produce data for the update func

# ---------


# Fixing random state for reproducibility
 """
