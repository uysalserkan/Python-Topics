import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd


statusInfo = "YERDE"
statusColor = 'r'
customLegend = []
df = pd.read_csv('SimpleRadar.csv', index_col=0)
y = np.linspace(start=0, stop=len(df), num=len(df), dtype=np.int32)
x = df['ATTITUDE']
# print(y)
# print(x.values)
# print("x max size: {}\ny len: {}".format(np.max(x), len(y)))

# print(df)
# print(len(df.values))

# print(np.min(df.values))
# print(np.max(df.values))




fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)






YerHava = ax.text(s='updating..', x=0, y=400)

ax.axes.axis([int(np.min(y)), int(np.max(y))+5,
              int(np.min(x)), int(np.max(x))+5])
customLegend.append([Line2D([0], [0], marker='o', color='w',
                            label=YerHava.get_text(), markerfacecolor=statusColor, markersize=12)])
ax.legend(handles=customLegend[0], loc='best', fancybox=True, shadow=True)


line, = ax.plot(y, x, color='r', linestyle='--')


def updateFigure(num, x, y, line):
    if (x[num] > 400):
        YerHava.set_text("HAVADA: "+str(num))

    elif(x[num] <= 400):
        YerHava.set_text("YERDE: "+str(num))

    line.set_data(y[:num], x[:num])
    # ax.axes.axis([0, int(np.max(y))+5, 0, int(np.max(x))+5])
    print(YerHava.get_text())
    return line,


anim = animation.FuncAnimation(fig, updateFigure, frames=range(len(x)),  fargs=[
    x, y, line], interval=5, blit=True)
# anim.save('animsave.gif')
plt.show()
