import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

L = 50
theta = np.linspace(0, 2*np.pi, L)
r = np.ones_like(theta)

x = r*np.cos(theta)
y = r*np.sin(theta)

line, = ax.plot(1, 0, 'ro')

annotation = ax.annotate(
    'annotation', xy=(1, 0), xytext=(-1, 0),
    arrowprops={'arrowstyle': "fancy"}
)


def update(i):

    new_x = x[i % L]
    new_y = y[i % L]
    line.set_data(new_x, new_y)

    # annotation.xytext = (-new_x,-new_y) <-- does not work
    annotation.set_position((-new_x, -new_y))
    annotation.xy = (new_x, new_y)

    return line, annotation


ani = animation.FuncAnimation(
    fig, update, interval=500, blit=False
)

plt.show()
