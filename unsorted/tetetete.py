import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D

import matplotlib.widgets
import mpl_toolkits.axes_grid1
import animatplot as amp
import numpy as np
import pandas as pd


from matplotlib.widgets import Slider, Button
SCALE = 8
DESICION_LINE = 400

# statusInfo = "YERDE"
# statusColor = 'r'
# customLegend = []
df = pd.read_csv('exponential.csv', index_col=0)
y = np.linspace(start=0, stop=len(df), num=len(df), dtype=np.int32)
x = df['ATTITUDE']
# print(y)
# print(x.values)
# print("x max size: {}\ny len: {}".format(np.max(x), len(y)))

# print(df)
# print(len(df.values))

# print(np.min(df.values))
# print(np.max(df.values))

is_manual = False

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

axamp = plt.axes([0.25, .03, 0.50, 0.02])
initial_amp = .0
samp = Slider(axamp, 'Time', 0, len(x), valinit=initial_amp, valstep=1)

YerHava = ax.text(s='updating..', x=0, y=400)

ax.axes.axis([int(np.min(y)), int(np.max(y))+5,
              int(np.min(x)), int(np.max(x))+5])
# customLegend.append([Line2D([0], [0], marker='o', color='w',
#                             label=YerHava.get_text(), markerfacecolor=statusColor, markersize=12)])
# ax.legend(handles=customLegend[0], loc='best', fancybox=True, shadow=True)


line, = ax.plot(y, x, color='r', linestyle='--')


def mainUpdate(val):
    if val == len(x):
        if (x[val-1] > DESICION_LINE):
            YerHava.set_text("HAVADA: "+str(val))

        elif(x[val-1] <= DESICION_LINE):
            YerHava.set_text("YERDE: "+str(val))

        line.set_data(y[:val-1], x[:val-1])
        # ax.axes.axis([0, int(np.max(y))+5, 0, int(np.max(x))+5])
        # print(YerHava.get_text())
        # fig.canvas.draw_idle()
    else:
        if (x[val] > DESICION_LINE):
            YerHava.set_text("HAVADA: "+str(val))

        elif(x[val] <= DESICION_LINE):
            YerHava.set_text("YERDE: "+str(val))

        line.set_data(y[:val], x[:val])
        # ax.axes.axis([0, int(np.max(y))+5, 0, int(np.max(x))+5])
        # print(YerHava.get_text())
    fig.canvas.draw_idle()


# ? x y line parametreleri kaldırıldı
def updateFigure(num):
    global is_manual
    if is_manual:
        return line,

    val = (samp.val + SCALE) % samp.valmax
    #! üst satırda patladı
    # print("num value is: {}".format(num))
    # print("samp.valmax value is: {}".format(samp.valmax))
    samp.set_val(val)

    is_manual = False

    return line,
    # if num == 450:
    #     if (x[num-1] > 400):
    #         YerHava.set_text("HAVADA: "+str(num))

    #     elif(x[num-1] <= 400):
    #         YerHava.set_text("YERDE: "+str(num))

    #     line.set_data(y[:num-1], x[:num-1])
    #     # ax.axes.axis([0, int(np.max(y))+5, 0, int(np.max(x))+5])
    #     # print(YerHava.get_text())
    #     return line,
    # else:
    #     if (x[num] > 400):
    #         YerHava.set_text("HAVADA: "+str(num))

    #     elif(x[num] <= 400):
    #         YerHava.set_text("YERDE: "+str(num))

    #     line.set_data(y[:num], x[:num])
    #     # ax.axes.axis([0, int(np.max(y))+5, 0, int(np.max(x))+5])
    #     # print(YerHava.get_text())
    #     return line,


def sampUpdate(value):
    global is_manual
    is_manual = True
    mainUpdate(value)
    # # samp.set_val(value)
    # print("amp value is: {}".format(amp))
    # ax.text(s="VALUE IS: {}".format(int(value)), x=100,
    #         y=int(y.tolist().index(int(value))))
    # print(y)
    # print("YYYY: {}".format(y.tolist().index(int(value))))
    # print(x)
    # print("X value: {}, Y value: {}".format(
    #     y.tolist()[int(value-1)], x.tolist()[int(value-1)]))

    # print("Gelen Value: {}".format(int(amp)))
    # [DONE] ! -1 ve 450 olma durumları var fakat tam işe yaramıyor.
    # updateFigure(int(value), x, y, line)

    fig.canvas.draw_idle()


# runs = True
# step = 0


# def play():
#     while runs:
#         step += 1
#         if step > 0 and step < 450:
#             yield step
#         else:
#             yield step

# Slider

# pause_ax = fig.add_axes((0.7, 0.025, 0.1, 0.04))
# pause_button = Button(pause_ax, 'pause', hovercolor='0.975')
# pause_button.on_clicked(print("click pause"))


def resetGraph(event):

    samp.reset()


def playGraph(event):
    global is_manual
    if is_manual == True:
        is_manual = False
    else:
        is_manual = True
    #! Exception has occurred: UnboundLocalError local variable 'is_manual' referenced before assignment


def on_click(event):

    # Check where the click happened
    (xm, ym), (xM, yM) = samp.label.clipbox.get_points()
    if xm < event.x < xM and ym < event.y < yM:
        # Event happened within the slider, ignore since it is handled in update_slider
        return
    else:
        # user clicked somewhere else on canvas = unpause
        global is_manual
        is_manual = False


# fig.canvas.mpl_connect('button_press_event', on_click)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
resetButton = Button(resetax, 'Reset', hovercolor='0.975')


playax = plt.axes([0.1, 0.025, 0.1, 0.04])
playButton = Button(playax, "Play", hovercolor='0.975')

playButton.on_clicked(playGraph)

resetButton.on_clicked(resetGraph)


# updateFigure(0, x, y, line)

# samp.event_source.start()


# slider_ax = plt.axes([.18, .89, .5, .03])  # the rect of the axis
# button_ax = plt.axes([.78, .87, .1, .07])

# animation.toggle(ax=button_ax)
# anim.timeline_slider(text='TIME', ax=slider_ax, color='red', valfmt='%1.0f')

# anim.save('animsave.gif')
anim = animation.FuncAnimation(fig, updateFigure)
samp.on_changed(sampUpdate)

plt.show()


# ? External parameters of animation FuncAnimation
""" ,frames=len(x), interval=5, blit=False, repeat=True ,   fargs=[
    x, y, line]"""

# %%%%%%%%%%%%
""" 
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
 """
