import matplotlib.patches as patches
from matplotlib import pyplot as plt
from sympy.abc import x, y
import sympy
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as col
import matplotlib.pyplot as plt
values = np.random.random_integers(99, size=50)
cmap = cm.ScalarMappable(col.Normalize(0, 109), cm.binary)
plt.bar(np.arange(len(values)), values, color=cmap.to_rgba(values))
plt.show()
# %%%%
X = np.linspace(-6, 6, 1024)
Y1 = np.sinc(X)
Y2 = np.sinc(X) + 1
plt.plot(X, Y1, marker='o', color='.75', label='.75')
plt.plot(X, Y2, marker='o', color='r', markevery=32, label="red")
plt.legend()
plt.show()

# %%%%
X = np.linspace(0, 6, 1024)
Y1 = np.sin(X)
Y2 = np.cos(X)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(X, Y1, c='b', lw=3., label='sin(X)')
plt.plot(X, Y2, c='.5', lw=3., ls='--', label='cos(X)')
plt.legend()
plt.show()


# %% Visualizing the streamlines of a 2D vector field


def cylinder_stream_function(U=1, R=1):
    r = sympy.sqrt(x ** 2 + y ** 2)
    theta = sympy.atan2(y, x)
    return U * (r - R ** 2 / r) * sympy.sin(theta)


def velocity_field(psi):
    u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    return u, v


psi = cylinder_stream_function()
U_func, V_func = velocity_field(psi)
xmin, xmax, ymin, ymax = -3, 3, -3, 3
Y, X = np.ogrid[ymin:ymax:128j, xmin:xmax:128j]
U, V = U_func(X, Y), V_func(X, Y)
M = (X ** 2 + Y ** 2) < 1.
U = np.ma.masked_array(U, mask=M)
V = np.ma.masked_array(V, mask=M)
shape = patches.Circle((0, 0), radius=1., lw=2., fc='w', ec='k', zorder=0)
plt.gca().add_patch(shape)
plt.streamplot(X, Y, U, V, color='k')
plt.axes().set_aspect('equal')
plt.show()

