import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
import matplotlib.animation as animation


# X = np.random.randint(0, 100, 100)
X = np.linspace(0, 100, 100, dtype=np.int32)
print(X)
Y = np.random.randint(0, 10, 100)
print(Y)

fig, ax = plt.subplots()


# print("test")

ax.set_ylabel("2X")
ax.set_xlabel("1X")
data = np.array([X, Y])


def animFunction(num):
    hor_start = data[0][num] - PAN  # 1, 11, 21, ...
    hor_end = hor_start + PAN

    ver_start = 1 + data[1][num] - PAN
    ver_end = ver_start + PAN

    ax.set_xlim(hor_start, hor_end)
    ax.set_ylim(ver_start, ver_end)
    ax.set_xticks(np.arange(hor_start, hor_end, TICK))
    ax.set_yticks(np.arange(ver_start, ver_end, TICK))
    line.set_data(data[0][:num], data[1][:num])
    ax.figure.canvas.draw()

    return (line,)


NUM = 100
TICK = 1
PAN = 10


# print(data)
# (line,) = Line2D(X, Y)
(line,) = ax.plot(data[0], data[1])
anim = animation.FuncAnimation(fig, animFunction)

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
