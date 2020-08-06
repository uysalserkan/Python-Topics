import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
from tkinter import *
from tkinter import ttk
import matplotlib.widgets
import mpl_toolkits.axes_grid1
import animatplot as amp
import numpy as np
import pandas as pd
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
SCALE = 8
DESICION_LINE = 400

root = Tk()

root.wm_title("Test Graph Interaction")

df = pd.read_csv('exponential.csv', index_col=0)
y = np.linspace(start=0, stop=len(df), num=len(df), dtype=np.int32)
x = df['ATTITUDE']

is_manual = False

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# axamp = plt.axes([0.25, .03, 0.50, 0.02])
axamp = plt.axes([0, 0, 0, 5])
initial_amp = .0
samp = Slider(axamp, '', 0, len(x), valinit=initial_amp, valstep=1)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


YerHava = ax.text(s='updating..', x=0, y=400)

ax.axes.axis([int(np.min(y)), int(np.max(y))+5,
              int(np.min(x)), int(np.max(x))+5])

line, = ax.plot(y, x, color='r', linestyle='--')


slider = StringVar()
# slider.set('0.00')

testScale = ttk.Scale(root, from_=0, to_=len(x), length=len(x),
                      command=lambda s: mainUpdate(int(float(s))))
testScale.pack(side=TOP, fill=BOTH,padx=5,pady=3)


def mainUpdate(val):
    if val == len(x):
        if (x[val-1] > DESICION_LINE):
            YerHava.set_text("HAVADA: "+str(x[val-1]))

        elif(x[val-1] <= DESICION_LINE):
            YerHava.set_text("YERDE: "+str(x[val-1]))

        line.set_data(y[:val-1], x[:val-1])
    else:
        if (x[val] > DESICION_LINE):
            YerHava.set_text("HAVADA: "+str(x[val]))

        elif(x[val] <= DESICION_LINE):
            YerHava.set_text("YERDE: "+str(x[val]))

        line.set_data(y[:val], x[:val])
    fig.canvas.draw_idle()


# ? x y line parametreleri kaldırıldı
def updateFigure(num):
    global is_manual
    if is_manual:
        return line,

    # val = (samp.val + SCALE) % samp.valmax
    # slider.set(val)
    samp.set_val(int(testScale.get()+SCALE))

    is_manual = False

    return line,


def sampUpdate(value):
    global is_manual
    is_manual = True
    # slider.set(value)
    testScale.set(value)
    mainUpdate(value)
    fig.canvas.draw_idle()


def resetGraph():

    samp.reset()


def playGraph():
    global is_manual
    if is_manual == True:
        is_manual = False
    else:
        is_manual = True
    #! Exception has occurred: UnboundLocalError local variable 'is_manual' referenced before assignment


# def on_click(event):
#     (xm, ym), (xM, yM) = samp.label.clipbox.get_points()
#     if xm < event.x < xM and ym < event.y < yM:

#         return
#     else:

#         global is_manual
#         is_manual = False


# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# resetButton = Button(resetax, 'Reset', hovercolor='0.975')


# playax = plt.axes([0.1, 0.025, 0.1, 0.04])
# playButton = Button(playax, "Play", hovercolor='0.975')

# playButton.on_clicked(playGraph)

# resetButton.on_clicked(resetGraph)

anim = animation.FuncAnimation(fig, updateFigure)
samp.on_changed(sampUpdate)


#  lambda s: slider.set((int(float(s))))
# ttk.Label(root, textvariable=slider).pack()
ttk.Button(root, text="Play", command=playGraph).pack(
    side=LEFT, fill=BOTH)
ttk.Button(root, text="Reset", command=resetGraph).pack(
    side=LEFT, fill=BOTH)

# plt.show()

root.mainloop()
