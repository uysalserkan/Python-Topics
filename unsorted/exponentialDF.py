import pandas as pd
import numpy as np

T_SIZE = 1100


times = np.linspace(start=0, stop=T_SIZE-1, num=T_SIZE, dtype=np.int32)

attitude = []

test = 0
j = 0
for i in range(T_SIZE):
    if i < 380:
        test = test + int(np.power(i, 1.5))
        attitude.append(test)
        continue
    elif i > 380 and i < 660:
        attitude.append(test)
        # j = i
        continue
    else:
        if (test - int(np.power(j, 1.45)) > 0):
            test = test - int(np.power(j, 1.45))
        else:
            test = 0
        attitude.append(test)
        j = j+1
        continue


myData = {'ATTITUDE': attitude}
csvFile = pd.DataFrame(myData, columns=['ATTITUDE'], index=times)
# print(csvFile)
csvFile.to_csv('exponential.csv')
