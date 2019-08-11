num1=float(input("Sayi 1: "))
num2=float(input("Sayi 2: "))
if(num1==0):
   raise Exception("Num1 i 0 yapman hiç bir anlam ifade etmiyor güzel kardeşim")

try:
   print("Sonuc: ",num1/num2)
except ZeroDivisionError:
   print("Bir sayinin 0'a bölünmesi belirsizlik yaratıri.")
except TypeError:
   print("Sayi tipiniz gecersizdir")
except: 
   print("genel hata statementi")
finally:
   print("bu satır her türlü çalışır")
