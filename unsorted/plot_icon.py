import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

ax1.set_xlim((0, 500))
ax1.set_ylim((0, 200))

z = np.random.normal(0, 1, 255)
u = 0.1
sd = 0.3
counter = 0
price = [100]
t = [0]
artists = []
(l,) = plt.plot([], [], color="blue")


def add_annotation(annotated_message, value):
    annotation = plt.annotate(
        annotated_message,
        xy=(counter, value),
        xytext=(counter - 5, value + 20),
        textcoords="offset points",
        ha="right",
        va="bottom",
        bbox=dict(boxstyle="round,pad=0.1", fc="yellow", alpha=0.5),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )
    return annotation


def getNewPrice(s, mean, stdev):
    r = np.random.normal(0, 1, 1)
    priceToday = s + s * (mean / 255 + stdev / np.sqrt(225) * r)
    return priceToday


def animate(i):
    global t, u, sd, counter, artists
    x = t
    y = price
    counter += 1
    x.append(counter)
    value = getNewPrice(price[counter - 1], u, sd)
    y.append(value)
    l.set_data(x, y)

    if counter % 100 == 0:
        print(artists)
        new_annotation = add_annotation("100", value)
        artists.append(new_annotation)

    return [l] + artists


ani = animation.FuncAnimation(fig, animate, interval=20, frames=500)
plt.show()