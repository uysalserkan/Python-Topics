from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style

from matplotlib.widgets import Slider
""" 
    plt.rcParams['toolbar'] = 'None'  # Disable toolbar
    style.use('fivethirtyeight')

    fig = plt.figure(figsize=(6, 4))
    ax1 = fig.add_subplot(1, 1, 1)


    def animatePlot(i):
        data = open('data.txt', 'r').read()
        lines = data.split('\n')

        xs = []
        ys = []

        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)

        ax1.clear()
        ax1.plot(xs, ys)


    play_animation = animation.FuncAnimation(fig, animatePlot, interval=450)
    plt.xlabel('X values')
    plt.title('Animated Graph')

    plt.show()


    # %% Section 2
    fig2 = plt.figure()

    x = np.arange(-9, 10)
    y = np.arange(-9, 10).reshape(-1, 1)
    base = np.hypot(x, y)
    ims = []
    for add in np.arange(15):
        ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

    im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
                                    blit=True)
    # To save this second animation with some metadata, use the following command:
    # im_ani.save('im.mp4', metadata={'artist':'Guido'})
    plt.rcParams['toolbar'] = 'None'
    plt.show()

    # %% Section 3
    fig1 = plt.figure()


    def update_line(num, data, line):
        line.set_data(data[..., :num])
        return line,


    # Fixing random state for reproducibility
    np.random.seed()

    data = np.random.rand(2, 250)
    l, = plt.plot([], [], 'r-')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('x')
    plt.title('test')
    line_ani = animation.FuncAnimation(fig1, update_line, 50, fargs=(data, l),
                                    interval=50, blit=True)
    plt.rcParams['toolbar'] = 'None'
    plt.show()
 """

# %% Section 4
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
        # self.ann = plt.annotate("", (0, 0))

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        # annotation.remove()
        # annotation = plt.annotate("{:.2f}".format(t), xy=(t, y))
        # self.ann = annotation
        # ann = plt.annotate()
        # ann.remove()

        # self.ax.annotate("D", xy=(t, y))
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


# Fixing random state for reproducibility
np.random.seed(19680801)


fig, ax = plt.subplots()
scope = Scope(ax)


axamp = plt.axes([0.25, .03, 0.50, 0.02])
initial_amp = .5
# Slider
samp = Slider(axamp, 'Amp', 0, 1, valinit=initial_amp)

# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, emitter, interval=5,
                              blit=False)

plt.show()
