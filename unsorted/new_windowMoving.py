import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.animation as animation


# X = np.random.randint(0, 100, 100)
X = np.linspace(0, 100, 100, dtype=np.int32)
print(X)
Y = np.random.randint(0, 2, 100)
print(Y)

fig, ax = plt.subplots()


# print("test")

ax.set_ylabel("2X")
ax.set_xlabel("1X")
data = np.array([X, Y])

# 🛧
plane_text = u"\u2708"
ann = ax.annotate(plane_text, xy=(1, 0.1), size=16, rotation=45, ha="center")

""" 
ADDING IMAGE

arr_img = plt.imread(fn, format='png')

    imagebox = OffsetImage(arr_img, zoom=0.2)
    imagebox.image.axes = ax
 """


def animFunction(num):
    try:
        hor_start = data[0][num] - PAN  # 1, 11, 21, ...
        hor_end = hor_start + PAN
    except IndexError:
        print("DONE")

    # ann.set_animated(True)
    # ax.add_artist(ann)
    # ver_start = 1 + data[1][num] - PAN
    # ver_end = ver_start + PAN
    ann.xy = (data[0][num], data[1][num])
    ann.set_position((data[0][num], data[1][num]))
    # annBox.xy = (data[0][num], data[1][num])
    # annBox._update_position_xybox(ax, (data[0][num], data[1]))
    # ann.xy = (data[0][num], data[1][num])

    ax.set_xlim(hor_start, hor_end)
    # ax.set_ylim(ver_start, ver_end)
    ax.set_xticks(np.arange(hor_start, hor_end, TICK))
    # ax.set_yticks(np.arange(ver_start, ver_end, TICK))
    line.set_data(data[0][:num], data[1][:num])
    ax.figure.canvas.draw()

    return (line, ann)


NUM = 100
TICK = 1
PAN = 10


# print(data)
# (line,) = Line2D(X, Y)
(line,) = ax.plot(data[0], data[1])
anim = animation.FuncAnimation(fig, animFunction, blit=False)

plt.show()

"""
fig1 = plt.figure()


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return (line,)


# Fixing random state for reproducibility
np.random.seed()

data = np.random.rand(2, 250)
(l,) = plt.plot([], [], "r-")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("x")
plt.title("test")
line_ani = animation.FuncAnimation(
    fig1, update_line, 50, fargs=(data, l), interval=50, blit=True
)
plt.rcParams["toolbar"] = "None"
plt.show()
"""
