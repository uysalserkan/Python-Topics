""" import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from matplotlib.cbook import get_sample_data


arr_img = plt.imread('test.jpg')
# Create initial data
data = np.array([[1, 2, 3, 4, 5], [7, 4, 9, 2, 3]])

# Create figure and axes
fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

# Create initial objects
line, = ax.plot([], [], 'r-')
annotation = ax.annotate('A0', xy=(data[0][0], data[1][0]))
ann_image = ax.annotate(arr_img, xy=(data[0][0], data[1][0]))
annotation.set_animated(True)


xy = [3.3, 10.2]
imagebox = OffsetImage(arr_img, zoom=0.2)
imagebox.image.axes = ax

ab = AnnotationBbox(imagebox, xy,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5,
                    )

ax.add_artist(ab)

# Create the init function that returns the objects
# that will change during the animation process


def init():
    return line, annotation

# Create the update function that returns all the
# objects that have changed


def update(num):
    newData = np.array([[1 + num, 2 + num / 2, 3, 4 - num / 4, 5 + num],
                        [7, 4, 9 + num / 3, 2, 3]])
    line.set_data(newData)
    # This is not working i 1.2.1
    annotation.set_position((newData[0][0], newData[1][0]))
    ann_image.set_position((newData[0][0], newData[1][0]))
    annotation.xytext = (newData[0][0], newData[1][0])
    return line, annotation


anim = animation.FuncAnimation(fig, update, frames=25, init_func=init,
                               interval=200, blit=True)
plt.show()
 """

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8, 5))
image = 'test.jpg '
image = plt.imread(image)
im = OffsetImage(image, zoom=.3)

artists = []
xdata, ydata = [0], [0]
ln, = plt.plot(xdata, ydata, 'r', lw=9, animated=True)
annotation = AnnotationBbox(
    im, (xdata[0], ydata[0]), xycoords='data', frameon=False)
artists.append(ax.add_artist(annotation))


def init():
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.set_aspect('equal')
    ax.axis('off')
    # ax.patch.set_facecolor('gold')  # 図全体の背景色


def update(i):
    x_i = 0.5 * i * np.cos(i)
    y_i = 0.5 * i * np.sin(i)
    xdata.append(x_i)
    ydata.append(y_i)
    ln.set_data(xdata, ydata)
    annotation.xybox = (x_i, y_i)

    return ln, annotation


ani = FuncAnimation(fig, update, frames=np.linspace(0, 16*np.pi, 300),
                    interval=100, init_func=init, blit=False)

plt.show()