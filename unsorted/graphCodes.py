import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd

df = pd.read_csv('exponential.csv', index_col=0)
x = df['ATTITUDE']
y = np.linspace(start=0, stop=len(df), num=len(df), dtype=np.int32)


fig, ax = plt.subplots(figsize=(8, 5))

# x = ax.plot([], [], color='#0492C2')
varText = ax.text(s='TEST', x=len(df.columns), y=np.max(df.values)-np.max(df.values)/20)
# print(len(df.values), np.min(df.values), np.max(df.values))
ax.axes.axis([0, len(df.values), np.min(df.values), np.max(df.values)])

# print(x)
# print(y)

# plt.plot(x, x, label=varText)
line, = ax.plot(y, x, color='r', linestyle='--')


# Color'u koyunca update olmuyor


def animFunction(num):
    if x[num] > 718349:
        varText.set_text('HAVADA: {}'.format(num))
    else:
        varText.set_text('YERDE: {}'.format(num))
    line.set_data(y[:num], x[:num])
    # x.set_data(num, num)
    return line,


anim = animation.FuncAnimation(
    fig, animFunction, interval=15, frames=range(len(x)))

plt.show()
