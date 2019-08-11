myDictionary = {"Adana": "01", "BLue": "34"}
print(myDictionary["Adana"])

#Tuple daha sonradan değişemez
WeekDays=("Pzt","Sal","Cars","Pers","Cum","Cmt","Paz")
print(WeekDays)

#dir() fonksiyonu kullanılacak fonks. görüntüler.
for i in dir(WeekDays):
   print(i)
s=input("Aramayi girin: ")
print(myDictionary.get(s,"İstediğiniz şey sözlükte yok"))
print(myDictionary.keys())
print(myDictionary.values())


Contenental = {"Marmara":{"istanbul":"buyukcekmece","gebze":"kocaeli","Bursa":"falan filan"}
,"Ege":{"izmir":"buca","canakkale":"biyer","falan":"filan"}
}

print(Contenental.get("Marmara","Boyle yer yok").get("istanbul","şehir yok"))
print(Contenental.get("Marmara","Boyle yer yok").get("kast","şehir yok"))
print(Contenental.get("sazan","Boyle yer yok"))