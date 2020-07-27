import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
#from basic_units import radians
# # Set up formatting for the movie files
# Writer = writers['ffmpeg']
# writer = Writer(fps=20, metadata=dict(artist='Llew'), bitrate=1800)

# Polar stuff
fig = plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)
ax.set_title("A line plot on a polar axis", va='bottom')
ax.set_rticks([0.5, 1, 1.5, 2])  # fewer radial ticks
ax.set_facecolor(plt.cm.gray(.95))
ax.grid(True)
xT = plt.xticks()[0]
xL = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$',
      r'$\pi$', r'$\frac{5\pi}{4}$', r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
plt.xticks(xT, xL)
r = []
theta = []
# Animation requirements.
ln, = plt.plot([], [], 'r:',
               markersize=1.5,
               alpha=1,
               animated=True)


def init():
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    return ln,


N = 10


def update(frame):
    r.append(frame)
    theta.append(2*np.pi*frame)
    ln.set_data(theta[-N:], r[-N:])
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 400),
                    init_func=init, interval=10, blit=True, repeat=True)

plt.show()
