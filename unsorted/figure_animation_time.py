import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp


plt.rcParams['toolbar'] = 'None'
x = np.linspace(-2, 2, 41)
y = np.linspace(-2, 2, 41)
t = np.linspace(0, 2*np.pi, 60)

X, Y, T = np.meshgrid(x, y, t)

pcolormesh_data = np.sin(X*X+Y*Y-T)
line_data = pcolormesh_data[20, :, :]  # the slice where y=0


# standard matplotlib stuff
# create the different plotting axes
fig, (ax1, ax2) = plt.subplots(1, 2)

for ax in [ax1, ax2]:
    ax.set_aspect('equal')
    ax.set_xlabel('x')

ax2.set_ylabel('y', labelpad=-5)
ax1.set_ylabel('z')
ax1.set_ylim([-1.1, 1.1])

fig.suptitle('Multiple blocks')
ax1.set_title('Cross Section: $y=0$')
ax2.set_title(r'$z=\sin(x^2+y^2-t)$')

# animatplot stuff
# now we make our blocks
line_block = amp.blocks.Line(X[0, :, :], line_data,
                             ax=ax1, t_axis=1)
pcolormesh_block = amp.blocks.Pcolormesh(X[:, :, 0], Y[:, :, 0], pcolormesh_data,
                                         ax=ax2, t_axis=2, vmin=-1, vmax=1)
plt.colorbar(plt.cm.ScalarMappable())
timeline = amp.Timeline(t, fps=30)

# now to contruct the animation
anim = amp.Animation([pcolormesh_block, line_block], timeline)
anim.controls()

anim.save_gif('multiblock')
plt.show()
