import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
x = np.linspace(0, 1, 50)
t = np.linspace(0, 1, 20)

X, T = np.meshgrid(x, t)
Y = np.sin(2*np.pi*(X+T))


block = amp.blocks.Line(X, Y)

plt.subplots_adjust(top=0.8)  # squish the plot to make space for the controls
slider_ax = plt.axes([.18, .89, .5, .03])  # the rect of the axis
button_ax = plt.axes([.78, .87, .1, .07])  # x, y, width, height

anim = amp.Animation([block])

anim.toggle(ax=button_ax)
anim.timeline_slider(text='TIME', ax=slider_ax, color='red', valfmt='%1.0f')
# equivalent to:
# anim.controls({'text':'TIME', 'ax':slider_ax, 'color':'red', 'valfmt':'%1.0f'},
#               {'ax':button_axis})

# anim.save_gif('images/controls')
plt.show()
