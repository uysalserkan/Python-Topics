import numpy as np
import pandas as pd

RANGE = 500


attitude = 0
packed = []
time = []
pap_alfa = np.arange(0, 50, 0.1)
pap_beta = np.arange(50, 100, 0.1)
pap_pitot = np.random.rand(RANGE)
dusey_hiz = np.arange(5, 10, 0.01)


atTop = False

for i in range(RANGE):
    time.append(i)

    if attitude < 500 and not atTop:
        attitude = attitude + np.random.randint(7)

    elif atTop:
        attitude = attitude - np.random.randint(7)

    elif attitude == 600 or attitude == 601:
        atTop = True

    else:
        attitude = attitude + np.random.randint(2)

    packed.append(attitude)

j = 0

while j < RANGE:
    print(packed[j : j + 10])
    j = j + 10
# 'TIME': time,

myData = {
    "ATTITUDE": packed,
    "PAP_ALFA": pap_alfa,
    "PAP_BETA": pap_beta,
    "PAP_PITOT": pap_pitot,
    "DUSEY_HIZ": dusey_hiz,
}
# print(myData)

df = pd.DataFrame(
    myData,
    columns=["ATTITUDE", "PAP_ALFA", "PAP_BETA", "PAP_PITOT", "DUSEY_HIZ"],
    index=time,
)
print(df)
df.to_csv("SimpleRadar.csv")
