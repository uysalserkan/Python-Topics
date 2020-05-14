from os import system as getSys
import os
import time
import myModule
import random

triangle=lambda a,b,hypo : a**2+b**2==hypo**2
def factorial(num):
   if num == 1 or num == 0:
      return 1
   elif num<0:
      print("number cannot be negative for factorial.")
      return -1
   else:
      return num * factorial(num-1)

getSys("cls")
number=random.randint(0,100)
print(number)

print(triangle(3,4,5))



print(factorial(4))
print(factorial(-4))

print(myModule.summation([1,3,4]))

cur_dir = os.getcwdb()
print(cur_dir)
home_dir=os.path.expanduser("-")
print(home_dir)

print("1 sec delay")
time.sleep(1)
print("done.")

time1=time.time()
time.sleep(3)
time2=time.time()

print("Delay: {}".format(time1-time2))
