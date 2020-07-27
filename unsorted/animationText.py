import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import matplotlib as mlp
import numpy as np
import pandas as pd


def fermi(E: float, E_f: float, T: float) -> float:
    k_b = 8.617 * (10**-5)  # eV/K
    return 1/(np.exp((E - E_f)/(k_b * T)) + 1)


# General plot parameters
# mpl.rcParams['font.family'] = 'Avenir'
# mpl.rcParams['font.size'] = 18
# mpl.rcParams['axes.linewidth'] = 2
# mpl.rcParams['axes.spines.top'] = False
# mpl.rcParams['axes.spines.right'] = False
# mpl.rcParams['xtick.major.size'] = 10
# mpl.rcParams['xtick.major.width'] = 2
# mpl.rcParams['ytick.major.size'] = 10
# mpl.rcParams['ytick.major.width'] = 2

# Create figure and add axes
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

T = np.linspace(100, 1000, 10)

varStr = ax.text(s='', x=0.4, y=1)

colors = plt.get_cmap('Dark2_r', 10)

for i in range(len(T)):
    x = np.linspace(0, 1, 100)
    y = fermi(x, 0.5, T[i])
    # if i % 2 == 0:
    #     varStr.set_text("EVEN")
    # else:
    #     varStr.set_text("ODD")
    ax.plot(x, y, color=colors(i), linewidth=1.5, label=str(varStr))


# labels = ['100 K', '200 K', '300 K', '400 K', '500 K', '600 K',
#           '700 K', '800 K', '900 K', '1000 K']
# ax.legend(labels, bbox_to_anchor=(1.05, -0.1), loc='lower left',
#           frameon=False, labelspacing=0.2)


# Create variable reference to plot
# f_d, = ax.plot([], [], linewidth=2.5)


# Add text annotation and create variable reference
temp = ax.text(s='Test', x=0.7, y=1)


def animate(i):
    # x = np.linspace(0, 1, 100)
    # y = fermi(x, 0.5, T[i])
    # f_d.set_data(x, y)
    # f_d.set_color(colors(i))
    if i % 2 == 0:
        varStr.set_text("EVEN")
    else:
        varStr.set_text("ODD")
    temp.set_text(str(int(T[i])) + ' K')
    temp.set_color(colors(i))


# Create animation
ani = animation.FuncAnimation(fig=fig, func=animate, frames=range(
    len(T)), interval=300, repeat=True)

plt.show()
