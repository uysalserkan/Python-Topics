import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
initial_amp = .5
s = initial_amp*np.sin(t)
l, = plt.plot(t, s, lw=2, linestyle='--')

ax = plt.axis([0, TWOPI, -1, 1])

axamp = plt.axes([0.25, .03, 0.50, 0.02])
# Slider
samp = Slider(axamp, 'Amp', 0, 1, valinit=initial_amp)

# Animation controls
is_manual = False  # True if user has taken control of the animation
interval = 100  # ms, time between animation frames
loop_len = 5.0  # seconds per loop
scale = interval / 1000 / loop_len


def update(val):

    # print("in update function")
    # update curve
    l.set_ydata(val*np.sin(t))
    # redraw canvas while idle
    fig.canvas.draw_idle()


def update_plot(num):

    # print("in update_plot function")
    global is_manual
    if is_manual:
        return l,  # don't change

    val = (samp.val + scale) % samp.valmax
    samp.set_val(val)
    is_manual = False  # the above line called update_slider, so we need to reset this
    return l,


def update_slider(val):
    # print("in update_slider function")
    global is_manual
    is_manual = True
    update(val)


def on_click(event):

    # print("in on_click function")
    # Check where the click happened
    (xm, ym), (xM, yM) = samp.label.clipbox.get_points()
    if xm < event.x < xM and ym < event.y < yM:
        # Event happened within the slider, ignore since it is handled in update_slider
        return
    else:
        # user clicked somewhere else on canvas = unpause
        global is_manual
        is_manual = False


# call update function on slider value change
samp.on_changed(update_slider)

fig.canvas.mpl_connect('button_press_event', on_click)

ani = animation.FuncAnimation(fig, update_plot, interval=interval)

plt.show()
