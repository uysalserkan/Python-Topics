import numpy as np
import pandas as pd

RANGE = 450


attitude = 0
packed = []
time = []
atTop = False

for i in range(RANGE):
    time.append(i)

    if(attitude < 500 and atTop == False):
        attitude = (attitude + np.random.randint(7))

    elif (atTop == True):
        attitude = (attitude - np.random.randint(7))

    elif attitude == 600 or attitude == 601:
        atTop = True

    else:
        attitude = (attitude + np.random.randint(2))

    packed.append(attitude)

j = 0
while j < RANGE:
    print(packed[j:j+10])
    j = j+10
# 'TIME': time,
myData = {'ATTITUDE': packed}
# print(myData)

df = pd.DataFrame(myData, columns=['ATTITUDE'], index=time)
print(df)
df.to_csv('SimpleRadar.csv')
