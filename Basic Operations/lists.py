# kutuphane=["Adana",25,34,"Zeki",3.14]

# for i in kutuphane:
#    print(type(i),"->",i)
# kullanici=input("Kitap adi girin: ")
# kutuphane +=[kullanici]
# print("Girildikten sonraki liste")
# for i in kutuphane:
#    print(type(i),"->",i)

# Kutuphen Automation

Kutuphane = []
menu = """
1- Kitap Ekle
2- Kitap Cikar
3- Kitaplari Listele
4- Programdan Cikis Yap
"""

def kitapEkle(kitap, liste):
   kitap=input("Kitap adi: ")
   liste+=[kitap]
   print("Kitap eklendi!")
   input("anamenu'ye dönmek için enter tuşuna basın")

def kitaplariListele(liste):
   for i in liste:
      print("Kitap adi: {}".format((i)))
   input("Anamenu icin entere bas")

def cikis():
   quit()

while True:
   kitap=""
   print(menu)
   secim=input("Lütfen seçiminizi giriniz: ")

   if secim=="1":
      kitapEkle(kitap,Kutuphane)
   elif secim=="2":
      continue
   elif secim=="3":
      kitaplariListele(Kutuphane)
   elif secim=="4":
      cikis()
   else:
      print("Hatali giris yaptiniz!")
