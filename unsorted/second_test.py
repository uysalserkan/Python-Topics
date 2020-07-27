import random
import matplotlib
import tkinter as Tk
from tkinter import Frame
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

root = Tk.Tk()
root.wm_title("Embedding in TK")
testFrame = Frame(root)
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.25)

y_values = [random.randrange(20, 40, 1) for _ in range(40)]
x_values = [i for i in range(40)]

ax.axis([0, 9, 20, 40])
ax.plot(x_values, y_values)

ax_time = fig.add_axes([0.12, 0.1, 0.78, 0.03])
s_time = Slider(ax_time, 'Time', 0, 30, valinit=0)


def update(val):
    pos = s_time.val
    ax.axis([pos, pos+10, 20, 40])
    fig.canvas.draw_idle()


s_time.on_changed(update)

Tk.mainloop()
