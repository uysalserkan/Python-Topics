import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_csv('exponential.csv', index_col=0)
x = df['ATTITUDE']
print(df.sample(5))
print(df['ATTITUDE'])

fig, ax = plt.subplots(figsize=(6, 4))
ax.axes.axis([0, len(df), 0, np.max(df.values)])
plt.plot(df, label='ATTITUDE')
ax.legend(loc='upper left')

plt.show()
