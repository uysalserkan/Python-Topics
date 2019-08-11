import os
kumem = set([1, 2, 3, 4, 5, 6])
kume2 = set([9, 8, 7, 6, 5, 3, 2, 1, 4])


kumem.add("adnaa")
kumem.discard(3)
kumem.remove(4)
os.system("cls")
print(24*"=")
print(kume2.difference(kumem))
print(kume2.intersection(kumem))
print(kume2.union(kumem))
