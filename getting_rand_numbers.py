import random

def getRandNum(gettingValue):
    i = 0
    while i<int(gettingValue):
        print(random.randint(0,100))
        i=i+1

getRandNum(5)
print("After 5 numbers")
getRandNum(10)