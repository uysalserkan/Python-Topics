import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(frame):
    global x, y
    print(f"frame: {frame}")

    # Option 1: PAN sized windows on data
    start = 1 + (x[frame] // 10) * 10  # 1, 11, 21, ...
    end = start + PAN  # 10, 20, 30, ...

    # Option 2: sliding PAN window
    # start = x[max(frame-PAN//2, 0)]
    # start = x[max(frame - PAN + 1, 0)]
    # end = start + PAN

    ver_start = (y[frame] // 10) * 10
    ver_end = ver_start + PAN

    ax.set_xlim(start, end)
    ax.set_ylim(ver_start, ver_end)

    # start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(start, end, TICK))

    ax.figure.canvas.draw()

    line1.set_data(x[0 : frame + 1], y[0 : frame + 1])

    return (line1,)


# main
NUM = 100
TICK = 1
PAN = 9

x = np.arange(start=1, stop=NUM + 1, step=1)

for i in range(NUM):
    y = np.arange(start=1, stop=NUM + 1, step=1)
fig, ax = plt.subplots()

ax.set_xlim(0, PAN)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, TICK))

ax.set_ylim(0, 100)

(line1,) = ax.plot([], [], color="r")

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=100, repeat=False)

plt.show()
