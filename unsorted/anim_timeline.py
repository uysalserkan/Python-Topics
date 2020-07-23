import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import animatplot as amp


def psi(t):
    x = t
    y = np.sin(t)
    return x, y


t = np.linspace(0, 2*np.pi, 25)
x, y = psi(t)
X, Y = amp.util.parametric_line(x, y)

timeline = amp.Timeline(t, 's', 24)

ax = plt.axes(xlim=[0, 2], ylim=[-1.1, 1.1])
block1 = amp.blocks.Line(X, Y, ax=ax)
# or equivalently
# block1 = amp.blocks.ParametricLine(x, y, ax=ax)

anim = amp.Animation([block1], timeline)

# Your standard matplotlib stuff
plt.title('Parametric Line')
plt.xlabel('x')
plt.ylabel(r'y')

# Create Interactive Elements
anim.toggle()
anim.timeline_slider()

anim.save('parametric.gif', writer=PillowWriter(fps=5))
plt.show()