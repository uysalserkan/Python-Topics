import numpy as np
import datetime
import matplotlib.pyplot as plt

plt.rcParams["date.autoformatter.month"] = "%b %Y"

# my fake data
dates = np.array(
    [datetime.datetime(2000, 1, 1) + datetime.timedelta(days=i) for i in range(365)]
)
data = (
    np.sin(np.arange(365) / 365.0 * 2 * np.pi - 0.25 * np.pi) + np.random.rand(365) / 3
)

# creates fig with 2 subplots
fig, ax = plt.subplots(figsize=(6, 2))
## plot dates
ax.plot_date(dates, data)

# rotates labels
plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45)

plt.tight_layout()
plt.show()
